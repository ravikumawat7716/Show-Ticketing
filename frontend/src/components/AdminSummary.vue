<template>
    <div>
      <SummaryNavbar></SummaryNavbar>
      <br>
      <button @click="sendDailyReportRequest">Daily Report</button>
      <br>
      <button @click="sendMonthlyReportRequest">Monthly Report</button>
    </div>
  </template>
  
  <script>
  import SummaryNavbar from './SummaryNavbar.vue'
  import axios from 'axios'
  
  export default {
    name: 'AdminSummary',
    components: {
      SummaryNavbar,
    },
    methods: {
      async sendDailyReportRequest() {
        try {
          // Get the Bearer token from localStorage
          const token = localStorage.getItem("Auth-Token");
          if (!token) {
            alert('Authentication token not found.');
            return;
          }
  
          // Set up the Axios configuration
          const tokenValue = JSON.parse(token || null);
          const authValue = "Bearer " + tokenValue;
          const url = "http://127.0.0.1:5000/dailyreport"; 
          const config = {
            headers: {
              'Content-Type': 'application/json',
              'Authorization': authValue
            }
          };
  
          // Send the GET request with authentication headers
          const response = await axios.get(url, config);
          alert(response.data.message);
        } catch (error) {
          alert('Failed to send Daily Report request.');
          console.log(error);
        }
      },
      async sendMonthlyReportRequest() {
        try {
          // Get the Bearer token from localStorage
          const token = localStorage.getItem("Auth-Token");
          if (!token) {
            alert('Authentication token not found.');
            return;
          }
  
          // Set up the Axios configuration
          const tokenValue = JSON.parse(token || null);
          const authValue = "Bearer " + tokenValue;
          const url = "http://127.0.0.1:5000/monthlyreport"; 
          const config = {
            headers: {
              'Content-Type': 'application/json',
              'Authorization': authValue
            }
          };
  
          // Send the GET request with authentication headers
          const response = await axios.get(url, config);
          
          alert(response.data.message);
        } catch (error) {
          alert('Failed to send Monthly Report request.');
          console.log(error);
        }
      },
    },
  }
  </script>
  