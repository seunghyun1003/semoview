<template>
  <div id="myreview">
    <div class="page-title">
      {{username}}님의 리뷰 ({{reviewList.length}}개)
    </div>
    <div class="myreview-list">        
      <div class="myreview-item" v-for="myreview in reviewList" :key="myreview.id">
          <div id="myreview-item-1">
            <div class="myreview-item-title"><strong>{{myreview.stage_stageTitle}}</strong></div> 
            <div class="myreview-item-point">
              <span v-for="myreview in myreview.point" :key=myreview.point>★</span>
              <span v-for="myreview in 5-myreview.point" :key=myreview.point>☆</span>
              <span> ({{myreview.point}})</span>
            </div>  
          </div>
          <div id="myreview-item-2">
            <div class="myreview-item-content">{{myreview.reviewContents}} </div>
            <div class="myreview-item-date">{{$moment(myreview.created_at).format('YYYY-MM-DD')}}</div>
          </div>
          <div>
            <button @click="delete_my_reviews(myreview.id)">삭제</button>
            <button @click="detailshow(myreview.id)">수정</button>
          </div>
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
        console.log(err);
      })
    },
    delete_my_reviews: function (review_pk) {
      axios.delete(`http://127.0.0.1:8000/review/${review_pk}/delete`)
      .then(res => {             
        console.log("DELETED", res);
        this.reviewList.splice(review_pk, 1);
        this.$router.go();
        console.log("삭제성공");
      })
      .catch(err => {
        console.log(err);
      })
    },
    detailshow(index) {
      this.$router.push({
        name: "ReviewUpdate",
        params: {
          ReviewId: index
        }
      });
    }
  },
}
</script>

<style scoped>
  .page-title{
    font-weight: bolder;
    font-size: 1.2em;
    text-align: left;
    margin-bottom: 1em;
  }

  .myreview-item{
    padding: 1em 0.8em;
    border-top: 1px solid rgb(72, 72, 72);
  }
  #myreview-item-1{
    text-align: left;
  }
  #myreview-item-2{
    text-align: right;
  }
  .myreview-item-title{
    font-size: 1em;
  }
  .myreview-item-content{
    font-size: 0.86em;
  }
  .myreview-item-point{
    color: rgb(231, 194, 43);
    font-size: 0.8em;
  }
  .myreview-item-date {
    font-size: 0.6em;
    color: gray;
  }
</style>
