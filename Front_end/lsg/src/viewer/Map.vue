<script setup>
import * as DC from '@dvgis/dc-sdk'

import JsonToWall from "../module/Map/JsonToWall.js";
import axios from "axios";
import MainPage from "./Map/MainPage.vue";


function initViewer(){
  let viewer = new DC.Viewer('viewer-container')
  window.viewer = viewer
  viewer.zoomToPosition(DC.Position.fromArray([115.9800, 29.5210, 4000, 360, -45]))
  let key = "8899fd3e86aa994f71465b1c56a98727"
  let tdtImg = DC.ImageryLayerFactory.createImageryLayer(DC.ImageryType.XYZ,{
    url: "https://t0.tianditu.gov.cn/DataServer?T=img_w&x={x}&y={y}&l={z}&tk="+key,
    maximumLevel:18,
  })
  let tdtCia = DC.ImageryLayerFactory.createImageryLayer(DC.ImageryType.XYZ,{
    url: "https://t0.tianditu.gov.cn/DataServer?T=cia_w&x={x}&y={y}&l={z}&tk="+key,
    maximumLevel:18,
  })
  viewer.addBaseLayer([tdtImg, tdtCia])

  let areaLayer = new DC.VectorLayer("areaLayer")
  viewer.addLayer(areaLayer)
  axios.get("api/jsonData/roi.json").then((res) => {
    res.data.forEach(item => {
      let polyline = new DC.Polyline(item.feature)
      polyline.setStyle({
        width: 5,
        material: DC.Color.RED,
        clampToGround: true
      })
      areaLayer.addOverlay(polyline)
    })
  })
  // JsonToWall(areaLayer, "api/jsonData/roi.json")

  let tile3dLayer = new DC.TilesetLayer("3Dtiles")
  viewer.addLayer(tile3dLayer)

  let tileset1 = new DC.Tileset("./api/3Dtiles/tileset.json")
  // tileset1.setHeight(0, true)
  tile3dLayer.addOverlay(tileset1)

  let ter =  DC.TerrainFactory.createUrlTerrain({
    url: "https://data.mars3d.cn/terrain"
  })
  viewer.setTerrain(ter)

}

DC.ready().then(initViewer)

</script>

<template>
  <div class="viewer-container" id="viewer-container">
    <div class="content">
      <MainPage></MainPage>
    </div>
  </div>
</template>

<style scoped>


#viewer-container {
  width: 100%;
  height: 100%;
  position: absolute;
}
</style>