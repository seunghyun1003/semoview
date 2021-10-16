<template>
  <div id="app">
    <Nav />
    <div id="contents">
      <router-view />
    </div>
  </div>
</template>

<script>
import Nav from "./components/Nav.vue";

export default {
  name: "App",
  components: {
    Nav,
  },
  methods: {
    ScrollTop: function() {
      this.$router.go("#");
    },
  },
};
</script>

<style>
#app {
  font-family: "-apple-system", "BlinkMacSystemFont", "Apple SD Gothic Neo",
    "Inter", "Spoqa Han Sans", "Segoe UI", Sans-Serif, "Apple Color Emoji",
    "Segoe UI Emoji", "Segoe UI Symbol";
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  background-color: black;
  color: white;
  height: 100%;
  overflow: auto;
}
#contents {
  margin-top: 3em;
  padding: 1em;
  height: 100%;
}
ul,
li {
  list-style: none;
  padding-left: 0px;
}
a:active,
a:focus,
a {
  color: white !important;
}
</style>
