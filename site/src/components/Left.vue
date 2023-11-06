<script lang="ts">
export default {
  data(){
    return{
      day:0,
      hour:0,
      min:0,
      sec:0,
      timer:0
    }
  },
  props:{
    msg:{
      type:String,
      require:true
    },
    date:{
      type:Date,
      default:new Date('2024-07-14T12:00:00Z')
    }
  },
  methods:{
    getTime(){
      this.timer=window.setTimeout(()=>{
        const date1 = new Date();
        const date2 = new Date(this.date);
        const timeDiff = Math.abs(date2.getTime() - date1.getTime());
        this.day = Math.floor(timeDiff / (1000 * 60 * 60 * 24));
        this.hour = Math.floor(timeDiff / (1000 * 60 * 60)%24);
        this.min = Math.floor((timeDiff / (1000 * 60)) % 60);
        this.sec = Math.floor((timeDiff / 1000) % 60);
        this.getTime()
      },1000)
    }
  },
  beforeMount() {
    this.getTime()
  }

}
</script>

<template>
  <div class="greetings">
    <h1 class="green">{{ msg }}</h1>
    <h3>
      距离水系公测还有
    </h3>
    <h2>
      {{ day }} 天 {{ hour }} 时 {{ min }} 分 {{ sec }} 秒
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
