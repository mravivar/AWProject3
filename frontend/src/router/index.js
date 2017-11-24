import Router from 'vue-router'

const routerOptions = [
  { path: '/', name:'home', component: 'home' },
  { path: '/questions', name:'questions', component: 'home' },
  { path: '/settings', component: 'settings' },
  { path: '/questions/:id', name: 'question', component: 'question'},
  { path: '/ask_question', name: 'ask-question', component: 'ask-question'}
]
const routes = routerOptions.map(route => {
  return {
    ...route,
    component: () => import(`../components/${route.component}`)
  }
})

Vue.use(Router)

export default new Router({
  routes,
  mode: 'history'
})
