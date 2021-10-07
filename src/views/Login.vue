<template>
    <div>
        <h1>Login</h1>
        <div>
        <label for="username">사용자 이름: </label>
        <input type="text" id="username" v-model="credentials.username">
        </div>
        <div>
        <label for="password">비밀번호: </label>
        <input type="password" id="password" v-model="credentials.password">
        </div>

        <button @click="login">로그인</button>
        <div>
            <router-link :to="{name: 'Signup'}">아직 회원이 아니신가요?</router-link>
        </div>

    </div>
</template>

<script>
import axios from 'axios'

// const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
    name: 'Login',
    data: function () {
        return {
            credentials : {
                username : null,
                password : null,
            }
        }
    },
    methods: {
        login: function () {
            axios({
                method : 'post',
                url : 'http://127.0.0.1:8000/api-token-auth/obtain_token/',
                data : this.credentials,
            })
            .then(res => {
                // 로컬스토리지에 토큰 저장
                localStorage.setItem('jwt', res.data.token)
                
                this.$router.push({ name : 'Home'})
                this.$router.go()
            })
            .catch(err => {
                console.log(err)
            })
        },
    },
}
</script>