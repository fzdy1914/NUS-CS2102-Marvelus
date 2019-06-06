import Vue from 'vue'
import Router from 'vue-router'
import EventListPage from '../components/user/EventListPage'
import Event from '../components/user/Event'
import Login from '../components/Login'
import AdminItemList from '../components/admin/AdminItemList'
import AdminEventListPage from '../components/admin/AdminEventListPage'
import AdminChannelList from '../components/admin/AdminChannelList'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: EventListPage
    },
    {
      path: '/events',
      name: 'EventList',
      component: EventListPage
    },
    {
      path: '/event/:eventId',
      name: 'Event',
      component: Event
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/admin',
      component: AdminItemList,
      meta: {
        requireAdmin: true
      },
      children: [
        {
          path: '/',
          name: 'AdminIndex',
          component: AdminEventListPage,
          meta: {
            requireAdmin: true
          }
        },
        {
          path: 'events',
          name: 'AdminEventList',
          component: AdminEventListPage,
          meta: {
            requireAdmin: true
          }
        },
        {
          path: 'channels',
          name: 'AdminChannelList',
          component: AdminChannelList,
          meta: {
            requireAdmin: true
          }
        }
      ]
    }
  ]
})
