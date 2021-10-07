<template>
  <div id="myreview">
    <div class="page-title">
      {{username}}님의 리뷰 페이지
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'MyReview',
  data: function () {
    return {
      user : '',
    }
  },
  created : function(){
    axios({
        method : 'get',
        url : 'http://127.0.0.1:8000/rest-auth/user/',
    })
    .catch(err => {
        console.log(err)
    })
  }
}
</script>
