<template>
    <MenuHeader />
    <input v-model="text" class="testinput" type="text" placeholder="Enter a valid url to test ...">
</template>

<script>

import MenuHeader from '@/components/MenuHeader.vue'

export default {
    name: 'TestView',
    components: {
        MenuHeader
    },
    data() {
        return {
            text: ''
        }
    }
}
</script>

<style>
@font-face {
    font-family: DidactGothic-Regular;
    src: url('../assets/DidactGothic-Regular.ttf');
}

.testinput {
    width: 500px;
    height: 50px;
    font-size: 20px;
    box-sizing: border-box;
    background-image: url('../assets/loupe.png');
    background-position: 3% 50%;
    margin-right: 40px;
    margin-left: 50px;
    filter: drop-shadow(6px 2px 24px rgba(0, 0, 0, 0.13));
    background-size: 15px;
    background-repeat: no-repeat;
    padding-left: 35px;
    border-radius: 20px;
}
</style>