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
    background-blend-mode: darken;
    position: sticky;
    top: 0;
    align-items: center;
    justify-content: space-between;
    height: 100px;
    padding: 10px 48px 0 0;
    width: 100%;
}

#logo {
    height: 70px;
    transition: all .2s ease-out;
    background-color: #a7c6da;
    padding: 10px 10px 10px 15px;
    border-radius: 20px;
    margin-left: 30px;
}

#logo:hover {
    transform: scale(1.2);
}

.navigation {
    color: #7c7287;
    font-size: 20px;
    margin: 10px;
    text-decoration: none;
    text-align: left;
    transition: all .2s ease-out;
    background-color: #a7c6da;
    padding: 10px;
    border-radius: 10px;

}

.navigation:hover {
    color: white;
    font-weight: bold;
    font-size: 30px;
}
</style>
