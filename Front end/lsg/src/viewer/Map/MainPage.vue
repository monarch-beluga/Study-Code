<script setup>

import {useRouter} from "vue-router";

const router = useRouter();

</script>

<template>
  <div :class="router.currentRoute.value.path.startsWith('/map/main')?'main-content':'main-content-sub'" id="MainContent">
    <div class="w100 h100 relative">
      <router-view/>
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