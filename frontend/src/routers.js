import HomePage from './components/HomePage.vue'
import SignUp from './components/SignUp.vue'
import UserLogin from './components/UserLogin.vue'
import AdminDashboard from './components/AdminDashboard.vue'
import AddVenue from './components/AddVenue.vue'
import UpdateVenue from './components/UpdateVenue.vue'
import AddShow from './components/AddShow.vue'
import UpdateShow from './components/UpdateShow.vue'
import ShowBooking from './components/ShowBooking.vue'
import UserBookings from './components/UserBookings.vue'
import AdminSummary from './components/AdminSummary.vue'

import NotFoundComponent from './components/NotFoundComponent.vue'
import { createRouter, createWebHistory } from 'vue-router'



const routes = [
    {
        name: 'Home',
        component: HomePage,
        meta: { requiresAuth: true },
        path: '/'
    },
    {
        name: 'SignUp',
        component: SignUp,
        path: '/register'
    },
    {
        name: 'UserLogin',
        component: UserLogin,
        path: '/login'
    },
    {
        name: 'AdminDashboard',
        component: AdminDashboard,
        meta: { requiresAuth: true, roles: ['Admin'] },
        path: '/admin/dashboard'
    },
    {
        name: 'AddVenue',
        component: AddVenue,
        meta: { requiresAuth: true, roles: ['Admin'] },
        path: '/addvenue'
    },
    {
        name: 'UpdateVenue',
        component: UpdateVenue,
        meta: { requiresAuth: true, roles: ['Admin'] },
        path: '/updatevenue/:id'
    },
    {
        name: 'AddShow',
        component: AddShow,
        meta: { requiresAuth: true, roles: ['Admin'] },
        path: '/addshow/:id'
    },
    {
        name: 'UpdateShow',
        component: UpdateShow,
        meta: { requiresAuth: true, roles: ['Admin'] },
        path: '/updateshow/:id'
    },
    {
        name: 'ShowBooking',
        component: ShowBooking,
        meta: { requiresAuth: true, roles: ['User'] },
        path: '/book/:sid/:vid'
    },
    {
        name: 'UserBookings',
        component: UserBookings,
        meta: { requiresAuth: true, roles: ['User'] },
        path: '/bookings'
    },
    {
        name: 'AdminSummary',
        component: AdminSummary,
        meta: { requiresAuth: true, roles: ['Admin'] },
        path: '/summary'
    },




        // Wildcard route to catch all undefined routes
  { 
    path: '/:catchAll(.*)', 
  component: NotFoundComponent
 },
];

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router