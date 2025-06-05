<script setup>

import MainContent from "./MainContent.vue";

</script>

<template>
 <div class="w100 h100 relative main-content" id="MainContent">
   <MainContent></MainContent>
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
  background: url('/images/header.png') no-repeat center / 100% 100%, url('/images/pro-bg.png') center center / 100% 100% no-repeat, rgb(0, 0, 0);
}
</style>