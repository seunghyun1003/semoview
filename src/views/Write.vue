<template>
  <div id="home">
    <div class="page-title">
      리뷰 작성
    </div>
    <div>
      
    </div>
  </div>
</template>

<script>
export default {
  name: 'Write',
  data: function () {
    return {

    }
  },
  beforeCreate() {
    if (localStorage.getItem('jwt')){ 
      console.log("로그인된 사용자")
    } else {
      console.log("로그인 안된 사용자")
      if (confirm('로그인이 필요한 서비스입니다. 로그인 하시겠습니까?')) {
        // Save it!
        this.$router.push({name : 'Login'})
      } else {
        // Do nothing!
        this.$router.push({name : 'Home'})
      }
    } 
  }
  
}
</script>

<style>
  .page-title{
    font-weight: bolder;
    font-size: 1.2em;
    text-align: left;
  }
</style>
