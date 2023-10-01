<template>
    <div>
      <h1>404 Not Found</h1>
      <p>The page you're looking for doesn't exist.</p>
      <p>You'll be redirected to the home page in {{ countdown }} seconds...</p>
    </div>
  </template>
  
  <script>
  export default {
    name: 'NotFoundComponent',
    data() {
      return {
        countdown: 3,
      };
    },
    mounted() {
      this.startCountdown();
    },
    methods: {
      startCountdown() {
        this.timer = setInterval(() => {
          if (this.countdown > 0) {
            this.countdown = this.countdown-1;
          } else {
            clearInterval(this.timer);
            this.$router.push('/');
          }
        }, 1000);
      },
    },
    beforeUnmount() {
      clearInterval(this.timer);
    },
  };
  </script>
  