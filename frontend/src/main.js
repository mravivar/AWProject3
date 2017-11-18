import App from './App.vue'
import router from './router'

Vue.component('top-bar', require('./components/top-bar').default);
Vue.component('pagination', require('./components/pagination').default);

new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})
