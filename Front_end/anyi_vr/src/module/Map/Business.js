import axios from "axios";
import {storage} from "../../store/storage.js";
import * as DC from '@dvgis/dc-sdk'
import {getDivIconPopupHtml} from "./IconHtml.js";

const path = "./api/jsonData/anyi_qyfb.json"
const layerName = "qyfb"
const className = "public-map-popup qyfb-box"
const img = "./img/mapicon/qy.png"


function changeBusiness(name){
    storage.set("businessName", name)
}

async function getBusinesses(){
    const res = await axios.get(path)
    return res.data
}

function getCurrBusiness(){
    return storage.get("businessName")
}

async function getBusinessDetail(){
    const data = await getBusinesses()
    const currBusiness = getCurrBusiness()
    return data.filter(item => item.name === currBusiness)[0]
}

async function getBusinessesLayer(){
    let layer = new DC.HtmlLayer(layerName).addTo($viewer)
    const data = await getBusinesses()
    data.forEach(item => {
        let position = new DC.Position(item.lng, item.lat)
        let divHtml = getDivIconPopupHtml(className, item.name, img)
        new DC.DivIcon(position, divHtml).addTo(layer)
    })
}

async function showBusinessesLayer(checked){
    if (checked){
        await getBusinessesLayer()
    }
    else{
        $viewer.getLayer(layerName).remove()
    }
}

export {
    getCurrBusiness,
    changeBusiness,
    getBusinesses,
    getBusinessDetail,
    showBusinessesLayer
}
