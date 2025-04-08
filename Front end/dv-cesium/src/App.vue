<script setup>
import MapPage from "./components/MapPage.vue";
import './divIcon.css'
import {provide, ref} from "vue";
import ZztPage from "./components/ZztPage.vue";
import TablePage from "./components/TablePage.vue";

let currTab = ref("应急空间")
const tabs = {
  "园区概况": MapPage,
  "风险源": ZztPage,
  "应急空间": MapPage,
  "应急物资": TablePage,
  "三级防控": MapPage,
  "360全景": MapPage,
  "突发事件模拟": MapPage,
  "救援队伍": TablePage,
  "作战图": ZztPage,
}
function changePage(tab){
  currTab.value = tab
}
provide("changePage", changePage)

</script>

<template>
  <div class="wrapper">
    <component :is="tabs[currTab]" :info="currTab"></component>
  </div>
</template>

<style scoped>
.wrapper{
  height: 100%;
  width: 100%;
  position: relative;
}
</style>
