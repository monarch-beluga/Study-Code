import * as DC from '@dvgis/dc-sdk'
import axios from "axios";
import {getDivIconPopupHtml, getRsDivPopupHtml} from "./IconHtml.js";

const path = "./api/jsonData/rs.json"
const params = {
    15: {
        "layer": "rs-yb",
        "class_name": "public-map-popup fxy-ordinary",
        "img_src": "./img/mapicon/fxy-yb.png",
        "type": "一般",
    },
    16: {
        "layer": "rs-jd",
        "class_name": "public-map-popup fxy-larger-b",
        "img_src": "./img/mapicon/fxy-zd-b.png",
        "type": "较大",
    },
    17: {
        "layer": "rs-qt",
        "class_name": "public-map-popup fxy-larger-a",
        "img_src": "./img/mapicon/fxy-zd.png",
        "type": "其他",
    }
}

async function getRsData(){
    const res = await axios.get(path)
    return res.data
}

function getRsDataByType(data, type){
    return data.filter(item => item.riskLevel === type)
}

function getRsLayer(data, layer, type){
    let param = params[type]
    data.forEach(item => {
        let position = new DC.Position(item.lon, item.lat)
        let divHtml = getDivIconPopupHtml(param.class_name, item.name, param.img_src)
        let divIcon = new DC.DivIcon(position, divHtml).addTo(layer)
        divIcon.on(DC.MouseEventType.CLICK, (e) => {
            if ($viewer.getLayer("popup"))
                $viewer.getLayer("popup").remove()
            let popupLayer = new DC.HtmlLayer("popup").addTo($viewer)
            let popupDivHtml = getRsDivPopupHtml(item.materialName, item.riskSourcesName,  item.riskLevel)
            let popupDivIcon = new DC.DivIcon(position, popupDivHtml)
            popupDivIcon.on(DC.MouseEventType.CLICK, e=>{
                popupLayer.remove()
            })
            popupDivIcon.addTo(popupLayer)
        })
    })
}

async function showRsLayer(type, checked){
    let param = params[type]
    if (checked){
        const data = await getRsData()
        const dataByType = getRsDataByType(data, param['type'])
        let layer = new DC.HtmlLayer(param.layer).addTo($viewer)
        getRsLayer(dataByType, layer, type)
    }else{
        $viewer.getLayer(param.layer).remove()
    }
}

export {showRsLayer, getRsData}