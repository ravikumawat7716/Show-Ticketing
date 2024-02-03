<template>
    <AdminNavbar></AdminNavbar>
    <div class="addvenue">
        <h2 style="color: black;">Add a new Venue</h2>
        <div class="addnewvenue">
            <form @submit.prevent="registerVenue">
                <input v-model="venue.venueName" type="text" placeholder="Venue Name" />
                <input v-model="venue.place" type="text" placeholder="Place" />
                <input v-model="venue.location" type="text" placeholder="Location" />
                <input v-model="venue.capacity" type="number" placeholder="Capacity" />
                <button type="submit">Submit</button>
            </form>
        </div>
    </div>
</template>

<script>
import AdminNavbar from './AdminNavbar.vue'
import axios from 'axios';
export default {
    name: 'AddVenue',
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
        async registerVenue() {
            try {
                let token = localStorage.getItem("Auth-Token");
                let tokenValue = JSON.parse(token || null);
                let authValue = "Bearer "+tokenValue
                const url = `${this.$globalData.backendUrl}/venue`;
                const data = {
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
                const response = await axios.post(url, data, config);
                if (response.status == 201) {
                    alert(response.data.message)
                    console.log(response)
                    this.$router.push({ name: 'UserLogin' })
                }

            } catch (error) {
                alert('something went wrong')
            }
        }
    }
}
</script>