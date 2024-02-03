<template>
<div class="nav">
    <router-link to="/admin/dashboard" style="float: left;">Admin Dashboard</router-link>
    <a v-on:click="logout" href="#">Logout</a>
    <a href="/summary">Summary</a>
    
</div>
</template>
<script>
export default{
    name : 'AdminNavbar',
    methods : {
        logout() {
            localStorage.clear()
            alert('You are logged out.')
            this.$router.push({ name: 'UserLogin' })
        }
    },
};
</script>
<style>
.nav{
    background-color: #aae15a;
    overflow: hidden;
}
.nav a{
    float: right;
    padding: 14px 16px;
    text-align: center;
    font-size: 17px;
    font-family: Arial, Helvetica, sans-serif;
    color: black;
    text-decoration: none;
}
.nav a:hover{
    background-color: aliceblue;
}
</style>