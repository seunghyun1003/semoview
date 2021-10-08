<template>
  <div id="nav">
    <div class="logo">
      <router-link to="/">
        <strong>SEMOVIEW</strong>
      </router-link>
    </div>
    <div class="nav-menu">
      <div class="nav-item">
        <button>
          <b-icon icon="search"></b-icon>
        </button>
      </div>
      <div class="nav-item">
        <b-nav-item-dropdown
          id="my-nav-dropdown"
          text="username"
          toggle-class="nav-link-custom"
          right
        >
          <b-dropdown-item v-if="isLogin">
            <router-link :to="{ name: 'MyReview' }">작성한 리뷰</router-link>
            <div></div>
            <button @click="logout">Logout</button>
          </b-dropdown-item>
          <b-dropdown-item v-else router-link :to="{ name: 'Login' }">Login
          </b-dropdown-item>
        </b-nav-item-dropdown>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Nav',
  data: function () {
    return {
      isLogin : false,
    }
  },
  methods: {
    logout: function () {
      localStorage.removeItem('jwt'),
      this.$router.push({ name : 'Login'})
      this.$router.go()
    }
  },
  created : function(){
    // 로컬스토리지에 jwt 이 존재하는지에 따라 로그인 여부 판단하기
    const token = localStorage.getItem('jwt')
    if(token){
      this.isLogin = true
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
#nav{
  display: flex;
  height: 3em;
  line-height: 3em;
  background-color: rgb(192, 57, 43);
  justify-content: space-between;
  padding: 0 1em;
  width: 100%;
  position: absolute;
  z-index: 1;
}
.logo {
  font-size: 1.2em;
}
.logo > a{
  color: white;
  background-color: inherit;
  border: none;
  margin: 0;
  padding:0;
  text-decoration:none
}
a > a{
  text-decoration-line: none;
  color: black;
  font-weight: bold;
}
.nav-menu{
  display: flex;
  justify-content: end;
}
.nav-item > button,
.nav-item > a{
  color: white;
  background-color: inherit;
  border: none;
  padding:0 0.2em 0 0.7em;
  text-decoration:none;
}
.nav-link{
  font-size: 1.2em;
}
#my-nav-dropdown > ul {
  background-color: rgb(82, 82, 82);
  border: 1px solid rgb(90, 90, 90);
}
#my-nav-dropdown > ul > li > a > button {
  background-color: inherit;
  border: none;
  color: white;
  font-size: bold;
  padding: 0;
}
</style>