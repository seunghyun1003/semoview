<template>
  <div id="myreview">
    <div class="page-title">
      {{username}}님의 리뷰 ({{reviewList.length}}개)
    </div>
    <div class="myreview-list">        
      <div class="myreview-item" v-for="myreview in reviewList" :key="myreview.id">
          <div id="myreview-item-content">{{myreview.reviewContents}} </div> 
          <div id="myreview-item-title">{{myreview.point}}</div> 
          <div id="myreview-item-date">{{$moment(myreview.created_at).format('YYYY-MM-DD')}}</div> 
      </div> 
    </div> 
  </div>
</template>

<script>
import jwt_decode from "jwt-decode";
import axios from 'axios'

export default {
  name: 'MyReview',
  data: function () {
    return {
      username : jwt_decode(localStorage.getItem('jwt')).username,
      reviewList : [],
    }
  },
  created: function() {
    this.fetch_my_reviews()
  },
  methods: {
    fetch_my_reviews: function () {
      const userId = jwt_decode(localStorage.getItem('jwt')).user_id;
      axios.get(`http://127.0.0.1:8000/get/myreviews/userId/${userId}`)
      .then(res => {             
        this.reviewList = res.data;
      })
      .catch(err => {
        console.log(err)
      })
    },
  },
}
</script>

<style scoped>
  .page-title{
    font-weight: bolder;
    font-size: 1.2em;
    text-align: left;
  }

  .myreview-item{
    text-align: left;
    padding: 1em;
  }
</style>
