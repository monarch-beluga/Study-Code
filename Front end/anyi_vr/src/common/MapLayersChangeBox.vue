<script setup>

import {faClose} from "@fortawesome/free-solid-svg-icons";
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";
import {inject} from "vue";
const toolClose = inject("toolClose");
</script>

<template>
  <div class="map-layers-change-box">
    <div class="title">
      <slot name="title"></slot>
      <div class="close cursor-p" @click="toolClose">
        <font-awesome-icon :icon="faClose" />
      </div>
    </div>
    <div class="content">
      <slot name="content"></slot>
    </div>
  </div>
</template>

<style scoped>
.map-layers-change-box{
  position: absolute;
  right: 540px;
  z-index: 99;
  top: 152px;
  border: 1px solid #4081CB;
  border-radius: 4px;
  background: #1e243299;
  box-shadow: inset 0 3px 7px #2a8aecf2;
  pointer-events: auto;
  color: #fff;
}
.map-layers-change-box .title{
  display: flex;
  justify-content: space-between;
  padding: 0 10px;
  border-bottom: 1px solid;
  border-color: #20a0ff4d;
  height: 40px;
  line-height: 40px;
  color: #fff;
  font-size: 16px;
}
</style>