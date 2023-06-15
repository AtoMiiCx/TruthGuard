<template>
  <MenuHeader />
  <div class="container">
    <div class="bg"></div>
    <div class="bg"></div>
    <div class="bg"></div>
    <h1 class="welcome">Welcome to TruthGuard</h1>
    <p class="text t">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus malesuada eros in tellus elementum,
      non volutpat dolor porttitor. Ut ornare velit sed diam facilisis, a suscipit mi malesuada. Praesent accumsan nunc
      sed dapibus blandit. Aenean vitae augue cursus, vehicula purus ac, dignissim libero. Fusce vel rhoncus nisi, id
      elementum lacus. Maecenas semper urna id ex tempor, id condimentum ex commodo. Nulla posuere finibus metus. Mauris
      rutrum elit nec rhoncus suscipit. Donec eget magna enim. Nam feugiat dui at purus malesuada condimentum. Aenean
      faucibus commodo consectetur. Nullam sed efficitur leo, at venenatis libero.

      Sed erat velit, sodales quis placerat at, dignissim at urna. Phasellus tincidunt sapien aliquam, luctus tellus vel,
      tristique odio. Donec scelerisque pharetra lectus, quis cursus purus fermentum ac. In fermentum imperdiet justo at
      ornare. Nam malesuada risus urna. Sed malesuada condimentum eros, non volutpat lorem faucibus at. Sed vitae magna id
      est rhoncus vestibulum eu sit amet risus. Pellentesque libero velit, placerat a arcu sit amet, scelerisque faucibus
      turpis. Sed consectetur porttitor finibus. Aliquam vehicula, metus sit amet pellentesque tincidunt, risus mi gravida
      velit, quis egestas elit mauris eget nisi. Fusce dictum et felis eu porttitor. Donec vitae ligula sit amet mauris
      fringilla consectetur. Donec nunc tortor, vehicula et ante in, suscipit imperdiet ante. Aliquam ut fringilla nisi.
      Nam varius ullamcorper urna vel ullamcorper.
    </p>

    <p class="text t1">Aliquam volutpat, lacus tempor condimentum feugiat, purus ipsum fringilla ipsum, sit amet
      consectetur ante purus sit
      amet mauris. Cras erat ante, hendrerit imperdiet malesuada nec, auctor vitae eros. Curabitur ex erat, convallis sed
      bibendum eget, faucibus et nisi. Nunc aliquet viverra dolor, non hendrerit mi vulputate quis. Pellentesque feugiat
      libero sit amet magna blandit, quis sagittis urna mollis. Phasellus porttitor mauris vitae risus laoreet, vitae
      tincidunt ipsum elementum. Maecenas volutpat tortor non enim maximus elementum. Cras dictum ullamcorper velit
      scelerisque porta.

      In vel orci ac nulla suscipit molestie. Donec volutpat lorem nunc. Vivamus orci mauris, varius ut elit vehicula,
      placerat vestibulum nisl. Vivamus eget finibus nunc. Nulla tincidunt lectus velit, a porttitor mi faucibus ac. Cras
      nisi neque, tempus nec mauris sed, rhoncus aliquam dolor. Donec at dolor interdum, varius nunc et, luctus ante.
      Vivamus vitae eros auctor, vehicula nisl quis, condimentum justo. Pellentesque in ligula vitae erat cursus tempor
      non vel ante. Curabitur pharetra, dui nec accumsan malesuada, metus ante imperdiet nulla, at viverra nibh erat eu
      purus. Donec dictum vehicula facilisis. Ut eu blandit enim. Nam ac massa sit amet eros dictum feugiat.

    </p>
    <p class="text t2">Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Mauris
      leo magna,
      pellentesque vel lacinia pharetra, elementum ac velit. Morbi viverra malesuada urna, in sodales magna. Fusce
      gravida, ligula eu vulputate ultrices, diam ipsum fringilla ex, pellentesque dignissim turpis ligula quis justo. Nam
      luctus nulla id condimentum commodo. Praesent fringilla, turpis at tincidunt scelerisque, magna sapien lobortis
      purus, at mollis lacus tellus sed justo. Pellentesque habitant morbi tristique senectus et netus et malesuada fames
      ac turpis egestas. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Ut
      semper, nisl vel congue fermentum, sapien libero vulputate ipsum, et suscipit urna ipsum non eros. Praesent nec
      pharetra dui, at dictum mauris. Etiam maximus urna ut velit fringilla convallis. Sed a justo et ipsum ornare sodales
      sit amet ac ligula.
    </p>
  </div>
  <testButton />
  <div class="footer">
    <p>footer</p>
  </div>
</template>

<script>

import MenuHeader from '@/components/MenuHeader.vue'
import testButton from '@/components/testButton.vue'

export default {
  name: 'HomeView',
  components: {
    MenuHeader, testButton
  }
}
</script>

<style>
@font-face {
  font-family: DidactGothic-Regular;
  src: url('../assets/DidactGothic-Regular.ttf');
}

body {
  background: #a7c6da;
}

body,
html {
  height: 100%;
  margin: 0;
}

.container {
  height: 100%;
}

.home {
  display: flex;
  flex-direction: column;
  align-items: center;
  flex-direction: column;
  justify-content: center;
}

.welcome {
  font-size: 50px;
  color: white;
  margin-top: 20px;
  margin-bottom: 60px;
  text-align: center;
  text-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

.text {
  font-size: 20px;
  color: white;
  margin-top: 20px;
  margin-left: 20%;
  margin-right: 20%;
  margin-bottom: 60px;
  text-align: center;
  text-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

.t {
  background: #e1b07e;
  /* extend the margin of the block to the beginning of the next one */
  margin-bottom: -20px;
}

.t1 {
  background: #230903;
  /* extend the margin of the block to the beginning of the next one */
  margin-bottom: -20px;

}

.t2 {
  background: #7c7287;
  margin-bottom: 130px;
}

.footer {
  background: #7c7287;
  padding: 100px;
  margin-top: 150px;
}
</style>