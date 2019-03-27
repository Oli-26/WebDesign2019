import Vue from 'vue'
import Router from 'vue-router'
import Main from '@/components/Main'
import Carriers from '@/components/carriers'
import Airport from '@/components/airport'
import Carrier from '@/components/carrier'
import Statistics from '@/components/statistics'
import Flights from '@/components/Flights'
import Delays from '@/components/Delays'
import DMinutes from '@/components/DMinutes'
import DAmount from '@/components/DAmount'

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
      path: '/carriers/:carrierCode/statistics',
      name: 'Statistics',
      component: Statistics
    },
    {
      path: '/carriers/:carrierID/statistics/flights',
      name: 'Flights',
      component: Flights
    },
    {
      path: '/carriers/:carrierID/statistics/delays',
      name: 'Delays',
      component: Delays
    },
    {
      path: '/carriers/:carrierID/statistics/delays/minutes',
      name: 'DelaysMinutes',
      component: DMinutes
    },
    {
      path: '/carriers/:carrierID/statistics/delays/amount',
      name: 'DelaysAmount',
      component: DAmount
    }
  ]
})
