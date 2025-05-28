<script setup>
import {faClose} from "@fortawesome/free-solid-svg-icons";
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";
import {ref} from "vue";

const panShow = ref(false)
const title_text = ref(null)
const iframe = ref(null)
defineExpose({panShow, title_text, iframe})

</script>

<template>
  <div class="panorama-container" v-show="panShow">
    <div class="title">
      <div ref="title_text"></div>
      <div class="close cursor-p" @click="panShow=false">
        <font-awesome-icon :icon="faClose" />
      </div>
    </div>
    <div class="content">
      <iframe ref="iframe" class="w100 h100" src allow="xr-spatial-tracking"></iframe>
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