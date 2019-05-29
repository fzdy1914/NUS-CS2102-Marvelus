import Vue from 'vue'
import Router from 'vue-router'
import EventList from '../components/user/EventList'
import Event from '../components/user/Event'
import Login from '../components/Login'
import AdminItemList from '../components/admin/AdminItemList'
import AdminEventList from '../components/admin/AdminEventList'
import AdminChannelList from '../components/admin/AdminChannelList'

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
      component: AdminItemList,
      meta: {
        requireAdmin: true
      },
      children: [
        {
          path: '/',
          name: 'AdminIndex',
          component: AdminEventList
        },
        {
          path: 'events',
          name: 'AdminEventList',
          component: AdminEventList
        },
        {
          path: 'channels',
          name: 'AdminChannelList',
          component: AdminChannelList
        }
      ]
    }
  ]
})
