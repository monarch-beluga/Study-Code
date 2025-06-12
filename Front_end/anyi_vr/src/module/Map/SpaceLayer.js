import * as DC from '@dvgis/dc-sdk'
import axios from "axios";
import {getDivIconPopupHtml, getDivPopupHtml} from "./IconHtml.js";

const path = "./api/jsonData/anyi_yjkj.json"
const params = {
    6: {
        "class_name": "public-map-popup yjc-box",
        "img_src": "./img/mapicon/yjc.png",
        "layer": "yjc-yq",
    },
    7: {
        "class_name": "public-map-popup yjc-box",
        "img_src": "./img/mapicon/yjc.png",
        "layer": "ysc-yq",
    },
    8: {
        "class_name": "public-map-popup ysf-box",
        "img_src": "./img/mapicon/ysf.png",
        "layer": "chz-yq",
    },
    9: {
        "class_name": "public-map-popup sk-box",
        "img_src": "./img/mapicon/kt.png",
        "layer": "kt-yq",
        "vLayer": "vkt-yq",
    },
    10: {
        "class_name": "public-map-popup sk-box",
        "img_src": "./img/mapicon/zb.png",
        "layer": "zb-yq",
    },
    11: {
        "class_name": "public-map-popup xfs-box",
        "img_src": "./img/mapicon/gouqu.png",
        "layer": "gouqu-yq",
        "vLayer": "vgouqu-yq"
    },
    12: {
        "class_name": "public-map-popup sk-box",
        "img_src": "./img/mapicon/sk.png",
        "layer": "sk-yq",
        "vLayer": "vsk-yq",
    },
    13: {
        "class_name": "public-map-popup xfs-box",
        "img_src": "./img/mapicon/ql.png",
        "layer": "ql-yq",
    },
    17: {
        "class_name": "public-map-popup xfs-box",
        "img_src": "./img/mapicon/sd.png",
        "layer": "sd-yq",
    },
    18: {
        "layer": "sg-yq",
    }
}

async function getSpaceData(){
    const res = await axios.get(path)
    return res.data
}

function getSpaceDataByType(data, type){
    return data.filter(item => item.type === type)
}

function getSpaceHtmlLayer(item, layer){
    let param = params[item.type]
    let position = new DC.Position(item.lng, item.lat)
    let divHtml = getDivIconPopupHtml(param.class_name, item.name, param.img_src)
    let divIcon = new DC.DivIcon(position, divHtml).addTo(layer)
    divIcon.on(DC.MouseEventType.CLICK, (e) => {
        if ($viewer.getLayer("popup"))
            $viewer.getLayer("popup").remove()
        let popupLayer = new DC.HtmlLayer("popup").addTo($viewer)
        let popupDivHtml = getDivPopupHtml(item.firmName, item.mainFuncName, "./api/"+item.facilityImg, item.capacity)
        let popupDivIcon = new DC.DivIcon(position, popupDivHtml)
        popupDivIcon.on(DC.MouseEventType.CLICK, e=>{
            popupLayer.remove()
        })
        popupDivIcon.addTo(popupLayer)
        })
}

function getSpacePolygonLayer(item, layer){
    if (item.feature !== null){
        let polygon = new DC.Polygon(item.feature)
        polygon.setStyle({
            material: DC.Color.fromCssColorString("#0051ff"),
        })
        polygon.addTo(layer)
    }
}

function getSpaceLineLayer(item, layer){
    let polyline = new DC.Polyline(item.feature)
    polyline.setStyle({
        width: 10,
        material: DC.Color.fromCssColorString("#000eff"),
    })
    polyline.addTo(layer)
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

function getSpacePipeLayer(item, layer){
    let plc = new DC.PolylineVolume(item.feature, computeCircle(1))
    plc.setStyle({
        "cornerType": 1,
        "fill": true,
        "material": DC.Color.AQUA.withAlpha(0.5)
    })
    let polyline = new DC.Polyline(item.feature)
    polyline.setStyle({
        width: 5,
        material: new DC.PolylineImageTrailMaterialProperty({
            color: DC.Color.fromCssColorString("#008cff"),
            speed: 20,
            image: './images/right.png',
            repeat: { x: Math.floor(polyline.distance / 10), y: 0.7 }
        }),
        clampToGround: false
    })
    polyline.addTo(layer)
    plc.addTo(layer)
}


async function showSpaceHtmlLayerByType(type, checked){
    let param = params[type]
    if (checked){
        let data = await getSpaceData();
        let dataByType = getSpaceDataByType(data, type)
        let layer = new DC.HtmlLayer(param.layer).addTo($viewer)
        dataByType.forEach(item => {
            getSpaceHtmlLayer(item, layer)
        })
    }else{
        $viewer.getLayer(param.layer).remove()
    }
}

async function showSpaceLayerByType(type, checked){
    let param = params[type]
    if (checked){
        let data = await getSpaceData();
        let dataByType = getSpaceDataByType(data, type)
        let layer = new DC.HtmlLayer(param.layer).addTo($viewer)
        let vLayer = new DC.VectorLayer(param.vLayer).addTo($viewer)
        dataByType.forEach(item => {
            getSpaceHtmlLayer(item, layer)
            getSpacePolygonLayer(item, vLayer)
        })
    }else{
        $viewer.getLayer(param.layer).remove()
        $viewer.getLayer(param.vLayer).remove()
    }
}

async function showSpaceDitchLayerByType(type, checked){
    let param = params[type]
    if (checked){
        let data = await getSpaceData();
        let dataByType = getSpaceDataByType(data, type)
        let layer = new DC.HtmlLayer(param.layer).addTo($viewer)
        let vLayer = new DC.VectorLayer(param.vLayer).addTo($viewer)
        dataByType.forEach(item => {
            getSpaceHtmlLayer(item, layer)
            getSpaceLineLayer(item, vLayer)
        })
    }else{
        $viewer.getLayer(param.layer).remove()
        $viewer.getLayer(param.vLayer).remove()
    }
}

async function showSpacePipeLayerByType(type, checked){
    let param = params[type]
    if (checked){
        let data = await getSpaceData();
        let dataByType = getSpaceDataByType(data, type)
        let vLayer = new DC.VectorLayer(param.layer).addTo($viewer)
        dataByType.forEach(item => {
            getSpacePipeLayer(item, vLayer)
        })
    }else{
        $viewer.getLayer(param.layer).remove()
    }
}

export {
    getSpaceData,
    getSpaceDataByType,
    getSpaceHtmlLayer,
    getSpaceLineLayer,
    getSpacePolygonLayer,
    getSpacePipeLayer,
    showSpaceHtmlLayerByType,
    showSpaceLayerByType,
    showSpaceDitchLayerByType,
    showSpacePipeLayerByType
}
