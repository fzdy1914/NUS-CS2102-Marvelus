import Vue from 'vue'
import Router from 'vue-router'
import CoursePage from './views/CoursePage.vue'
import Login from "./views/Login";
import CourseDetailPage from "./views/courses/CourseDetailPage";
import CourseSearchPage from "./views/CourseSearchPage";
import CourseListPage from "./views/courses/CourseListPage";
import AssistPage from "./views/AssistPage";
import CourseDetailInfoPage from "./views/courses/CourseDetailInfoPage";
import AssistListPage from "./views/assists/AssistListPage";

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
          name: 'CourseList',
          component: CourseListPage,
        },
        {
          path: ':code',
          component: CourseDetailPage,
          children: [
            {
              path: '/',
              name: 'CourseDetail',
              component: CourseDetailInfoPage,
            },
            {
              path: 'info',
              name: 'CourseDetailInfo',
              component: CourseDetailInfoPage,
            },
          ]
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
    {
      path: '/assists',
      component: AssistPage,
      children: [
        {
          path: '/',
          name: 'AssistList',
          component: AssistListPage,
        },
        {
          path: ':code',
          component: CourseDetailPage,
          children: [
            {
              path: '/',
              name: 'AssistDetail',
              component: CourseDetailInfoPage,
            },
            {
              path: 'info',
              name: 'AssistDetailInfo',
              component: CourseDetailInfoPage,
            },
          ]
        }
      ]
    },
  ]
})
