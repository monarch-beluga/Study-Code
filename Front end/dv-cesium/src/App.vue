<script setup>
import MapPage from "./components/MapPage.vue";
import './divIcon.css'
import {provide, ref} from "vue";
import ZztPage from "./components/ZztPage.vue";

let currTab = ref("应急空间")
const tabs = {
  "应急空间": MapPage,
  "三级防控": MapPage,
  "360全景": MapPage,
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
