<template>
  <div id="signup">
    <div class="errorMsg">{{ message }}</div>
    <h1><b>Signup</b></h1>
    <div>
      <label for="username"></label>
      <input
        type="text"
        id="username"
        v-model="credentials.username"
        placeholder="USERNAME"
      />
      <button id="iddupcheckBtn" @click="checkUsername(credentials.username)">
        중복확인
      </button>
    </div>
    <div>
      <label for="email"></label>
      <input
        type="email"
        id="email"
        v-model="credentials.email"
        placeholder="EMAIL"
      />
    </div>
    <div>
      <label for="password"></label>
      <input
        type="password"
        id="password1"
        v-model="credentials.password1"
        placeholder="PASSWORD"
      />
    </div>
    <div>
      <label for="passwordConfirmation"></label>
      <input
        type="password"
        id="password2"
        v-model="credentials.password2"
        placeholder="PASSWORD CHECK"
        @keyup.enter="signup"
      />
    </div>
    <button @click="signup">회원가입</button>
  </div>
</template>

<script>
import axios from "axios";

// const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: "Signup",
  data: function() {
    return {
      message: "",
      ckUsername: false,
      credentials: {
        username: null,
        email: null,
        password1: null,
        password2: null,
      },
    };
  },
  methods: {
    checkUsername: function(username) {
      if (username != null) {
        axios({
          method: "post",
          url: "http://127.0.0.1:8000/ckeck/username",
          data: username,
        })
          .then((res) => {
            if (res.data) {
              this.message = "사용가능한 아이디입니다.";
              this.ckUsername = true;
            } else {
              this.message = "다른 아이디를 사용해주세요.";
              this.ckUsername = false;
            }
          })
          .catch((err) => {
            console.log(err);
            this.message = "실패) 다른 아이디로 시도해주세요.";
          });
      } else {
        this.message = "중복확인 실패) USERNAME을 입력해주세요.";
      }
    },
    signup: function() {
      if (
        this.credentials.username != "" &&
        this.credentials.email != "" &&
        this.credentials.password1 != "" &&
        this.credentials.password2 != ""
      ) {
        if (this.ckUsername == true) {
          axios({
            method: "post",
            url: "http://127.0.0.1:8000/rest-auth/signup/",
            data: this.credentials,
          })
            .then((res) => {
              console.log(res.status, "Success Signup");
              // 회원가입에 성공하면 로그인 페이지로 보내기
              this.$router.push({ name: "Signin" });
            })
            .catch((err) => {
              console.log(err);
              this.message = "실패) 다시 시도해주세요.";
            });
        } else {
          alert("ID 중복 확인이 필요합니다.");
        }
      } else {
        alert("모든 정보를 입력해주세요.");
      }
    },
  },
};
</script>

<style scoped>
#signup {
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
#signup > h1 {
  margin-bottom: 1em;
  font-size: 2.5em;
}
input[type="text"],
input[type="password"],
input[type="email"] {
  text-align: center;
  margin-bottom: 1.2em;
  padding: 0.2em 0.4em;
}
#iddupcheckBtn {
  font-size: 0.8em;
  background-color: gray;
  border: none;
  color: white;
  margin-left: 0.4em;
  padding: 0.2em 0.4em;
  border-radius: 0.8em;
}
#signup > button {
  background-color: rgb(85, 85, 85);
  border: gray;
  color: white;
  padding: 0.4em 0.6em;
  border-radius: 0.4em;
  margin: 0.8em 0 1.5em 0;
}
@media screen and (max-width: 300px) {
  input[type="text"] {
    text-align: center;
    margin-bottom: 0.6em;
  }
  #iddupcheckBtn {
    margin-bottom: 1em;
  }
}
</style>
