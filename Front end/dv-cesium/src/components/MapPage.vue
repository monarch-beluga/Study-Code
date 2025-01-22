<script setup>
import * as DC from '@dvgis/dc-sdk'
import '@dvgis/dc-sdk/dist/dc.min.css'
import axios  from "axios"
import PageElement from "./PageElement.vue"
import ToolBarRight from "./ToolBarRight.vue"
import PanContainer from "./PanContainer.vue"
import {inject, provide, ref, toRefs} from 'vue'

const staticData = inject("staticData")

const props = defineProps({
  info: String
})
const {info} = toRefs(props)


// geoJson图层转为DC.Wall, 自定义高度
function geoJsonToWall(layer, path, alt) {
  let tempLayer = new DC.GeoJsonLayer('temp', path)

  tempLayer.eachOverlay((i) => {
    let poly = undefined;
    if (i.polyline)
      poly = DC.Polyline.fromEntity(i)
    if (i.polygon)
      poly = DC.Polygon.fromEntity(i)
    let ps = []
    poly.positions.forEach((p) => {
      ps.push(DC.Position.fromArray([p.lng, p.lat, alt]))
    })

    let wall = new DC.Wall(ps)
    wall.setStyle({
      material: new DC.WallTrailMaterialProperty({
        color: DC.Color.fromCssColorString("#13599d"),
        speed: 10
      })
    })
    layer.addOverlay(wall)
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

function getDivPopupHtml(name, mainFuncName, facilityImg){

  return `
          <div class="public-map-popup-two">
            <div class="marsBlueGradientPnl">
              <div>企业名称：${name}</div>
              <div>作用：${mainFuncName}</div>
              <img class="popup-img" src='${facilityImg}'/>
            </div>
          </div>
        `
}

function getYjkjLayer(layer, type){
  let param = staticData.htmlLayerParam[type]
  axios.get(staticData.api + param.jsonPath + `?type=${param.type}`).then((response) => {
    let data = response.data
    data.forEach((record, index) => {
      if (record.type === param.type){
        let position = new DC.Position(record.lng, record.lat, record.ele)
        let divIcon = new DC.DivIcon(position, getDivIconPopupHtml(param.class_name, record.name, param.img_src))
        divIcon.on(DC.MouseEventType.CLICK, e=>{
          if (viewer.getLayer('popup'))
            viewer.getLayer('popup').remove()
          let popupLayer = new DC.HtmlLayer("popup").addTo(viewer)
          let popupDivIcon = new DC.DivIcon(position, getDivPopupHtml(record.firmName, record.mainFuncName,
              staticData.api + '/' + record.facilityImg))
          popupDivIcon.on(DC.MouseEventType.CLICK, e=>{
            viewer.getLayer('popup').remove()
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

function getKzqjLayer(layer, type){
  let param = staticData.htmlLayerParam[type]
  axios.get(staticData.api + param.jsonPath).then((response) => {
    let data = response.data
    data.forEach((record) => {
      let position = new DC.Position(record.lng, record.lat, record.ele)
      let divIcon = new DC.DivIcon(position, getDivIconPopupHtml(param.class_name, record.name, param.img_src))
      divIcon.on(DC.MouseEventType.CLICK, e=>{
        let pc = document.querySelector(".panorama-container")
        pc.setAttribute("style", "")

        let title = document.querySelector(".panorama-container .title div")
        title.innerHTML = record.name

        let iframe = document.querySelector(".panorama-container .content iframe")
        if (!iframe.getAttribute('src'))
          iframe.setAttribute('src', record.url)
      })
      divIcon.addTo(layer)
    })
  })
}

function getSjfkLayer(layer, level){
  let types = {
    "1": 6, "2": 7, "5": 8, "6": 9, "7": 10, "8": 11, "9": 12, "10": 13, "11": 14
  }
  axios.get(staticData.api + staticData.yjkjJson + `?preLevel=${level}`).then((response) => {
    let data = response.data
    data.forEach(record => {
      if (record.preLevel === level){
        let param = staticData.htmlLayerParam[types[record.type]]
        let position = new DC.Position(record.lng, record.lat, record.ele)
        let divIcon = new DC.DivIcon(position, getDivIconPopupHtml(param.class_name, record.name, param.img_src))
        divIcon.addTo(layer)
      }
    })
  })
}

function showSjfkLayer(level, check){
  let layerName = staticData.sjfkLayerName[level]
  let layer  = viewer.getLayer(layerName);
  if (layer){
    layer.show = check
  }
  else {
    if (check){
      layer = new DC.HtmlLayer(layerName).addTo(viewer)
      getSjfkLayer(layer, level)
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
  if (viewer.getLayer('popup'))
    viewer.getLayer('popup').remove()
  let popupLayer = new DC.HtmlLayer("popup").addTo(viewer)
  let popupDivIcon = new DC.DivIcon(position, getDivPopupHtml(e.firmName, e.mainFuncName, staticData.api + '/' + e.facilityImg))
  popupDivIcon.on(DC.MouseEventType.CLICK, e=>{
    viewer.getLayer('popup').remove()
  })
  popupDivIcon.addTo(popupLayer)
  viewer.flyToPosition(flyP)
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

provide("getDivPopupHtml", getDivPopupHtml)
provide("showInitLayer", showInitLayer)
provide("showYjkjLayer", showYjkjLayer)
provide("showQyfbLayer", showQyfbLayer)
provide("showSjfkLayer", showSjfkLayer)
provide("mapTreeChange", mapTreeChange)
provide("measureTool", measureTool)
provide("viewFlyToPoint", viewFlyToPoint)
provide("BaseMapChange", BaseMapChange)
provide("setTer", setTer)
provide("exportScene", exportScene)
let measure = undefined
let viewer = undefined

function initViewer() {
  viewer = new DC.Viewer('viewer-container')
  measure = new DC.Measure(viewer)
  window.$viewer = viewer
  viewer.zoomToPosition(DC.Position.fromArray(staticData.zoomPosition))
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
  geoJsonToWall(areaLayer,staticData.api + staticData.htmlLayerParam[4].jsonPath, staticData.htmlLayerParam[4].alt)

  let planLayer = new DC.HtmlLayer(staticData.htmlLayerParam[5].layer).addTo(viewer)
  getKzqjLayer(planLayer, 5)

  if (info.value === "应急空间")
    mapTreeChange(6, true)
  else if(info.value === "三级防控")
    showSjfkLayer("1", true)
  // viewer.flyTo(tileset)
}

DC.ready().then(initViewer)

</script>

<template>
  <div class="viewer-container" id="viewer-container">
    <div class="content">
      <div class="main-content" id="MainContent">
        <ToolBarRight ref="toolBar"></ToolBarRight>
        <PanContainer></PanContainer>
        <div class="w100 h100 relative">
          <PageElement :info="info"></PageElement>
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

#viewer-container {
  width: 100%;
  height: 100%;
  position: absolute;
}
</style>