<script setup>
  import * as Cesium from 'cesium'
  import "./Widgets/widgets.css"
  import {onMounted} from 'vue'

  Cesium.Ion.defaultAccessToken = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJmZTg2NjE4OC00MDdlLTQ5MTAtOWE1Yi01ODE4NDNmZTg0NGYiLCJpZCI6MjY3MzcyLCJpYXQiOjE3MzYyNTE1MjZ9.rNEN-2zDT2yCOXP1T4yyr6axw7mM_Y-28e8hGvUzPdg'

  window.CESIUM_BASE_URL = '/';

  onMounted(function () {
    let viewer = new Cesium.Viewer('cesiumContainer', {
      // 取消cesium默认控件
      infoBox: false,
      homeButton: false,
      geocoder: false,
      sceneModePicker: false,
      baseLayerPicker: false,
      navigationHelpButton: false,
      animation: false,
      timeline: false,
      fullscreenButton: false,
    })
    // 隐藏loge
    viewer.cesiumWidget.creditContainer["style"].display = 'none';

  })

</script>

<template>
  <div id="cesiumContainer" ref="cesiumContainer"></div>
</template>

<style scoped>

#cesiumContainer{
  width: 100%;
  height: 100%;
}

</style>
