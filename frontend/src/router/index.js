import Vue from 'vue'
import Router from 'vue-router'
import EventList from '../components/EventList'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: EventList
    },
    {
      path: '/events/',
      name: 'EventList',
      component: EventList
    }
  ]
})
