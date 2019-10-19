import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import util from './util'
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.min.js";

const backendUrl = 'http://127.0.0.1:8000/new/'

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
        store.commit('isProf', data.data.user.isProf)
        if (to.meta.requireAdmin && !store.state.isAdmin) {
          next({name: 'Index'})
        } else {
          next()
        }
      } else {
        next({name: 'Login'})
      }
    })
  }
})

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
