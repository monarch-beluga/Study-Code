<script setup>
import {onMounted, onUnmounted, ref} from 'vue';
import { mapManager } from '../utils/mapManager';
import { setTerrain} from "../utils/cesiumTools.js";
import * as Cesium from "cesium";
import WaterSimulation from "../viewer/WaterSimulation.vue";
import FloodAnalysis from "../viewer/FloodAnalysis.vue";

const isLoaded = ref(false);

onMounted(async () => {
  let viewer = mapManager.init('cesiumContainer', {
    animation: false,       // 隐藏左下角动画控件
    timeline: false,        // 隐藏底部时间轴
    fullscreenButton: false, // 隐藏全屏按钮
    geocoder: false,        // 隐藏右上角查询按钮
    homeButton: false,      // 隐藏视角复位按钮
    sceneModePicker: false, // 隐藏 2D/3D 切换按钮
    navigationHelpButton: false, // 隐藏帮助按钮
    baseLayerPicker: false,  // 隐藏底图选择器

    shouldAnimate: true,

    infoBox: false,

    contextOptions: {
      requestWebgl2: true // 开启 WebGL2 性能更好
    },
    scene3DOnly: true,
    logarithmicDepthBuffer: true // 缓解远距离闪烁
  });

  viewer.shadows = true; // 开启阴影
  viewer.resolutionScale = 0.5; // 分辨率
  viewer.scene.msaaSamples = 4; // msaa
  viewer.scene.globe.depthTestAgainstTerrain = true; // 深度测试
  viewer.scene.logarithmicDepthBuffer = true; // log深度
  viewer.scene.highDynamicRange = true;
  viewer.scene.screenSpaceCameraController.enableCollisionDetection = false;


  viewer.camera.setView({
    // 1. 坐标转换：经纬度 -> 笛卡尔
    destination:Cesium.Cartesian3.fromDegrees(115.615, 27.875, 4000),

    // 2. 角度转换：角度 -> 弧度
    orientation: {
      heading: Cesium.Math.toRadians(0),
      pitch: Cesium.Math.toRadians(-45),
      roll: Cesium.Math.toRadians(0)
    }
  });

  viewer.scene.globe.depthTestAgainstTerrain = true;
  // 初始化 viewer

  await setTerrain("world", {
    requestVertexNormals: true, // 开启地形法线，用于产生光照阴影效果
    // requestWaterMask: true      // 开启水面特效
  })

  isLoaded.value = true;

  // const fluid = new FluidDemo(viewer, {})



});


onUnmounted(() => {
  mapManager.destroy(); // 记得清理，释放显存
});

</script>

<template>
  <div id="cesiumContainer">
<!--    <FloodAnalysis v-if="isLoaded"></FloodAnalysis>-->
    <WaterSimulation v-if="isLoaded"></WaterSimulation>
<!--    <StockholmsStrom v-if="isLoaded"></StockholmsStrom>-->
  </div>
</template>

<style scoped>

#cesiumContainer {
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
}

</style>