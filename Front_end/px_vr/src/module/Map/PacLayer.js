
import * as DC from '@dvgis/dc-sdk'
import {ref} from "vue"
import {
    getSpaceData,
    getSpaceHtmlLayer, getSpaceLineLayer, getSpacePipeLayer,
} from "./SpaceLayer.js";

const params = {
    "1": {
        layer: "pacLayer1",
        vLayer: "pacVLayer1",
    },
    "2": {
        layer: "pacLayer2",
        vLayer: "pacVLayer2",
    },
    "3": {
        layer: "pacLayer3",
        vLayer: "pacVLayer3",
    },
    "4": {
        layer: "pacLayer4",
        vLayer: "pacVLayer4",
    }
}
const pacLayers = ref([])

function getPacDataByPreLevel(data, preLevel){
    return data.filter(item => item.preLevel.search(preLevel) !== -1)
}

function getPacLayer(item, layer, vLayer){
    switch (item.type){
        case 6:
        case 7:
        case 8:
        case 10:
        case 9:
        case 11:
        case 12:
            getSpaceHtmlLayer(item, layer)
            break
        case 13:
            getSpacePipeLayer(item, vLayer)
            getSpaceHtmlLayer(item, layer)
            break
    }
}

async function showPacLayer(preLevel, checked){
    let param = params[preLevel]
    let layer = $viewer.getLayer(param.layer)
    let vLayer = $viewer.getLayer(param.vLayer)
    if (layer){
        layer.show = checked
        vLayer.show = checked
    }else{
        if (checked){
            layer = new DC.HtmlLayer(param.layer).addTo($viewer)
            vLayer = new DC.VectorLayer(param.vLayer).addTo($viewer)
            pacLayers.value.push(param.layer)
            pacLayers.value.push(param.vLayer)
            const data = await getSpaceData()
            const dataByPreLevel = await getPacDataByPreLevel(data, preLevel)
            dataByPreLevel.forEach(item => {
                getPacLayer(item, layer, vLayer)
            })
        }
    }
}

function removePacLayer(){
    pacLayers.value.forEach(item => {
        $viewer.getLayer(item).remove()
    })
    pacLayers.value = []
}

export {showPacLayer, removePacLayer, getPacLayer}
