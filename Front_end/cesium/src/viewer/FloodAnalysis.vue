<script setup>

import {FloodAnalysis} from "../utils/FloodAnalysis.js";
import {onMounted, ref} from "vue";
import {mapManager} from "../utils/mapManager.js";


const isAnimating = ref(false);
const hasStarted = ref(false);
let floodHandler = null;
let viewer = null;

function handleStart(){
  const array = [115.605207,
    27.909986,
    115.604863,
    27.912717,
    115.613359,
    27.921818,
    115.625288,
    27.921666,
    115.629408,
    27.912792,
    115.628378,
    27.904601,
    115.622113,
    27.899139,
    115.617736,
    27.894436,
    115.609669,
    27.894057,
    115.606236,
    27.902022,
    115.605207,
    27.909986]

  if (!hasStarted.value) {
    // 第一次启动
    floodHandler.start(array, {
      minHeight: 35,
      maxHeight: 75,
      duration: 5
    });
    hasStarted.value = true;
    isAnimating.value = true;
  } else {
    // 切换暂停/播放状态
    isAnimating.value = !isAnimating.value;

  }
  // 切换 Cesium 时钟的运行状态
  viewer.clock.shouldAnimate = isAnimating.value;
}

const handleStop = () => {
  floodHandler.stop();
  hasStarted.value = false;
  isAnimating.value = false;
  // 重置时钟
  viewer.clock.shouldAnimate = false;
};

onMounted(() => {
  viewer = mapManager.getViewer();
  floodHandler = new FloodAnalysis(viewer);
})

</script>

<template>
  <div class="flood-controls">
    <el-card class="box-card">

      <div class="button-group">
        <el-button
            :type="isAnimating ? 'warning' : 'primary'"
            @click="handleStart"
        >
          {{ isAnimating ? '暂停' : '开始' }}
        </el-button>

        <el-button
            type="danger"
            :disabled="!hasStarted"
            @click="handleStop"
        >
          清理
        </el-button>
      </div>

    </el-card>
  </div>
</template>

<style scoped>
.flood-controls {
  position: absolute;
  top: 20px;
  right: 20px;
  z-index: 100;
  width: 180px;
}

.button-group {
  display: flex;
  justify-content: space-between;
}
</style>