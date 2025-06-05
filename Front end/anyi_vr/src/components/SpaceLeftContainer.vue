<script setup>
import { ref, inject } from "vue"
import LeftContainer from "../common/LeftContainer.vue";
const labels = {
  "事故应急池": 6,
  "初期雨水池": 7,
  "污水处理站": 8,
  "坑塘": 9,
  "闸坝": 10,
  "人工渠": 11,
  "水库": 12,
  "桥梁": 13,
  "湿地": 17,
  "管道": 18
}

const currIndex = ref(6)

const initSpaceRightData = inject("initSpaceRightData")
const MapLayerTreeChange = inject("MapLayerTreeChange")

function labelClick(index){
  MapLayerTreeChange(currIndex.value, false)
  MapLayerTreeChange(index, true)
  initSpaceRightData(index)
  currIndex.value = index
}

</script>

<template>
  <LeftContainer class="label">
    <template #content>
      <div class="tablist h100">
        <div
            v-for="(index, label) in labels"
            :class="['cursor-p', {on: currIndex === index}]"
            @click="labelClick(index)">
          <div class="label-box">
            {{label}}
          </div>
        </div>
      </div>
    </template>
  </LeftContainer>
</template>

<style scoped>
.label{
  background: transparent;
}
.tablist {
  display: flex;
  flex-direction: column;
  pointer-events: all;
}
.tablist>div.on {
  position: relative;
  box-shadow: inset 0 0 100px #2a8ef1;
}
.tablist>div{
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 10px;
  padding: 8px;
  width: 64px;
  height: 48px;
  border-radius: 50%;
  box-shadow: inset 0 0 40px #409eff;
  color: #fff;
  box-sizing: content-box;
  font-size: 12px;
}
</style>