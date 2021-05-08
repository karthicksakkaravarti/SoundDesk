<template>
  <!-- <div> -->
    <!-- <v-row class="pt-1"> -->
      <!-- <v-col cols="12" sm="8">

         <div class="container table-block">
      <div class="table-row">
        <div>
          <h4>handlers:</h4>
        </div>
        <span v-for="handler in ['r', 'rb', 'b', 'lb', 'l', 'lt', 't', 'rt']" :key="handler">
          {{handler}}:
          <input type="checkbox" v-model="handlers" :value="handler">
        </span>
      </div>
      <div class="table-row">
        <div class="table-cell">minWidth:
          <input class="table-input" type="number" v-model.number="minW">
        </div>
        <div class="table-cell">maxWidth:
          <input class="table-input" type="number" v-model.number="maxW">
        </div>
      </div>
      <div class="table-row">
        <div class="table-cell">minHeight:
          <input class="table-input" type="number" v-model.number="minH">
        </div>
        <div class="table-cell">maxHeight:
          <input class="table-input" type="number" v-model.number="maxH">
        </div>
      </div>
      <div class="table-row">
        <div class="table-cell">width:
          <input class="table-input" type="number" v-model.number="width">
        </div>
        <div class="table-cell">height:
          <input class="table-input" type="number" v-model.number="height">
        </div>
      </div>
      <div class="table-row">
        <div class="table-cell">left:
          <input class="table-input" type="number" v-model.number="left">
        </div>
        <div class="table-cell">top:
          <input class="table-input" type="number" v-model.number="top">
        </div>
      </div>
      <div class="table-row">
        <div class="table-cell">fitParent:
          <input type="checkbox" v-model.number="fit">
        </div>
      </div>
      <div class="table-row" style="text-align: left;">
        <div class="table-cell" style="padding: 0 20px;width: 100%">lastEvent: {{event}}</div>
      </div>
    </div>
      </v-col> -->
      <!-- <v-col cols="12" sm="12">
       <v-card height="300"  width="900" class="mr-2"> -->
          <vue-resizable
        class="resizable"
        ref="resizableComponent1"
        :dragSelector="dragSelector"
        :active="handlers"
        :fit-parent="fit"
        :max-width="maxW | checkEmpty"
        :max-height="maxH | checkEmpty"
        :min-width="minW | checkEmpty"
        :min-height="minH | checkEmpty"
        :width="width"
        :height="height"
        :left="left"
        :top="0"
        @mount="eHandler"
        @resize:move="eHandler"
        @resize:start="eHandler"
        @resize:end="eHandler"
        @drag:move="eHandler"
        @drag:start="eHandler"
        @drag:end="eHandler"
      >
        <div  class="block">
          <div class="drag-container-1">drag_1</div>
          <div class="table-container">
            <table>
              <tr>
                <td>w:{{width}}</td>
                <td>h:{{height}}</td>
              </tr>
              <tr>
                <td>l:{{left}}</td>
                <td>t:{{top}}</td>
              </tr>
            </table>
          </div>
          <div class="drag-container-2">drag_2</div>
        </div>
        
      </vue-resizable>
       <!-- </v-card>
      </v-col>
    </v-row> -->


   
  <!-- </div> -->
</template>

<script>
import VueResizable from "vue-resizable";

export default {
  name: "App",
  components: { VueResizable },
  data() {
    const panes = [
    ];

    const tW = 150;
    const tH = 150;
    return {
      handlers: ["r", "rb", "b", "lb", "l", "lt", "t", "rt"],
      left: `calc( 50% - ${tW / 2}px)`,
      top: `calc(50% - ${tH / 2}px)`,
      height: tH,
      width: tW,
      maxW: 250,
      maxH: 250,
      minW: 100,
      minH: 100,
      fit: true,
      event: "",
      dragSelector: ".drag-container-1, .drag-container-2",
      activeKey: 0,
      panes,
      newTabIndex: 0,
    };
  },
  methods: {
    eHandler(data) {
      this.width = data.width;
      this.height = data.height;
      this.left = data.left;
      this.top = data.top;
      this.event = data.eventName;
    },
    callback(key) {
      console.log(key);
    },
    onEdit(targetKey, action) {
      this[action](targetKey);
    },
    add() {
      const panes = this.panes;
      const activeKey = `newTab${this.newTabIndex++}`;
      panes.push({
        title: `Single Line Message`,
        content: `Content of new Tab ${activeKey}`,
        key: activeKey,
      });
      this.panes = panes;
      this.activeKey = activeKey;
    },
    remove(targetKey) {
      let activeKey = this.activeKey;
      let lastIndex;
      this.panes.forEach((pane, i) => {
        if (pane.key === targetKey) {
          lastIndex = i - 1;
        }
      });
      const panes = this.panes.filter(pane => pane.key !== targetKey);
      if (panes.length && activeKey === targetKey) {
        if (lastIndex >= 0) {
          activeKey = panes[lastIndex].key;
        } else {
          activeKey = panes[0].key;
        }
      }
      this.panes = panes;
      this.activeKey = activeKey;
    },
  },
  filters: {
    checkEmpty(value) {
      return typeof value !== "number" ? 0 : value;
    }
  },
  
};
</script>

<style scoped>
.block {
  height: 100%;
  width: 100%;
  background-color: aqua;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>
<style>
body,
html {
  height: 100%;
  width: 100%;
  margin: 0;
  padding: 0;
  overflow: auto;
}

.container {
  width: 300px;
  height: 300px;
  display: inline-block;
  border: 1px solid #dddddd;
  background: #ffffff;
  color: #333333;
  float: left;
  margin: 10px;
}

#block1 {
  border: solid black 1px;
  height: 300px;
  width: 300px;
  display: inline-block;
  float: left;
}

.resizable {
  background-position: top left;
  width: 150px;
  height: 150px;
  border: 1px solid #003eff;
  background: #007fff;
  font-weight: normal;
  color: #ffffff;
  position: relative;
}

.table-block {
  display: table;
}

.table-row {
  display: table-row;
  text-align: center;
}

.table-cell {
  width: 50%;
  display: inline-block;
}

.table-input {
  width: 50px;
}

.drag-container-1,
.drag-container-2 {
  width: 100%;
  height: 20px;
  background: red;
  color: white;
  text-align: center;
  cursor: pointer;
}

.table-container {
  flex: 1;
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>