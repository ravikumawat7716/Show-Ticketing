<template>
    <div class="nav">
        <router-link to="/summary" style="float: left;">Summary</router-link>
        <a v-on:click="logout" href="#">Logout</a>
        <a href="/admin/dashboard">Dashboard</a>
        
    </div>
    </template>
    <script>
    export default{
        name : 'SummaryNavbar',
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
        background-color: yellow;
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