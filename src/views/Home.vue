<template>
  <div id="home">
    <div class="page-title">
      예매랭킹
    </div>
    <div class="stage-list">        
      <div class="item" v-for="stage in stageList" :key="stage.id" @click="detailshow(stage.id)">
          <div id="item-id">{{stage.id}} </div> 
          <div id="item-img"><img :src="stage.stageImglink" alt /></div>
          <div id="item-title"><span><strong>{{stage.stageTitle}}</strong></span></div> 
      </div> 
      <div class="card-footer pb-0 pt-3">
            <jw-pagination :items="exampleItems" @changePage="onChangePage"></jw-pagination>
        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const exampleItems = [...Array(10).keys()].map(i => ({ id: (i+1), name: 'Item ' + (i+1) }));

export default {
  name: 'Home',
  data() {
    return {
      stageList : [],
      exampleItems,
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
    onChangePage(stageList) {
      // update page of items
      this.stageList = stageList;
    },
    detailshow(index) {
      this.$router.push({
        name: "Detail",
        params: {
          contentId: index
        }
      });
    }
  }
}
</script>

<style scoped>
  #home{
    overflow: auto ;
  }
  .page-title{
    font-weight: bolder;
    font-size: 1.2em;
    text-align: left;
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
</style>
