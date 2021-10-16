<template>
  <div id="myreview">
    <div class="page-title">
      <div class="page-title-1">{{ username }}님의 리뷰</div>
      <div class="page-title-2">
        <span>★ </span> {{ this.avg }} ({{ reviewList.length }})
      </div>
    </div>
    <div class="myreview-list">
      <div
        class="myreview-item"
        v-for="myreview in reviewList"
        :key="myreview.id"
      >
        <div id="myreview-item-1">
          <div id="myreview-item-1-1">
            <div class="myreview-item-title">
              <strong>{{ myreview.stage_stageTitle }}</strong>
            </div>
            <div class="myreview-item-point">
              <span
                class="filled"
                v-for="myreview in myreview.point"
                :key="myreview.point"
                >★</span
              >
              <span v-for="myreview in 5 - myreview.point" :key="myreview.point"
                >☆</span
              >
            </div>
          </div>
          <div id="myreview-item-1-2">
            <button @click="delete_my_reviews(myreview.id)">삭제</button>
            <button @click="detailshow(myreview.id)">수정</button>
          </div>
        </div>
        <div id="myreview-item-2">
          <div class="myreview-item-content">{{ myreview.reviewContents }}</div>
          <div class="myreview-item-date">
            {{ $moment(myreview.created_at).format("YYYY-MM-DD") }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import jwt_decode from "jwt-decode";
import axios from "axios";

export default {
  name: "MyReview",
  data: function() {
    return {
      username: jwt_decode(localStorage.getItem("jwt")).username,
      reviewList: [],
      avg: null,
    };
  },
  created: function() {
    this.fetch_my_reviews();
  },
  methods: {
    fetch_my_reviews: function() {
      const userId = jwt_decode(localStorage.getItem("jwt")).user_id;
      axios
        .get(`http://127.0.0.1:8000/get/myreviews/userId/${userId}`)
        .then((res) => {
          this.reviewList = res.data;
          this.computedAvg();
        })
        .catch((err) => {
          console.log(err);
        });
    },
    delete_my_reviews: function(review_pk) {
      if (confirm("정말 삭제하시겠습니까?")) {
        axios
          .delete(`http://127.0.0.1:8000/review/${review_pk}/delete`)
          .then((res) => {
            console.log("DELETED", res);
            this.reviewList.splice(review_pk, 1);
            this.$router.go();
            console.log("삭제성공");
          })
          .catch((err) => {
            console.log(err);
          });
      }
    },
    detailshow(index) {
      this.$router.push({
        name: "ReviewUpdate",
        params: {
          ReviewId: index,
        },
      });
    },
    computedAvg: function() {
      let sum = 0;
      let avg = 0;
      for (let i = 0; i < this.reviewList.length; i++) {
        sum += this.reviewList[i].point;
      }
      avg = Math.round((sum / this.reviewList.length) * 10) / 10;

      this.avg = avg;
    },
  },
};
</script>

<style scoped>
.page-title {
  margin-bottom: 1em;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.page-title-1 {
  font-weight: bolder;
  font-size: 1.2em;
}
.page-title-2 {
  font-size: 0.875em;
}
.page-title-2 > span {
  color: rgb(231, 194, 43);
}
.myreview-item {
  padding: 1em 0.8em;
  border-top: 1px solid rgb(72, 72, 72);
}
#myreview-item-1 {
  text-align: left;
}
#myreview-item-1-2 > button {
  border: none;
  background-color: rgb(85, 85, 85);
  color: rgb(225, 225, 225);
  font-size: 0.7em;
  padding: 0.2em 0.4em;
  margin: 0 0.7em 1em 0;
}
#myreview-item-2 {
  text-align: right;
}
.myreview-item-title {
  font-size: 1em;
}
.myreview-item-content {
  font-size: 0.86em;
}
.myreview-item-point {
  font-size: 0.8em;
  margin-bottom: 0.6em;
  color: gray;
}
.myreview-item-point > .filled {
  color: rgb(231, 194, 43);
}
.myreview-item-date {
  font-size: 0.6em;
  color: gray;
}
@media screen and (max-width: 320px) {
  #myreview-item-1 {
    display: block;
  }
  #myreview-item-1-2 > button {
    border: none;
    background-color: rgb(85, 85, 85);
    color: rgb(225, 225, 225);
    font-size: 0.7em;
    padding: 0.2em 0.4em;
  }
}
</style>
