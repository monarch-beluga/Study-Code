import * as DC from '@dvgis/dc-sdk'
import {ref} from "vue";

const key = "8899fd3e86aa994f71465b1c56a98727"
const baseLayerIndex = ref(1)

function changeBaseLayer(index){
    $viewer.changeBaseLayer(index)
    baseLayerIndex.value = index
}

function getBaseLayer() {
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

    $viewer.addBaseLayer([tdtVec, tdtCva])
    $viewer.addBaseLayer([tdtImg, tdtCia])
    $viewer.addBaseLayer([gdVec, tdtCva])
    $viewer.addBaseLayer([gdImg, tdtCia])
    $viewer.changeBaseLayer(1)
}

export {getBaseLayer, changeBaseLayer}

