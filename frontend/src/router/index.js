import Vue from 'vue'
import Router from 'vue-router'
import EventList from '../components/user/EventList'
import Event from '../components/user/Event'
import Login from '../components/Login'
import AdminItemList from '../components/admin/AdminItemList'
import AdminEventList from '../components/admin/AdminEventList'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: EventList
    },
    {
      path: '/events',
      name: 'EventList',
      component: EventList
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
      name: 'Admin',
      component: AdminItemList,
      meta: {
        requireAdmin: true
      },
      children: [
        {
          path: 'events',
          name: 'AdminEventList',
          component: AdminEventList
        },
        {
          path: '/',
          name: 'AdminIndex',
          component: AdminEventList
        }
      ]
    }
  ]
})
