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
                component: () => import("../viewer/MainContent.vue"),
                redirect: "/map/main/survey",
                children: [
                    {
                        path:"survey",
                        component: () => import("../viewer/Map/MapSurvey.vue"),
                    },
                    {
                        path:"rs",
                        component: () => import("../viewer/Map/MapRs.vue"),
                    },
                    {
                        path:"space",
                        component: () => import("../viewer/Map/MapSpace.vue"),
                    },
                    {
                        path:"pac",
                        component: () => import("../viewer/Map/MapPac.vue"),
                    },
                    {
                        path:"pd",
                        component: () => import("../viewer/Map/MapPd.vue",)
                    }
                ]
            },
            {
                path:"sub",
                component: () => import("../viewer/SubContent.vue"),
                redirect: "/map/sub/companyInfo",
                children: [
                    {
                        path:"companyInfo",
                        component: () => import("../viewer/Map/CompanyInfo.vue"),
                    },
                    {
                        path:"companySup",
                        component: () => import("../viewer/Map/CompanySup.vue"),
                    },
                    {
                        path:"companyRt",
                        component: () => import("../viewer/Map/CompanyRt.vue"),
                    },
                    {
                        path:"companySpace",
                        component: () => import("../viewer/Map/CompanySpace.vue"),
                    }
                ]
            }
        ]
    },
    {
        path:'/table',
        component: () => import("../viewer/Table.vue"),
        children: [
            {
                path:"supplies",
                component: () => import("../viewer/Table/TableSupplies.vue"),
            },
            {
                path:"rt",
                component: () => import("../viewer/Table/TableRt.vue"),
            },
            {
                path:"zzt",
                component: () => import("../viewer/Table/ZZT.vue"),
            }
        ]
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes,
})

export default router

