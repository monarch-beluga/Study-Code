
import axios from "axios";
import * as DC from '@dvgis/dc-sdk'
import {getPanoramicLayer} from "./PanoramicLayer.js";
import {getCurrBusiness} from "./Business.js";

const path = "./api/jsonData/yjwzqj.json"
const layerName = "qy_yjwz"
const className = "public-map-popup qyfb-box"
const img = "./img/mapicon/yjwz.png"

async function getSuppliesLayer(){
    let layer = new DC.HtmlLayer(layerName).addTo($viewer)
    let res = await axios.get(path)
    let name = getCurrBusiness()
    let data = res.data.filter(item => item.Name === name || item.Name === "湘东工业园应急物资库")
    data.forEach(item => {
        getPanoramicLayer(item, layer, className, img)
    })
}

function removeSuppliesLayer(){
    $viewer.getLayer(layerName).remove()
}

export {getSuppliesLayer, removeSuppliesLayer}

