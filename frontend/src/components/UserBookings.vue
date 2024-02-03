<template>
    <UserNavbar2></UserNavbar2>
    <div class="userbookings" style="background-color: red; text-align: center;" v-if="nobookings">
        <h1 style="color: white;">No Bookings Yet.</h1>
    </div>
    <div class="userbookings" v-for="booking in bookings" :key="booking.venuename">
        <h2>Venue : {{ booking.venuename }} | Show : {{ booking.showname }} | Timing : {{ booking.timing }}
</h2>
        <div class="ratingdiv">
            <RatingStars :initialRating="booking.rating" :booking_id="booking.id" :readonly="booking.rating > 0"
                @rating-updated="updateRating(booking.id, $event)"></RatingStars>
        </div>
        <p style="font-size: 15px;" v-if="booking.rating > 0">Thanks for the rating.</p>
    </div>
</template>

<script>
import axios from 'axios'
import UserNavbar2 from './UserNavbar2.vue';
import RatingStars from "./RatingStars.vue";
export default {
    name: 'UserBookings',
    data() {
        return {
            nobookings: false,
            bookings: [],
            selectedRatings: []
        }
    },
    components: {
        UserNavbar2,
        RatingStars
    },
    methods: {
        async updateRating(id, rating) {
            this.booking_id = id,
            this.stars = rating
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
            }
            else {
                let tokenValue = JSON.parse(token || null);
                let authValue = "Bearer " + tokenValue
                const url = `${this.$globalData.backendUrl}/book`;
                const config = {
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': authValue
                    }
                }
                const result = await axios.get(url, config);
                console.log(result)
                if (result.status == 200) {
                    if (result.data.message == 'ok') {
                        this.bookings = result.data.bookings
                    }
                    else {
                        this.nobookings = true
                    }

                }
            }
        }
        else {
            this.$router.push({ name: 'UserLogin' })
        }

    }

}
</script>
<style>
.userbookings {
    display: flex;
    flex-wrap: wrap;
    flex: 0 0 calc(90% - 40px);
    margin-left: 6px;
    margin-right: 6px;
    margin-top: 30px;
    margin-bottom: 30px;
    background-color: aliceblue;
    height: auto;
    box-sizing: border-box;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    padding: 10px;
}

.ratingdiv {
    margin-top: 3px;
    margin-left: 2px;
    float: left;
    margin-right: 10px;
    flex: 0 0 calc(33.33% - 20px);
    justify-content: center;
}

.ratingbutton {
    margin-top: 10px;
    margin-bottom: 10px;
    border-radius: 5px;
    background-color: green;
}
</style>

