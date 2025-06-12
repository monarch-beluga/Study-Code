import axios from "axios";
import * as DC from '@dvgis/dc-sdk'

import {getDivIconPopupHtml} from "./IconHtml.js";
import {ref} from "vue";

const path = "./api/jsonData/anyi_kzqj.json"
const layerName = "kzqj"
const className = "public-map-popup"
const img = "./img/mapicon/qj.png"

const panoShow = ref(false)
const panoTitle = ref("")
const iframeSrc = ref("")

function getPanoShow(){
    return panoShow.value
}
function getPanoTitle(){
    return panoTitle.value
}
function getIframeSrc(){
    return iframeSrc.value
}
function closePano(){
    panoShow.value = false
}

function getPanoramicLayer(item, layer, className, img){
    let position = new DC.Position(item.lng, item.lat)
    let divHtml = getDivIconPopupHtml(className, "应急物资", img)
    let divIcon = new DC.DivIcon(position, divHtml)
    divIcon.on(DC.MouseEventType.CLICK, e => {
        panoShow.value = true
        panoTitle.value = item.Name
        iframeSrc.value = item.url
    })
    divIcon.addTo(layer)
}

async function getPanoramicData(layer){
    let res = await axios.get(path)
    let data = res.data
    data.forEach(item => {
        let position = new DC.Position(item.lng, item.lat)
        let divHtml = getDivIconPopupHtml(className, item.name, img)
        let divIcon = new DC.DivIcon(position, divHtml)
        divIcon.on(DC.MouseEventType.CLICK, e => {
            panoShow.value = true
            panoTitle.value = item.name
            iframeSrc.value = item.url+"?startscene="+item.scene_name
        })
        divIcon.addTo(layer)
    })
}

async function showPanoLayer(checked){
    if (checked){
        let layer = new DC.HtmlLayer(layerName).addTo($viewer)
        await getPanoramicData(layer)
    }
    else{
        $viewer.getLayer(layerName).remove()
    }
}

export {getPanoramicLayer, showPanoLayer, getPanoShow, getPanoTitle, getIframeSrc, closePano}
