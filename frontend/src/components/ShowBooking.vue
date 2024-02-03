<template>
    <UserNavbar></UserNavbar>
    <div class="titlebar2">
        <div style="float: left;">Booking {{ showname }} at {{ venuename }}</div>
        <div style="float: right;">Show Timing: {{ timing }}</div>
    </div>
    <div class="seats">Total Available Seats : {{ seats }}</div>
        
    <div class="signup">
        <h2 style="color: black;">Book Your Show</h2>
        <div class="register">
            <form @submit.prevent="bookTickets">
                <input v-model="booking.number" type="number" required="True" :min="1" :max="seats" step="1" placeholder="Number of Tickets" v-onblur="calculateTotal()" />
                <input v-model="booking.price" type="number" required="True" placeholder="Price" readonly />
                <input v-model="booking.total" type="number" required="True" placeholder="Total" readonly/>
                <button type="submit">Confirm Booking</button>
            </form>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import UserNavbar from './UserNavbar.vue';
export default {
    name: 'ShowBooking',
    components: {
        UserNavbar,
    },
    data() {
        return {
            showname: '',
            venuename: '',
            seats:'',
            name : '',
            timing:'',
            booking : {
                number : '',
                price: '',
                total: '',
            }
        }
    },
    methods: {
        calculateTotal(){
            this.booking.total = this.booking.number * this.booking.price
        },
        async bookTickets(){
            let token = localStorage.getItem("Auth-Token");
            const id = parseInt(this.$route.params.sid)
                let tokenValue = JSON.parse(token || null);
                let authValue = "Bearer " + tokenValue
                const url = `${this.$globalData.backendUrl}/book`;
                const config = {
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': authValue
                    }
                }
                const data ={
                    show_id : id,
                    tickets : this.booking.number
                }
                const result = await axios.post(url,data,config);
                console.log(result)
                if (result.status == 200){
                    alert(result.data.message)
                    this.$router.push('/');

                }
        }
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
            }
            else {
                const id = parseInt(this.$route.params.sid)
                let tokenValue = JSON.parse(token || null);
                let authValue = "Bearer " + tokenValue
                const url = `${this.$globalData.backendUrl}/fetch_showdata?id=${id}`;
                const config = {
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': authValue
                    }
                }
                const result = await axios.get(url,config);
                this.showname = result.data.showname
                this.venuename = result.data.venuename
                this.seats = result.data.seats
                this.booking.price = result.data.price
                this.timing = result.data.timing
                
            }
        }
        else {
            this.$router.push({ name: 'UserLogin' })
        }
    }
}
</script>
<style>
.titlebar2 {
    color: black;
    font-size: 20px;
    padding: 20px;
}
.seats{
    width: 30%;
    margin-left: auto;
    margin-right: auto;
    margin-top: 20px;
    margin-bottom: 20px;
    background-color: red;
    color: aliceblue;
    height:25px;
    border-radius: 5px;
    border-color: aliceblue;
    border: 1px;
    padding: 5px;
}
</style>