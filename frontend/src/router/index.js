import Vue from 'vue'
import Router from 'vue-router'
import EventList from '../components/EventList'
import HelloWorld from '../components/HelloWorld'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: EventList,
    },
    {
      path: '/events/',
      name: 'EventList',
      component: EventList
    },
    {
      path: '/hello',
      name: 'HelloWorld',
      component: HelloWorld
    }
  ]
})
