import Vue from 'vue'
import Vuex from 'vuex'
import {UserStore} from './UserStore'
import {VMDStore} from './VMDStore'
import {Messaging} from './Messaging'

Vue.use(Vuex)

export default new Vuex.Store({
  modules:{
    UserStore,
    VMDStore,
    Messaging
  },
  state: {
  },
  mutations: {
  },
  actions: {
  }
})
