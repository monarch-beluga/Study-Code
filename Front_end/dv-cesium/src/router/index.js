import {createRouter, createWebHashHistory} from "vue-router";

const routes = [
    {
        path: "/",
        redirect: "/map/main/survey"
    },
    {
        path: "/map/main/survey",
        component: () => import("../components/MapPage.vue"),
    },
    {
        path: "/map/main/rs",
        component: () => import("../components/MapPage.vue"),
    },
    {
        path: "/map/main/space",
        component: () => import("../components/MapPage.vue"),
    },
    {
        path: "/map/main/pac",
        component: () => import("../components/MapPage.vue"),
    },
    {
        path: "/map/main/pd",
        component: () => import("../components/MapPage.vue"),
    },
    {
        path: "/map/sub/companyInfo",
        component: () => import("../components/MapPage.vue"),
    },
    {
        path: "/table/supplies",
        component: () => import("../components/table/TablePage.vue"),
    },
    {
        path: "/table/rt",
        component: () => import("../components/table/TablePage.vue"),
    },
    {
        path: "/zzt",
        component: () => import("../components/zzt/ZztPage.vue"),
    }

]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router




