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
import CourseDetailTutPage from "./views/courses/CourseDetailTutPage";
import TeachPage from "./views/TeachPage";
import TeachListPage from "./views/teachs/TeachListPage";
import TeachDetailPage from "./views/teachs/TeachDetailPage";
import TeachDetailStudentPage from "./views/teachs/TeachDetailStudentPage";
import TeachDetailRequestsPage from "./views/teachs/TeachDetailRequestsPage";
import TeachDetailTAsPage from "./views/teachs/TeachDetailTAsPage";
import TeachDetailTutListPage from "./views/teachs/TeachDetailTutListPage";
import TeachDetailTutPage from "./views/teachs/TeachDetailTutPage";
import TeachDetailTutDetailPage from "./views/teachs/TeachDetailTutDetailPage";
import CourseDetailForumPage from "./views/courses/CourseDetailForumPage";
import CourseDetailForumListPage from "./views/courses/CourseDetailForumListPage";
import CourseDetailForumDetailPage from "./views/courses/CourseDetailForumDetailPage";
import CourseDetailPostListPage from "./views/courses/CourseDetailPostListPage";

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
            {
              path: 'forum',
              component: CourseDetailForumPage,
              children: [
                {
                  path: '/',
                  name: 'CourseDetailForumList',
                  component: CourseDetailForumListPage,
                },
                {
                  path: ':fid',
                  component: CourseDetailForumDetailPage,
                  children: [
                    {
                      path: '/',
                      name: 'CourseDetailPostList',
                      component: CourseDetailPostListPage
                    }
                  ]
                },
              ]
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
              component: TeachDetailTutPage,
              children: [
                {
                  path: '/',
                  name: 'TeachDetailTutList',
                  component: TeachDetailTutListPage,
                },
                {
                  path: ':group_num',
                  name: 'TeachDetailTutDetail',
                  component: TeachDetailTutDetailPage,
                }
              ]
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
