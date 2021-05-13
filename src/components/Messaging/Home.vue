<template>
  <div class="pa-1">
    

    <v-breadcrumbs :items="items"></v-breadcrumbs>

    <v-card elevation="0">
      <!-- <v-card-title class="title font-weight-regular justify-space-between">
      <span>{{ currentTitle }}</span>
      <v-avatar
        color="primary lighten-2"
        class="subheading white--text"
        size="24"
        v-text="step"
      ></v-avatar>
    </v-card-title> -->

      <v-overlay :value="overlayMain">
        <div class="text-center">
          <v-progress-circular
            indeterminate
            color="primary"
          ></v-progress-circular>
          Saving
        </div>
      </v-overlay>
      <v-overlay :value="SendApiLoader">
        <div class="text-center">
          <v-progress-circular
            indeterminate
            color="primary"
          ></v-progress-circular>
          Sending Messages to VMD's, Please wait ...
        </div>
      </v-overlay>
      <v-alert dense v-if="userError" outlined type="error">
        {{ userError }}
      </v-alert>
      <v-window v-model="step">
        <v-window-item :value="1">
          <v-card elevation="0" color="grey lighten-4" flat tile>
            <v-toolbar outlined elevation="0" dense>
              <!-- <v-app-bar-nav-icon></v-app-bar-nav-icon> -->

              <v-toolbar-title>Message Config</v-toolbar-title>

              <v-btn-toggle dense class="ml-2" v-model="icon">
                <a-tooltip placement="bottom">
                  <template slot="title">
                    <span>Single Line Message</span>
                  </template>
                  <v-btn value="Single">
                    <v-icon>mdi-sort-variant</v-icon>
                  </v-btn>
                </a-tooltip>

                <a-tooltip placement="bottom">
                  <template slot="title">
                    <span>Multi Line Message</span>
                  </template>
                  <v-btn value="Multi">
                    <!-- <span class="hidden-sm-and-down">Multi</span> -->

                    <v-icon>mdi-format-align-center</v-icon>
                  </v-btn>
                </a-tooltip>

                <a-tooltip placement="bottom">
                  <template slot="title">
                    <span>Image Message</span>
                  </template>
                  <v-btn value="Image">
                    <!-- <span class="hidden-sm-and-down">Image</span> -->

                    <v-icon>mdi-file-image</v-icon>
                  </v-btn>
                </a-tooltip>

                <a-tooltip placement="bottom">
                  <template slot="title">
                    <span>Video Message</span>
                  </template>
                  <v-btn value="Video">
                    <!-- <span class="hidden-sm-and-down">Video</span> -->

                    <v-icon>mdi-file-video</v-icon>
                  </v-btn>
                </a-tooltip>
                <a-tooltip placement="bottom">
                  <template slot="title">
                    <span>Combinational Message</span>
                  </template>
                  <v-btn value="Combine">
                    <!-- <span class="hidden-sm-and-down">Video</span> -->

                    <v-icon>mdi-vector-combine</v-icon>
                  </v-btn>
                </a-tooltip>
              </v-btn-toggle>
              <v-spacer></v-spacer>
              <a-input
                class="mr-2"
                v-model="playlist"
                style="width: 150px"
                placeholder="Playlist Name"
              />

              <a-dropdown-button @click="sendData" type="primary">
                Send <v-icon color="primary">mdi-send-circle</v-icon>
                <a-menu slot="overlay">
                  <a-menu-item v-if="icon == 'Combine'" key="1" @click="SaveCombinationalMessage">
                    Save to playlist
                  </a-menu-item>
                  <a-menu-item v-else key="1" @click="SaveToPlaylist">
                    Save to playlist
                  </a-menu-item>
                </a-menu>
              </a-dropdown-button>

              <!-- <v-btn color="success" @click="sendData">
          Send <v-icon>mdi-send-circle</v-icon>
        </v-btn> -->
            </v-toolbar>
          </v-card>
          <template v-if="icon == 'Combine'">
            <Combinational ref="combinationActualPreviewRef" />
          </template>
          <v-row class="pt-1" v-else>
            <v-col cols="12" sm="8">
              <v-card outlined>
                <v-card-text>
                  <RegionDimension
                    :loaddata="false"
                    ref="RegionDimension_ref"
                  />
                  <h3 style="border-left: 5px solid #394a59" class="pl-3">
                    Message Details
                  </h3>
                  <template v-if="icon == 'Single'">
                    <Editor
                      :single="true"
                      :image-provider="imageProvider"
                      disableimage="true"
                      disablevideo="true"
                      v-model="messageModal"
                    />

                    <!-- <v-text-field label="Single Line Message" v-model="messageModal"></v-text-field> -->
                  </template>
                  <template v-if="icon == 'Multi'">
                    <Editor
                      :image-provider="imageProvider"
                      disableimage="true"
                      disablevideo="true"
                      v-model="messageModal"
                    />
                  </template>
                  <template v-if="icon == 'Image'">
                    <input ref="fileInput" type="file" @input="pickFile" />

                    <!-- <v-file-input accept="image/*" v-model="imageModal" @change="pickFile" show-size label="File input"></v-file-input> -->
                  </template>
                  <template v-if="icon == 'Video'">
                    <v-file-input
                      accept="image/*"
                      v-model="VideoModal"
                      show-size
                      label="Please Upload Video Files"
                    ></v-file-input>
                  </template>
                </v-card-text>
              </v-card>
            </v-col>
            <v-col cols="12" sm="4">
              <v-card outlined>
                <v-card-title
                  >Message Preview
                  <!-- <b v-if="$refs.RegionDimension_ref"
              >$refs.RegionDimension_ref
              {{ $refs.RegionDimension_ref.dataObj }}</b
            > -->
                </v-card-title>
                <v-divider></v-divider>
                <v-card-text v-if="$refs.RegionDimension_ref">
                  <div
                    v-if="icon == 'Image'"
                    class="imagePreviewWrapper"
                    :style="{ 'background-image': `url(${previewImage})` }"
                    @click="selectImage"
                  ></div>
                  <div v-else-if="icon == 'Video'">
                    <center>No Preview Avaialble for Video</center>
                  </div>
                  <center v-else>
                    <iframe
                      :style="`background-color:${$refs.RegionDimension_ref.dataObj.BackGroundColor};border: 4px solid ${$refs.RegionDimension_ref.dataObj.BorderLine}`"
                      :srcdoc="messageModal"
                      :height="$refs.RegionDimension_ref.dataObj.Height"
                      :width="$refs.RegionDimension_ref.dataObj.Width"
                      title="Iframe Example"
                    >
                    </iframe>
                    <br />
                    <v-btn small color="primary" @click="overlay = !overlay">
                      Preview
                    </v-btn>

                    <v-overlay :value="overlay">
                      <v-row>
                        <v-col>
                          <iframe
                            :style="`background-color:${$refs.RegionDimension_ref.dataObj.BackGroundColor};border: 4px solid ${$refs.RegionDimension_ref.dataObj.BorderLine}`"
                            :srcdoc="messageModal"
                            :height="$refs.RegionDimension_ref.dataObj.Height"
                            :width="$refs.RegionDimension_ref.dataObj.Width"
                            title="Iframe Example"
                          >
                          </iframe>
                        </v-col>
                      </v-row>
                      <v-row
                        ><v-col>
                          <v-btn small color="primary" @click="overlay = false">
                            Close
                          </v-btn>
                        </v-col>
                      </v-row>
                    </v-overlay>
                  </center>
                </v-card-text>
              </v-card>
            </v-col>
          </v-row>
        </v-window-item>

        <v-window-item :value="2">
          <h3 style="border-left: 5px solid #394a59" class="mt-3 pl-3">
            Message Preview
          </h3>
         
          <v-card-text v-if="$refs.RegionDimension_ref && icon != 'Combine'">
            <div
              v-if="icon == 'Image'"
              class="imagePreviewWrapper"
              :style="{ 'background-image': `url(${previewImage})` }"
              @click="selectImage"
            ></div>
            <div v-else-if="icon == 'Video'">
              <center>No Preview Avaialble for Video</center>
            </div>
            <center v-else>
              <iframe
                :style="`background-color:${$refs.RegionDimension_ref.dataObj.BackGroundColor};border: 4px solid ${$refs.RegionDimension_ref.dataObj.BorderLine}`"
                :srcdoc="messageModal"
                :height="$refs.RegionDimension_ref.dataObj.Height"
                :width="$refs.RegionDimension_ref.dataObj.Width"
                title="Iframe Example"
              >
              </iframe>
              <br />

              <v-overlay :value="overlay">
                <v-row>
                  <v-col>
                    <iframe
                      :style="`background-color:${$refs.RegionDimension_ref.dataObj.BackGroundColor};border: 4px solid ${$refs.RegionDimension_ref.dataObj.BorderLine}`"
                      :srcdoc="messageModal"
                      :height="$refs.RegionDimension_ref.dataObj.Height"
                      :width="$refs.RegionDimension_ref.dataObj.Width"
                      title="Iframe Example"
                    >
                    </iframe>
                  </v-col>
                </v-row>
                <v-row
                  ><v-col>
                    <v-btn small color="primary" @click="overlay = false">
                      Close
                    </v-btn>
                  </v-col>
                </v-row>
              </v-overlay>
            </center>
          </v-card-text>
           <template v-else>
             <v-card elevation="0"  class="mt-2" v-if="combinatioPreview" >
               <!-- <b>{{combinatioPreview}}</b> -->
                       <CombinationalPreview :PreviewData="combinatioPreview" />
          
        </v-card>
          </template>
          <h3 style="border-left: 5px solid #394a59" class="mt-3 pl-3">
            VMD/VMD Group Selection
          </h3>
          <br />
          <a-radio-group class="ml-3" v-model="VmDSelectionValue">
            <a-radio-button value="VMD" @click="vmd_or_Group = []">
              VMD
            </a-radio-button>
            <a-radio-button value="VMDGroup" @click="vmd_or_Group = []">
              VMD Group
            </a-radio-button>
          </a-radio-group>
          <v-row class="pa-2">
            <v-col cols="12" sm="6" v-if="VmDSelectionValue == 'VMD'">
              <v-autocomplete
                class="pt-3"
                chips
                multiple
                deletable-chips
                v-model="vmd_or_Group"
                dense
                label="VMD's*"
                auto-select-first
                item-text="VMDName"
                item-value="id"
                :items="GetVMDS"
              ></v-autocomplete>
            </v-col>
            <v-col cols="12" sm="6" v-else>
              <v-autocomplete
                class="pt-2"
                chips
                multiple
                deletable-chips
                v-model="vmd_or_Group"
                dense
                label="VMD Group*"
                auto-select-first
                item-text="GroupName"
                item-value="id"
                :items="GetVMDGroups"
              ></v-autocomplete>
            </v-col>
          </v-row>
        </v-window-item>

        <v-window-item :value="3" >
          <!-- <a-result status="success" title="Successfully Message Send to VMD">
            <template #extra>
              <a-button key="console" @click="step = 1" type="primary">
                Back To Message
              </a-button>
              <a-input
                class="mr-2"
                v-model="playlist"
                style="width: 150px"
                placeholder="Playlist Name"
              />
              <a-button key="buy" @click="SaveToPlaylist">
                Save into PLaylist
              </a-button>
            </template>
          </a-result> -->
          <!-- <b>ApiResponse{{ApiResponse}}</b> -->
          <h3 style="border-left: 5px solid #394a59" class="mt-3 pl-3">
            Message Status
          </h3>
          <v-data-table
          :headers="[
            {'text': 'IP', 'value': 'IP' },
            {'text': 'Status Code', 'value': 'StatusCode' },
            {'text': 'Response', 'value': 'Response' }
            ]"
          :items="ApiResponse">

          </v-data-table>
         <center>
           <a-button key="console" @click="step = 1" type="primary">
                Back To Message
              </a-button>
         </center>
        </v-window-item>
      </v-window>

      <v-divider></v-divider>

      <v-card-actions v-if="step != 1 && step != 3">
        <v-btn text @click="step--" outlined> Back </v-btn>
        <v-spacer></v-spacer>
        <v-btn
          v-if="step != 3"
          color="success"
          outlined
          depressed
          :disabled="!vmd_or_Group.length >= 1"
          :loading="SendApiLoader"
          @click="SendMessageToVMD"
        >
          Send <v-icon color="success">mdi-send-circle</v-icon>
        </v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>
<script>
import { VMDMixins } from "../../mixins/VMDMixins";
import { utility } from "../../mixins/utility";
import { MessagingMixins } from "../../mixins/MessagingMixins";
import { UsersMixins } from "../../mixins/UsersMixins";
// import VueDragResize from "vue-drag-resize";

import Editor from "@/index.js";
// import Moveable from "vue-moveable";

import RegionDimension from "./RegionDimension";
import Combinational from "./Combinational";
import CombinationalPreview from "./CombinationalPreview";

export default {
  components: {
    RegionDimension,
    Editor,
    Combinational,
    // VueDragResize,
    CombinationalPreview
    // Moveable,
  },
  mixins: [VMDMixins, utility, UsersMixins, MessagingMixins],
  mounted() {
    this.get_VMDS();
    this.get_VMDSGroups();
    this.load = true;
    this.messageModal = " ";
  },
  methods: {
    SendMessageToVMD(){
      this.SendApiLoader = true
      console.log("SendMessageToVMD")
      var payload = {
            playlistname: this.playlist,
            XCoOrdinates: this.$refs.RegionDimension_ref.dataObj.XCoOrdinates,
            YCoOrdinates: this.$refs.RegionDimension_ref.dataObj.YCoOrdinates,
            Width: this.$refs.RegionDimension_ref.dataObj.Width,
            Height: this.$refs.RegionDimension_ref.dataObj.Height,
            BorderLine: this.$refs.RegionDimension_ref.dataObj.BorderLine,
            BackGroundColor: this.$refs.RegionDimension_ref.dataObj
              .BackGroundColor,
            type: this.icon,
            singleLineMessage: "",
            multilineMessage: "",
            imageMessage: null,
            videoMessage: null,
            user: this.GetCurrentUser.id,
            vmd_or_Group: this.vmd_or_Group,
            VmDSelectionValue: this.VmDSelectionValue
          };
        if (
            ["Single", "Multi"].includes(this.icon) &&
            this.messageModal.length >= 2
          ) {
            console.log("Validation Done");

            if (this.icon == "Single") {
              payload.singleLineMessage = this.messageModal;
            } else if (this.icon == "Multi") {
              payload.multilineMessage = this.messageModal;
            } else if (this.icon == "Image") {
              payload.multilineMessage = this.ImageFile;
            } else if (this.icon == "Video") {
              payload.multilineMessage = this.messageModal;
            }
            console.log(payload);
          }
      this.post_callColorLightApi(payload)
      .then(data => {
        this.SendApiLoader = false
        this.ApiResponse = data.data
        this.step++
        console.log(data)
      })
      .catch(err =>{
        console.log(err)
        this.SendApiLoader = false
      })
    },
    sendData() {
      if (this.icon != 'Combine'){
        this.$refs.RegionDimension_ref.validateFun().then((data) => {
        console.log(this.messageModal.length);
        if (
          data &&
          ["Single", "Multi"].includes(this.icon) &&
          this.messageModal.length >= 2
        ) {
          console.log("Validation Done");
          this.step++;
        } else if (data && this.previewImage && this.icon == "Image") {
          this.step++;
        } else {
          console.log("Please fill all the fields");
          this.$notification["warn"]({
            message: "Please fill all required fields",
            // description: "Predefined Message Updated",
          });
        }
      });
      }
      else{
                  this.combinatioPreview = this.$refs.combinationActualPreviewRef.panes
                  this.step++;
      }
      
    },
    SaveCombinationalMessage(){
      console.log("Calles combination message funcation")
      console.log(this.$refs.combinationActualPreviewRef)
      if(this.$refs.combinationActualPreviewRef.panes.length >=1){
        console.log("Message added")
        var payload = {
            playlistname: this.playlist,
            XCoOrdinates: null,
            YCoOrdinates: null,
            Width: null,
            Height: null,
            BorderLine: null,
            BackGroundColor: null,
            type: this.icon,
            singleLineMessage: "",
            multilineMessage: "",
            combineMessae: JSON.stringify(this.$refs.combinationActualPreviewRef.panes),
            imageMessage: null,
            videoMessage: null,
            user: this.GetCurrentUser.id,
          };
          console.log(payload)
          this.post_Playlist(payload)
              .then((data) => {
                this.$notification["success"]({
                  message: "Playlist Saved Successfully",
                });
                this.overlayMain = false;

                console.log(data);
              })
              .catch((err) => {
                err;
                this.overlayMain = false;
                this.userError = err.response.data.Error;
              });

      }
      else{
        this.$notification["warn"]({
            message: "Please add atleast one message to save as playlist",
            // description: "Predefined Message Updated",
          });
      }
    },
    SaveToPlaylist() {
      this.overlayMain = true;
      this.$refs.RegionDimension_ref.validateFun()
        .then((data) => {
          console.log(this.messageModal.length);
          var payload = {
            playlistname: this.playlist,
            XCoOrdinates: this.$refs.RegionDimension_ref.dataObj.XCoOrdinates,
            YCoOrdinates: this.$refs.RegionDimension_ref.dataObj.YCoOrdinates,
            Width: this.$refs.RegionDimension_ref.dataObj.Width,
            Height: this.$refs.RegionDimension_ref.dataObj.Height,
            BorderLine: this.$refs.RegionDimension_ref.dataObj.BorderLine,
            BackGroundColor: this.$refs.RegionDimension_ref.dataObj
              .BackGroundColor,
            type: this.icon,
            singleLineMessage: "",
            multilineMessage: "",
            imageMessage: null,
            videoMessage: null,
            user: this.GetCurrentUser.id,
          };
          if (
            data &&
            ["Single", "Multi"].includes(this.icon) &&
            this.messageModal.length >= 2
          ) {
            console.log("Validation Done");

            if (this.icon == "Single") {
              payload.singleLineMessage = this.messageModal;
            } else if (this.icon == "Multi") {
              payload.multilineMessage = this.messageModal;
            } else if (this.icon == "Image") {
              payload.multilineMessage = this.ImageFile;
            } else if (this.icon == "Video") {
              payload.multilineMessage = this.messageModal;
            }
            console.log(payload);
            this.post_Playlist(payload)
              .then((data) => {
                this.$notification["success"]({
                  message: "Playlist Saved Successfully",
                });
                this.overlayMain = false;

                console.log(data);
              })
              .catch((err) => {
                err;
                this.overlayMain = false;
                this.userError = err.response.data.Error;
              });
          } else if (data && this.previewImage && this.icon == "Image") {
            let formData = new FormData();
            formData.append("playlistname", payload.playlistname);
            formData.append("XCoOrdinates", payload.XCoOrdinates);
            formData.append("YCoOrdinates", payload.YCoOrdinates);
            formData.append("Width", payload.Width);
            formData.append("Height", payload.Height);
            formData.append("BorderLine", payload.BorderLine);
            formData.append("BackGroundColor", payload.BackGroundColor);
            formData.append("type", payload.type);
            formData.append("user", payload.user);
            if (this.icon == "Image") {
              formData.append("imageMessage", this.ImageFile);
            } else if (this.icon == "Video") {
              formData.append("videoMessage", this.VideoModal);
            }
            console.log(payload);
            this.post_Playlist(formData)
              .then(() => {
                this.$notification["success"]({
                  message: "Playlist Saved Successfully",
                });
                this.overlayMain = false;
              })
              .catch((err) => {
                err;
                this.overlayMain = false;
                this.userError = err.response.data.Error;
              });
          } else if (data && this.VideoModal && this.icon == "Video") {
            let formData = new FormData();
            formData.append("playlistname", payload.playlistname);
            formData.append("XCoOrdinates", payload.XCoOrdinates);
            formData.append("YCoOrdinates", payload.YCoOrdinates);
            formData.append("Width", payload.Width);
            formData.append("Height", payload.Height);
            formData.append("BorderLine", payload.BorderLine);
            formData.append("BackGroundColor", payload.BackGroundColor);
            formData.append("type", payload.type);
            formData.append("user", payload.user);
            if (this.icon == "Video") {
              formData.append("videoMessage", this.VideoModal);
            }
            console.log(payload);
            this.post_Playlist(formData)
              .then(() => {
                this.$notification["success"]({
                  message: "Playlist Saved Successfully",
                });
                this.overlayMain = false;
              })
              .catch((err) => {
                err;
                this.overlayMain = false;
                this.userError = err.response.data.Error;
              });
          } else {
            this.overlayMain = false;
            console.log("Please fill all the fields");
            this.$notification["warn"]({
              message: "Please fill all required fields",
              // description: "Predefined Message Updated",
            });
          }
        })
        .catch((err) => {
          err;
          this.overlayMain = false;
          console.log(err);
          this.userError = err.response.data.Error;
        });
    },
    selectImage() {
      this.$refs.fileInput.click();
    },
    pickFile() {
      let input = this.$refs.fileInput;
      let file = input.files;
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
    SendMessage() {
      this.$refs.RegionDimension_ref.validateFun().then((data) => {
        console.log(data);
        this.$refs.messageForm.validate();
      });
    },
    handleDrag({ target, left, top }) {
      console.log("onDrag left, top", left, top);
      target.style.left = `${left}px`;
      target.style.top = `${top}px`;
    },
    handleResize({ target, width, height, delta }) {
      console.log("onResize", width, height);
      delta[0] && (target.style.width = `${width}px`);
      delta[1] && (target.style.height = `${height}px`);
    },
    handleScale({ target, transform, scale }) {
      console.log("onScale scale", scale);
      target.style.transform = transform;
    },
    handleRotate({ target, dist, transform }) {
      console.log("onRotate", dist);
      target.style.transform = transform;
    },
    handleWarp({ target, transform }) {
      console.log("onWarp", target);
      target.style.transform = transform;
    },
  },
  computed: {
    currentTitle() {
      switch (this.step) {
        case 1:
          return "Sign-up";
        case 2:
          return "Create a password";
        default:
          return "Account created";
      }
    },
  },
  data() {
    return {
      SendApiLoader: false,
      ApiResponse: null,
      loadPreview: false,
      combinatioPreview: null,
      playlist: "Playlist 1",
      userError: "",
      overlayMain: false,
      vmd_or_Group: "",
      VmDSelectionValue: "VMD",
      step: 1,
      overlay: false,
      ImageFile: null,
      previewImage: "",
      icon: "Single",
      imageModal: "",
      VideoModal: "",
      moveable: {
        draggable: true,
        throttleDrag: 1,
        resizable: true,
        throttleResize: 1,
        keepRatio: true,
        scalable: true,
        throttleScale: 0,
        rotatable: true,
        throttleRotate: 0,
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
      messageModal: "",
      load: false,
      items: [
        {
          text: "Dashboard",
          disabled: false,
          href: "/#/dashboard",
        },
        {
          text: "Messaging",
          disabled: false,
        },
      ],
      dialogm1: "",
      dialog: false,
      dialog1: false,
      messageType: null,
      selectedVmd: null,
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
    };
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
