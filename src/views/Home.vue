<template>
  <div id="home">
    <div id="home-header">
      <div class="header-title">
        <div>
          <button v-bind:class="setBtnColor(1)" @click="toggleRank(1)">예매랭킹순</button>
          <button v-bind:class="setBtnColor(2)" @click="toggleRank(2)">리뷰평점순</button>
          <button v-bind:class="setBtnColor(3)" @click="toggleRank(3)">리뷰개수순</button>
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
      <div class="item" v-for="stage in stageList.slice(perPage*(currentPage-1),perPage*(currentPage))" :key="stage.id" @click="detailshow(stage.id)">
          <div id="item-id">{{stage.id}} </div> 
          <div id="item-img"><img :src="stage.stageImglink" alt /></div>
          <div id="item-title">
            <span>
              <strong>{{stage.stageTitle}} <div><span>★</span>  {{stage.pointAvg}} ({{stage.reviewCount}})</div></strong>
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
import axios from 'axios'

export default {
  name: 'Home',
  data() {
    return {
      buttontoggle: localStorage.getItem('rank'),
      stageList : [],
      currentPage: 1,
      perPage: 20,
    }
  },
  created: function() {
    this.fetch_all_stage(); 
  },
  methods: {
    fetch_all_stage: function () {
      let url = ''
      if (this.buttontoggle == 1) {
        url = 'http://127.0.0.1:8000/stages_1'
      } else if (this.buttontoggle == 2) {
        url = 'http://127.0.0.1:8000/stages_2'
      } else {
        url = 'http://127.0.0.1:8000/stages_3'
      }
      axios.get(url)
      .then(res => {         
        this.stageList = res.data;
      })
      .catch(err => {
        console.log(err)
      })
    },
    detailshow:function (index) {
      this.$router.push({
        name: "Detail",
        params: {
          contentId: index
        }
      });
    },
    toggleRank:function (condition) {
      this.buttontoggle = condition
      localStorage.setItem('rank', this.buttontoggle)

      this.fetch_all_stage()
      this.$router.go()
    },
    setBtnColor: function (condition) {
      if (this.buttontoggle == condition) {
        return 'actBtn'
      } else return 'deactBtn'
    }
  }
}
</script>

<style scoped>
  #home{
    overflow: auto ;
  }
  #home-header{
    display: flex;
    justify-content: space-between;
  }
  .header-title > div > button{
    font-weight: bolder;
    font-size: 0.85em;
    text-align: left;
    text-align: left;
    border-radius: 0.4em;
    border: none;
    margin-right: 0.6em;
    padding: 0.25em 0.5em;
    background-color: rgb(75, 75, 75);
    color: white;
  }
  .actBtn{
    background-color: rgb(192, 57, 43) !important;
  }
  .header-nav > button{
    color: white;
    background-color: inherit;
    border: none;
    padding:0 1em;
    text-decoration:none;
  }
  .item{
    display: flex;
    height: 10em;
    line-height: 10em;
    padding: 0 0.4em ;
  }
  #item-id{
    color: rgb(192, 57, 43);
    font-weight: bolder;
    font-size: x-large;
    padding: 0 1em 0 0;
  }
  #item-img{
    min-width: 120px;
    width: 120px;
    height: 8em;
    padding: 0 1em 0 0;
  }
  #item-img img{
    width: 100%;
    height: 100%;
  }
  #item-title{
    padding-top: 1.5em;
  }
  #item-title > span{
    font-size: small;
    white-space: normal; 
    line-height: 1.2; 
    height: 3.6em; 
    text-align: left; 
    word-wrap: break-word; 
    display: -webkit-box; 
    -webkit-line-clamp: 3; 
    -webkit-box-orient: vertical;
  }
  #item-title > span > strong > div{
    padding-top: 0.6em;
  }
  #item-title > span > strong > div > span{
    color: rgb(231, 194, 43);
  }
  .pagination{
    margin: 1.4em 0;
  }
</style>