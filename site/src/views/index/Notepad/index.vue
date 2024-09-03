<script lang="ts">
export default {
  props: {
    title: {
      type: String,
      default: "1",
    },
    message: {
      type: String,
      require: true
    },
    date: {
      type: Date,
      default: new Date('2024-07-14T12:00:00Z')
    }
  },
}
</script>


<template>
  <div class="details" style="overflow-y:scroll;overflow-x:hidden;height:100%">
    <h3>
      {{ title }}
    </h3>
    <v-md-preview :text="message" ></v-md-preview>
  </div>
</template>


<style scoped>


h3 {
  font-size: 1.2rem;
  font-weight: 500;
  margin-bottom: 0.4rem;
  color: var(--color-heading);
}

.details {
  flex: 1;
  width: 30dvw;
}
</style>
