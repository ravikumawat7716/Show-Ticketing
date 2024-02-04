<template>
  <router-view></router-view>
</template>

<script>

export default {
  name: 'App',
  components: {
  }
}
</script>

<style>
h1{
  text-align: center;
  color: #fff;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color: #3c555b;
  margin-top: 0px;
  flex: 1;
}

.routerLink {
  text-decoration: none;
}
.signup , .addvenue {
  background-color: #ffffff;
  border-radius: 10px;
  padding: 20px;
  padding-bottom: 30px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 40px;
  margin-top: 30px;
  width: 400px;
}

.register input , .addnewvenue input {
  margin-top: 20px;
  width: 200px;
  height: 30px;
  margin-left: auto;
  margin-right: auto;
  display: block;
  border-radius: 3px;
  border: #0d2329 sloid 1px;
}

.register button , .addnewvenue button {
  margin-top: 20px;
  width: 210px;
  height: 36px;
  margin-left: auto;
  margin-right: auto;
  display: block;
  border-radius: 3px;
  border: #0d2329 sloid 1px;
  background-color: #42b72a;
  color: #ffffff;
  font-style: bold;
  font-size: 20px;
  
}

.register input::placeholder ,  .addnewvenue input::placeholder {
  color: #0d2329;
  font-style: bold;
}


.middleline{
  align-items: center;
    border-bottom: 1px solid #dadde1;
    display: flex;
    margin: 30px 16px;
    text-align: center;
    color: #dadde1;
    direction: ltr;
    line-height: 1.34;
    background-color: #dadde1;
}
.middleline2{
  align-items: center;
    border-bottom: 1px solid #dadde1;
    display: flex;
    margin: 10px 10px;
    text-align: center;
    color: #dadde1;
    direction: ltr;
    line-height: 1.34;
    background-color: #dadde1;
}
router-link{
  text-decoration: none;
}

.uservenue {
    display: flex;
    flex-wrap: wrap;
    flex: 0 0 calc(90% - 40px);
    margin-left: 20px;
    margin-right: 20px;
    margin-top: 30px;
    margin-bottom: 30px;
    background-color: aliceblue;
    height: auto;
    box-sizing: border-box;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

@media(max-width: 473px){
  .signup , .addnewvenue{
  background-color: #ffffff;
  border-radius: 2%;
  padding: 2%;
  padding-bottom: 2px;
  box-shadow: 0 0 4px rgba(0, 0, 0, 0.2);
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 2px;
  margin-top: 3px;
  width: 90%;

  }
  .register button , .addnewvenue button {
  margin-top: 5px;
  width: 70%;
  height: 36px;
  margin-left: auto;
  margin-right: auto;
  display: block;
  border-radius: 3px;
  border: #0d2329 sloid 1px;
  background-color: #42b72a;
  color: #ffffff;
  font-style: bold;
  font-size: 8px;
  
}
#registrationh1{
  width: 70%;
}
}

</style>
