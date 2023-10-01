<template>
    <div class="signup">
        <h1 style="color: black;">User Login</h1>
        <div class="register">
            <form @submit.prevent="loginUser">
                <input v-model="email" type="email" required="true" placeholder="Enter Your Email Address" />
                <input v-model="password" type="password" required="true" placeholder="Enter Your Password" />
                <button type="submit">
                    {{ loading ? 'Logging In...' : 'Login' }}
                </button>
            </form>
            <router-link class="routerLink" to="/register"><button style="background-color: blue;">Register</button></router-link>
        </div>
    </div>
</template>
  
<script>
import axios from 'axios';

export default {
    name: 'UserLogin',
    data() {
        return {
            email: '',
            password: '',
            loading: false,
        };
    },
    methods: {
        async loginUser() {
            try {
                this.loading = true;
                const url = 'http://127.0.0.1:5000/login';
                const data = {
                    email: this.email,
                    password: this.password,
                }
                const config = {
                    headers: {
                        'Content-Type': 'application/json'
                    }
                }
                const response = await axios.post(url, data, config);
                if (response.status == 200) {
                    const token = JSON.stringify(response.data.access_token)
                    if (token != undefined) {
                        localStorage.setItem("Auth-Token", token)
                        localStorage.setItem("name", JSON.stringify(response.data.username))
                        localStorage.setItem("user-role", JSON.stringify(response.data.userrole))
                        this.loading = false;
                        alert('You are logged in.')
                    }
                    let userRole = JSON.stringify(response.data.userrole)
                    let Role = JSON.parse(userRole || {});

                    if (Role == "USER") {
                        this.$router.push({ name: 'Home' })
                    }
                    if (Role == "ADMIN") {
                        this.$router.push({ name: 'AdminDashboard' })
                    }

                }
            } catch (error) {
                this.loading = false;
                alert('Incorrect Credentials.')
            } finally {
                this.loading = false;
            }
        },
    },
    mounted() {
        let token = localStorage.getItem("Auth-Token");
        if (token) {
            let userRole = localStorage.getItem("user-role")
            let Role = JSON.parse(userRole || {});
            if (Role == "USER") {
                this.$router.push({ name: 'Home' })
            }
            if (Role == "ADMIN") {
                this.$router.push({ name: 'AdminDashboard' })
            }

        }
    }
};
</script>
<style>
.signup {
    background-color: #ffffff;
    border-radius: 10px;
    padding: 20px;
    padding-bottom: 30px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
    margin-left: auto;
    margin-right: auto;
    margin-bottom: 40px;
    width: 400px;
}

.register input {
    margin-top: 20px;
    width: 200px;
    height: 30px;
    margin-left: auto;
    margin-right: auto;
    display: block;
    border-radius: 3px;
    border: #0d2329 sloid 1px;
}

.register button {
    margin-top: 20px;
    width: 210px;
    height: 36px;
    margin-left: auto;
    margin-right: auto;
    display: block;
    border-radius: 3px;
    border: #0d2329 sloid 1px;
    background-color: green;
    color: #ffffff;
    font-style: bold;
}

.register input::placeholder {
    color: #0d2329;
    font-style: bold;
}

.routerLink {
    text-decoration: none;
}
</style>