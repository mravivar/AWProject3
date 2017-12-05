<template>
  <div id="app">
    <top-bar/>
    <router-view :key="$route.name + ($route.params.id || '')"/>
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
