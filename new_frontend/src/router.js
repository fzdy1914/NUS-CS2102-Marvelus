import Vue from 'vue'
import Router from 'vue-router';
import CoursePage from './views/CoursePage.vue'
import Login from "./views/Login";
import CourseDetailPage from "./views/courses/CourseDetailPage";
import CourseSearchPage from "./views/CourseSearchPage";
import CourseListPage from "./views/courses/CourseListPage";
import AssistPage from "./views/AssistPage";
import CourseDetailInfoPage from "./views/courses/CourseDetailInfoPage";
import AssistListPage from "./views/assists/AssistListPage";
import CourseDetailTutPage from "./views/courses/CourseDetailTutPage";
import TeachPage from "./views/TeachPage";
import TeachListPage from "./views/teachs/TeachListPage";
import TeachDetailPage from "./views/teachs/TeachDetailPage";
import TeachDetailStudentPage from "./views/teachs/TeachDetailStudentPage";
import TeachDetailRequestsPage from "./views/teachs/TeachDetailRequestsPage";
import TeachDetailTAsPage from "./views/teachs/TeachDetailTAsPage";

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
          component: CourseListPage,
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
            {
              path: 'tut',
              name: 'CourseDetailTut',
              component: CourseDetailTutPage,
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
    {
      path: '/teach',
      component: TeachPage,
      children: [
        {
          path: '/',
          name: 'TeachList',
          component: TeachListPage,
        },
        {
          path: ':code',
          component: TeachDetailPage,
          children: [
            {
              path: '/',
              name: 'TeachDetail',
              component: CourseDetailInfoPage,
            },
            {
              path: 'info',
              name: 'TeachDetailInfo',
              component: CourseDetailInfoPage,
            },
            {
              path: 'tut',
              name: 'TeachDetailTut',
              component: CourseDetailTutPage,
            },
            {
              path: 'students',
              name: 'TeachDetailStudent',
              component: TeachDetailStudentPage,
            },
            {
              path: 'requests',
              name: 'TeachDetailRequests',
              component: TeachDetailRequestsPage,
            },
            {
              path: 'tas',
              name: 'TeachDetailTAs',
              component: TeachDetailTAsPage,
            },
          ]
        }
      ]
    }
  ]
})
