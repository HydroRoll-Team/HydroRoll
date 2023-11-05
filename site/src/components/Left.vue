<script setup lang="ts">
import {computed} from "vue";

defineProps({
  msg: {
    type: String,
    required: true
  }
})

const day=100
const hour=18
const min=50
const sec=50
</script>

<template>
  <div class="greetings">
    <h1 class="green">{{ msg }}</h1>
    <h3>
      距离水系公测还有
    </h3>
    <h2>
      {{ day }}d {{ hour }}h {{ min }}m {{ sec }}s
    </h2>
  </div>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  position: relative;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
