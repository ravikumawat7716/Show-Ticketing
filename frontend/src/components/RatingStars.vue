<template>
  <div class="rating">
    <span
      v-for="star in totalStars"
      :key="star"
      @click="this.initialRating === 0 && rate(star)"
      :class="[
        'star', 
        { 'filled': star <= currentRating, 'unfilled': star > currentRating && initialRating > 0 }
      ]"
      :style="{ 'pointer-events': clickable ? 'none' : 'auto' }"
    >
    {{ initialRating > 0 ? '★' : (star <= currentRating ? '★' : '☆') }}

    </span>
    <button
      type="submit"
      class="ratingbutton"
      v-on:click="sendrating(booking_id)"
      v-if="initialRating === 0" :disabled="currentRating === 0">
      Rate Now
    </button>
  </div>
</template>


<script>
import axios from 'axios';
export default {
  name: "RatingStars",
  props: {
    initialRating: Number,
    booking_id: Number,
     // Prop to pass the initial rating
  },
  data() {
    return {
      totalStars: 5,
      currentRating: this.initialRating,
      ratingpresent : false
    };
  },
  methods: {
    rate(rating) {
      this.currentRating = rating;
      this.$emit('rating-updated', this.currentRating);
    },
    async sendrating(id) {
      console.log("id & rating  ", id , this.currentRating)
            let token = localStorage.getItem("Auth-Token");
            let tokenValue = JSON.parse(token || null);
            let authValue = "Bearer " + tokenValue
            const url = "http://127.0.0.1:5000/rate";
            const data = {
                "booking_id": id,
                "stars": this.currentRating
            }
            const config = {
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': authValue
                }
            }
            if (token) {
                const result = await axios.post(url, data, config);
                alert(result.data.message)
                if (result) {
                    this.$router.go(0);
                }
            }
        },
        
  },
};
</script>

<style>
.rating {
  font-size: 40px; 
  display: inline;
}

.filled {
  color: gold; 
}

.unfilled{
  color: black;
}

.ratingbutton {
    margin-top: 10px;
    margin-bottom: 10px;
    border-radius: 5px;
    background-color: green;
    justify-self: center;
    margin-left: 15px;
    padding: 2px;
    height: 50%;
}
</style>
