import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import VueAxios from 'vue-axios'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.min.css' 
import 'bootstrap-vue/dist/bootstrap-vue.css' 


Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(VueAxios, axios);

import JwPagination from 'jw-vue-pagination';
Vue.component('jw-pagination', JwPagination);

import VueMoment from 'vue-moment'
Vue.use(VueMoment);

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

Vue.config.productionTip = false

new Vue({ el: '#app', router, render: h => h(App) })