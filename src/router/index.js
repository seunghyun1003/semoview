import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/views/Home.vue'
import MyReview from '@/views/MyReview.vue'
import Signup from '@/views/Signup.vue'
import Login from '@/views/Login.vue'
import Write from '@/views/Write.vue'
import Detail from '@/views/Detail.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '',
      name: 'Home',
      component: Home
    },
    {
      path: '/myreview',
      name: 'MyReview',
      component: MyReview
    },
    {
      path: '/signup',
      name: 'Signup',
      component: Signup
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/write',
      name: 'Write',
      component: Write
    },
    {
      path: '/detail/:contentId?',
      name: 'Detail',
      component: Detail
    },
  ]
})
