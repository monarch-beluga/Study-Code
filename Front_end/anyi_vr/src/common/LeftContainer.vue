<script setup>

</script>

<template>
  <div class="left-container">
    <slot name="content"></slot>
  </div>
</template>

<style scoped>
.left-container {
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