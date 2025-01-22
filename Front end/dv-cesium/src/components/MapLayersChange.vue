<script setup>
import {ref} from 'vue'
import {inject} from 'vue'

const defaultProps = {
  children: 'children',
  label: 'label',
}
const data = [
  {
    id: 1,
    label: '园区倾斜摄影',
    children: [],
  },
  {
    id: 2,
    label: '企业分布',
    children: [],
  },
  {
    id: 3,
    label: '应急空间',
    children: [
      {
        id: 6,
        label: "应急池",
        children: []
      },
      {
        id: 7,
        label: "阀门",
        children: []
      },
      {
        id: 8,
        label: "水库",
        children: []
      },
      {
        id: 9,
        label: "坑塘",
        children: []
      },
      {
        id: 10,
        label: "明渠",
        children: []
      },
      {
        id: 11,
        label: "桥梁",
        children: []
      },
      {
        id: 12,
        label: "湿地",
        children: []
      },
      {
        id: 13,
        label: "洼地",
        children: []
      },
      {
        id: 14,
        label: "闸坝",
        children: []
      },
    ],
  },
  {
    id: 4,
    label: "园区范围",
    children: []
  },
  {
    id: 5,
    label: "空中全景分布",
    children: []
  }
]

const mapTree = ref(null)
function mapTreeChange(index, check){
  mapTree.value.setChecked(index, check)
}
defineExpose({mapTreeChange})
const showInitLayer = inject("showInitLayer")

const showQyfbLayer = inject("showQyfbLayer")

const showYjkjLayer = inject("showYjkjLayer")

function layerChangeShow(e, check){
  switch(e.id){
    case 1:
    case 4:
    case 5:
      showInitLayer(e.id, check)
      break
    case 2:
      showQyfbLayer(e.id, check)
      break
    case 6:
    case 7:
    case 8:
    case 9:
    case 10:
    case 11:
    case 12:
    case 13:
    case 14:
      showYjkjLayer(e.id, check)
      break
  }
}

</script>

<template>
  <div class="tree-content">
    <el-tree
        class="tree-line"
        ref="mapTree"
        style="font-size:12px"
        :data="data"
        node-key="id"
        @check-change="layerChangeShow"
        show-checkbox
        highlight-current
        :default-expand-all="true"
        :default-checked-keys="[1, 4, 5]"
        :props="defaultProps"
    />

  </div>
</template>

<style scoped>
  .tree-content{
    min-width: 200px;
    padding: 10px;
  }
  .tree-content .el-tree {
    color: #fff;
    background: transparent;
  }
</style>