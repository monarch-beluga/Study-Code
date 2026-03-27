import {createRouter, createWebHashHistory} from "vue-router";
import Map  from "../viewer/Map.vue";
import Login from "../viewer/Login.vue";
import {storage} from "../store/storage.js";
import axios from "axios";

const routes = [
    {
        path: '/',
        redirect: "/map",
        meta: { requiresAuth: true }
    },
    {
        path: "/login",
        name: "login",
        component: Login,
        meta: { requiresAuth: false }
    },
    {
        path:'/map',
        component: Map,
        redirect: "/map/main",
        meta: { requiresAuth: true },
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
        meta: { requiresAuth: true },
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

let lastVerifyTime = 0;
const VERIFY_GAP = 60000; // 30秒内不重复向后端请求验证
router.beforeEach(async (to, from, next) => {

    if (from.path === '/login') {
        return next();
    }

    if (to.path === "/login") {
        return next();
    }

    const authUser = storage.get("username")
    const authToken = storage.get("token")

    const now = Date.now();
    if (now - lastVerifyTime < VERIFY_GAP) {
        return next();
    }
    lastVerifyTime = now
    const baseUrl = import.meta.env.VITE_API_BASE_URL;

    const res = await axios.post(baseUrl + "/auth/verify", {"username": authUser, "token": authToken})
    const {status, type, message} = res.data;
    if (status !== 200) {
        ElMessage({
            message: message,
            type: type,
            duration: 3000
        })
        return next("/login")
    }
    next()
})

export default router

