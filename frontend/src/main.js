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

const backendUrl = 'http://127.0.0.1:8000/api/'

Vue.config.productionTip = false
Vue.prototype.$axios = axios
axios.defaults.withCredentials = true
Vue.prototype.$url = backendUrl
Vue.prototype.$util = util

router.beforeEach((to, from, next) => {
  if (store.state.username || to.name === 'Login') {
    if (to.meta.requireAdmin && !store.state.isAdmin) {
      next({name: 'Index'})
    } else {
      next()
    }
  } else {
    axios({
      method: 'get',
      url: backendUrl + 'login/'
    }).then(response => {
      let data = response.data
      if (data.state) {
        store.commit('setUsername', data.data.user.username)
        store.commit('isAdmin', data.data.user.isAdmin)
        if (to.meta.requireAdmin && !store.state.isAdmin) {
          next({name: 'Index'})
        }
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
