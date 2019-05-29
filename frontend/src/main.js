// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import util from './util'
import Vuex from 'vuex'
import store from './store'

Vue.use(Vuex)

Vue.config.productionTip = false
Vue.prototype.$axios = axios
axios.defaults.withCredentials = true
Vue.prototype.$url = 'http://127.0.0.1:8000/api/'
Vue.prototype.$util = util

router.beforeEach((to, from, next) => {
  if (store.state.username || to.name === 'Login') {
    next()
  } else {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/login/'
    }).then(response => {
      let data = response.data
      if (data.state) {
        store.commit('setUsername', data.data.user.username)
        next()
      } else {
        next({name: 'Login'})
      }
    })
  }
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
