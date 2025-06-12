<script setup>
import * as echarts from 'echarts';
import axios from "axios";
import {inject, onMounted, ref} from "vue";

const staticData = inject("staticData");

const chartContainer1 = ref(null)
const chartContainer2 = ref(null)
const chartContainer3 = ref(null)


const getStaticData = async(jsonPath) => {
  let url = staticData.api + jsonPath;
  let data = []
  await axios.get(url).then((response) => {
    data = response.data
  })
  return data
}

let chartInstance1 = null
let chartInstance2 = null
let chartInstance3 = null

let option = {
  tooltip: {
    trigger: 'item'
  },
  legend: {
    orient: 'vertical',
    top: 'center',
    textStyle: {
      color: '#ffffff'  // 文字颜色
    },
    left: '5%'
  },
  series: [
    {
      type: 'pie',
      radius: ['40%', '70%'],
      center: ['60%', '50%'],
      avoidLabelOverlap: true,
      label: {
        show: false,
      },
      emphasis: {
        label: {
          show: false
        }
      },
      labelLine: {
        show: false
      },
    }
  ],
  graphic: [
    {
      type: 'text',
      left: '55%',
      top: '40%',  // 垂直位置
      style: {
        text: '总数',
        textAlign: 'center',
        fill: '#ffffff',
        fontSize: 14,
        fontWeight: 'bold'
      }
    },
    {
      type: 'text',
      left: '55%',
      top: '50%',  // 垂直位置
      style: {
        textAlign: 'center',
        fill: '#ffffff',
        fontSize: 28,
        fontWeight: 'bold'
      }
    }
  ]
};

const initChart = async() => {
  const chartData1 = await getStaticData("/jsonData/anyi_yqjy_StatisticData.json")
  chartInstance1  = echarts.init(chartContainer1.value)
  let x_data = []
  let y_data = []
  let colors = ["#9370db", "#ff6b6b", "#66bb6a", "#42a5f5", "#ab47bc", "#ffd54f", "#ff85c0", "#9ccc65", "#ffa726", "#78909c", "#5470c6"]
  chartData1.forEach((item) => {
    x_data.push(item.name)
    y_data.push(item.value)
  })
  let option1 = {
    tooltip: {
      trigger: 'item'
    },
    grid: {
      show: false,
      top: '5%',
      left: '8%',
      right: '4%',
      bottom: '4%',  // 为倾斜标签留出更多底部空间
      containLabel: true
    },
    xAxis: {
      type: 'category',
      data: x_data,
      axisLine: {
        lineStyle: {
          color: "#fff"
        },
      },
      axisTick: {
        alignWithLabel: true
      },
      axisLabel: {
        interval: 0,
        rotate: 45
      },
      splitLine: {
        show: false
      }
    },
    yAxis: {
      type: 'value',
      splitLine: {
        show: false
      },
      axisLine: {
        show: true,
        lineStyle: {
          color: "#fff"
        },
      },
    },
    series: [
      {
        data: y_data,
        itemStyle: {
          color: function(params) {
            return colors[params.dataIndex]
          }
        },
        barWidth: '80%',
        type: 'bar'
      }
    ]
  };
  chartInstance1.setOption(option1)

  const chartData2 = await getStaticData("/jsonData/anyi_yjkj_StatisticData.json")
  chartInstance2  = echarts.init(chartContainer2.value)
  let totalValue2 = 0;
  chartData2.forEach((record) => {
    totalValue2 += record.value;
  })
  let option2 = option;
  option2.series[0].data = chartData2;
  option2.graphic[1].style.text = totalValue2.toString();
  chartInstance2.setOption(option2)

  const chartData3 = await getStaticData("/jsonData/anyi_rs_StatisticData.json")
  chartInstance3  = echarts.init(chartContainer3.value)
  let totalValue3 = 0;
  chartData3.forEach((record) => {
    totalValue3 += record.value;
  })
  let colors3 = ["#ffff00", "#ffa500"]
  let option3 = {
    tooltip: {
      trigger: 'item'
    },
    legend: {
      orient: 'vertical',
      top: 'center',
      textStyle: {
        color: '#ffffff'  // 文字颜色
      },
      left: '5%'
    },
    series: [
      {
        type: 'pie',
        radius: ['40%', '70%'],
        center: ['60%', '50%'],
        avoidLabelOverlap: true,
        data: chartData3,
        itemStyle: {
          color: function(params) {
            return colors3[params.dataIndex]
          }
        },
        label: {
          show: false,
        },
        emphasis: {
          label: {
            show: false
          }
        },
        labelLine: {
          show: false
        },
      }
    ],
    graphic: [
      {
        type: 'text',
        left: '55%',
        top: '40%',  // 垂直位置
        style: {
          text: '总数',
          textAlign: 'center',
          fill: '#ffffff',
          fontSize: 14,
          fontWeight: 'bold'
        }
      },
      {
        type: 'text',
        left: '55%',
        top: '50%',  // 垂直位置
        style: {
          text: totalValue3.toString(),
          textAlign: 'center',
          fill: '#ffffff',
          fontSize: 28,
          fontWeight: 'bold'
        }
      }
    ]
  };
  chartInstance3.setOption(option3)
}
const resizeCharts = () => {
  chartInstance1?.resize()
  chartInstance2?.resize()
  chartInstance3?.resize()
}


onMounted(() => {
  initChart()
  window.addEventListener('resize', resizeCharts)
})

</script>

<template>
  <div class="data box h0 flex-1">
    <div class="title-box">
      <div class="title">
        救援队伍统计
      </div>
    </div>
    <div class="content-box">
      <div class="w100 h100" ref="chartContainer1" style="position: relative; left: 0px; top: 0px; height: 100%">

      </div>
    </div>
  </div>
  <div class="unit box h0 flex-1">
    <div class="title-box">
      <div class="title">
        应急空间统计
      </div>
    </div>
    <div class="content-box">
      <div class="w100 h100" ref="chartContainer2" style="position: relative; left: 0px; top: 0px; height: 100%">

      </div>
    </div>
  </div>
  <div class="fire box h0 flex-1">
    <div class="title-box">
      <div class="title">
        风险源统计
      </div>
    </div>
    <div class="content-box">
      <div class="w100 h100" ref="chartContainer3" style="position: relative; left: 0px; top: 0px; height: 100%">

      </div>
    </div>
  </div>
</template>

<style scoped>
.title-box{
  position: relative;
  height: 38px;
  line-height: 38px;
  background: url("/images/title-box.png") no-repeat center / 100% 100%;
}
.title-box .title {
  margin-left: 30px;
  text-align: left;
  font-size: 18px;
  font-family: Alibaba PuHuiTi;
  font-weight: 700;
  font-style: italic;
  color: transparent;
  -webkit-background-clip: text;
  text-shadow: 0px 2px 8px rgba(5, 28, 55, .42);
  background-image: linear-gradient(180deg, #0ec5ec5c 5%, #31beff5c 20%, #fff 40%);
}
.content-box{
  display: flex;
  flex-direction: column;
  height: calc(100% - 38px)
}

.h100{
  height: 100%;
}
.w100{
  width: 100%;
}
.h0{
  height: 0;
}
.flex-1{
  flex: 1;
}

</style>