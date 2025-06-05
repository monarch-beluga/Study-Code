<script setup>

</script>

<template>
<div class="right-container">
  <slot name="content"></slot>
</div>
</template>

<style scoped>
.right-container {
  right: 0;
  display: flex;
  flex-direction: column;
  position: absolute;
  top: 0;
  width: 408px;
  height: 100%;
  pointer-events: auto;
  background: #1c73c333;
}
</style>