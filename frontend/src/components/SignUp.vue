<template>
  <div class="signup">
    <h1 id="registartionh1" style="color: black;">Registration</h1>
    <div class="register">
      <form @submit.prevent="registerUser">
        <input v-model="name" type="text" placeholder="Enter Your Name" />
        <input v-model="email" type="email" placeholder="Enter Your Email Address" />
        <input v-model="password" type="password" placeholder="Create Your Password" />
        <button type="submit">
          {{ loading ? 'Registering...' : 'Register' }}
        </button>

      </form>
      <hr class="middleline">
      <p>Already Registered? Login Here.</p>
      <router-link class="routerLink" to="/login"><button style="background-color: #1877f2;">Login</button></router-link>
    </div>
  </div>
</template>
  
<script>
import axios from 'axios';

export default {
  name: 'SignUp',
  data() {
    return {
      name: '',
      email: '',
      password: '',
      loading: false,
    };
  },
  methods: {
    async registerUser() {
      try {
        this.loading = true;
        const url = `${this.$globalData.backendUrl}/register`;
        const data = {
          name: this.name,
          email: this.email,
          password: this.password,
        }
        const config = {
          headers: {
            'Content-Type': 'application/json'
          }
        }
        const response = await axios.post(url, data, config);
        if (response.status == 201) {
          this.loading = false;
          alert(response.data.message)
          console.log(response)
          this.$router.push({ name: 'UserLogin' })
        }

      } catch (error) {
        this.loading = false;
        alert('something went wrong')
      }finally {
        this.loading = false;
      }
    },
  },
  mounted() {
    let token = localStorage.getItem("Auth-Token");
    if (token) {
      this.$router.push({ name: 'Home' })
    }
  }
};
</script>
<style>
</style>