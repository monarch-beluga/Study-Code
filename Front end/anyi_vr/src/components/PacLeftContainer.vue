<script setup>
import { ref, inject } from "vue"
import LeftContainer from "../common/LeftContainer.vue";
import {showPacLayer} from "../module/Map/PacLayer.js";

const currIndex = ref("1")
const labels = {
  "一级防控": "1",
  "二级防控": "2",
  "三级防控": "3",
  "四级防控": "4",
}
const MapLayerTreeChange = inject("MapLayerTreeChange")
const changePacRightContent = inject("changePacRightContent")

function labelClick(index){
  showPacLayer(currIndex.value, false)
  if (index === "4"){
    MapLayerTreeChange(20, true)
  }else{
    MapLayerTreeChange(20, false)
  }
  showPacLayer(index, true)
  changePacRightContent(index)
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
  margin-top: 86px;
  padding: 10px;
  width: 64px;
  height: 64px;
  line-height: 64px;
  text-align: center;
  border-radius: 50%;
  box-shadow: inset 0 0 40px #409eff;
  color: #fff;
  box-sizing: content-box;
}
</style>