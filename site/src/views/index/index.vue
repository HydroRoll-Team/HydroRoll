<script setup lang="ts">
import Left from './Left.vue'
import Right from './Right.vue'
</script>

<template>
  <header>
    <img alt="Vue logo" class="logo" src="@/assets/Hydroroll-small.svg" width="125" height="125" />

    <div class="wrapper">
      <Left msg="饼在画了！" />
    </div>
  </header>

  <main class="main">
    <video src="@/assets/video/bg.mp4" loop=true autoplay=true></video>
    <Right />
  </main>
</template>

<style scoped>
header {
  display: flex;
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media screen and (orientation:landscape) {
  header {
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}

video{
  position: fixed;
  right: 0;
  bottom: 0;
  min-width: 100%;
  min-height: 100%;
  width: auto;
  height: auto; 
  z-index: -100;
  filter: grayscale(20%);
}
</style>
