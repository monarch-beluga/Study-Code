<script setup>
import {onMounted, onUnmounted} from "vue"
import * as DC from '@dvgis/dc-sdk'
import {getSpaceData} from "../../module/Map/SpaceLayer.js";
import {getCurrBusiness} from "../../module/Map/Business.js";
import {getPacLayer} from "../../module/Map/PacLayer.js";

function getSpaceDataByFirmName(data, firmName){
  return data.filter(item => item.firmName === firmName)
}

const layerName = "qy_yjkj"
const vLayerName = "vqy_yjkj"

onMounted(async ()=>{
  const data = await getSpaceData()
  const dataByFirmName = getSpaceDataByFirmName(data, getCurrBusiness())
  let layer = new DC.HtmlLayer(layerName).addTo($viewer)
  let vLayer = new DC.VectorLayer(vLayerName).addTo($viewer)
  dataByFirmName.forEach(item => {
    getPacLayer(item, layer, vLayer)
  })
})

onUnmounted(() => {
  $viewer.getLayer(layerName).remove()
  $viewer.getLayer(vLayerName).remove()
})

</script>

<template>

</template>

<style scoped>

</style>