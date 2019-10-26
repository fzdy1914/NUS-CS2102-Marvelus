import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import util from './util'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.min.js'
import 'primevue/resources/themes/nova-light/theme.css'
import 'primevue/resources/primevue.min.css'
import 'primeicons/primeicons.css'
import 'primeflex/primeflex.css'
import ToastService from 'primevue/toastservice';

const backendUrl = 'http://127.0.0.1:8000/new/'

Vue.config.productionTip = false
Vue.prototype.$axios = axios
axios.defaults.withCredentials = true
Vue.prototype.$url = backendUrl
Vue.prototype.$util = util
Vue.use(ToastService);

router.beforeEach((to, from, next) => {
  if (store.state.username || to.name === 'Login') {
    if (to.meta.requireAdmin && !store.state.isAdmin) {
      if (store.state.isProf) {
        next({name: 'TeachList'})
      } else {
        next({name: 'Index'})
      }
    } else {
      if (to.name === 'Index' && store.state.isProf) {
        next({name: 'TeachList'})
      } else {
        next()
      }
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
        store.commit('isTA', data.data.user.isTA)
        if (to.meta.requireAdmin && !store.state.isAdmin) {
          if (store.state.isProf) {
            next({name: 'TeachList'})
          } else {
            next({name: 'Index'})
          }
        } else {
          if (to.name === 'Index' && store.state.isProf) {
            next({name: 'TeachList'})
          } else {
            next()
          }
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
