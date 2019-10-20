import Vue from 'vue'
import Router from 'vue-router'
import CoursePage from './views/CoursePage.vue'
import Login from "./views/Login";
import CourseDetailPage from "./views/courses/CourseDetailPage";
import CourseSearchPage from "./views/CourseSearchPage";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      component: CoursePage,
      children: [
        {
          path: '/',
          name: 'Index',
          component: CourseDetailPage,
        }
      ]
    },
    {
      path: '/courses',
      component: CoursePage,
      children: [
        {
          path: '/',
          name: 'CourseDetail',
          component: CourseDetailPage,
        }
      ]
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/search',
      name: 'CourseSearch',
      component: CourseSearchPage
    },
  ]
})
