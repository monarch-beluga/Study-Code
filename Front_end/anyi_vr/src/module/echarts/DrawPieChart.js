import * as echarts from 'echarts';

function drawPieChart(chartContainer, data, count) {
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
                radius: ['50%', '80%'],
                center: ['60%', '50%'],
                avoidLabelOverlap: true,
                data: data,
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
                    fontSize: 20,
                    fontWeight: 'bold'
                }
            },
            {
                type: 'text',
                left: '55%',
                top: '50%',  // 垂直位置
                style: {
                    text: count.toString(),
                    textAlign: 'center',
                    fill: '#ffffff',
                    fontSize: 24,
                    fontWeight: 'bold'
                }
            }
        ]
    };
    const chartInstance = echarts.init(chartContainer.value)
    chartInstance.setOption(option)
}

export default drawPieChart

