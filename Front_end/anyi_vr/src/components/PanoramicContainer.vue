<script setup>
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";
import {faClose} from "@fortawesome/free-solid-svg-icons";
import {closePano, getIframeSrc, getPanoShow, getPanoTitle} from "../module/Map/PanoramicLayer.js";
</script>

<template>
  <div class="panorama-container" v-show="getPanoShow()">
    <div class="title">
      <div ref="title_text">{{getPanoTitle()}}</div>
      <div class="close cursor-p" @click="closePano()">
        <font-awesome-icon :icon="faClose" />
      </div>
    </div>
    <div class="content">
      <iframe ref="iframe" class="w100 h100" :src="getIframeSrc()" allow="xr-spatial-tracking"></iframe>
    </div>
  </div>
</template>

<style scoped>
.panorama-container{
  display: flex;
  flex-direction: column;
  position: fixed;
  inset: 0;
  z-index: 999;
  background: transparent;
  background-color: #000;
  pointer-events: auto;
  box-shadow: inset 0 0 200px #0377eb;
}

.panorama-container .title{
  padding: 0 10px;
  display: flex;
  justify-content: space-between;
  height: 44px;
  line-height: 44px;
  color: #fff;
}

.panorama-container .content{
  padding: 0 10px 10px;
  width: 100%;
  height: 0;
  flex: 1;
}
</style>