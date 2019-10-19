import Vue from 'vue'
import Router from 'vue-router'
import CoursePage from './views/CoursePage.vue'
import Login from "./views/Login";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: CoursePage
    },
    {
      path: '/courses',
      name: 'courses',
      component: CoursePage
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
  ]
})
