<template>
    <AdminNavbar></AdminNavbar>
    <div class="addshow">
        <h2 style="color: black;">Add a new Show</h2>
        <div class="addnewshow">
            <form @submit.prevent="registerShow">
                <input v-model="show.Show_Name" type="text" required="True" placeholder="Show Name" />
                <select v-model="show.Rating" id="rating" required class="select2">
                    <option value="" disabled selected>Select Rating</option>
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                    <option value="5">5</option>
                </select>
                <h6 id="timingh6">Start Timing : </h6>
                <div class="timing-input-div">
                    <input id="timinginput" v-model="show.Start_Timing" type="time" required="true"
                        placeholder="Start Timing" />
                    <select v-model="show.Start_AMPM" id="#select1">
                        <option value="AM">AM</option>
                        <option value="PM">PM</option>
                    </select>
                </div>
                <h6 id="timingh6">End Timing : </h6>
                <div class="timing-input-div">
                    <input id="timinginput" v-model="show.End_Timing" type="time" required="true"
                        placeholder="End Timing" />
                    <select v-model="show.End_AMPM" id="#select1">
                        <option value="AM">AM</option>
                        <option value="PM">PM</option>
                    </select>
                </div>
                <input v-model="show.Tags" type="text" required="True" placeholder="Tags" />
                <input v-model="show.Price" type="number" required="True" placeholder="Price" />
                <button type="submit">Submit</button>
            </form>
        </div>
    </div>
</template>

<script>
import AdminNavbar from './AdminNavbar.vue'
import axios from 'axios';
export default {
    name: 'AddShow',
    data() {
        return {
            show: {
                Show_Name: '',
                Rating: '',
                Start_Timing: '',
                End_Timing: '',
                Tags: '',
                Price: ''
            }
        }
    },
    components: {
        AdminNavbar,
    },
    methods: {
        async registerShow() {
            console.log(this.show.Start_Timing)
            try {
                let token = localStorage.getItem("Auth-Token");
                let tokenValue = JSON.parse(token || null);
                let authValue = "Bearer " + tokenValue
                const id = parseInt(this.$route.params.id)
                const url = `${process.env.VUE_APP_BACKEND_URL}/show`;
                const data = {
                    Show_Name: this.show.Show_Name,
                    Rating: this.show.Rating,
                    Timing: `${this.show.Start_Timing} ${this.show.Start_AMPM} - ${this.show.End_Timing} ${this.show.End_AMPM}`,
                    Tags: this.show.Tags,
                    Price: this.show.Price,
                    Venue_id: id
                }
                const config = {
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': authValue
                    }
                }
                console.log(data)
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

<style>
.timing-input-div {
    margin-top: 10px;
    margin-bottom: 10px;
    width: 200px;
    height: 30px;
    margin-left: auto;
    margin-right: auto;
    display: flex;
    flex-wrap: wrap;

}

#select1 {
    margin-top: 10px;
    border-radius: 3px;
    border: #0d2329 sloid 1px;
    width: 30%;
    height: 30px;
    display: flex;
}

#timinginput {
    margin-top: 0px;
    width: 70%;
    height: 30px;
    float: left;
    margin-left: 0px;
    margin-right: auto;
    display: flex;
    border-radius: 3px;
    border: #0d2329 sloid 1px;
}

#timingh6 {
    margin-top: 6px;
    margin-bottom: 0px;
}


h1 {
    text-align: center;
    color: #fff;
}

#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 0px;
    flex: 1;
}

.routerLink {
    text-decoration: none;
}

.signup,
.addvenue,
.addshow {
    background-color: #ffffff;
    border-radius: 10px;
    padding: 20px;
    padding-bottom: 30px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
    margin-left: auto;
    margin-right: auto;
    margin-bottom: 40px;
    margin-top: 30px;
    width: 400px;
}

.register input,
.addnewvenue input,
.addnewshow input {
    margin-top: 20px;
    width: 200px;
    height: 30px;
    margin-left: auto;
    margin-right: auto;
    display: block;
    border-radius: 3px;
    border: #0d2329 sloid 1px;
}

.select2{
    margin-top: 20px;
    width: 200px;
    height: 30px;
    margin-left: auto;
    margin-right: auto;
    display: block;
    border-radius: 3px;
    border: #0d2329 sloid 1px;
}




.register button,
.addnewvenue button,
.addnewshow button {
    margin-top: 20px;
    width: 210px;
    height: 36px;
    margin-left: auto;
    margin-right: auto;
    display: block;
    border-radius: 3px;
    border: #0d2329 sloid 1px;
    background-color: #42b72a;
    color: #ffffff;
    font-style: bold;
    font-size: 20px;

}

.register input::placeholder,
.addnewvenue input::placeholder,
.addnewshow input::placeholder {
    color: #0d2329;
    font-style: bold;
}


.middleline {
    align-items: center;
    border-bottom: 1px solid #dadde1;
    display: flex;
    margin: 30px 16px;
    text-align: center;
    color: #dadde1;
    direction: ltr;
    line-height: 1.34;
    background-color: #dadde1;
}

.middleline2 {
    align-items: center;
    border-bottom: 1px solid #dadde1;
    display: flex;
    margin: 10px 10px;
    text-align: center;
    color: #dadde1;
    direction: ltr;
    line-height: 1.34;
    background-color: #dadde1;
}

router-link {
    text-decoration: none;
}

.uservenue {
    display: flex;
    flex-wrap: wrap;
    flex: 0 0 calc(90% - 40px);
    margin-left: 20px;
    margin-right: 20px;
    margin-top: 30px;
    margin-bottom: 30px;
    background-color: #0d2329;
    height: auto;
    box-sizing: border-box;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

@media(max-width: 473px) {

    .signup,
    .addnewvenue {
        background-color: #ffffff;
        border-radius: 2%;
        padding: 2%;
        padding-bottom: 2px;
        box-shadow: 0 0 4px rgba(0, 0, 0, 0.2);
        margin-left: auto;
        margin-right: auto;
        margin-bottom: 2px;
        margin-top: 3px;
        width: 90%;

    }

    .register button,
    .addnewvenue button {
        margin-top: 5px;
        width: 70%;
        height: 36px;
        margin-left: auto;
        margin-right: auto;
        display: block;
        border-radius: 3px;
        border: #0d2329 sloid 1px;
        background-color: #42b72a;
        color: #ffffff;
        font-style: bold;
        font-size: 8px;

    }

    #registrationh1 {
        width: 70%;
    }
}</style>