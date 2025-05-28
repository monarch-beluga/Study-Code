<script setup>
import * as DC from '@dvgis/dc-sdk'
import '@dvgis/dc-sdk/dist/dc.min.css'
import axios  from "axios"
import PageElement from "./PageElement.vue"
import ToolBarRight from "./ToolBarRight.vue"
import PanContainer from "./PanContainer.vue"
import {inject, onMounted, provide, ref, render, toRefs} from 'vue'
import qyPageElement from "./qyfw/qyPageElement.vue";
import {useRouter} from "vue-router";

const staticData = inject("staticData")

const props = defineProps({
  info: String
})
const {info} = toRefs(props)


function JsonToWall(layer, path) {
  axios.get(path).then((res) => {
    res.data.forEach(item => {
      let wall = new DC.Wall(item.feature)
      wall.setStyle({
        material: new DC.WallTrailMaterialProperty({
          color: DC.Color.fromCssColorString("#00ff3b"),
          speed: 10
        })
      })
      layer.addOverlay(wall)
    })
  })
}

function getDivIconPopupHtml(class_name, map_name, img_src){
  return `
        <div class='${class_name}'>
          <div class="map-name">${map_name}</div>
          <div class="map-icon">
            <img src='${img_src}'>
          </div>
        </div>
        `
}

function getDivPopupHtml(name, mainFuncName, facilityImg, capacity){

  if (capacity !== "\\")
    return `
          <div class="public-map-popup-two">
            <div class="marsBlueGradientPnl">
              <div>所属单位：${name}</div>
              <div>作用：${mainFuncName}</div>
              <div>容量：${capacity}立方米</div>
              <img class="popup-img" src='${facilityImg}'/>
            </div>
          </div>
        `
  else
    return `
          <div class="public-map-popup-two">
            <div class="marsBlueGradientPnl">
              <div>所属单位：${name}</div>
              <div>作用：${mainFuncName}</div>
              <img class="popup-img" src='${facilityImg}'/>
            </div>
          </div>
        `


}

function getQjmnDivPopupHtml(content){
  return `
      <div class="dynamic-map-popup">
        <div class="content-wrap">
          <div class="content">
            <p>${content}</p>
          </div>
        </div>
        <div class="arrow"></div>
      </div>
        `
}

function getRsDivPopupHtml(materialName, riskSourcesName, riskLevel){
  return `
          <div class="public-map-popup-three">
            <div></div>
            <div class="marsBlueGradientPnl">
              <li>行业类别：${materialName}</li>
              <li>风险等级: ${riskLevel}</li>
              <li>风险物质：${riskSourcesName}</div>
            </div>
          </div>
        `
}

function getYjkjLayer(layer, type){
  let param = staticData.htmlLayerParam[type]
  axios.get(staticData.api + param.jsonPath + `?type=${type}`).then((response) => {
    let data = response.data
    data.forEach((record, index) => {
      if (record.type === type){

          let position = new DC.Position(record.lng, record.lat)
          let divIcon = new DC.DivIcon(position, getDivIconPopupHtml(param.class_name, record.name, param.img_src))
          divIcon.on(DC.MouseEventType.CLICK, e=>{
            let popupLayer = viewer.getLayer('popup')
            viewer.removeLayer(popupLayer)
            viewer.addLayer(popupLayer)
            popupLayer.clear()
            let popupDivIcon = new DC.DivIcon(position, getDivPopupHtml(record.firmName, record.mainFuncName,
                staticData.api + '/' + record.facilityImg, record.capacity))
            popupDivIcon.on(DC.MouseEventType.CLICK, e=>{
              popupLayer.clear()
            })
            popupDivIcon.addTo(popupLayer)
          })
          divIcon.addTo(layer)
        }
    })
  })
}

function getQyYjwzLayer(layer, name, pan){
  let param = staticData.htmlLayerParam[21]
  axios.get(staticData.api + param.jsonPath).then((response) => {
    let data = response.data
    data.forEach((record) => {
      if (name === record.Name || record.Name === "园区"){
        let position = new DC.Position(record.lng, record.lat)
        let divIcon = new DC.DivIcon(position, getDivIconPopupHtml(param.class_name, "应急物资", param.img_src))
        divIcon.on(DC.MouseEventType.CLICK, e=>{
          pan.title_text.innerHTML = record.Name
          pan.iframe.setAttribute('src', record.url)
          pan.panShow = true
        })
        divIcon.addTo(layer)
      }
    })
  })

}

function initQyYjwzLayer(){
  let layer = viewer.getLayer('qy_yjwz');
  if (layer)
    layer.clear()
  else{
    layer = new DC.HtmlLayer('qy_yjwz')
    viewer.addLayer(layer)
  }
}
provide("initQyYjwzLayer", initQyYjwzLayer)
function showQyYjwzLayer(name, pan){
  initQyYjkjLayer()
  let layer = viewer.getLayer('qy_yjkj');
  getQyYjwzLayer(layer, name, pan)
}
provide("showQyYjwzLayer", showQyYjwzLayer)

function getQyYjkjLayer(layer, name){
  axios.get("api/jsonData/anyi_yjkj.json").then((response) => {
    let data = response.data
    data.forEach((record, index) => {
      if (name === record.firmName){
        let param = staticData.htmlLayerParam[record.type]
        let position = new DC.Position(record.lng, record.lat)
        let divIcon = new DC.DivIcon(position, getDivIconPopupHtml(param.class_name, record.name, param.img_src))
        divIcon.on(DC.MouseEventType.CLICK, e=>{
          let popupLayer = viewer.getLayer('popup')
          viewer.removeLayer(popupLayer)
          viewer.addLayer(popupLayer)
          popupLayer.clear()
          let popupDivIcon = new DC.DivIcon(position, getDivPopupHtml(record.firmName, record.mainFuncName,
              staticData.api + '/' + record.facilityImg, record.capacity))
          popupDivIcon.on(DC.MouseEventType.CLICK, e=>{
            popupLayer.clear()
          })
          popupDivIcon.addTo(popupLayer)
        })
        divIcon.addTo(layer)
      }
    })
  })
}

function initQyYjkjLayer(){
  let layer = viewer.getLayer('qy_yjkj');
  if (layer)
    layer.clear()
  else{
    layer = new DC.HtmlLayer('qy_yjkj')
    viewer.addLayer(layer)
  }
}
provide("initQyYjkjLayer", initQyYjkjLayer)

function showQyYjkjLayer(name){
  initQyYjkjLayer()
  let layer = viewer.getLayer('qy_yjkj');
  getQyYjkjLayer(layer, name)
}
provide("showQyYjkjLayer", showQyYjkjLayer)

function getRsLayer(layer, type){
  let param = staticData.htmlLayerParam[type]
  axios.get(staticData.api + param.jsonPath).then((response) => {
    let data = response.data
    data.forEach((record, index) => {
      if (record.riskLevel === param.type){
        let position = new DC.Position(record.lon, record.lat)
        let divIcon = new DC.DivIcon(position, getDivIconPopupHtml(param.class_name, record.name, param.img_src))
        divIcon.on(DC.MouseEventType.CLICK, e=>{
          let popupLayer = viewer.getLayer('popup')
          viewer.removeLayer(popupLayer)
          viewer.addLayer(popupLayer)
          popupLayer.clear()
          let popupDivIcon = new DC.DivIcon(position, getRsDivPopupHtml(record.materialName, record.riskSourcesName, record.riskLevel))
          popupDivIcon.on(DC.MouseEventType.CLICK, e=>{
            popupLayer.clear()
          })
          popupDivIcon.addTo(popupLayer)
        })

        divIcon.addTo(layer)
      }
    })
  })
}

function getQyfbLayer(layer, type){
  let param = staticData.htmlLayerParam[type]
  axios.get(staticData.api + param.jsonPath + `?type=${param.type}`).then((response) => {
    let data = response.data
    data.forEach(record => {
      if (record.type === param.type){
        let position = new DC.Position(record.lng, record.lat, record.ele)
        let divIcon = new DC.DivIcon(position, getDivIconPopupHtml(param.class_name, record.name, param.img_src))
        divIcon.addTo(layer)
      }
    })
  })
}

const kzPan = ref(null)
function getKzqjLayer(layer, type){
  let param = staticData.htmlLayerParam[type]
  axios.get(staticData.api + param.jsonPath).then((response) => {
    let data = response.data
    data.forEach((record) => {
      let position = new DC.Position(record.lng, record.lat, record.ele)
      let divIcon = new DC.DivIcon(position, getDivIconPopupHtml(param.class_name, record.name, param.img_src))
      divIcon.on(DC.MouseEventType.CLICK, e=>{
        kzPan.value.title_text.innerHTML = record.name
        if (kzPan.value.iframe.getAttribute("src") !== record.url + "?startscene=" + record.scene_name)
          kzPan.value.iframe.setAttribute('src', record.url + "?startscene=" + record.scene_name)
        kzPan.value.panShow = true
        })
      divIcon.addTo(layer)
    })
  })
}

function getSjfkLayer(htmlLayer, vLayer, level){
  axios.get(staticData.api + staticData.yjkjJson + `?preLevel=${level}`).then((response) => {
    let data = response.data
    data.forEach(record => {
      if (record.preLevel.search(level) !== -1){
        if (record.type === 18){
          addSgLayer(vLayer, record)
        }
        else{
          let param = staticData.htmlLayerParam[record.type]
          let position = new DC.Position(record.lng, record.lat, record.ele)
          let divIcon = new DC.DivIcon(position, getDivIconPopupHtml(param.class_name, record.name, param.img_src))
          divIcon.on(DC.MouseEventType.CLICK, e=>{
            let popupLayer = viewer.getLayer('popup')
            viewer.removeLayer(popupLayer)
            viewer.addLayer(popupLayer)
            popupLayer.clear()
            let popupDivIcon = new DC.DivIcon(position, getDivPopupHtml(record.firmName, record.mainFuncName,
                staticData.api + '/' + record.facilityImg, record.capacity))
            popupDivIcon.on(DC.MouseEventType.CLICK, e=>{
              popupLayer.clear()
            })
            popupDivIcon.addTo(popupLayer)
          })
          divIcon.addTo(htmlLayer)
          if (record.type === 9 || record.type === 12){
            if (record.feature !== null){
              let polygon = new DC.Polygon(record.feature)
              polygon.setStyle({
                material: DC.Color.fromCssColorString("#0051ff"),
              })
              vLayer.addOverlay(polygon)
            }
          }
          if (record.type === 11){
            if (record.feature !== null){
              let polyline = new DC.Polyline(record.feature)
              polyline.setStyle({
                width: 10,
                material: DC.Color.fromCssColorString("#000eff"),
              })
              vLayer.addOverlay(polyline)
            }
          }
        }
      }
    })
  })
}

function getLineLayer(layer, type){
  let param = staticData.htmlLayerParam[type]
  axios.get(staticData.api + param.jsonPath).then((response) => {
    let data = response.data
    data.forEach(record => {
      let polyline = new DC.Polyline(record.feature)
      polyline.setStyle({
        width: param.width,
        material: DC.Color.fromCssColorString(param.color),
      })
      layer.addOverlay(polyline)
    })
  })
}

function showLineLayer(type, check){
  let param = staticData.htmlLayerParam[type]
  let layer  = viewer.getLayer(param.layer);
  if (layer){
    layer.show = check
  }
  else {
    if (check){
      layer = new DC.VectorLayer(param.layer).addTo(viewer)
      getLineLayer(layer, type)
    }
  }
}
provide("showLineLayer", showLineLayer)

function showRsLayer(type, check){
  let param = staticData.htmlLayerParam[type]
  let layer  = viewer.getLayer(param.layer);
  if (layer){
    layer.show = check
  }
  else {
    if (check){
      layer = new DC.HtmlLayer(param.layer).addTo(viewer)
      getRsLayer(layer, type)
    }
  }
}

function showSjfkLayer(level, check){
  let htmlLayerName = staticData.sjfkLayerName[level][0]
  let vLayerName = staticData.sjfkLayerName[level][1]
  let htmlLayer  = viewer.getLayer(htmlLayerName);
  let vLayer = viewer.getLayer(vLayerName);
  if (htmlLayer){
    vLayer.show = check
    htmlLayer.show = check
  }
  else {
    if (check){
      htmlLayer = new DC.HtmlLayer(htmlLayerName).addTo(viewer)
      vLayer = new DC.VectorLayer(vLayerName).addTo(viewer)
      getSjfkLayer(htmlLayer, vLayer, level)
    }
  }
}

function showInitLayer(type, check){
  let param = staticData.htmlLayerParam[type]
  let layer = viewer.getLayer(param.layer)
  if (layer){
    layer.show = check
  }
}

function showKzqjLayer(type, check){
  let param = staticData.htmlLayerParam[type]
  let layer = viewer.getLayer(param.layer)
  if (layer){
    layer.show = check
  }
  else{
    if (check) {
      layer = new DC.HtmlLayer(param.layer).addTo(viewer)
      getKzqjLayer(layer, type)
    }
  }
}

function computeCircle(radius) {
  let positions = []
  for (let i = 0; i < 360; i++) {
    let radians = DC.Math.toRadians(i)
    positions.push({
      x: radius * Math.cos(radians),
      y: radius * Math.sin(radians),
    })
  }
  return positions
}

function addSgLayer(layer, item){
  if (item.feature === null)
    return
  let plc = new DC.PolylineVolume(item.feature, computeCircle(1))
  plc.setStyle({
    "cornerType": 1,
    "fill": true,
    "material": DC.Color.AQUA.withAlpha(0.5)
  })
  let polyline = new DC.Polyline(item.feature)
  polyline.setStyle({
    width: 5,
    material: new DC.PolylineTrailMaterialProperty({
      color: DC.Color.fromCssColorString("#ff0000"),
      speed: item.speed
    }),
    clampToGround: false
  })
  layer.addOverlay(polyline)
  layer.addOverlay(plc)
}

function showSgLayer(type, check){
  let param = staticData.htmlLayerParam[type]
  let layer = viewer.getLayer(param.layer)
  if (layer){
    layer.show = check
  }
  else{
    if (check) {
      layer = new DC.VectorLayer(param.layer)
      viewer.addLayer(layer)

      axios.get(staticData.api + param.jsonPath).then((res) => {
        res.data.forEach(item => {
          if (item.type === type){
            addSgLayer(layer, item)
          }
        })
      })
    }
  }
}

function showKtLayer(type, check){
  let param = staticData.htmlLayerParam[type]
  let layer = viewer.getLayer(param.vLayer)
  if (layer){
    layer.show = check
  }
  else{
    if (check) {
      layer = new DC.VectorLayer(param.vLayer)
      viewer.addLayer(layer)

      axios.get(staticData.api + param.jsonPath).then((res) => {
        res.data.forEach(item => {
          if (item.type === type){
            if (item.feature !== null)
            {
              let polygon = new DC.Polygon(item.feature)
              polygon.setStyle({
                material: DC.Color.fromCssColorString("#0051ff"),
              })
              layer.addOverlay(polygon)
            }
          }
        })
      })
    }
  }
}

function showGqLayer(type, check){
  let param = staticData.htmlLayerParam[type]
  let layer = viewer.getLayer(param.vLayer)
  if (layer){
    layer.show = check
  }
  else{
    if (check) {
      layer = new DC.VectorLayer(param.vLayer)
      viewer.addLayer(layer)

      axios.get(staticData.api + param.jsonPath).then((res) => {
        res.data.forEach(item => {
          if (item.type === type){
            if (item.feature !== null)
            {
              let polyline = new DC.Polyline(item.feature)
              polyline.setStyle({
                width: 10,
                material: DC.Color.fromCssColorString("#000eff"),
              })
              layer.addOverlay(polyline)
            }
          }
        })
      })
    }
  }
}

function showQyfbLayer(type, check){
  let param = staticData.htmlLayerParam[type]
  let layer = viewer.getLayer(param.layer)
  if (layer){
    layer.show = check
  }
  else {
    if (check) {
      layer = new DC.HtmlLayer(param.layer).addTo(viewer)
      getQyfbLayer(layer, type)
    }
  }
}

function showYjkjLayer(type, check){
  let param = staticData.htmlLayerParam[type]
  let layer  = viewer.getLayer(param.layer);
  if (layer){
    layer.show = check
  }
  else {
    if (check){
      layer = new DC.HtmlLayer(param.layer).addTo(viewer)
      getYjkjLayer(layer, type)
    }
  }
}

function viewFlyToPoint(e){
  let flyP = DC.Position.fromArray(e.position)
  let position = new DC.Position(e.position[0], e.position[1])
  let popupLayer = viewer.getLayer('popup')
  viewer.removeLayer(popupLayer)
  viewer.addLayer(popupLayer)
  popupLayer.clear()
  let popupDivIcon = new DC.DivIcon(position, getDivPopupHtml(e.firmName, e.mainFuncName,
      staticData.api + '/' + e.facilityImg, e.capacity))
  popupDivIcon.on(DC.MouseEventType.CLICK, e=>{
    popupLayer.clear()
  })
  popupDivIcon.addTo(popupLayer)
  viewer.flyToPosition(flyP)
}

function viewFlyRsToPoint(e){
  let flyP = DC.Position.fromArray(e.position)
  let position = new DC.Position(e.position[0], e.position[1])
  let popupLayer = viewer.getLayer('popup')
  viewer.removeLayer(popupLayer)
  viewer.addLayer(popupLayer)
  popupLayer.clear()
  let popupDivIcon = new DC.DivIcon(position, getRsDivPopupHtml(e.materialName, e.riskSourcesName, e.riskLevel))
  popupDivIcon.on(DC.MouseEventType.CLICK, e=>{
    popupLayer.clear()
  })
  popupDivIcon.addTo(popupLayer)
  viewer.flyToPosition(flyP)
}

const speechSynthesis = window.speechSynthesis;
const voices = ref([]);
const voice = ref(null);
const currentSpeech = ref('');
const speakMessage = (text) => {
  return new Promise((resolve) => {
    if (!window.speechSynthesis) {
      resolve(false);
      return;
    }

    const utterance = new SpeechSynthesisUtterance(text);
    currentSpeech.value = text;

    utterance.onend = () => {
      resolve(true);
    };

    utterance.onerror = () => {
      resolve(false);
    };

    window.speechSynthesis.speak(utterance);
  });
};
const stopSpeak = () => {
  speechSynthesis.cancel();
};

let tc = undefined
function initQjmnLayer(){
  let vLayer = viewer.getLayer("qjmn_v")
  if (vLayer)
    vLayer.clear()
  else{
    vLayer = new DC.VectorLayer('qjmn_v')
    viewer.addLayer(vLayer)
  }

  let hLayer = viewer.getLayer("qjmn_h")
  if (hLayer)
    hLayer.clear()
  else{
    hLayer = new DC.HtmlLayer('qjmn_h')
    viewer.addLayer(hLayer)
  }
  if (tc)
    tc.clear()
}

const qjmnFun = async (path) => {
  let data = []
  await axios.get(path).then((response) => {
    data = response.data
  })
  initQjmnLayer();
  stopSpeak();
  let vLayer = viewer.getLayer("qjmn_v")
  let hLayer = viewer.getLayer("qjmn_h")
  for (const item of data) {
    await viewer.flyToPosition(DC.Position.fromArray(item.flyPosition), null, 1)
    let popupDivIcon = new DC.DivIcon(item.point, getQjmnDivPopupHtml(item.content))
    popupDivIcon.addTo(hLayer)
    item.features.forEach(feature => {
      if (feature.type === 'p') {
        let circle = new DC.Circle(feature.feature, feature.size)
        circle.setStyle({
          material: new DC.CircleWaveMaterialProperty({
            color: feature.color !== "" ? DC.Color.fromCssColorString(feature.color) : DC.Color.fromRandom(),
            count: 5,
            gradient: 0.2,
            speed: 10
          })
        })
        circle.addTo(vLayer)
      }
      else if (feature.type === 'l'){
        let polyline = new DC.Polyline(feature.feature)
        polyline.setStyle({
          width: 20,
          material: new DC.PolylineImageTrailMaterialProperty({
            color: feature.color !== "" ? DC.Color.fromCssColorString(feature.color) : DC.Color.fromRandom(),
            speed: 10,
            image: './img/mapicon/arrow.png',
            repeat: { x: feature.size, y: 1 }
          }),
          clampToGround: true
        })
        polyline.addTo(vLayer)
      }
      else if (feature.type === "c"){
        let polyline = new DC.Polyline(feature.feature)
        polyline.setStyle({
          width: feature.size,
          material: feature.color !== "" ? DC.Color.fromCssColorString(feature.color) : DC.Color.fromRandom(),
          clampToGround: true
        })
        polyline.addTo(vLayer)
      }
      else if (feature.type === "tc"){
        tc.clear()
        let track = new DC.Track(feature.feature,feature.duration, null, {clampToTileset: true})
        track.setModel('./img/mapicon/Truck.glb',{
          scale:10
        })
        track.setPath(true,{
          width:feature.size,
          color:feature.color !== "" ? DC.Color.fromCssColorString(feature.color) : DC.Color.fromRandom(),
        })
        tc.addTrack(track)
        tc.play()
      }
    })
    let s = await speakMessage(item.content)
    if (!s)
      break
  }
}


function setTer(flag){
  if (flag){
    let ter =  DC.TerrainFactory.createUrlTerrain({
      url: staticData.terrainPath
    })
    viewer.setTerrain(ter)
  }
  else{
    viewer.setTerrain(null)
  }
}

const toolBar = ref(null)
function mapTreeChange(index, check){
  toolBar.value.mapTreeChange(index, check)
}

function measureTool(name){
  switch (name){
    case "空间距离":
      measure.distance()
      break
    case "贴地距离":
      measure.distanceSurface()
      break
    case "水平面积":
      measure.area()
      break
    case "贴地面积":
      measure.areaSurface();
      break
    case "角度":
      measure.angle();
      break
    case "高度差":
      measure.angle({
        clampToModel:true
      });
      break
    case "三角测量":
      measure.triangleHeight();
      break
    case "贴物高度":
      measure.height({
        clampToModel:true
      });
      break
    default:
      measure.deactivate();
      break
  }
}

function exportScene(){
  viewer.exportScene("scene")
}

function BaseMapChange(index){
  viewer.changeBaseLayer(index)
}
function initViewrPs(){
  viewer.zoomToPosition(DC.Position.fromArray(staticData.zoomPosition))
}

function initQyfwLayer(){
  let layer = viewer.getLayer("qyfw")
  if (layer)
    layer.clear()
  else{
    layer = new DC.VectorLayer('qyfw')
    viewer.addLayer(layer)
  }
}
provide("initQyfwLayer", initQyfwLayer)
function showQyfwLayer(name){
  initQyfwLayer()
  let data;
  let layer = viewer.getLayer("qyfw")
  axios.get("api/jsonData/anyi_qyfb.json").then((response) => {
    response.data.forEach(item => {
      if (item.name === name){
        let wall = new DC.Wall(item.feature)
        wall.setStyle({
          material: new DC.WallTrailMaterialProperty({
            color: DC.Color.fromCssColorString("#e1d930"),
            speed: 10
          })
        })
        layer.addOverlay(wall)
        data = item
      }
    })
    viewer.flyTo(layer, 3)
  })
  return data
}

provide("qjmnFun", qjmnFun)
provide("showInitLayer", showInitLayer)
provide("showGqLayer", showGqLayer)
provide("showSgLayer", showSgLayer)
provide("showKzqjLayer", showKzqjLayer)
provide("showYjkjLayer", showYjkjLayer)
provide("showKtLayer", showKtLayer)
provide("showQyfbLayer", showQyfbLayer)
provide("showSjfkLayer", showSjfkLayer)
provide("showRsLayer", showRsLayer)
provide("mapTreeChange", mapTreeChange)
provide("measureTool", measureTool)
provide("viewFlyToPoint", viewFlyToPoint)
provide("viewFlyRsToPoint", viewFlyRsToPoint)
provide("BaseMapChange", BaseMapChange)
provide("setTer", setTer)
provide("exportScene", exportScene)
provide("stopSpeak", stopSpeak)
provide("initViewrPs", initViewrPs)
provide("initQjmnLayer", initQjmnLayer)
let measure = undefined
let viewer = undefined
const uRouter = useRouter()
const tabs = {
  "/map/main/survey":  "园区概况",
  "/map/main/rs":  "风险源",
  "/map/main/space":  "应急空间",
  "/map/main/pac": "多级防控",
  "/map/main/pd": "情景模拟",
  "/table/supplies": "应急物资",
  "/table/rt": "救援队伍",
  "/zzt": "作战图"
}
function initViewer() {
  viewer = new DC.Viewer('viewer-container')
  measure = new DC.Measure(viewer)
  window.$viewer = viewer
  initViewrPs()
  // viewer.zoomToPosition(DC.Position.fromArray(staticData.zoomPosition))
  let key = staticData.tdtKey
  let tdtImg = DC.ImageryLayerFactory.createImageryLayer(DC.ImageryType.XYZ,{
    url: "https://t0.tianditu.gov.cn/DataServer?T=img_w&x={x}&y={y}&l={z}&tk="+key,
    maximumLevel:18,
  })

  let tdtCia = DC.ImageryLayerFactory.createImageryLayer(DC.ImageryType.XYZ,{
    url: "https://t0.tianditu.gov.cn/DataServer?T=cia_w&x={x}&y={y}&l={z}&tk="+key,
    maximumLevel:18,
  })

  let tdtVec = DC.ImageryLayerFactory.createImageryLayer(DC.ImageryType.XYZ,{
    url: "https://t0.tianditu.gov.cn/DataServer?T=vec_w&x={x}&y={y}&l={z}&tk="+key,
    maximumLevel:18,
  })

  let tdtCva = DC.ImageryLayerFactory.createImageryLayer(DC.ImageryType.XYZ,{
    url: "https://t0.tianditu.gov.cn/DataServer?T=cva_w&x={x}&y={y}&l={z}&tk="+key,
    maximumLevel:18,
  })

  let gdImg = DC.ImageryLayerFactory.createImageryLayer(DC.ImageryType.AMAP,{
    style: 'img',
    maximumLevel:18,
    crs:'WGS84'
  })

  let gdVec = DC.ImageryLayerFactory.createImageryLayer(DC.ImageryType.AMAP, {
    maximumLevel:18,
    style: "vec",
    crs:'WGS84'
  })
  viewer.addBaseLayer([tdtVec, tdtCva])
  viewer.addBaseLayer([tdtImg, tdtCia])
  viewer.addBaseLayer([gdVec, tdtCva])
  viewer.addBaseLayer([gdImg, tdtCia])
  viewer.changeBaseLayer(1)

  setTer(true)

  let tile3dLayer = new DC.TilesetLayer(staticData.htmlLayerParam[1].layer)
  viewer.addLayer(tile3dLayer)
  staticData.tilePath.forEach(item => {
    let tileset = new DC.Tileset(staticData.api + item)
    tile3dLayer.addOverlay(tileset)
  })


  let areaLayer = new DC.VectorLayer(staticData.htmlLayerParam[4].layer)
  viewer.addLayer(areaLayer)
  JsonToWall(areaLayer,staticData.api + staticData.htmlLayerParam[4].jsonPath)

  tc = new DC.TrackController(viewer)
  new DC.HtmlLayer("popup").addTo(viewer)

  if (tabs[uRouter.currentRoute.value.path] === "园区概况")
    mapTreeChange(5, true)
  if (tabs[uRouter.currentRoute.value.path] === "应急空间")
    mapTreeChange(6, true)
  else if(tabs[uRouter.currentRoute.value.path] === "多级防控")
    showSjfkLayer("1", true)
  else if(tabs[uRouter.currentRoute.value.path] === "风险源") {
    mapTreeChange(15, true)
    mapTreeChange(16, true)
    mapTreeChange(19, true)
  }
  else if (tabs[uRouter.currentRoute.value.path] === "情景模拟"){
    mapTreeChange(18, true)
  }
}

const currPageTab = ref("page")
const pageElemntTabs = {
  "page": PageElement,
  "qyPage": qyPageElement
}

const mainClass = {
  "page": "main-content",
  "qyPage": "main-content-sub"
}

const infos = ref({
  "page": info.value,
  "qyPage": "",
})

function changePage1(i) {
  currPageTab.value = i
  infos.value.page = "园区概况"
}
provide("changePage1", changePage1)

function qyEnter(name){
  uRouter.push('/map/sub/companyInfo')
  currPageTab.value = "qyPage"
  infos.value.qyPage = name
  for (let i=5; i <= 13; i++)
    mapTreeChange(i, false)
  mapTreeChange(15, false)
  mapTreeChange(16, false)
  showQyfwLayer(name)
}
provide("qyEnter", qyEnter)

DC.ready().then(initViewer)
onMounted(() => {
  // 某些浏览器需要延迟加载语音列表
  setTimeout(() => {
    voices.value = speechSynthesis.getVoices();
    // 默认选择中文语音（如果存在）
    voice.value = voices.value.find(v => v.lang.includes('zh')) || voices.value[0];
  }, 100);
});

</script>

<template>
  <div class="viewer-container" id="viewer-container">
    <div class="content">
      <div :class="mainClass[currPageTab]" id="MainContent">
        <ToolBarRight ref="toolBar"></ToolBarRight>
        <PanContainer ref="kzPan"></PanContainer>
        <div class="w100 h100 relative">
          <component :is="pageElemntTabs[currPageTab]" :info="infos[currPageTab]"></component>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.wrapper  .main-content{
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 99;
  unicode-bidi: isolate;
  pointer-events: none;
  background: url('/images/header.png') no-repeat center / 100% 100%, url('/images/pro-bg.png') no-repeat center / 100% 100%;
}
.wrapper .main-content-sub{
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 99;
  unicode-bidi: isolate;
  pointer-events: none;
  background: url('/images/wrapper-box-bg.png') no-repeat center / 100% 100%, url('/images/pro-bg.png') no-repeat center / 100% 100%;
}
#viewer-container {
  width: 100%;
  height: 100%;
  position: absolute;
}
</style>