<script lang="ts">
import Notepad from './Notepad/index.vue'
import DocumentationIcon from '@/components/icons/IconDocumentation.vue'
import { getChangeLog } from './Notepad/changelog'


export default {
  data() {
    return {
      mainPage: 0,
      tooltip: [
        "ChangeLog",
        "What's new?",
        "敬请期待",
        "敬请期待",
      ],
      title: "",
      message:"",
      changeLogMessage:"",
    }
  },
  components: {
    Notepad,
    DocumentationIcon
  },
  methods: {
    change_page(n: number) {
      this.mainPage = n;
      this.title = this.tooltip[n];
      switch (n) {
        case 0:
          this.message = this.changeLogMessage;
          break;
        default:
          this.message = "敬请期待";
          break;
      }
    },
    getBgColor(index: number) {
      if (index < this.mainPage) {
        return "var(--color-border)"
      } else if (index == this.mainPage) {
        return "var(--icon-highlight)"
      } else {
        return "var(--color-border-hover)"
      }
    }
  },
  beforeCreate() {
    getChangeLog().then(res => {
      this.changeLogMessage = res;
      this.change_page(this.mainPage);
    })
  },
}

</script>

<template>
  <div class="messageBar">
    <div class="options">
      <li v-for="(item, index) in tooltip" :key="index" class="item">
        <el-tooltip :content="item" placement="left" >
          <i :style="{background:getBgColor(index)}" @mouseover="change_page(index)">
            <DocumentationIcon/>
          </i>
        </el-tooltip>
      </li>
    </div>
    <div class="messageBox">
      <Notepad :title="title" :message="message"/>
    </div>
  </div>
</template>

<style lang="scss">

.messageBar {
  display: flex;
  height: 500px;
  margin-top: 2rem;
  position: relative;
  flex-direction: row;
}

.messageBar .options{
  display: flex;
  flex-direction: column;
  flex-grow: 1;
  width: 32px;
  color: var(--color-text);
}

.messageBar .options .item{
  display: flex;
  margin: auto;
}

.messageBar .messageBox {
  height: 100%;
  width: 100%;
  overflow-y: auto;
  overflow-x: hidden;
}

i {
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.2rem;
  color: var(--color-text);
  width: 50px;
  height: 50px;
  border-radius: 8px;
}

@media screen and (orientation:landscape) {
  .messageBar {
    margin-top: 0;
    padding: 5rem 0 5rem calc(var(--section-gap) / 2);
  }

  i {
    left: -21px;
    position: absolute;
    border-radius: 8px;
    width: 40px;
    height: 40px;
  }

  // 黑线
  .messageBar:before {
    content: ' ';
    border-left: 1px solid var(--color-border);
    position: absolute;
    left: 0;
    bottom: calc(50% + 25px);
    height: calc(50% - 25px);
  }

  // 画白线
  .messageBar:after {
    content: ' ';
    border-left: 1px solid var(--vt-c-divider-dark-2);
    position: absolute;
    left: 0;
    top: calc(15%);
    height: calc(75%);
    z-index: -10;
  }

  .messageBar:first-of-type:before {
    display: none;
  }

  .item:last-of-type:after {
    display: none;
  }
}
</style>
