<template>
    <div id="reviewupdate">
        <div>
            <div class="review-title">연극은 어떠셨나요?</div>
            <b-form @submit="onSubmit(review_id)" @reset="onReset">
                <star-rating 
                    v-model="form.point"
                    v-bind:increment="1"
                    v-bind:max-rating="5"
                    inactive-color="white"
                    active-color="gold"
                    v-bind:star-size="40"
                ></star-rating>
                <b-form-textarea
                id="input-2"
                v-model="form.content"
                v-bind:placeholder=form.content
                required
                ></b-form-textarea>
                <div class="btns">
                    <b-button type="reset">취소</b-button>
                    <b-button type="submit" variant="primary">완료</b-button>
                </div>
            </b-form>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import StarRating from 'vue-star-rating'
import jwt_decode from "jwt-decode";

export default {
  name: 'ReviewUpdate',
  components: {
    StarRating
  },
  data() {
    return {
      review : null,
      review_id : this.$route.params.ReviewId,
      form: {
          point: 0,
          content: '',
      },
    };
  },
  created: function() {
    if(localStorage.getItem('jwt')){
      this.isLogin = true
    } else this.isLogin = false;
    this.fetch_this_review(this.review_id);
  },
  methods: {
    setToken : function () { // header 내용에 토큰 붙여주기
      const token = localStorage.getItem('jwt')
      const config = {
         Authorization : `JWT ${token}`
      }
      return config
    },
    fetch_this_review: function (review_id) {
      axios.get(`http://127.0.0.1:8000/get/review/${review_id}`)
      .then(res => {             
        this.review = res.data[0]
        this.form.point = this.review.point
        this.form.content = this.review.reviewContents
      })
      .catch(err => {
        console.log(err)
      })
    },
    onSubmit(review_pk) {
        const userId = jwt_decode(localStorage.getItem('jwt')).user_id;

        const url = `http://127.0.0.1:8000/review/${review_pk}/update`
        axios.put(url, {
            headers : this.setToken(),
            user_id : userId,
            stage_id : this.review.stage_id,
            point : this.form.point,
            reviewContents : this.form.content,
        })
        .then(res => { 
            console.log(res.status, "Review Updated")      
            this.$router.push({name: "MyReview"});
        })
        .catch(err => {
            console.log(err)
        })
    },
    onReset() {
      this.$router.push({name: "MyReview"});
      console.log("Cancel Review Update")
    },
  }
}

</script>

<style scoped>
.review-title{
    font-size: 1.1em;
    font-weight: bold;
}
.vue-star-rating{
    justify-content: center;
    margin: 0.8em 0 1.5em 0;
}
textarea {
    height: 10em;
}
.btns{
    display: flex;
    justify-content: space-between;
    padding: 0 3%;
    margin-top: 1.5em;
}
.btns > button{
    width: 47%;
}
</style>
