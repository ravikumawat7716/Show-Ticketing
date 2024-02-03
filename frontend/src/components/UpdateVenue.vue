<template>
    <AdminNavbar></AdminNavbar>
    <div class="addvenue">
        <h2 style="color: black;">Edit Venue</h2>
        <div class="addnewvenue">
            <form @submit.prevent="updateVenue">
                <input  v-model="venue.venueName" type="text" placeholder="Venue Name" />
                <input  v-model="venue.place" type="text" placeholder="Place" />
                <input  v-model="venue.location" type="text" placeholder="Location" />
                <input  v-model="venue.capacity" type="number" placeholder="Capacity" />
                <button type="submit">Update</button>
            </form>
        </div>
    </div>
</template>

<script>
import AdminNavbar from './AdminNavbar.vue'
import axios from 'axios';
export default {
    name: 'UpdateVenue',
    data (){
        return{
        venue : {
            venueName:'',
            place: '',
            location: '',
            capacity: ''
        }
    }
    },
    components: {
        AdminNavbar,
    },
    methods: {
        async updateVenue() {
            try {
                let token = localStorage.getItem("Auth-Token");
                let tokenValue = JSON.parse(token || null);
                let authValue = "Bearer "+tokenValue
                const id = parseInt(this.$route.params.id)
                const url = `${this.$globalData.backendUrl}/venue`;
                const data = {
                    id : id,
                    Venue_Name: this.venue.venueName,
                    Place: this.venue.place,
                    Location: this.venue.location,
                    Capacity: this.venue.capacity
                }
                const config = {
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization' : authValue
                    }
                }
                console.log(data)
                const response = await axios.put(url, data, config);
                if (response.status == 200) {
                    alert(response.data.message)
                    console.log(response)
                    this.$router.push({ name: 'AdminDashboard' })
                }

            } catch (error) {
                alert('something went wrong')
            }
        }
    },
    async mounted() {
        let token = localStorage.getItem("Auth-Token");
        let tokenValue = JSON.parse(token || null);
        let authValue = "Bearer "+tokenValue
        const url = `${this.$globalData.backendUrl}/venue`;
        const config = {
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization' : authValue
                    }
                }
        if (token) {
            const result = await axios.get(url,config);
            const id = parseInt(this.$route.params.id)
            const venue = result.data.venues.find(venue => venue.id === id);
            this.venue.venueName = venue.Venue_Name;
            this.venue.place = venue.Place;
            this.venue.location = venue.Location;
            this.venue.capacity = venue.Capacity;
            console.log(result)
            
        }
    },
}
</script>