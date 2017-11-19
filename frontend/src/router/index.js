import Router from 'vue-router'

const routerOptions = [
  { path: '/', component: 'home' },
  { path: '/settings', component: 'settings' },
  { path: '/questions/:id', name: 'question', component: 'question'}
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
