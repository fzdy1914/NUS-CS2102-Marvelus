// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import util from './util'
import Vuex from 'vuex'
import store from './store/store'

Vue.config.productionTip = false
Vue.use(Vuex)
Vue.prototype.$axios = axios
Vue.prototype.$url = 'http://127.0.0.1:8000/api/'
Vue.prototype.$util = util

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
