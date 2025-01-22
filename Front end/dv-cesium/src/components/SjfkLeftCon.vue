<script setup>
import {inject, ref} from "vue";

let curr = ref("一级防控")
const labels = {
  "一级防控": "1",
  "二级防控": "2",
  "三级防控": "3",
}
const showSjfkLayer = inject("showSjfkLayer")
const changeData = inject("changeData")
function labelFun(index, i) {
  if (index !== i) {
    showSjfkLayer(i, false)
    showSjfkLayer(index, true)
    changeData(index)
  }
}

</script>

<template>
  <div class="tablist h100">
    <div
        v-for="(index, label) in labels"
        :key="label"
        :class="['cursor-p', {on: curr === label}]"
        @click="labelFun(index, labels[curr]);curr = label;">
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