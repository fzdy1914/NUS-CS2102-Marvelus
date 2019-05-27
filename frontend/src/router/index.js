import Vue from 'vue'
import Router from 'vue-router'
import EventList from '../components/EventList'
import Event from '../components/Event'
import Login from '../components/Login'

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
    }
  ]
})
