<template>
  <div id="detail">
    <div id="stage-item">
      <div class="stage-img">
        <div id="item-img"><img :src="stage.stageImglink" alt /></div>
      </div>
      <div class="stage-info">
        <div class="stage-id" v-if="stage.id">
          <span>예매 {{ stage.id }}위</span>
        </div>
        <div class="stage-title">
          {{ stage.stageTitle }}
        </div>
        <div class="stage-pointAvg" v-if="stage.pointAvg >= 0">
          <span>★</span> {{ stage.pointAvg }} ({{ stage.reviewCount }})
        </div>
      </div>
    </div>

    <div id="review">
      <div v-if="isShow == false">
        <div class="review-header">
          <div class="review-title">최근 리뷰</div>
          <div class="review-write-btn">
            <button @click="showReviewForm()" v-b-modal.modal-prevent-closing>
              <b-icon icon="pencil-square"></b-icon>
            </button>
          </div>
        </div>
        <b-modal id="modal-prevent-closing" ref="modal" @ok="goLogin" centered
          >로그인이 필요한 서비스입니다. 로그인하시겠습니까?</b-modal
        >
        <div v-if="stage.reviewCount" class="review-item">
          <div v-for="review in reviewList" :key="review.id">
            <div id="review-item-1">
              <div class="review-item-username">{{ review.user_username }}</div>
              <div class="review-item-point">
                <span
                  class="filled"
                  v-for="review in review.point"
                  :key="review.point"
                  >★</span
                >
                <span v-for="review in 5 - review.point" :key="review.point"
                  >☆</span
                >
              </div>
            </div>
            <div id="review-item-2">
              <div class="review-item-content">{{ review.reviewContents }}</div>
              <div class="review-item-date">
                {{ $moment(review.created_at).format("YYYY-MM-DD") }}
              </div>
            </div>
          </div>
        </div>
        <div v-else class="review-none">
          아직 작성된 리뷰가 없습니다.
        </div>
      </div>

      <div v-else>
        <div class="review-title">연극은 어떠셨나요?</div>
        <b-form @submit="onSubmit" @reset="onReset">
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
            placeholder="내용을 입력해주세요."
            required
          ></b-form-textarea>
          <div class="btns">
            <b-button type="reset">취소</b-button>
            <b-button type="submit" variant="primary">완료</b-button>
          </div>
        </b-form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import StarRating from "vue-star-rating";
import jwt_decode from "jwt-decode";

export default {
  name: "Detail",
  components: {
    StarRating,
  },
  data() {
    return {
      stage: [],
      reviewList: [],
      isLogin: true,
      isShow: false,
      form: {
        point: 0,
        content: "",
      },
    };
  },
  created: function() {
    this.fetch_this_stage();
    this.fetch_all_review();
    if (localStorage.getItem("jwt")) {
      this.isLogin = true;
    } else this.isLogin = false;
  },
  methods: {
    setToken: function() {
      // header 내용에 토큰 붙여주기
      const token = localStorage.getItem("jwt");
      const config = {
        Authorization: `JWT ${token}`,
      };
      return config;
    },
    fetch_this_stage: function() {
      axios
        .get("http://127.0.0.1:8000/stages_1")
        .then((res) => {
          const index = this.$route.params.contentId - 1;
          this.stage = res.data[index];
        })
        .catch((err) => {
          console.log(err);
        });
    },
    fetch_all_review: function() {
      const url = `http://127.0.0.1:8000/reviews/${this.$route.params.contentId}`;
      axios({
        method: "get",
        url: url,
      })
        .then((res) => {
          this.reviewList = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    showReviewForm() {
      if (this.isLogin == false) {
        console.log("modal show");
      } else {
        this.isShow = true;
      }
    },
    goLogin() {
      this.$router.push({ name: "Signin" });
    },
    onSubmit(event) {
      event.preventDefault();
      if (this.form.content === 0) {
        alert("별점을 선택해주세요.");
      }

      const userId = jwt_decode(localStorage.getItem("jwt")).user_id;

      const url = `http://127.0.0.1:8000/stage/${this.$route.params.contentId}/create`;
      axios
        .post(url, {
          headers: this.setToken(),
          user_id: userId,
          stage_id: this.$route.params.contentId,
          point: this.form.point,
          reviewContents: this.form.content,
        })
        .then((res) => {
          this.reviewList.push(res.data);
          this.form.point = 0;
          this.form.content = "";
          this.isShow = false;
          this.$router.go();
        })
        .catch((err) => {
          console.log(err);
        });
    },
    onReset(event) {
      event.preventDefault();
      this.form.content = "";
      this.form.point = 0;
      console.log("작성취소");
      this.isShow = false;
    },
    deleteReview: function(review) {
      axios({
        method: "delete",
        url: `http://127.0.0.1:8000/reviews/${review.id}/`,
        headers: this.setToken(),
      })
        .then((res) => {
          console.log(res);
          this.fetch_all_review();
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style scoped>
#detail {
  overflow: auto;
}
#stage-item {
  display: flex;
  border-bottom: 1px solid rgb(157, 157, 157);
  text-align: left;
}
.stage-id {
  font-size: 0.85em;
  margin-top: 0.8em;
}
.stage-id > span {
  font-size: 1em;
  color: rgb(192, 57, 43);
  font-weight: bold;
}
.stage-title {
  font-weight: bold;
  font-size: 1em;
  margin-top: 0.4em;
}
.stage-pointAvg {
  margin-top: 0.4em;
}
.stage-pointAvg > span {
  font-size: 0.8em;
  padding-top: 0.6em;
  color: rgb(231, 194, 43);
}
.stage-img {
  padding: 0.8em 0.6em 1.8em;
}
.stage-pointAvg {
  font-size: 0.8em;
}
#item-img {
  min-width: 140px;
  width: 140px;
  height: 10em;
  padding: 0 1em 0 0;
}
#item-img img {
  width: 100%;
  height: 100%;
}

#review {
  padding: 1em;
}
.review-header {
  display: flex;
  justify-content: space-between;
}
.review-title {
  font-size: 1.1em;
  font-weight: bold;
  display: flex;
  align-items: center;
}
.review-title > div {
  font-size: 0.8em;
  padding-left: 1em;
}
.review-write-btn > button {
  background-color: rgb(231, 194, 43);
  border: none;
  color: black;
}
.review-none {
  font-size: 0.85em;
  margin-top: 1.2em;
}
.review-item > div {
  padding: 0.6em 0.6em;
  display: flex;
  justify-content: space-between;
}
#review-item-1 {
  text-align: left;
}
#review-item-2 {
  text-align: right;
}
.review-item-username {
  font-size: 1.1em;
}
.review-item-point {
  font-size: 0.6em;
  color: gray;
}
.review-item-point .filled {
  color: rgb(231, 194, 43);
}
.review-item-date {
  font-size: 0.6em;
  color: gray;
}
.review-item-content {
  padding: 0.4em 0 0.2em 1.4em;
  font-size: 0.86em;
}

#review-item > div > div.vue-star-rating {
  justify-content: center;
}

.vue-star-rating {
  justify-content: center;
  margin: 0.8em 0 1.5em 0;
}
textarea {
  height: 10em;
}
.btns {
  display: flex;
  justify-content: space-between;
  padding: 0 3%;
  margin-top: 1.5em;
}
.btns > button {
  width: 47%;
}
</style>
