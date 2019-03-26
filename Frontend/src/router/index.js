import Vue from 'vue'
import Router from 'vue-router'
import Main from '@/components/Main'
import HelloWorld from '@/components/HelloWorld'
import Airports from '@/components/airports'
import Carriers from '@/components/carriers'
import Airport from '@/components/airport'
import Carrier from '@/components/carrier'
import Statistics from '@/components/statistics'
Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Main',
      component: Main
    },
    {
      path: '/HelloWorld',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/airports',
      name: 'Airports',
      component: Airports
    },
    {
      path: '/airports/:airportCode',
      name: 'Airport',
      component: Airport
    },
    {
      path: '/carriers',
      name: 'Carriers',
      component: Carriers 
    },
    {
      path: '/carriers/:carrierCode',
      name: 'Carrier',
      component: Carrier
    },
    {
      path: '/carriers/:carrierCode/statistics',
      name: 'Statistics',
      component: Statistics
    }
  ]
})
