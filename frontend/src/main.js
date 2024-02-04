import { createApp } from 'vue'
import App from './App.vue'
import router from './routers'

import { getUserRole } from './auth';
import './registerServiceWorker'

// const globalData = {
  
//   backendUrl: "http://127.0.0.1:5000",
// };

router.beforeEach((to, from, next) => {
  const requiresAuth = to.meta.requiresAuth;
  const requiredRoles = to.meta.roles;

  if (requiresAuth) {
    if (!getUserRole()) {
      return next('/login');
    } else if (requiredRoles && !requiredRoles.includes(getUserRole())) {
      return next('/unauthorized');
    }
  }

  next(); // Allow access
});

const app = createApp(App)

// app.config.globalProperties.$globalData = globalData;

app.use(router)
app.mount('#app');
