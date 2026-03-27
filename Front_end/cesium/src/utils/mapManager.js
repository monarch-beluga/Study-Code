// src/utils/mapManager.js
import * as Cesium from 'cesium';

// 使用普通的变量，严禁使用 ref/reactive 包装 viewer
let viewer = null;

const mapManager = {
    /**
     * 初始化 Viewer 并保存引用
     * @param {string | Element} containerId
     * @param {object} options
     */
    init(containerId, options = {}) {
        if (viewer) {
            console.warn('Viewer 已存在，正在销毁旧实例...');
            viewer.destroy();
        }

        viewer = new Cesium.Viewer(containerId, options);

        return viewer;
    },

    /**
     * 获取当前的 Viewer 实例
     * @returns {Cesium.Viewer}
     */
    getViewer() {
        return viewer;
    },

    /**
     * 销毁实例并清空引用
     */
    destroy() {
        if (viewer && !viewer.isDestroyed()) {
            viewer.destroy();
            viewer = null;
        }
    }
};

export {mapManager};

