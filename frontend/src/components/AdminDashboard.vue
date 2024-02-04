<template>
    <div>
        <AdminNavbar></AdminNavbar>
        <div class="container">
            <div class="venue" v-for="venue in venues" :key="venue.id">
                <h4>{{ venue.Venue_Name }}</h4>
                <h6>Place : {{ venue.Place }} </h6>
                <h6> Locaton : {{ venue.Location }} | Capacity : {{ venue.Capacity }}</h6>
                <hr class="middleline2">
                <div class="show" v-for="show in getShowsByVenue(venue.id)" :key="show.id">
                    <p>{{ show.Show_Name }} </p>
                    <router-link :to="'/updateshow/'+show.id" ><button class="showactions">Edit</button></router-link>
                    <button class="showactions" v-on:click="deleteshow(show.id)">Delete</button>
                </div>
                <div class="show">
                    <div class="centered-button">
                        <router-link style="text-decoration: none;" :to="'/addshow/' + venue.id"><button class="circle-button">
                            <span class="plus-sign">+</span>
                        </button></router-link>
                    </div>
                </div>
                <hr class="middleline2">
                <router-link :to="'/updatevenue/' + venue.id"><button>Update</button></router-link>
                <button v-on:click="deletevenue(venue.id)">Delete</button>
            </div>
            <div class="venue">
                <div class="centered-button">
                    <button v-on:click="addVenue" class="circle-button">
                        <span class="plus-sign">+</span>
                    </button>
                </div>
            </div>
            <div>
            </div>
        </div>
    </div>
</template>
  
<script>
import axios from 'axios'
import AdminNavbar from './AdminNavbar.vue'
export default {
    name: 'AdminDashboard',
    data() {
        return {
            venues: [],
            shows: [],
        }
    },
    components: {
        AdminNavbar
    },
    methods: {
        addVenue() {
            this.$router.push({ name: 'AddVenue' })
        },
        async deletevenue(id) {
            let token = localStorage.getItem("Auth-Token");
            let tokenValue = JSON.parse(token || null);
            let authValue = "Bearer " + tokenValue
            const url = `${process.env.VUE_APP_BACKEND_URL}/venue`;
            const data = {
                id: id
            }
            const config = {
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': authValue
                },
                data: data
            }
            if (token) {
                const result = await axios.delete(url, config);
                alert(result.data.message)
                if (result) {
                    this.$router.push({ name: 'Home' })
                }
            }
        },
        async deleteshow(id) {
            let token = localStorage.getItem("Auth-Token");
            let tokenValue = JSON.parse(token || null);
            let authValue = "Bearer " + tokenValue
            const url = `${process.env.VUE_APP_BACKEND_URL}/show`;
            const data = {
                id: id
            }
            const config = {
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': authValue
                },
                data: data
            }
            if (token) {
                const result = await axios.delete(url, config);
                alert(result.data.message)
                if (result) {
                    this.$router.push({ name: 'Home' })
                }
            }
        }
    },

    computed: {
        getShowsByVenue() {
            return (venueId) => {
                return this.shows.filter(show => show.Venue_id == venueId);
            };
        }
    },

    async mounted() {
    try {
        let token = localStorage.getItem("Auth-Token");
        let tokenValue = JSON.parse(token || null);
        let authValue = "Bearer " + tokenValue;
        const url = `${process.env.VUE_APP_BACKEND_URL}/venue`;
        const url2 = `${process.env.VUE_APP_BACKEND_URL}/show`;
        const config = {
            headers: {
                'Content-Type': 'application/json',
                'Authorization': authValue
            }
        }

        if (token) {
            const [venueResponse, showResponse] = await Promise.all([
                axios.get(url, config),
                axios.get(url2, config)
            ]);

            this.venues = venueResponse.data.venues;
            this.shows = showResponse.data.shows;
        }
    } catch (error) {
        console.error("An error occurred while fetching data:", error);
        alert("Something Went Wrong.")
    }
}
,
    
}
</script>
  
<style>
.container {
    display: flex;
    flex-wrap: wrap;
    margin: 10px;
}

.venue {
    flex: 0 0 calc(33.33% - 20px);
    margin: 10px;
    padding: 10px;
    background-color: aliceblue;
    height: auto;
    box-sizing: border-box;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.venue button{
    margin: 10px;
}

.show {
    border: 1px black;
    margin-top: 2px;
    margin-bottom: 2px;
    margin-left: 5px;
    margin-left: 5px;
    padding-top: 1px;
    padding-bottom: 1px;
    height: auto;
    /* background-color: #aae15a; */
    /* background-color: rgb(231, 254, 85); */
    background-color: #aae15a;
    text-align: center;
    border-radius: 5px;

}

h4 {
    color: black;
}

.circle-button {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 50px;
    height: 50px;
    background-color: blue;
    border: none;
    border-radius: 50%;
    color: white;
    font-size: 24px;
    cursor: pointer;

}

.centered-button {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
    padding-top: 3px;
    padding-bottom: 3px;
}

.plus-sign {
    font-size: 24px;
}

.showactions {
    margin-left: 5px;
    margin-right: 5px;
    padding-bottom: 5px;
    margin-bottom: 5px;
}
</style>
  