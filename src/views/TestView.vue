<template>
    <MenuHeader />
    <input v-model="url" id="testinput" type="text" placeholder="Enter a valid url to test ...">
    <button id="testbtn" @click="verifyArticle">Check it !</button>
    <div class="result-box">
      <h2>Prediction</h2>
      <p>{{ prediction }}</p>
    </div>
    <div class="result-box">
      <h2>Detected Language</h2>
      <p>{{ language }}</p>
    </div>
    <div class="result-box">
      <h2>Website Status</h2>
      <p>{{ site }} : {{ status }}</p>
    </div>
    
</template>

<script>

import MenuHeader from '@/components/MenuHeader.vue'
import axios from 'axios'

export default {
    name: 'TestView',
    components: {
        MenuHeader
    },
    data() {
        return {
            url: '',
            prediction: '',
            language: '',
            site: '',
            status: ''
        };
    },
    methods: {
        verifyArticle() {
            axios.post('http://localhost:5000/verify', {
                url: this.url, // Pass the input URL to the API
            })
        .then(response => {
            console.log(response);
            const data = response.data;
            this.prediction = data[0]['Prediction'];
            this.language = data[0]['Language'];
            this.site = data[0]['Site'];
            this.status = data[0]['Status'];
            
        })
        .catch(error => {
            console.error('Error:', error);
            // Handle errors, if any
        });
        }
    }
}
</script>

<style>
@font-face {
    font-family: DidactGothic-Regular;
    src: url('../assets/DidactGothic-Regular.ttf');
}

#testinput {
    width: 500px;
    height: 50px;
    font-size: 20px;
    box-sizing: border-box;
    background-image: url('../assets/loupe.png');
    background-position: 3% 50%;
    margin-right: 40px;
    margin-left: 50px;
    margin-top: 50px;
    
    filter: drop-shadow(6px 2px 24px rgba(0, 0, 0, 0.13));
    background-size: 15px;
    background-repeat: no-repeat;
    padding-left: 35px;
    border-radius: 20px;
}

.result-box {
    border: 1px solid #ccc;
    background-color: #ae4b55;
    padding: 10px;
    margin-bottom: 10px;
}

.result-box h2 {
    font-size: 18px;
    margin-bottom: 5px;
}

</style>