<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
window.axios = require('axios');
window.API_BASE_URL = 'http://localhost:5000/api';

export default {
  name: 'app'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
