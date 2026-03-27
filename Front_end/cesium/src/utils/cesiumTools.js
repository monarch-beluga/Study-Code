
import * as Cesium from 'cesium';
import { mapManager } from './mapManager';

/**
 * 切换/添加地形
 * @param {string|number|null} source 地形来源
 * @param {object} options 配置项
 */
async function setTerrain(source, options = {}) {
    const viewer = mapManager.getViewer();
    if (!viewer) return;

    try {
        if (source === 'world') {
            // 方式 A: 官方全球地形
            viewer.scene.setTerrain(
                Cesium.Terrain.fromWorldTerrain(options)
            )
        } else if (typeof source === 'string' || typeof source === 'number') {
            // 方式 B: 加载特定 URL 或 ion 资产 ID 的地形
            viewer.terrainProvider = await Cesium.CesiumTerrainProvider.fromUrl(source, options);
        } else {
            // 方式 C: 恢复为平坦椭球体
            viewer.terrainProvider = new Cesium.EllipsoidTerrainProvider();
        }
    } catch (error) {
        console.error("地形加载失败:", error);
    }
}

/**
 * 加载 3D Tiles 模型
 * @param {string|number} url ion资产ID或本地/在线 tileset.json 路径
 * @param {boolean} flyTo 是否飞行
 * @param {object} offset 模型偏移
 * @param {object} options
 * @returns {Promise<Cesium.Cesium3DTileset>}
 */
async function add3DTiles(url, flyTo=false, options = {}, offset) {
    const viewer = mapManager.getViewer();
    if (!viewer) throw new Error('Viewer 未初始化');

    try {
        // 1. 根据输入类型选择加载方式
        const tileset = await Cesium.Cesium3DTileset.fromUrl(url, options);

        // 2. 将模型添加到场景
        viewer.scene.primitives.add(tileset);

        // 3. 自动调整位置（如果传入了 offset）
        if (offset) {
            updateTilesetPosition(tileset, offset);
        }

        // 4. 是否加载完成后自动飞过去
        if (flyTo) {
            await viewer.zoomTo(tileset);
        }

        return tileset;
    } catch (error) {
        console.error(`3D Tiles 加载失败: ${error}`);
    }
}

/**
 * 内部工具：调整 3D Tiles 的高度、经纬度偏移
 */
function updateTilesetPosition(tileset, offset) {
    const { longitude, latitude, height } = offset;

    // 计算模型中心点的笛卡尔坐标
    const cartographic = Cesium.Cartographic.fromCartesian(tileset.boundingSphere.center);

    // 应用偏移量
    const targetLon = longitude || Cesium.Math.toDegrees(cartographic.longitude);
    const targetLat = latitude || Cesium.Math.toDegrees(cartographic.latitude);
    const targetAlt = height || 0;

    const surface = Cesium.Cartesian3.fromDegrees(targetLon, targetLat, 0);
    const offsetPos = Cesium.Cartesian3.fromDegrees(targetLon, targetLat, targetAlt);
    const translation = Cesium.Cartesian3.subtract(offsetPos, surface, new Cesium.Cartesian3());

    // 设置模型的 modelMatrix 进行平移
    tileset.modelMatrix = Cesium.Matrix4.fromTranslation(translation);
}

export { add3DTiles , setTerrain};

