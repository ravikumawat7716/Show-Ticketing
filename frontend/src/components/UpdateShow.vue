<template>
    <AdminNavbar></AdminNavbar>
    <div class="addvenue">
        <h2 style="color: black;">Edit Show</h2>
        <div class="addnewvenue">
            <form @submit.prevent="updateVenue">
                <input v-model="show.Show_Name" type="text" required="True" placeholder="Show Name" />
                <input v-model="show.Rating" type="text" required="True" placeholder="Rating" />
                <input v-model="show.Timing" type="text" required="True" placeholder="Timing" />
                <input v-model="show.Tags" type="text" required="True" placeholder="Tags" />
                <input v-model="show.Price" type="number" required="True" placeholder="Price" />
                <button type="submit">Update</button>
            </form>
        </div>
    </div>
</template>

<script>
import AdminNavbar from './AdminNavbar.vue'
import axios from 'axios';
export default {
    name: 'UpdateShow',
    data (){
        return{
            show : {
            Show_Name:'',
            Rating: '',
            Timing: '',
            Tags: '',
            Price: ''
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
                const url = 'http://127.0.0.1:5000/show';
                const data = {
                    id: id,
                    Show_Name: this.show.Show_Name,
                    Rating: this.show.Rating,
                    Timing: this.show.Timing,
                    Tags: this.show.Tags,
                    Price: this.show.Price
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
        const url = "http://127.0.0.1:5000/show";
        const config = {
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization' : authValue
                    }
                }
        if (token) {
            const result = await axios.get(url,config);
            const id = parseInt(this.$route.params.id)
            const show = result.data.shows.find(show => show.id === id);
            this.show.Show_Name = show.Show_Name;
            this.show.Rating = show.Rating;
            this.show.Timing = show.Timing;
            this.show.Tags = show.Tags;
            this.show.Price = show.Price;
            
        }
    },
}
</script>