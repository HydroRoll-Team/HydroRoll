<script setup lang="ts">
import Left from './Left.vue'
import Right from './Right.vue'
</script>

<script lang="ts">
export default {
  data() {
    return {
      isplay: false
    }
  },
  methods: {
    PlayOn() {
      this.isplay = true
    }
  }
}
</script>

<template>
  <header>
    <img src="@/assets/Hydroroll-small.svg" 
      alt="Vue logo" 
      class="logo" 
      width="125" height="125" />

    <div class="wrapper">
      <Left msg="饼在画了！" />
    </div>
  </header>

  <main class="main">
    <video loop=true preload="auto" muted="true" autoplay @canplay="PlayOn" v-show="isplay" >
      <source src="@/assets/video/bg.mp4" type="video/mp4" />
    </video>
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
