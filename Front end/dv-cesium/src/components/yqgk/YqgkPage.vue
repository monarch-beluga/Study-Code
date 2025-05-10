<script setup>

import YqgkRightCon from "./YqgkRightCon.vue";
import YqgkLeftCon from "./YqgkLeftCon.vue";

</script>

<template>
  <div class="container page-container">
    <div class="left-container">
      <YqgkLeftCon></YqgkLeftCon>
    </div>

    <YqgkRightCon></YqgkRightCon>
  </div>
</template>

<style scoped>
.page-container .left-container {
  display: flex;
  flex-direction: column;
  position: absolute;
  top: 0;
  width: 408px;
  height: 100%;
  pointer-events: auto;
  background: #1c73c333;
}
.left-container>div{
  display: flex;
  flex-direction: column;
}
</style>