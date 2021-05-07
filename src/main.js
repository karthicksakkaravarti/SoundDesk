import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import 'ant-design-vue/dist/antd.css';
import Antd from 'ant-design-vue';
Vue.use(Antd);
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify';
import VueLayers from 'vuelayers'
import 'vuelayers/lib/style.css' // needs css-loader
Vue.use(VueLayers)
// import Buefy from 'buefy'
// import 'buefy/dist/buefy.css'

// Vue.use(Buefy, {
//   defaultIconPack: 'fa',
// })
Vue.config.productionTip = false

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
