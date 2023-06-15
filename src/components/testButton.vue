<template>
  <router-link class="testbtn" role="button" to="/test" >Test TruthGuard</router-link>
</template>

<script>
export default {
    name: 'testButton'
}
</script>

<style>
.testbtn{  
  padding: 1rem 3.2rem;
  text-align: center;
  font-size: 16px;
  text-transform: uppercase;
  border-radius: 4px;
  color: rgb(255, 255, 255);
  text-decoration: none;
  background: linear-gradient(to right, #a7c6da 50%, #7c7287 50%);
  background-size: 200% 100%;
  background-position: right bottom;
  transition: all .5s ease-out;
  box-shadow: 9px 9px 16px rgb(110, 110, 110),
              -9px -9px 16px rgb(110, 110, 110);
}

.testbtn:hover{
  font-weight: bold;
  background-position: left bottom;
  box-shadow: none;
}

.text {
  text-align: center;
  font-size: 16px;
  line-height: 30px; 
  color: black;
  transition: all .6s ease-out;
  display: block;
}

.text:hover {
  color: white;  
}
</style>