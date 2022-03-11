import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'

Vue.config.productionTip = false

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
    ]
});

new Vue({
    vuetify,
    router,
    render: h => h(App)
}).$mount('#app')
