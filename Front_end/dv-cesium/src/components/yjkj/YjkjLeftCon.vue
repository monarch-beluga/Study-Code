<script setup>
import {inject, ref} from 'vue'

let curr = ref("事故应急池")
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
const mapTreeChange = inject("mapTreeChange")
const mapDataChange = inject("mapDataChange")
function labelFun(index, i) {
  if (index !== i) {
    mapTreeChange(i, false)
    mapTreeChange(index, true)
    mapDataChange(index)
  }
}
</script>

<template>
  <div class="tablist h100">
    <div
      v-for="(index, label) in labels"
      :key="label"
      :class="['cursor-p', {on: curr === label}]"
      @click="labelFun(index, labels[curr]);curr = label;"
      >
      <div class="label-box">
        {{label}}
      </div>
    </div>
  </div>
</template>

<style scoped>
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