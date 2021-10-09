import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/views/Home.vue'
import MyReview from '@/views/MyReview.vue'
import Signup from '@/views/Signup.vue'
import Signin from '@/views/Signin.vue'
import Search from '@/views/Search.vue'
import Detail from '@/views/Detail.vue'
import ReviewUpdate from '@/views/ReviewUpdate.vue'

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
      path: '/signin',
      name: 'Signin',
      component: Signin
    },
    {
      path: '/search',
      name: 'Search',
      component: Search
    },
    {
      path: '/detail/:contentId?',
      name: 'Detail',
      component: Detail
    },
    {
      path: '/update/:ReviewId?',
      name: 'ReviewUpdate',
      component: ReviewUpdate
    },
  ]
})
