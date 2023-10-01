import { createApp } from 'vue'
import App from './App.vue'
import router from './routers'

import { getUserRole } from './auth';
import './registerServiceWorker'

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

createApp(App).use(router).mount('#app');
