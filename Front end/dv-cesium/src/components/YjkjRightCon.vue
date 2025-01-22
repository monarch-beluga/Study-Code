<script setup>

import YjkjRightConBox from "./YjkjRightConBox.vue";
import {ref} from "vue";

const rightConBox = ref(null)
function mapDataChange(index){
  rightConBox.value.getYjkjData(index)
}
defineExpose({mapDataChange})

</script>

<template>
<div class="right-container">
  <div class="data box h0 flex-1">
    <div class="title-box">
      <div class="title">应急空间信息</div>
    </div>
    <div class="context-box">
      <YjkjRightConBox ref="rightConBox"></YjkjRightConBox>
    </div>
  </div>
</div>
</template>

<style scoped>
.right-container {
  right: 0;
}
.page-container .left-container>div, .page-container .right-container>div {
  display: flex;
  flex-direction: column;
}
.page-container .right-container {
  display: flex;
  flex-direction: column;
  position: absolute;
  top: 0;
  width: 408px;
  height: 100%;
  pointer-events: auto;
  background: #1c73c333;
}
.page-container .right-container>div {
  display: flex;
  flex-direction: column;
}
.right-container>div .title-box {
  position: relative;
  height: 38px;
  line-height: 38px;
  background: url("/images/title-box.png") no-repeat center / 100% 100%;
}
.title-box .title {
  margin-left: 30px;
  text-align: left;
  font-size: 18px;
  font-family: Alibaba PuHuiTi;
  font-weight: 700;
  font-style: italic;
  color: transparent;
  text-shadow: 0px 2px 8px rgba(5, 28, 55, .42);
  background-image: linear-gradient(180deg, #0ec5ec5c 5%, #31beff5c 20%, #fff 40%);
  -webkit-background-clip: text;
}


</style>