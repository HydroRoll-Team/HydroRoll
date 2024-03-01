<script lang="ts">
import axios from 'axios';

export default {
  data() {
    return {
      ChangeLogMessage: 'testChangeLogMessage',
    }
  },
  props: {
    msg: {
      type: String,
      require: true
    },
    date: {
      type: Date,
      default: new Date('2024-07-14T12:00:00Z')
    }
  },
  methods: {
    getChangeLog() {
      axios.get('https://api.github.com/repos/HydroRoll-Team/HydroRoll/releases/latest').then(res => {

        this.ChangeLogMessage ="## "+ res.data['tag_name']+"\n"+res.data['body'];
        console.log(res.data);
      })
    }
  },
  beforeMount() {
    this.getChangeLog()
  }

}
</script>


<template>
  <div class="details" style="overflow-y:scroll;overflow-x:hidden;height:100%">
    <h3>
      ChangeLog
    </h3>
    <v-md-preview :text="ChangeLogMessage"></v-md-preview>
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
  margin-left: 1rem;
}
</style>
