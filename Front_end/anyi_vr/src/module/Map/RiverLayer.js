import axios from "axios";
import * as DC from '@dvgis/dc-sdk'

const path = "./api/jsonData/anyi_hl.json"
const layerName = "hl-yq"

async function getRiverLayer(){
    let layer = new DC.VectorLayer(layerName).addTo($viewer)
    const res = await axios.get(path)
    const data = res.data
    data.forEach(item => {
        let polyline = new DC.Polyline(item.feature)
        polyline.setStyle({
            width: 3,
            material: DC.Color.fromCssColorString("#0033ff"),
        })
        layer.addOverlay(polyline)
    })
}
async function showRiverLayer(checked){
    if (checked){
        await getRiverLayer()
    }else{
        $viewer.getLayer(layerName).remove()
    }
}

export {showRiverLayer}
