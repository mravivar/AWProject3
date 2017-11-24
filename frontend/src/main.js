import App from './App.vue'
import router from './router'

Vue.component('loading', require('./components/loading').default);
Vue.component('top-bar', require('./components/top-bar').default);
Vue.component('pagination', require('./components/pagination').default);
Vue.component('questions-list', require('./components/questions-list').default);

new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})
