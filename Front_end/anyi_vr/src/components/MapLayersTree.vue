<script setup>
import MapLayersChangeBox from "../common/MapLayersChangeBox.vue";
import {faCubes} from "@fortawesome/free-solid-svg-icons";
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";
import {showTilesetLayer} from "../module/Map/TilesetLayer.js";
import {showBusinessesLayer} from "../module/Map/Business.js";
import {
  showSpaceDitchLayerByType,
  showSpaceHtmlLayerByType,
  showSpaceLayerByType,
  showSpacePipeLayerByType
} from "../module/Map/SpaceLayer.js";
import {ref} from 'vue'
import {showPanoLayer} from "../module/Map/PanoramicLayer.js";
import {showParkScopeLayer} from "../module/Map/ParkScope.js";
import {showRsLayer} from "../module/Map/RsLayer.js";
import {showHCRLayer} from "../module/Map/HCRLayer.js";
import {showRiverLayer} from "../module/Map/RiverLayer.js";

const defaultProps = {
  children: 'children',
  label: 'label'
}

const data = [
  {
    id: 1,
    label: "园区倾斜摄影",
    children: []
  },
  {
    id: 2,
    label: "企业分布",
    children: []
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
const mapLayerTree = ref("")

function MapLayerTreeChange(index, check){
  mapLayerTree.value.setChecked(index, check)
}
defineExpose({MapLayerTreeChange})

async function layerChangeShow(e, checked){
  switch(e.id){
    case 1:
      showTilesetLayer(checked)
      break
    case 2:
      await showBusinessesLayer(checked)
      break
    case 6:
    case 7:
    case 8:
    case 10:
    case 13:
    case 17:
      await showSpaceHtmlLayerByType(e.id, checked)
      break
    case 9:
    case 12:
      await showSpaceLayerByType(e.id, checked)
      break
    case 11:
      await showSpaceDitchLayerByType(e.id, checked)
      break
    case 18:
      await showSpacePipeLayerByType(e.id, checked)
      break
    case 5:
      await showPanoLayer(checked)
      break
    case 4:
      showParkScopeLayer(checked)
      break
    case 15:
    case 16:
      await showRsLayer(e.id, checked)
      break
    case 19:
      await showHCRLayer(checked)
      break
    case 20:
      await showRiverLayer(checked)
      break
  }
}

</script>

<template>
  <MapLayersChangeBox>
    <template #title>
      <div class="name"><span><font-awesome-icon :icon="faCubes"/>图层</span></div>
    </template>
    <template #content>
      <div class="tree-content">
        <el-tree
            class="tree-line"
            ref="mapLayerTree"
            :data="data"
            node-key="id"
            show-checkbox
            @check-change="layerChangeShow"
            :default-expand-all="true"
            :default-checked-keys="[1, 4]"
            :props="defaultProps"
        />
      </div>
    </template>
  </MapLayersChangeBox>

</template>

<style scoped>
.tree-content{
  min-width: 200px;
  padding: 10px;
}
.el-tree {
  color: #fff;
  background: transparent;
}
.el-tree :deep(.el-text) {
  color: #fff;
  font-size: 12px;
}
:deep(.el-tree .el-tree-node:hover>.el-tree-node__content:hover){
  background-color: #0074b7 !important;
}

:deep(.el-tree .el-tree-node:focus>.el-tree-node__content){
  background-color: #0074b7 !important;
}
:deep(.svg-inline--fa){
  margin-right: 5px;
}
</style>