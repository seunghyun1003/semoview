<template>
  <div id="home">
    <div id="home-header">
      <div class="header-title">
        예매랭킹
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
          <div id="item-title"><span><strong>{{stage.stageTitle}}</strong></span></div> 
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
      stageList : [],
      currentPage: 1,
      perPage: 40,
    }
  },
  created: function() {
    this.fetch_all_stage(); 
  },
  methods: {
    fetch_all_stage: function () {
      axios.get('http://127.0.0.1:8000/stages')
      .then(res => {             
        this.stageList = res.data;
      })
      .catch(err => {
        console.log(err)
      })
    },
    detailshow(index) {
      this.$router.push({
        name: "Detail",
        params: {
          contentId: index
        }
      });
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
    font-weight: bolder;
    font-size: 1.2em;
    text-align: left;
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

  .pagination{
    margin-top: 1.4em;
  }
</style>