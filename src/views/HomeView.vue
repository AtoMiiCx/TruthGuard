<template>
  <MenuHeader />
  <div class="container">
    <h1 class="welcome">Welcome to TruthGuard</h1>
    <div class="div1">
      <p class="text t">The proliferation of fake news, particularly in the realm of politics, has reached alarming proportions,
      threatening the very fabric of democratic societies. Recent studies have revealed that misinformation campaigns have 
      influenced major elections, shaping public opinion and sowing discord among citizens. For instance, during the 2016 
      United States presidential election, it was estimated that false stories reached over 150 million Americans on social media, 
      exacerbating existing political divisions and distorting the truth. Such manipulative tactics undermine the fundamental 
      principles of transparency, accountability, and informed decision-making that are vital to the functioning of a democratic society.
      </p>
    </div>
    <h1 class="welcome">How can I protect myself from fake news?</h1>
    <div class="div2">
      <p class="text t1">Meet TruthGuard, our groundbreaking fact-checking application and website that will help you distinguish 
      what's true or fake! Our solution employs the power of Python and utilizes a range of libraries and algorithms to thoroughly 
      evaluate the credibility of URLs and determine whether they contain fake news. We leave no stone unturned in our quest for 
      accuracy. By examining the source of the URL, scrutinizing the orthography and vocabulary, and analyzing the content, we 
      provide a comprehensive assessment of its veracity.
    </p>
    </div>
    
    <h1 class="welcome">How does it works ?</h1>
    <div class="div3">
      <p class="text t2">Let's dive deeper into the functionality of our fact-checking solution. Our system employs a multi-faceted 
      approach to evaluate the authenticity of a given URL. The first block focuses on source checking, where we examine the 
      reliability and reputation of the website or platform hosting the content. This helps establish the initial credibility 
      of the information.
      The second block centers around orthography and vocabulary. Our algorithms analyze the linguistic aspects of the content, 
      looking for inconsistencies, grammatical errors, and unusual vocabulary usage that may indicate fabricated information. 
      By conducting this thorough linguistic analysis, we can identify potential red flags.
      The final block of our solution delves into the content itself. Here, we employ sophisticated algorithms to evaluate the 
      reliability and accuracy of the information presented. By cross-referencing against reputable sources, fact-checking 
      databases, and statistical analysis, we generate a comprehensive assessment of the likelihood of fake news presence in the 
      given URL.
      To provide users with a clear understanding of our evaluation, we present an overall percentage indicating the URL's 
      susceptibility to containing fake news. This percentage serves as a quick reference point for users to gauge the credibility 
      of the information they encounter online. We believe that empowering individuals with the tools to make informed decisions 
      is crucial in the fight against fake news.
      </p>
    </div>
    <div class="div4">
      <p class="text t3">With TruthGuard, we aim to combat the dissemination of misinformation and foster a more informed and 
      responsible digital community. Together, let's stand against fake news and prioritize the pursuit of truth.
      </p>
    </div>
  </div>
  <img src="@/assets/truthguard.png" alt="TruthGuard logo" id="logo">
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
  padding-inline:500px;
  align-items: center;
  justify-content: center;

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
  display: flex;
  margin-top: 60px;
  margin-bottom: 60px;
  text-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

.text {
  font-size: 20px;
  color: white;
  margin-top: 20px;
  margin-left: 20%;
  margin-right: 20%;
  margin-bottom: 60px;
  text-align: justify;
  text-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

.div1 {
  background: #e1b07e;
  /* extend background color to the whole width of the page */
  margin-left: -500px;
  margin-right: -500px;
  padding-top: 55px;
  padding-bottom: 20px;
}

.t1 {
  background: #230903;
  /* extend the margin of the block to the beginning of the next one */
  margin-bottom: -20px;

}

.div2 {
  background: #230903;
  margin-left: -500px;
  margin-right: -500px;
  padding-top: 50px;
  padding-bottom: 80px;
}

.t2 {
  background: #7c7287;
  margin-bottom: 70px;
}

.div3{
  background: #7c7287;
  margin-left: -500px;
  margin-right: -500px;
  padding-top: 50px;
  padding-bottom: 1px;
}

.div4{
  background: #230903;
  margin-left: -500px;
  margin-right: -500px;
  padding-top: 50px;
  padding-bottom: 100px;
}

#logo{
  height: 170px;
  /*center the logo*/
  display: block;
  margin-left: auto;
  margin-right: auto;
  transition: all .2s ease-out;
  background-color: #a7c6da;
  padding: 10px;
  border-radius: 10px;
  margin-top: 50px;
  margin-bottom: 50px;
}

.footer {
  /*leave no space between the footer and the last element*/
  margin-top: auto;
  background: #7c7287;
  padding: 40px;
  margin-top: 150px;
}
</style>