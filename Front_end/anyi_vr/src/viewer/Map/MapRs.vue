<script setup>
import {inject, onMounted, onUnmounted} from "vue";
import RsRightContainer from "../../components/RsRightContainer.vue";

const MapLayerTreeChange = inject("MapLayerTreeChange")
const initMainMapLayer = inject("initMainMapLayer")
onMounted(()=>{
  MapLayerTreeChange(15, true)
  MapLayerTreeChange(16, true)
  MapLayerTreeChange(19, true)
})

onUnmounted(() => {
  try{
    initMainMapLayer()
  }catch (err){

  }
})
</script>

<template>
  <RsRightContainer></RsRightContainer>
</template>

<style scoped>

</style>