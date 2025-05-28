import {createRouter, createWebHashHistory} from "vue-router";

const routes = [
    {
        path: "/",
        redirect: "/login"
    },
    {
        path: "/login",
        name: "name",
        component: () => import("../Login/LoginForm.vue"),
        meta: {requiresGuest: true}
    },
    {
        path: "/form/root",
        name: "root",
        meta: {requiresAuth: true},
        component: () => import("../components/RootUserForm/Form.vue"),
        redirect: '/form/root/enterprise',
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
        redirect: '/form/user/esocs',
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
