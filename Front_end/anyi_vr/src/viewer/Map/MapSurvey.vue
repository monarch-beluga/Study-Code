<script setup>
import SurveyLeftContainer from "../../components/SurveyLeftContainer.vue";
import SurveyRightContainer from "../../components/SurveyRightContainer.vue";
import {onUnmounted, inject, onMounted} from "vue"

const MapLayerTreeChange = inject("MapLayerTreeChange")
const initMainMapLayer = inject("initMainMapLayer")

onMounted(()=>{
  MapLayerTreeChange(5, true)
})

onUnmounted(()=>{
  try{
    initMainMapLayer()
  }catch (err){

  }
})
</script>

<template>
  <SurveyLeftContainer></SurveyLeftContainer>
  <SurveyRightContainer></SurveyRightContainer>
</template>

<style scoped>


</style>