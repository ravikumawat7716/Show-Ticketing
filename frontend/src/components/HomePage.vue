<template>
    <UserNavbar></UserNavbar>
    <h3>Hello {{ name }}!, Welcome Show Ticket Booking App</h3>
    <select class="searchoption" v-model="searchOption">
    <option value="showName">Show Name</option>
    <option value="venueName">Venue Name</option>
    <option value="location">Location</option>
    <option value="city">City</option>
  </select>
    <input class="showsearch" type="text" v-model="search" placeholder="Search Shows">
    <div class="uservenue" v-for="venue in filteredVenues" :key="venue.id">
      <div class="venuetitle">
        <h4>{{ venue.Venue_Name }}</h4>
        <h5>Place: {{ venue.Place }} | City: {{ venue.Location }} | Seating Capacity: {{ venue.Capacity }}</h5>
      </div>
      <div class="usershow" v-for="show in getShowsByVenue(venue.id)" :key="show.id">
        <h3 style="color: black;">{{ show.Show_Name }}</h3>
        <h5>Rating: {{ show.Rating }} | Tags: {{ show.Tags }}</h5>
        <h5>Show Timing: {{ show.Timing }}</h5>
        <h6>Available Seats: {{ show.Available_Seats }}</h6>
        <router-link :to="'/book/' + show.id + '/' + venue.id">
          <button :disabled="show.Available_Seats <= 0"
                  :style="{ backgroundColor: show.Available_Seats <= 0 ? 'red' : '', color: show.Available_Seats <= 0 ? 'white' : '' }">
            {{ show.Available_Seats <= 0 ? 'Houseful' : 'Book' }}
          </button>
        </router-link>
      </div>
      <h4 style="text-align: center; margin-left: 45%;" v-if="getShowsByVenue(venue.id).length === 0">No Shows Here</h4>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  import UserNavbar from './UserNavbar.vue'
  export default {
    name: 'HomePage',
    components: {
      UserNavbar,
    },
    data() {
      return {
        name: '',
        venues: [],
        shows: [],
        search: '',
        searchOption: 'showName', 
      }
    },
    methods: {
      logout() {
        localStorage.clear()
        alert('You are logged out.')
        this.$router.push({ name: 'UserLogin' })
      }
    },
    computed: {
      getShowsByVenue() {
        return (venueId) => {
          return this.searchedshows.filter(show => show.Venue_id == venueId);
        };
      },
      searchedshows() {
        if (this.searchOption === 'showName') {
        return this.shows.filter(show => {
          const lowerCaseSearch = this.search.toLowerCase();
          const lowerCaseShowName = show.Show_Name.toLowerCase();
          return lowerCaseShowName.includes(lowerCaseSearch);
        });} else {
            return this.shows
        }
      },
      filteredVenues() {
      if (this.search.trim() === '') {
        return this.venues;
      } else {
        if (this.searchOption !== 'showName') {
          return this.venues.filter(venue => {
            switch (this.searchOption) {
              case 'venueName':
                return venue.Venue_Name.toLowerCase().includes(this.search.toLowerCase());
              case 'location':
                return venue.Place.toLowerCase().includes(this.search.toLowerCase());
              case 'city':
                return venue.Location.toLowerCase().includes(this.search.toLowerCase());
              default:
                return false; 
            }
          });
        } else {
            return this.venues.filter(venue => {
          return this.searchedshows.some(show => show.Venue_id == venue.id);
        });
        }
      }
    },
    },
    async mounted() {
      let token = localStorage.getItem("Auth-Token");
      let username = localStorage.getItem("name");
      this.name = JSON.parse(username || {});
      let userRole = localStorage.getItem("user-role")
      let Role = JSON.parse(userRole || {});
      if (token) {
        if (Role == "ADMIN") {
          this.$router.push({ name: 'AdminDashboard' })
        } else {
          let tokenValue = JSON.parse(token || null);
          let authValue = "Bearer " + tokenValue
          const url = `${process.env.VUE_APP_BACKEND_URL}/venue`;
          const url2 = `${process.env.VUE_APP_BACKEND_URL}/show`;
          const config = {
            headers: {
              'Content-Type': 'application/json',
              'Authorization': authValue
            }
          }
          try {
            const [venueResponse, showResponse] = await Promise.all([
              axios.get(url, config),
              axios.get(url2, config)
            ]);
  
            this.venues = venueResponse.data.venues;
            this.shows = showResponse.data.shows;
          } catch (error) {
            console.error("An error occurred while fetching data:", error);
            alert("Something Went Wrong.")
          }
        }
      } else {
        this.$router.push({ name: 'UserLogin' })
      }
    }
  }
  </script>
  
  <style>
  h3 {
    color: aliceblue;
  }
  
  .uservenue {
    display: flex;
    flex-wrap: wrap;
    flex: 0 0 calc(90% - 40px);
    margin-left: 20px;
    margin-right: 20px;
    margin-top: 30px;
    margin-bottom: 30px;
    /* background-color: aliceblue; */
    background-color:#0d2329;
    height: auto;
    box-sizing: border-box;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  .usershow {
    flex: 0 0 calc(33.33% - 20px);
    margin: 10px;
    padding: 10px;
    background-color: aliceblue;
    /* background-color: rgb(231, 254, 85); */
    height: auto;
    box-sizing: border-box;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  .venuetitle {
    /* background-color: #4de873; */
    /* background-color: rgb(231, 254, 85);
    background-color: blue; */
    /* background-color: #aae15a; */
    background-color: aliceblue;
    width: 100%;
    margin: 0px;
    text-align: center;
    border-radius: 4px;
  }
  
  .showsearch {
    width: 60%;
    height: 30px;
    border-radius: 15px;
  }
  .searchoption {
    height: 30px;
    border-radius: 15px;
    margin-right: 2px;
    padding-left: 2px;
    padding-right: 2px;
  }
  </style>
  