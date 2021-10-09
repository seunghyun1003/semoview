<template>
  <div id="signup">
    <h1><strong>Signup</strong> </h1>
    <div>
      <label for="username"></label>
      <input type="text" id="username" v-model="credentials.username" placeholder="USERNAME">
    </div>
    <div>
      <label for="email"></label>
      <input type="email" id="email" v-model="credentials.email" placeholder="EMAIL">
    </div>
    <div>
      <label for="password"></label>
      <input type="password" id="password1" v-model="credentials.password1" placeholder="PASSWORD">
    </div>
    <div>
      <label for="passwordConfirmation"></label>
      <input type="password" id="password2" v-model="credentials.password2" placeholder="PASSWORD CHECK">
    </div>
    <button @click="signup">회원가입</button>
  </div>
</template>

<script>
import axios from 'axios'

// const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Signup',
  data: function () {
    return {
      credentials : {
        username : null,
        email : null,
        password1 : null,
        password2 : null,
      }
    }
  },
  methods: {
    signup: function () {
      axios ({
        method : 'post',
        url : 'http://127.0.0.1:8000/rest-auth/signup/',
        data: this.credentials,
      })
        .then(res => {
          console.log(res)
          // 회원가입에 성공하면 로그인 페이지로 보내기
          this.$router.push({ name : 'Login'})
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>

<style scoped>
#signup{
    display: flex;
    flex-flow: column;
    justify-content : center;
    align-items: center;
    height:100%;
    padding-bottom: 10em;
}
#signup > h1 {
    margin-bottom: 1em;
}
input[type="text"],
input[type="password"],
input[type="email"]{
text-align:center;
margin-bottom: 0.6em;
}
#signup > button {
    background-color: rgb(85, 85, 85);
    border:gray;
    color:white;
    padding: 0.4em 0.6em;
    border-radius: 0.4em;
    margin: 0.8em 0 1.5em 0;
}
</style>