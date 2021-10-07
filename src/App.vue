<template>
  <div id="app">
    <Nav/>
    <div class="contents">
      <router-view/>
    </div>
    <button id="toTop" 
      @click="ScrollTop()"
      width="55" 
      height="55" 
      style="display:scroll;position:fixed;bottom:10px;right:10px;" >
      <b-icon 
        icon="arrow-up-circle"
        title="맨 위로"
      ></b-icon>
    </button>
  </div>
</template>

<script>
import Nav from './components/Nav.vue'

export default {
  name: 'App',
  components: {
    Nav
  },
  methods: {
    ScrollTop() {
      this.$router.go("#");
    }
  }
}
</script>



<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  background-color: black;
  color: white;
  height: 100%;
  overflow: auto ;
}
.contents{
  margin-top: 3em;
  padding: 1em;
}
ul, li{
  list-style:none;
  padding-left:0px;
}
</style>
