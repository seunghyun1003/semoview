<template>
  <div id="search">
    <div id="searchrequire">
      <div class="search-form-input">
        <b-form-input id="input-default" 
        type="text"
        v-model="keyword"
        v-on:input="keywordChanged()"
        v-on:keyup.enter="searchresultshow(keyword)"
        >
        {{keyword}}
        </b-form-input>
      </div>
      <div class="search-form-button">
        <button @click="searchresultshow(keyword)">
          검색
        </button>
      </div>
    </div>
    <div v-if="isResultShow" v-bind:keyword="keyword" class="search-result">
        <div class="item"  v-if="resultList.length > 0">
            <div v-for="stage in resultList.slice(perPage*(currentPage-1),perPage*(currentPage))" :key="stage.id" @click="detailshow(stage.id)">
                <div id="item-id">{{stage.id}} </div> 
                <div id="item-img"><img :src="stage.stageImglink" alt /></div>
                <div id="item-title"><span><strong>{{stage.stageTitle}}</strong></span></div> 
            </div> 
            <b-pagination
            v-model="currentPage"
            :total-rows="resultList.length"
            :per-page="perPage"
            first-text="<<"
            prev-text="<"
            next-text=">"
            last-text=">>"
            align="center"
            ></b-pagination>
        </div>
        <div class="item" v-if="resultList.length == 0">
            조건에 만족하는 검색결과가 없습니다.
        </div>
    </div>
    <div v-else class="search-result">
        검색버튼을 클릭해주세요.
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Search',
  data() {
    return {
      isResultShow:false,
      keyword: '',
      resultList : [],
      currentPage: 1,
      perPage: 10,
    }
  },
  methods: {
    searchresultshow(keyword) {
      if (keyword !== ''){
        console.log('"',keyword,'"' + ' 검색');
        this.isResultShow = true;
        this.getSearchResult(keyword);
      } else {
        alert('검색어를 입력해주세요!');
      }
    },
    keywordChanged() {
      this.isResultShow = false
    },
    getSearchResult: function (keyword) {
        event.preventDefault()
        axios.get(`http://127.0.0.1:8000/search/keyword/${keyword}`)
        .then(res => {      
            this.resultList = res.data;
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
.page-title{
font-weight: bolder;
font-size: 1.2em;
text-align: left;
}
#searchrequire {
  display: flex;
  width: 100%;
  border-bottom: 2px solid gray;
  padding-bottom: 1em;
  justify-content: space-evenly;
}
.search-form-input {
  flex-basis: 80%;
}
.search-form-input > input[type="text"] {
  width: 100%;
}
.search-form-button {
  flex-basis: 16%;
}
.search-form-button > button {
  width: 100%;
  height: 2.375em;
  background-color: rgb(192, 57, 43);
  border: 1px solid gray;
  border-radius: 0.4em;
  color: white;
  font-weight: 600;
}

.search-result{
    margin-top: 1em;
}
.stage-list{
}
.item > div{
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
