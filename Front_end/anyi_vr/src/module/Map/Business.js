import axios from "axios";
import {storage} from "../../store/storage.js";
import * as DC from '@dvgis/dc-sdk'
import {getDivIconPopupHtml} from "./IconHtml.js";

const baseUrl = import.meta.env.VITE_API_BASE_URL;
const path = "/data/businesses"
const layerName = "qyfb"
const className = "public-map-popup qyfb-box"
const img = "./img/mapicon/qy.png"


function changeBusiness(name){
    storage.set("businessName", name)
}

async function getBusinesses(){
    const res = await axios.get(baseUrl + path)
    return res.data
}

async function getBusinessesByName(name){
    const res = await axios.get(baseUrl + path, {
        params: {name: name}})
    return res.data
}

function getCurrBusiness(){
    return storage.get("businessName")
}

async function getBusinessDetail(){
    const currBusiness = getCurrBusiness()
    const data = await getBusinessesByName(currBusiness)
    return data[0]
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
