<script setup>
import SjfkLeftCon from "./SjfkLeftCon.vue";
import SjfkRightCon from "./SjfkRightCon.vue";
import {provide, ref} from "vue";

const rightCon = ref(null)
function changeData(level){
  rightCon.value.changeData(level)
}
provide("changeData", changeData)
</script>

<template>
  <div class="container page-container">
    <div class="left-container cur-container">
      <SjfkLeftCon></SjfkLeftCon>
    </div>
    <SjfkRightCon ref="rightCon"></SjfkRightCon>
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