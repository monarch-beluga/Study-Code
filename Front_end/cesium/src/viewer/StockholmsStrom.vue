<script setup>

import {onMounted} from "vue";
import {mapManager} from "@/utils/mapManager.js";
import {createBoxPrimitive, createMaterialAppearance } from "@/utils/ZippyZaps.js";
import * as Cesium from "cesium";

let viewer = null;



onMounted(() => {
  viewer = mapManager.getViewer();
  const scene = viewer.scene;

  viewer.clock.currentTime.secondsOfDay = 65398;
  scene.globe.enableLighting = true;
  scene.fog.enabled = true;

  let lon = 115.614
  let lat = 27.870
  let height = 100

  const destination = Cesium.Cartesian3.fromDegrees(lon, lat, height);

  let lastTime = Date.now();
  const appearance = createMaterialAppearance();
  const primitive = createBoxPrimitive(destination, appearance);
  scene.preRender.addEventListener(() => {
    const now = Date.now();
    appearance.material.uniforms.iTime += (now - lastTime) / 1000;
    lastTime = now;
  });

  viewer.scene.primitives.add(primitive);
  viewer.camera.lookAt(
      destination,
      new Cesium.HeadingPitchRange(6.283185307179577, -0.4706003213405664, 100)
  );
})



</script>

<template>

</template>

<style scoped>

</style>