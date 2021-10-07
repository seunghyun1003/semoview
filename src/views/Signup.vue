<template>
  <div id="Signup">
    <h1>Signup</h1>
    <div>
      <label for="username">사용자 이름: </label>
      <input type="text" id="username" v-model="credentials.username">
    </div>
    <div>
      <label for="email">이메일: </label>
      <input type="email" id="email" v-model="credentials.email">
    </div>
    <div>
      <label for="password">비밀번호: </label>
      <input type="password" id="password1" v-model="credentials.password1">
    </div>
    <div>
      <label for="passwordConfirmation">비밀번호 확인: </label>
      <input type="password" id="password2" v-model="credentials.password2">
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