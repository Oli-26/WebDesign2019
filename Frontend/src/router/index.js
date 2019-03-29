import Vue from 'vue'
import Router from 'vue-router'
import Main from '@/components/Main'
import Carriers from '@/components/carriers'
import Airport from '@/components/airport'
import Carrier from '@/components/carrier'
import Descriptive from '@/components/descriptive'

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
      path: '/airports',
      name: 'Airports',
      component: Main
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
      path: '/carriers/:carrierCode/averages',
      name: 'Averages',
      component: Descriptive
    }
  ]
})
