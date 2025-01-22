<script setup>
import YjkjLeftCon from "./YjkjLeftCon.vue";
import YjkjRightCon from "./YjkjRightCon.vue";
import {provide, ref} from "vue";

const rightCon = ref(null)
function mapDataChange(index){
  rightCon.value.mapDataChange(index)
}
provide("mapDataChange", mapDataChange)

</script>

<template>
  <div class="container page-container">
      <div class="left-container cur-container">
        <YjkjLeftCon></YjkjLeftCon>
      </div>

    <YjkjRightCon ref="rightCon"></YjkjRightCon>
  </div>
</template>

<style scoped>
.container{
  position: absolute;
  width: 100%;
  height: 100%;
}
.cur-container {
  background: transparent;
  pointer-events: none;
  display: flex;
  flex-direction: column;
  position: absolute;
  top: 0;
  height: 100%;
}
.left-container{
  width: auto;
}

</style>