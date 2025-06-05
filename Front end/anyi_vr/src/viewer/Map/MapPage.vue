<script setup>
import * as DC from '@dvgis/dc-sdk'
import ToolBarRight from "../../components/ToolBarRight.vue";

import {useRouter} from "vue-router";
import PanoramicContainer from "../../components/PanoramicContainer.vue";
import {provide, ref, onMounted} from "vue";
import {stopSpeak} from "../../module/Map/SpeechText.js";

const router = useRouter();
const mapLayerTree = ref("")
function MapLayerTreeChange(index, check){
  mapLayerTree.value.MapLayerTreeChange(index, check)
}
provide("MapLayerTreeChange", MapLayerTreeChange)

function initMainMapLayer(){
  $viewer.zoomToPosition(DC.Position.fromArray([115.6493, 28.79954, 7000, 360, -45]))
  for (let i=1; i<21;i++){
    if (i===1 || i===4)
      continue
    MapLayerTreeChange(i, false)
  }
  stopSpeak()
}
provide("initMainMapLayer", initMainMapLayer)

const speechSynthesis = window.speechSynthesis;
const voices = ref([]);
const voice = ref(null);
onMounted(()=>{
  setTimeout(() => {
    voices.value = speechSynthesis.getVoices();
    voice.value = voices.value.find(v => v.lang.includes('zh')) || voices.value[0];
  }, 100);
})

</script>

<template>
  <div :class="router.currentRoute.value.path.startsWith('/map/sub')?'main-content-sub':'main-content'" id="MainContent">
    <ToolBarRight ref="mapLayerTree"></ToolBarRight>
    <PanoramicContainer></PanoramicContainer>
    <div class="w100 h100 relative">
      <div class="container page-container">
        <router-view/>
      </div>
    </div>
  </div>
</template>

<style scoped>
.main-content{
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 99;
  unicode-bidi: isolate;
  pointer-events: none;
  background: url('/images/header.png') no-repeat center / 100% 100%, url('/images/pro-bg.png') no-repeat center / 100% 100%;
}
.main-content-sub{
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 99;
  unicode-bidi: isolate;
  pointer-events: none;
  background: url('/images/wrapper-box-bg.png') no-repeat center / 100% 100%, url('/images/pro-bg.png') no-repeat center / 100% 100%;
}
</style>