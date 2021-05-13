import Vue from 'vue'
import VueRouter from 'vue-router'
import Landingpage from '../components/Landingpage'

Vue.use(VueRouter)

const routes = [
  {
    path :'/', 
        redirect: '/dashboard',
        component: Landingpage ,
            children:[
                {
                path: '/dashboard',
                component: () => import(/* webpackChunkName: "demo" */ '../components/Dashboard.vue'),
                meta: { title: 'DashBoard' }
                },
                {
                path: '/Devices',
                component: () => import(/* webpackChunkName: "demo" */ '../components/Devices.vue'),
                meta: { title: 'DashBoard' }
                },
                {
                path: '/Usermanagement',
                component: () => import(/* webpackChunkName: "demo" */ '../components/Usermanagement/home.vue'),
                meta: { title: 'Usermanagement' }
                },
                {
                path: '/VmdManagement',
                component: () => import(/* webpackChunkName: "demo" */ '../components/VMD_Management/home.vue'),
                meta: { title: 'VmdManagement' }
                },
                {
                path: '/GoogleMap',
                component: () => import(/* webpackChunkName: "demo" */ '../components/GoogleMap.vue'),
                meta: { title: 'VmdManagement' }
                },
                {
                path: '/Predefined',
                component: () => import(/* webpackChunkName: "demo" */ '../components/Messaging/Predefined_Sequence.vue'),
                meta: { title: 'Predefined Messages' }
                },
                {
                path: '/VmdInfo/:id',
                component: () => import(/* webpackChunkName: "demo" */ '../components/VMD_Management/VMD_Info.vue'),
                meta: { title: 'Predefined Messages' }
                },
                {
                path: '/Sequence',
                component: () => import(/* webpackChunkName: "demo" */ '../components/Messaging/Sequence.vue'),
                meta: { title: 'Sequence Messages' }
                },
                {
                path: '/reports',
                component: () => import(/* webpackChunkName: "demo" */ '../components/Reports/Home.vue'),
                meta: { title: 'Sequence Messages' }
                },
                {
                path: '/Schedule',
                component: () => import(/* webpackChunkName: "demo" */ '../components/Messaging/Schedule.vue'),
                meta: { title: 'Sequence Messages' }
                },
                {
                path: '/VmdConfiguration',
                component: () => import(/* webpackChunkName: "demo" */ '../components/VMD_Configuration/home.vue'),
                meta: { title: 'VmdManagement' }
                },
                {
                path: '/playlist',
                component: () => import(/* webpackChunkName: "demo" */ '../components/Playlist/Home.vue'),
                meta: { title: 'VmdManagement' }
                },
                {
                path: '/SendMessage',
                component: () => import(/* webpackChunkName: "demo" */ '../components/Messaging/Home.vue'),
                meta: { title: 'Send Message' }
                },
                {
                path: '/MessagingConfig',
                component: () => import(/* webpackChunkName: "demo" */ '../components/Messaging/HomeConfig.vue'),
                meta: { title: 'Send Message' }
                },
            ]
          
  }
  
]

export const router = new VueRouter({
  base: process.env.BASE_URL,
  routes
})

export default router
