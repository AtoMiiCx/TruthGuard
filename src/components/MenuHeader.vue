<template>
    <nav class="navbar">
        <a href="/"><img src="@/assets/truthguard.png" alt="truthguard logo" id="logo"></a>
        <div>
            <router-link class="navigation" to="/about">About us</router-link>
            <router-link class="navigation" to="/">Login</router-link>
        </div>
    </nav>
</template>

<script>
export default { name: 'MenuHeader' }
</script>

<style scoped>
.navbar{
    display: flex;
    /*make this header sticky while scrolling down the page*/
    position: sticky;
    top: 0;
    margin-bottom: 20px;
    align-items: center;
    justify-content: space-between;
}

#logo {
height: 145px;
}

.navigation {
    color: #7c7287;
    margin: 10px;
    text-decoration: none;
    text-align: left;
    transition: all .2s ease-out;
}

.navigation:hover {
    color: white;
    font-weight: bold;
}
</style>
