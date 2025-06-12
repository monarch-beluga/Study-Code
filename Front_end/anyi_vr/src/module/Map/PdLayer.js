
import * as DC from '@dvgis/dc-sdk'
import {ref} from 'vue'
import {speakMessage, stopSpeak} from "./SpeechText.js";
import axios from "axios";
import {getPdDivPopupHtml} from "./IconHtml.js";

const paths = {
    1: "./api/jsonData/anyi_qjmn1.json",
    2: "./api/jsonData/anyi_qjmn2.json",
    3: "./api/jsonData/anyi_qjmn3.json",
    4: "./api/jsonData/anyi_qjmn4.json",
}
const layerName = "qjmn_h"
const vLayerName = "qjmn_v"

let tc = ref("")

function initPdLayer(){
    new DC.VectorLayer(vLayerName).addTo($viewer)
    new DC.HtmlLayer(layerName).addTo($viewer)
    if (!tc.value)
        tc.value = new DC.TrackController($viewer)
}

async function getPdLayer(index){
    let hLayer = $viewer.getLayer(layerName)
    let vLayer = $viewer.getLayer(vLayerName)
    let path = paths[index]
    hLayer.clear()
    vLayer.clear()
    tc.value.clear()
    stopSpeak()
    const res = await axios.get(path)
    const data = res.data
    for (const item of data) {
        await $viewer.flyToPosition(DC.Position.fromArray(item.flyPosition), null, 1)
        let popupDivIcon = new DC.DivIcon(item.point, getPdDivPopupHtml(item.content))
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
            } else if (feature.type === 'l') {
                let polyline = new DC.Polyline(feature.feature)
                polyline.setStyle({
                    width: 20,
                    material: new DC.PolylineImageTrailMaterialProperty({
                        color: feature.color !== "" ? DC.Color.fromCssColorString(feature.color) : DC.Color.fromRandom(),
                        speed: 20,
                        image: './img/mapicon/arrow.png',
                        repeat: {x: feature.size, y: 1}
                    }),
                    clampToGround: true
                })
                polyline.addTo(vLayer)
            } else if (feature.type === "c") {
                let polyline = new DC.Polyline(feature.feature)
                polyline.setStyle({
                    width: feature.size,
                    material: feature.color !== "" ? DC.Color.fromCssColorString(feature.color) : DC.Color.fromRandom(),
                    clampToGround: true
                })
                polyline.addTo(vLayer)
            } else if (feature.type === "tc") {
                tc.value.clear()
                let track = new DC.Track(feature.feature, feature.duration, null, {clampToTileset: true})
                track.setModel('./img/mapicon/Truck.glb', {
                    scale: 10
                })
                track.setPath(true, {
                    width: feature.size,
                    color: feature.color !== "" ? DC.Color.fromCssColorString(feature.color) : DC.Color.fromRandom(),
                })
                tc.value.addTrack(track)
                tc.value.play()
            }
        })
        let s = await speakMessage(item.content)
        if (!s)
            break
    }
}

function removePdLayer(){
    $viewer.getLayer(layerName).remove()
    $viewer.getLayer(vLayerName).remove()
}

export {initPdLayer, getPdLayer, removePdLayer}

