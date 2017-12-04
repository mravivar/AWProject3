import App from './App.vue'
import router from './router'

Vue.component('loading', require('./components/loading').default);
Vue.component('top-bar', require('./components/top-bar').default);
Vue.component('pagination', require('./components/pagination').default);
Vue.component('questions-list', require('./components/questions-list').default);
Vue.component('line-item', require('./components/line-item').default);
Vue.component('user-line-item', require('./components/user-line-item').default);
Vue.component('add-answer', require('./components/add-answer').default);
Vue.component('graph', require('./components/graph').default);
Vue.component('heat-map', require('./components/heat-map').default);

new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})
