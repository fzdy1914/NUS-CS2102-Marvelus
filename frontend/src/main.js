// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import HelloWorld from './components/HelloWorld'
import axios from 'axios'

Vue.config.productionTip = false

Vue.component('hello', HelloWorld)

Vue.prototype.$axios = axios
Vue.prototype.$url = 'http://127.0.0.1:8000/api/'

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
