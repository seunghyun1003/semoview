<template>
  <div id="home">
    <div id="home-header">
      <div class="header-title">
        <div>
          <button v-bind:class="setBtnColor(1)" @click="toggleRank(1)">
            예매랭킹순
          </button>
          <button v-bind:class="setBtnColor(2)" @click="toggleRank(2)">
            리뷰평점순
          </button>
          <button v-bind:class="setBtnColor(3)" @click="toggleRank(3)">
            리뷰개수순
          </button>
        </div>
      </div>
      <div class="header-nav">
        <button>
          <router-link :to="{ name: 'Search' }">
            <b-icon icon="search"></b-icon>
          </router-link>
        </button>
      </div>
    </div>
    <div class="stage-list">
      <div
        class="item"
        v-for="stage in stageList.slice(
          perPage * (currentPage - 1),
          perPage * currentPage
        )"
        :key="stage.id"
        @click="detailshow(stage.id)"
      >
        <div class="item-id">{{ stage.id }}</div>
        <div class="item-img"><img :src="stage.stageImglink" alt /></div>
        <div class="item-title">
          <span>
            <div>
              <span class="filled">★</span> {{ stage.pointAvg }} ({{
                stage.reviewCount
              }})
            </div>
            <strong>{{ stage.stageTitle }}</strong>
          </span>
        </div>
      </div>
      <b-pagination
        v-model="currentPage"
        :total-rows="1000"
        :per-page="perPage"
        first-text="<<"
        prev-text="<"
        next-text=">"
        last-text=">>"
        align="center"
      ></b-pagination>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Home",
  data() {
    return {
      buttontoggle: localStorage.getItem("rank"),
      stageList: [],
      currentPage: 1,
      perPage: 20,
    };
  },
  created: function() {
    this.fetch_all_stage();
  },
  methods: {
    fetch_all_stage: function() {
      let url = "";
      if (this.buttontoggle == 1) {
        url = "http://127.0.0.1:8000/stages_1";
      } else if (this.buttontoggle == 2) {
        url = "http://127.0.0.1:8000/stages_2";
      } else {
        url = "http://127.0.0.1:8000/stages_3";
      }
      axios
        .get(url)
        .then((res) => {
          this.stageList = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    detailshow: function(index) {
      this.$router.push({
        name: "Detail",
        params: {
          contentId: index,
        },
      });
    },
    toggleRank: function(condition) {
      this.buttontoggle = condition;
      localStorage.setItem("rank", this.buttontoggle);

      this.fetch_all_stage();
      this.$router.go();
    },
    setBtnColor: function(condition) {
      if (this.buttontoggle == condition) {
        return "actBtn";
      } else return "deactBtn";
    },
  },
};
</script>

<style scoped>
#home {
  overflow: auto;
}
#home-header {
  display: flex;
  justify-content: space-between;
}
.header-title > div > button {
  font-size: 0.85em;
  text-align: left;
  border-radius: 0.4em;
  border: none;
  margin: 0 0.6em 0.2em 0;
  padding: 0.25em 0.5em;
  background-color: rgb(75, 75, 75);
  box-shadow: 0.8px 0.8px 0.8px 0.8px rgb(34, 34, 34);
  color: rgb(240, 240, 240);
}
.actBtn {
  background-color: rgb(192, 57, 43) !important;
  box-shadow: 0.3px 0.3px 0.3px 0.3px rgb(75, 75, 75) !important;
  color: white !important;
}
.header-nav > button {
  color: white;
  background-color: inherit;
  border: none;
  padding: 0 1em;
  text-decoration: none;
}
.item {
  display: flex;
  height: 10em;
  line-height: 10em;
  padding: 0 0.4em;
}
.item-id {
  color: rgba(192, 58, 43);
  font-weight: bold;
  font-size: x-large;
  padding: 0 1em 0 0;
}
.item-img {
  min-width: 120px;
  width: 120px;
  height: 8em;
  padding: 0 1em 0 0;
}
.item-img img {
  width: 100%;
  height: 100%;
}
.item-title {
  padding-top: 1.5em;
}
.item-title > span {
  font-size: small;
  white-space: normal;
  line-height: 1.2;
  height: 4.2em;
  text-align: left;
  word-wrap: break-word;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.item-title > span > div {
  padding-bottom: 0.6em;
}
.item-title .filled {
  color: rgb(231, 194, 43);
}
.pagination {
  margin: 1.4em 0;
}

@media screen and (max-width: 348px) {
  .header-nav > button {
    display: none;
  }
  .header-title > div > button {
    font-size: 0.8em;
  }
}
@media screen and (max-width: 300px) {
  #home-header {
    display: flex;
    justify-content: space-between;
  }
  .header-title > div > button {
    margin: 0 0.4em 0.2em 0;
  }

  .item {
    display: flex;
    height: 7.2em;
    line-height: 7.2em;
    padding: 0 0.4em;
  }
  .item-id {
    color: rgba(192, 58, 43);
    font-weight: bold;
    font-size: large;
    padding: 0 0.8em 0 0;
  }
  .item-img {
    min-width: 90px;
    width: 90px;
    height: 6em;
    padding: 0 0.6em 0 0;
  }
  .item-img img {
    width: 100%;
    height: 100%;
  }
  .item-title {
    padding-top: 0.8em;
  }
  .item-title > span {
    font-size: small;
    white-space: normal;
    line-height: 1.2;
    height: 4.2em;
    text-align: left;
    word-wrap: break-word;
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }
  .item-title > span > div {
    padding-bottom: 0.6em;
  }
}
</style>
