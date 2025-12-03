<script setup>
import * as DC from '@dvgis/dc-sdk'
import {getParkScopeLayer} from "../module/Map/ParkScope.js";
import {getBaseLayer} from "../module/Map/BaseLayer.js";
import MainPage from "./Map/MapPage.vue";
import setTer from "../module/Map/TerrainLayer.js";
import {getTilesetLayer} from "../module/Map/TilesetLayer.js";
import {ref} from "vue";

const mapLayerTree = ref("")
const loading = ref(false)
function initViewer(){
  let viewer = new DC.Viewer('viewer-container')
  window.$viewer = viewer
  viewer.zoomToPosition(DC.Position.fromArray([113.6710986691894, 27.60570497563303, 9000, 360, -90]))

  getBaseLayer()

  getTilesetLayer()

  setTer(true)

  getParkScopeLayer()

  loading.value = true
}

DC.ready().then(initViewer)
</script>

<template>
  <div class="viewer-container" id="viewer-container">
    <div class="content">
      <MainPage ref="mapLayerTree" v-if="loading"></MainPage>
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