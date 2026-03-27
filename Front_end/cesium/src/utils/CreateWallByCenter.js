import * as Cesium from "cesium";

function CreateWallByCenter(lon, lat, d, height) {
    const center = Cesium.Cartesian3.fromDegrees(lon, lat);
    const localMatrix = Cesium.Transforms.eastNorthUpToFixedFrame(center);

    // 1. 定义局部坐标点 (注意：Cartesian3 需要三个参数，这里补上 0)
    const localPoints = [
        new Cesium.Cartesian3(-d, -d, 0), // 左下
        new Cesium.Cartesian3( d, -d, 0), // 右下
        new Cesium.Cartesian3( d,  d, 0), // 右上
        new Cesium.Cartesian3(-d,  d, 0)  // 左上
    ];

    // 2. 转换为世界坐标
    const worldPositions = localPoints.map(p => {
        return Cesium.Matrix4.multiplyByPoint(localMatrix, p, new Cesium.Cartesian3());
    });

    // --- 新增部分：从世界坐标计算 Rectangle ---
    // 先转为弧度坐标 (Cartographic)
    const cartographics = worldPositions.map(pos => Cesium.Cartographic.fromCartesian(pos));
    // 直接利用 Cesium 的工具函数生成矩形范围
    const rectangle = Cesium.Rectangle.fromCartographicArray(cartographics);
    // ---------------------------------------

    // 为了闭合墙体，需要在数组末尾重复第一个点
    const closedPositions = [...worldPositions, worldPositions[0]];

    const entity = new Cesium.Entity({
        wall: {
            positions: closedPositions,
            maximumHeights: new Array(5).fill(height),
            minimumHeights: new Array(5).fill(0),
            material: Cesium.Color.WHITE.withAlpha(0),
            outline: true,
            outlineColor: Cesium.Color.WHITE.withAlpha(0.5)
        }
    });

    // 返回对象，包含实体和矩形范围
    return {
        entity: entity,
        rectangle: rectangle,
        center: center,
    };
}

export { CreateWallByCenter }

