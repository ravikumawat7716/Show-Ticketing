<template>
    <div class="nav">
        <router-link to="/" style="float: left;"> {{name}}'s Bookings</router-link>
        <a v-on:click="logout" href="#">Logout</a>
        <router-link to="/">Home</router-link>
        <a href="#">Profile</a>
        
    </div>
    </template>
    <script>
    export default{
        name : 'UserNavbar2',
        data (){
            return{
                name:'',
            }
            
        },
        methods : {
            logout() {
                localStorage.clear()
                alert('You are logged out.')
                this.$router.push({ name: 'UserLogin' })
            }
        },
        mounted(){
            let username = localStorage.getItem("name");
            this.name = JSON.parse(username || {});
        }
    };
    </script>
    <style>
    .nav{
        /* background-color: yellow; */
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