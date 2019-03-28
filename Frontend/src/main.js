// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import App from './App';
import Carrier from './components/Carrier';
import router from './router';
import SuiVue from 'semantic-ui-vue';
import '../semantic/dist/semantic.min.css';
import MonthPicker from 'vue-month-picker'
import MonthPickerInput from 'vue-month-picker'
import axios from 'axios'

import VueApexCharts from 'vue-apexcharts'
Vue.use(VueApexCharts)


axios.defaults.baseURL = 'http://127.0.0.1:5002/';
Vue.use(MonthPicker)
Vue.use(MonthPickerInput)


Vue.use(SuiVue);
Vue.config.productionTip = false;
Vue.component();
 
Vue.component('apexchart', VueApexCharts)

/* eslint-disable no-new */
var vm = new Vue({
  el: '#app',
  router,
  components: {App, 'carrier' : Carrier},
  template: '<App/>'
})
