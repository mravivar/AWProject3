import App from './App.vue'
import router from './router'

Vue.component('TopBar', require('./components/TopBar.vue').default);

new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})
