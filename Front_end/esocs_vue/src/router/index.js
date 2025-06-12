import {createRouter, createWebHashHistory} from "vue-router";
import {storage} from "../store/storage.js";
import axios from "axios";

const routes = [
    {
        path: "/",
        name: "Home",
        redirect: "/login"
    },
    {
        path: "/login",
        name: "name",
        meta: {public: true},
        component: () => import("../Login/LoginForm.vue"),
    },
    {
        path: "/form/root",
        name: "root",
        meta: {requiresAuth: true},
        redirect: "/form/root/enterprise",
        component: () => import("../components/RootUserForm/Form.vue"),
        children: [
            {
                path: "enterprise",
                component: () => import("../components/RootUserForm/enterprise.vue"),
            },
            {
                path: "esocs",
                component: () => import("../components/RootUserForm/esocs.vue"),
            }
        ]
    },
    {
        path: "/form/user",
        name: "user",
        component: () => import("../components/UserForm/Form.vue"),
        redirect: "/form/user/esocs",
        children: [
            {
                path: "esocs",
                component: () => import("../components/UserForm/esocs.vue"),
            }
        ]
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})


export default router;
