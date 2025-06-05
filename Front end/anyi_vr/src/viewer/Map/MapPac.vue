<script setup>
import {inject, onMounted, onUnmounted, ref, provide} from "vue";
import PacLeftContainer from "../../components/PacLeftContainer.vue";
import {removePacLayer, showPacLayer} from "../../module/Map/PacLayer.js";
import PacRightContainer from "../../components/PacRightContainer.vue";

const initMainMapLayer = inject("initMainMapLayer")
const pacRight = ref("")

function changePacRightContent(index){
  pacRight.value.currIndex = index
}
provide("changePacRightContent", changePacRightContent)

onMounted(async () => {
  await showPacLayer("1", true)
})
onUnmounted(() => {
  try{
    initMainMapLayer()
    removePacLayer()
  }catch (err){

  }
})
</script>

<template>
  <PacLeftContainer></PacLeftContainer>
  <PacRightContainer ref="pacRight"></PacRightContainer>
</template>

<style scoped>

</style>