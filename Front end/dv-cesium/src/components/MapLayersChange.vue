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
        label: "事故应急池",
        children: []
      },
      {
        id: 7,
        label: "初期雨水池",
        children: []
      },
      {
        id: 8,
        label: "污水处理站",
        children: []
      },
      {
        id: 9,
        label: "坑塘",
        children: []
      },
      {
        id: 10,
        label: "闸坝",
        children: []
      },
      {
        id: 11,
        label: "人工渠",
        children: []
      },
      {
        id: 12,
        label: "水库",
        children: []
      },
      {
        id: 13,
        label: "桥梁",
        children: []
      },
      {
        id: 17,
        label: "湿地",
        children: []
      },
      {
        id: 18,
        label: "管道",
        children: []
      }
    ],
  },
  {
    id: 14,
    label: "风险源",
    children: [
      {
        id: 15,
        label: "一般",
        children: []
      },
      {
        id: 16,
        label: "较大",
        children: []
      },
      {
        id: 19,
        label: "危化品路线",
        children: []
      }
    ]
  },
  {
    id: 20,
    label: "河流水系",
    children: []
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

const showKzqjLayer = inject("showKzqjLayer")

const showKtLayer = inject("showKtLayer")

const showQyfbLayer = inject("showQyfbLayer")

const showYjkjLayer = inject("showYjkjLayer")

const showRsLayer = inject("showRsLayer")

const showSgLayer = inject("showSgLayer")

const showGqLayer = inject("showGqLayer")

const showLineLayer = inject("showLineLayer")

function layerChangeShow(e, check){
  switch(e.id){
    case 1:
    case 4:
      showInitLayer(e.id, check)
      break
    case 5:
      showKzqjLayer(e.id, check)
      break
    case 2:
      showQyfbLayer(e.id, check)
      break
    case 9:
    case 12:
    {
      showYjkjLayer(e.id, check)
      showKtLayer(e.id, check)
    }
      break
    case 11:
    {
      showYjkjLayer(e.id, check)
      showGqLayer(e.id, check)
    }
      break
    case 6:
    case 7:
    case 8:
    case 10:
    case 13:
    case 17:
      showYjkjLayer(e.id, check)
      break
    case 18:
      showSgLayer(e.id, check)
      break
    case 19:
    case 20:
      showLineLayer(e.id, check)
      break
    case 15:
    case 16:
      showRsLayer(e.id, check)
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
        :default-checked-keys="[1, 4]"
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