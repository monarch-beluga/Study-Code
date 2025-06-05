import {createRouter, createWebHashHistory} from "vue-router";
import Map  from "../viewer/Map.vue";

const routes = [
    {
        path: '/',
        redirect: "/map",
    },
    {
        path:'/map',
        component: Map,
        redirect: "/map/main",
        children: [
            {
                path:"main",
                component: () => import("../viewer/Map/MainContent.vue"),
                redirect: "/map/main/survey",
                children: [
                    {
                        path:"survey",
                        component: () => import("../viewer/Map/MapSurvey.vue"),
                    }
                ]
            },
            {
                path:"sub",
                component: () => import("../viewer/Map/SubContent.vue"),
            }
        ]
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes,
})

export default router

