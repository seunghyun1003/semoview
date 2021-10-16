<template>
  <div id="nav">
    <div class="logo">
      <router-link to="/">
        <span>MOVIEW</span>
      </router-link>
    </div>
    <div class="nav-menu">
      <div class="nav-item">
        <b-nav-item-dropdown
          id="my-nav-dropdown"
          v-bind:text="username"
          toggle-class="nav-link-custom"
          right
        >
          <b-dropdown-item router-link :to="{ name: 'Search' }">
            검색 <b-icon icon="search"></b-icon>
          </b-dropdown-item>
          <b-dropdown-divider></b-dropdown-divider>
          <b-dropdown-item v-if="isLogin">
            <router-link :to="{ name: 'MyReview' }">MY 리뷰</router-link>
            <div></div>
            <button @click="logout">로그아웃</button>
          </b-dropdown-item>
          <b-dropdown-item v-else router-link :to="{ name: 'Signin' }"
            >SignIn / SignUp
          </b-dropdown-item>
        </b-nav-item-dropdown>
      </div>
    </div>
  </div>
</template>

<script>
import jwt_decode from "jwt-decode";
export default {
  name: "Nav",
  data: function() {
    return {
      isLogin: false,
      username: this.isLogin
        ? jwt_decode(localStorage.getItem("jwt")).username
        : "-",
    };
  },
  methods: {
    logout: function() {
      if (confirm("로그아웃 하시겠습니까?")) {
        localStorage.removeItem("jwt"), this.$router.push({ name: "Signin" });
        this.$router.go();
      }
    },
  },
  created: function() {
    // 로컬스토리지에 jwt 이 존재하는지에 따라 로그인 여부 판단하기
    const token = localStorage.getItem("jwt");
    if (token) {
      this.isLogin = true;
      this.username = jwt_decode(localStorage.getItem("jwt")).username;
    }
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
#nav {
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
.logo > a {
  color: white;
  font-size: 1.2em;
  font-weight: bold;
  background-color: inherit;
  border: none;
  margin: 0;
  padding: 0;
  text-decoration: none;
}
.nav-menu {
  display: flex;
  justify-content: end;
}
.nav-item > button,
.nav-item > a {
  color: white;
  background-color: inherit;
  border: none;
  padding: 0 0.2em 0 0.7em;
  text-decoration: none;
}
.nav-link {
  font-size: 1.1em;
}
#my-nav-dropdown a > a {
  text-decoration-line: none;
  color: black;
}
#my-nav-dropdown > ul {
  background-color: rgb(46, 46, 46);
  box-shadow: 4px 4px 4px rgb(32, 32, 32);
  text-align: center;
  margin: 0;
  padding: 0;
}
.dropdown-divider {
  color: lightgray;
}
#my-nav-dropdown > ul > li :hover,
#my-nav-dropdown > ul > li :focus {
  background-color: inherit;
}
#my-nav-dropdown > ul > li > a > button {
  background-color: inherit;
  border: none;
  color: white;
  padding: 0;
}
</style>
