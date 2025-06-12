<script setup>
import {faCalculator, faMapPin, faDownload} from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

import {inject} from "vue";

const tools = {
  "图上量算": faCalculator,
  "坐标定位": faMapPin,
  "场景导出": faDownload
}
const changeBarTool = inject("changeBarTool")

function exportScene(){
  $viewer.exportScene("scene")
}

</script>

<template>
  <ul class="tool-list-box">
    <li v-for="(img, name) in tools"
        @click="name==='场景导出'?exportScene():changeBarTool(name)"
    >
      <font-awesome-icon :icon="img" />{{name}}
    </li>
  </ul>
</template>

<style scoped>
.tool-list-box{
  position: absolute;
  right: 540px;
  z-index: 101;
  top: 152px;
  background: #3f4854b3;
  pointer-events: auto;
}
.tool-list-box li:first-child {
  margin-top: 0;
}
.tool-list-box li{
  padding: 6px 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: #fff;
  cursor: pointer;
}
.tool-list-box li:hover{
  background-color: #4DB3FF;
}
:deep(.svg-inline--fa){
  margin-right: 5px;
}
</style>