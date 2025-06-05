import * as echarts from 'echarts';

function drawBarChart(chartContainer, x_data, y_data) {
    let option = {
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
                barWidth: '80%',
                type: 'bar'
            }
        ]
    }
    const chartInstance = echarts.init(chartContainer.value)
    chartInstance.setOption(option)
}

export default drawBarChart


