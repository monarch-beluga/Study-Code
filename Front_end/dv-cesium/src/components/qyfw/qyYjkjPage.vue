<script setup>
import {inject, toRefs} from "vue";

const showQyYjkjLayer = inject("showQyYjkjLayer");
const props = defineProps({
  info: String
})
const {info} = toRefs(props)

showQyYjkjLayer(info.value)
</script>

<template>

</template>

<style scoped>

</style>