<template>
  <div>
    <v-row class="pt-1">
      <v-col cols="12" sm="8">
        <div>
          <div :style="{ marginBottom: '16px' }">
            <a-button @click="add"> ADD Meesage</a-button>
          </div>
          <a-tabs
            v-model="activeKey"
            hide-add
            type="editable-card"
            @edit="onEdit"
          >
            <a-tab-pane
              v-for="pane in panes"
              :key="pane.key"
              :tab="pane.type"
              :closable="pane.closable"
            >
              <!-- <b>pane{{ pane }}</b> -->
              Select Message Type:
              <a-select
                default-value="Single Line Message"
                style="width: 200px"
                v-model="pane.type"
              >
                <a-select-option value="Single Line Message">
                  Single Line Message
                </a-select-option>
                <a-select-option value="Multi Line Message">
                  Multi Line Message
                </a-select-option>
                <a-select-option value="Image Message">
                  Image Message
                </a-select-option>
                <a-select-option value="Video Message">
                  Video Message
                </a-select-option>
              </a-select>

              <br />

              <v-row class="mt-5">
                <v-col>
                  <v-text-field
                    type="number"
                    v-model="pane.top"
                    :rules="[rules.required]"
                    dense
                    label="X Co-Ordinates "
                  ></v-text-field>
                </v-col>
                <v-col>
                  <v-text-field
                    v-model="pane.left"
                    :rules="[rules.required]"
                    dense
                    label="Y Co-Ordinates "
                  ></v-text-field>
                </v-col>
                <v-col>
                  <v-text-field
                    v-model.number="pane.width"
                    :rules="[rules.required]"
                    dense
                    @input="callchange"
                    label="Width "
                  ></v-text-field>
                </v-col>
                <v-col>
                  <v-text-field
                    v-model.number="pane.height"
                    :rules="[rules.required]"
                    dense
                    @input="callchange"
                    label="Height "
                  ></v-text-field>
                </v-col>
              </v-row>

              <template v-if="pane.type == 'Single Line Message'">
                <Editor
                  :single="true"
                  :image-provider="imageProvider"
                  disableimage="true"
                  disablevideo="true"
                  v-model="pane.message"
                />
              </template>
              <template v-if="pane.type == 'Multi Line Message'">
                <Editor
                  :image-provider="imageProvider"
                  disableimage="true"
                  disablevideo="true"
                  v-model="pane.message"
                />
              </template>
              <template v-if="pane.type == 'Image Message'">
                <input ref="fileInput" type="file" @input="pickFile" />
                <!-- <v-file-input accept="image/*" v-model="imageModal" @change="pickFile" show-size label="File input"></v-file-input> -->
              </template>
              <template v-if="pane.type == 'Video Message'">
                <v-file-input
                  accept="image/*"
                  v-model="VideoModal"
                  show-size
                  label="Please Upload Video Files"
                ></v-file-input>
              </template>
            </a-tab-pane>
          </a-tabs>
        </div>
      </v-col>
      <v-col v-if="panes.length >= 1" cols="12" sm="4">
        <b>Preview</b>
        <!-- <v-btn @click="load = !load">Refres</v-btn> -->
        <v-card width="450px" height="300px" v-if="load">
            <VueDragResize
            :x="Number(pane.left)"
            v-on:resizing="resize"
            v-on:dragging="resize"
            :y="Number(pane.top)"
            :w="Number(pane.width)"
            :h="Number(pane.height)"
            v-for="pane in panes"
            :key="pane.key"
            :snapToGrid="true"
            :parentLimitation="true"
            :isActive="pane.key == activeKey"
            :isResizable="pane.key == activeKey"
            :isDraggable="pane.key == activeKey"
          >
            <div
              v-if="
                pane.type == 'Image Message' || pane.type == 'Video Message'
              "
              class="imagePreviewWrapper"
              :style="{ 'background-image': `url(${previewImage})` }"
              @click="selectImage"
            >
              No Preview
            </div>

            <span v-else v-html="pane.message"></span>

            <!-- <h3>Hello World!</h3>
            <p>{{ top }} х {{ left }} </p>
            <p>{{ width }} х {{ height }}</p> -->
          </VueDragResize>
          
        </v-card>
        <br>
        <center>
                                        <v-btn @click="SaveData" v-if="NewChange" small color="primary">Save</v-btn>

        </center>

        <!-- <Resizable1/> -->
      </v-col>
    </v-row>
  </div>
</template>


<script>
import VueDragResize from "vue-drag-resize";
// import RegionDimension from "./RegionDimension";
import Editor from "@/index.js";

// import Resizable1 from "./Resizable1";

export default {
  name: "App",
  components: { VueDragResize, Editor },
  data() {
    // const panes = [];

    return {
      load: true,
      VideoModal: "",
      rules: {
        required: (value) => !!value || "Required.",
        counter: (value) => value.length <= 20 || "Max 20 characters",
        email: (value) => {
          const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
          return pattern.test(value) || "Invalid e-mail.";
        },
        confirmpassword: (value) => {
          if (this.userObj.password == value) {
            return true;
          } else {
            return false || "Not Match";
          }
        },
      },
      imageProvider: {
        name: "Custom", // provider name
        token:
          "-qWchT63mkZEJch0ygm3bN9h3peInHqCcSAEMtvV:9YAz4dCiB3EAdYuoDVO0YvObtqY=:eyJzY29wZSI6InRlc3QiLCJkZWFkbGluZSI6MTkwMjAyODY1NX0=", // upload token
        domain: "cdn-testing.zanquan.net", // upload domain
        modifier: ({ width, height, url }) => {
          console.log(height);
          if (width < 750) {
            return url;
          } else {
            return `${url}?imageMogr2/thumbnail/750x/`;
          }
        },
      },

      newTabIndex: 0,
      panes: [],
      width: 0,
      height: 0,
      top: 0,
      left: 0,
      activeKey: null,
      ImageFile: null,
      previewImage: "",NewChange : null
    };
  },
  props: {
    LoadData: {
      default: Object,
    },
  },

  methods: {
    SaveData(){
      console.log("this.NewChange",this.NewChange)
      for (var pane of this.panes){
        if (pane.key == this.activeKey){
          console.log("Called")
          pane.left = this.NewChange.left 
          pane.top = this.NewChange.top 
        }
      }
      this.NewChange =null
      console.log(this.NewChange)
    },
    callchange() {
      console.log("Changed");
      this.load = false;
      setTimeout(() => (this.load = true), 500);
    },
    selectImage() {
      this.$refs.fileInput.click();
    },
    pickFile() {
      let input = this.$refs.fileInput;
      let file = input.files;
      console.log(file);
      console.log("pickFile called");
      if (file && file[0]) {
        this.ImageFile = file[0];

        let reader = new FileReader();
        reader.onload = (e) => {
          this.previewImage = e.target.result;
        };
        reader.readAsDataURL(file[0]);
        this.$emit("input", file[0]);
      }
    },
    resize(newRect) {
      this.NewChange = null
      this.NewChange = newRect
      console.log("NewChange", this.NewChange)
      
    },
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
        type: "Single Line Message",
        top: 0,
        left: 0,
        width: 100,
        height: 100,
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
      const panes = this.panes.filter((pane) => pane.key !== targetKey);
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
    },
  },
};
</script>

<style scoped lang="scss">
.imagePreviewWrapper {
  width: 250px;
  height: 250px;
  display: block;
  cursor: pointer;
  margin: 0 auto 30px;
  background-size: cover;
  background-position: center center;
}
</style>