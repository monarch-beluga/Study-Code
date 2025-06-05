<script setup>
import {inject, onMounted, onUnmounted, ref, provide} from "vue";
import SpaceLeftContainer from "../../components/SpaceLeftContainer.vue";
import SpaceRightContainer from "../../components/SpaceRightContainer.vue";

const MapLayerTreeChange = inject("MapLayerTreeChange")
const initMainMapLayer = inject("initMainMapLayer")


const spaceRight = ref("")
function initSpaceRightData(type){
  spaceRight.value.initData(type)
}
provide("initSpaceRightData",initSpaceRightData)

onMounted(()=>{
  MapLayerTreeChange(6, true)
})

onUnmounted(() => {
  try{
    initMainMapLayer()
  }catch (err){

  }
})
</script>

<template>
  <SpaceLeftContainer></SpaceLeftContainer>
  <SpaceRightContainer ref="spaceRight"></SpaceRightContainer>
</template>

<style scoped>

</style>