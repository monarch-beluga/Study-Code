import * as Cesium from 'cesium';
import {TWaterMaterialAppearance, updateTWaterMaterial} from "../material/TileableWaterMaterial.js";

export class FloodAnalysis {
    constructor(viewer) {
        this.viewer = viewer;
        this.primitive = null;
        this._startTime = null;
        this.maxHeight = 100;
        this.minHeight = 0;
        this.duration = 10;

        // 绑定更新事件，Cesium 每一帧渲染前都会调用
        this.updateListener = this.onUpdate.bind(this);
    }

    /**
     * 开始淹没模拟
     * @param {Array} degreesArray 经纬度数组
     * @param options
     */
    start(degreesArray, options) {
        const {
            minHeight = 0,
            maxHeight = 100,
            duration = 10
        } = options;

        this.minHeight = minHeight;
        this.maxHeight = maxHeight;
        this.duration = duration;
        // 在 start 方法中确保每次重新开始都对齐当前时钟
        this._startTime = this.viewer.clock.currentTime.clone();

        // 1. 创建几何体实例 (GeometryInstance)
        const instance = new Cesium.GeometryInstance({
            geometry: new Cesium.PolygonGeometry({
                polygonHierarchy: new Cesium.PolygonHierarchy(
                    Cesium.Cartesian3.fromDegreesArray(degreesArray)
                ),
                height: minHeight,
                extrudedHeight: minHeight, // 初始拉伸高度
                vertexFormat: Cesium.EllipsoidSurfaceAppearance.VERTEX_FORMAT // 必须匹配外观格式
            }),
            id: 'flood_primitive'
        });

        // 2. 创建 Primitive 并应用 Water 材质
        // let appearance = TWaterMaterialAppearance();

        this.primitive = new Cesium.Primitive({
            geometryInstances: instance,
            // appearance: appearance,
            // 使用 EllipsoidSurfaceAppearance 以支持地形贴合和材质
            appearance: new Cesium.EllipsoidSurfaceAppearance({
                material: Cesium.Material.fromType('Water', {
                    baseWaterColor: new Cesium.Color(0.0, 0.5, 0.5, 0.4),
                    normalMap: Cesium.buildModuleUrl('Assets/Textures/waterNormals.jpg'),
                    frequency: 100.0,
                    animationSpeed: 0.02,
                    amplitude: 15.0,
                    specularIntensity: 0.5
                })
            }),
            asynchronous: false // 设为同步，防止初始化闪烁
        });

        this.viewer.scene.primitives.add(this.primitive);

        // 3. 注册帧监听事件，实现时间驱动的高度更新
        // this.viewer.scene.preRender.addEventListener(() => {
        //     updateTWaterMaterial(appearance)
        // });

        this.viewer.scene.preRender.addEventListener(this.updateListener);
    }

    /**
     * 每帧执行的更新函数
     */
    onUpdate() {
        if (!this.primitive) return;

        // 1. 获取当前场景时间
        const currentTime = this.viewer.clock.currentTime;
        // 计算从开始到现在经过的总秒数
        const diff = Cesium.JulianDate.secondsDifference(currentTime, this._startTime);

        // 2. 计算往返进度 (Ping-Pong 效果)
        // 假设 duration 是 10秒：0-10秒是涨水，10-20秒是退水
        const totalCycle = this.duration * 2; // 一个完整的涨退周期
        const timeInCycle = diff % totalCycle; // 当前处于周期的哪个位置

        let ratio;
        if (timeInCycle <= this.duration) {
            // 前半段：涨水 (0.0 -> 1.0)
            ratio = timeInCycle / this.duration;
        } else {
            // 后半段：退水 (1.0 -> 0.0)
            ratio = 1.0 - (timeInCycle - this.duration) / this.duration;
        }

        // 3. 增加缓动函数（可选，让水位到达顶端和底部时更平滑，不那么生硬）
        // 使用 Sine 缓动: ratio = (1 - Math.cos(ratio * Math.PI)) / 2;

        // 4. 计算当前高度
        const currentHeight = this.minHeight + (this.maxHeight - this.minHeight) * ratio;

        // 5. 应用平移矩阵
        const translation = Cesium.Cartesian3.fromElements(0, 0, currentHeight);
        this.primitive.modelMatrix = Cesium.Matrix4.fromTranslation(translation);
    }

    stop() {
        if (this.primitive) {
            this.viewer.scene.primitives.remove(this.primitive);
            this.primitive = null;
        }
        this.viewer.scene.preRender.removeEventListener(this.updateListener);
    }
}