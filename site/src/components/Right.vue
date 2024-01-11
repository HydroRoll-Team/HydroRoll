<script lang="ts">
import ChangeLog from './ChangeLog.vue'
import RightPage1 from './RightPage1.vue'
import DocumentationIcon from './icons/IconDocumentation.vue'

export default {
  data() {
    return {
      mainPage: 1,
      changelogDisplay: "",
      page2Display: "none",
      page3Display: "none",
      page4Display: "none",
      icon1Back:"var(--icon-highlight)",
      icon2Back:"",
      icon3Back:"",
      icon4Back:"",
    }
  },
  components: {
    ChangeLog,
    RightPage1,
    DocumentationIcon
  },
  methods: {
    control_page(type: string, n: number) {
      if (type == "over") {
        this.mainPage = n
        this.change_page(n)
      }
      if (type == "click") {
        this.mainPage = n
        this.change_page(n)
      }
      if (type == "out") {
        this.change_page(this.mainPage)
      }
    },
    change_page(n: number) {
      if (n == 1) {
        this.changelogDisplay = "";
        this.page2Display = "none";
        this.page3Display = "none";
        this.page4Display = "none";
        this.icon1Back="var(--icon-highlight)";
        this.icon2Back="";
        this.icon3Back="";
        this.icon4Back="";
      } else if (n == 2) {
        this.changelogDisplay = "none";
        this.page2Display = "";
        this.page3Display = "none";
        this.page4Display = "none";
        this.icon1Back="";
        this.icon2Back="var(--icon-highlight)";
        this.icon3Back="";
        this.icon4Back="";
      } else if (n == 3) {
        this.changelogDisplay = "none";
        this.page2Display = "none";
        this.page3Display = "";
        this.page4Display = "none";
        this.icon1Back="";
        this.icon2Back="";
        this.icon3Back="var(--icon-highlight)";
        this.icon4Back="";
      } else if (n == 4) {
        this.changelogDisplay = "none";
        this.page2Display = "none";
        this.page3Display = "none";
        this.page4Display = "";
        this.icon1Back="";
        this.icon2Back="";
        this.icon3Back="";
        this.icon4Back="var(--icon-highlight)";
      }

    }
  }
}

</script>

<template>
  <div class="item">
    <i :style="{background:icon1Back}" @mouseover="control_page('over',1)" @click="control_page('click',1)" @mouseout="control_page('out',1)">
      <DocumentationIcon/>
    </i>
    <i :style="{background:icon2Back}" @mouseover="control_page('over',2)" @click="control_page('click',2)" @mouseout="control_page('out',2)">
      <DocumentationIcon/>
    </i>
    <i :style="{background:icon3Back}" @mouseover="control_page('over',3)" @click="control_page('click',3)" @mouseout="control_page('out',3)">
      <DocumentationIcon/>
    </i>
    <i :style="{background:icon4Back}" @mouseover="control_page('over',4)" @click="control_page('click',4)" @mouseout="control_page('out',4)">
      <DocumentationIcon/>
    </i>
    <div>
      <ChangeLog :style="{display:changelogDisplay}"/>
      <RightPage1 title="Test Page 2" :style="{display:page2Display}"/>
      <RightPage1 title="Test Page 3" :style="{display:page3Display}"/>
      <RightPage1 title="Test Page 4" :style="{display:page4Display}"/>
    </div>
  </div>

</template>

<style>

.item {
  height: 600px;
  margin-top: 2rem;
  display: flex;
  position: relative;
}


i {
  display: flex;
  place-items: center;
  place-content: center;
  width: 32px;
  height: 32px;
  color: var(--color-text);
}


h3 {
  font-size: 1.2rem;
  font-weight: 500;
  margin-bottom: 0.4rem;
  color: var(--color-heading);
}

@media (min-width: 1024px) {
  .item {
    margin-top: 0;
    padding: 0.4rem 0 1rem calc(var(--section-gap) / 2);
  }

  i{
    left: -26px;
    position: absolute;
    border-radius: 8px;
    width: 50px;
    height: 50px;
  }

  div i:nth-child(1) {
    top: calc(20% - 25px);
  }

  div i:nth-child(2) {
    top: calc(40% - 25px);
  }

  div i:nth-child(3) {
    top: calc(60% - 25px);
  }

  div i:nth-child(4) {
    top: calc(80% - 25px);
  }

  .item:before {
    content: ' ';
    border-left: 1px solid var(--color-border);
    position: absolute;
    left: 0;
    bottom: calc(50% + 25px);
    height: calc(50% - 25px);
  }

  .item:after {
    content: ' ';
    border-left: 1px solid var(--color-border);
    position: absolute;
    left: 0;
    top: calc(50% + 25px);
    height: calc(50% - 25px);
  }

  .item:first-of-type:before {
    display: none;
  }

  .item:last-of-type:after {
    display: none;
  }
}
</style>
