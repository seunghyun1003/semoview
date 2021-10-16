<template>
  <div id="signin">
    <div class="errorMsg">{{ message }}</div>
    <h1><strong>Signin</strong></h1>
    <div>
      <label for="username"></label>
      <input
        type="text"
        id="username"
        v-model="credentials.username"
        placeholder="ID"
      />
    </div>
    <div>
      <label for="password"></label>
      <input
        type="password"
        id="password"
        v-model="credentials.password"
        @keyup.enter="signin"
        placeholder="PASSWORD"
      />
    </div>

    <button @click="signin">로그인</button>
    <div class="singuplink">
      <router-link :to="{ name: 'Signup' }"
        >아직 회원이 아니신가요?</router-link
      >
    </div>
  </div>
</template>

<script>
import axios from "axios";

// const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: "Signin",
  data: function() {
    return {
      message: "",
      credentials: {
        username: null,
        password: null,
      },
    };
  },
  methods: {
    signin: function() {
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/api-token-auth/obtain_token/",
        data: this.credentials,
      })
        .then((res) => {
          // 로컬스토리지에 토큰 저장
          localStorage.setItem("jwt", res.data.token);

          this.$router.push({ name: "Home" });
          this.$router.go();
        })
        .catch((err) => {
          console.log(err);
          this.message = "ID 또는 PASSWORD를 확인해주세요.";
        });
    },
  },
};
</script>

<style scoped>
#signin {
  display: flex;
  flex-flow: column;
  justify-content: center;
  align-items: center;
  height: 100%;
  padding-bottom: 10em;
}
.errorMsg {
  font-size: 0.8em;
  margin-bottom: 2em;
  color: salmon;
}
#signin > h1 {
  margin-bottom: 1em;
  font-size: 2.5em;
}
input[type="text"],
input[type="password"] {
  text-align: center;
  margin-bottom: 1.5em;
  padding: 0.2em 0.4em;
}
#signin > button {
  background-color: rgb(85, 85, 85);
  border: gray;
  color: white;
  padding: 0.4em 0.6em;
  border-radius: 0.4em;
  margin: 0.8em 0 1.5em 0;
}
.singuplink {
  font-size: 0.8em;
}
</style>
