<template>
  <div id="home">
    <div id="home-header">
      <div class="header-title">
        <button @click="toggleRank()">
          <span v-if="buttontoggle == 1">예매랭킹순</span>
          <span v-else-if="buttontoggle == 2">리뷰평점순</span>
          <span v-else>리뷰개수순</span>
          <b-icon icon="arrow-clockwise"></b-icon>
        </button>
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
    toggleRank:function () {
      if (this.buttontoggle == 1) {
        this.buttontoggle = 2
        console.log('리뷰평점순')
      } else if (this.buttontoggle == 2) {
        this.buttontoggle = 3
        console.log('리뷰개수순')
      } else {
        this.buttontoggle = 1
        console.log('예매랭킹순')
      }

      localStorage.setItem('rank', this.buttontoggle)
      this.fetch_all_stage();
      this.$router.go()
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
  .header-title{
  }
  .header-title > button{
    font-weight: bolder;
    font-size: 1.2em;
    text-align: left;
    text-align: left;
    background-color: inherit;
    border: none;
    color: white
  }
  .header-nav > button{
    color: white;
    background-color: inherit;
    border: none;
    padding:0 1em;
    text-decoration:none;
  }
  .stage-list{
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
    margin-top: 1.4em;
  }
</style>