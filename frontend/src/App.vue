<template>
  <div id="app">
    <top-bar/>
    <router-view/>
  </div>
</template>

<script>
require('./assets/js/bootstrap.js');

export default {
  name: 'app'
}
</script>

<style lang="scss">

@import 'src/assets/sass/app.scss';

</style>
