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
        <router-link to="/myreview">
          <b-icon icon="person-fill">-</b-icon>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Nav',
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#nav{
  display: flex;
  height: 3em;
  line-height: 3em;
  background-color: rgb(192, 57, 43);
  justify-content: space-between;
  padding: 0 1em;
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
.nav-menu{
  display: flex;
}
.nav-item{
  padding: 0 0.75em;
}
.nav-item > button,
.nav-item > a{
  color: white;
  background-color: inherit;
  border: none;
  padding:0;
  text-decoration:none;
}
.nav-item > a{
  font-size: 1.33em;
}
</style>
