import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'

Vue.config.productionTip = false


import axios from 'axios'
import VueAxios from 'vue-axios'
Vue.use(VueAxios, axios)
//Vue.axios.defaults.baseURL = 'http://127.0.0.1:5000/api';

import VueRouter from 'vue-router';

Vue.use(VueRouter);

const CreateTask = () => import('@/components/CreateTask.vue');
const ListTask = () => import('@/components/ListTask.vue');

const router = new VueRouter({
    mode: 'history',
    routes: [
        {
            path: '/',
            component: CreateTask,
        },
        {
            path: '/tasks',
            component: ListTask,
        },
        {
            path: '/tasks/:taskId',
            component: CreateTask,
            props: route => ({
                taskId: route.params.taskId,
            })
        }
    ]
});

new Vue({
    vuetify,
    router,
    render: h => h(App)
}).$mount('#app')
