<template>
  <section class="wrapper">
    <!--overview start-->
             <v-breadcrumbs :items="items"></v-breadcrumbs>

    <v-app>
      <div>
        <!-- Tabs -->
        <a-tabs v-model="tabs" default-active-key="1">
          <a-tab-pane key="1" tab="Single Line Text Message">
            <a-row>
              <a-col>
                <div v-if="this.GetCurrentUser.id" v-once>
                  {{ LoadSingleLineData() }}
                </div>

                <!-- RegionDimension -->
                <RegionDimension
                  v-if="tabs == 1"
                  ref="RegionDimension_ref"
                  typemessage="single"
                />
                <!-- RegionDimension End -->
                <b style="border-left: 5px solid blue" class="pl-3"
                  >Text Details</b
                >
                <Editor
                  class="mt-5"
                  disableimage="true"
                  disablevideo="true"
                  v-model="SingleTextMessagedata"
                  :image-provider="imageProvider"
                />
                <Schedule
                  ref="Schedule_ref"
                  v-if="tabs == 1"
                  typemessage="single"
                />
                <v-card elevation="0" class="d-flex flex-row-reverse" flat tile>
                  <v-card elevation="0" class="pa-2" tile>
                    <v-btn
                      class="d-flex flex-row"
                      color="green"
                      @click="saveSingleLineMessage"
                      >Save</v-btn
                    >
                  </v-card>
                </v-card>
              </a-col>
            </a-row>
          </a-tab-pane>
          <a-tab-pane key="2" tab="Multi Line Text Message" force-render>
            <a-row>
              <a-col>
                <div v-if="this.GetCurrentUser.id" v-once>
                  {{ LoadMultiLineData() }}
                </div>

                <!-- RegionDimension -->
                <RegionDimension
                  v-if="tabs == 2"
                  ref="RegionDimension_ref"
                  typemessage="multi"
                />
                <!-- RegionDimension End -->
                <b style="border-left: 5px solid blue" class="pl-3"
                  >Text Details</b
                >
                <Editor
                  class="mt-5"
                  disableimage="true"
                  disablevideo="true"
                  v-model="MultiTextMessagedata"
                  :image-provider="imageProvider"
                />
                <Schedule
                  ref="Schedule_ref"
                  v-if="tabs == 2"
                  typemessage="multi"
                />
                <v-card elevation="0" class="d-flex flex-row-reverse" flat tile>
                  <v-card elevation="0" class="pa-2" tile>
                    <v-btn
                      class="d-flex flex-row"
                      color="green"
                      @click="saveMultiLineMessage"
                      >Save</v-btn
                    >
                  </v-card>
                </v-card>
              </a-col>
            </a-row>
          </a-tab-pane>
          <a-tab-pane key="3" tab="Image Message">
            <a-row>
              <a-col>
                <div v-if="this.GetCurrentUser.id" v-once>
                  {{ LoadimageData() }}
                </div>

                <!-- RegionDimension -->
                <RegionDimension
                  v-if="tabs == 3"
                  ref="RegionDimension_ref"
                  typemessage="image"
                />
                <!-- RegionDimension End -->
                <b style="border-left: 5px solid blue" class="pl-3"
                  >Text Details</b
                >
                <!-- Image data -->
                <Editor
                  class="mt-5"
                  disablevideo="true"
                  v-model="ImageMessagedata"
                  :image-provider="imageProvider"
                />
                <!-- Image data end -->
                <Schedule
                  ref="Schedule_ref"
                  v-if="tabs == 3"
                  typemessage="image"
                />
                <v-card elevation="0" class="d-flex flex-row-reverse" flat tile>
                  <v-card elevation="0" class="pa-2" tile>
                    <v-btn
                      class="d-flex flex-row"
                      color="green"
                      @click="saveImageMessage"
                      >Save</v-btn
                    >
                  </v-card>
                </v-card>
              </a-col>
            </a-row>
          </a-tab-pane>
          <a-tab-pane key="4" tab="Video Message">
            <a-row>
              <a-col>
                <div v-if="this.GetCurrentUser.id" v-once>
                  {{ LoadMediaData() }}
                </div>

                <!-- RegionDimension -->
                <RegionDimension
                  v-if="tabs == 4"
                  ref="RegionDimension_ref"
                  typemessage="video"
                />
                <!-- RegionDimension End -->
                <b style="border-left: 5px solid blue" class="pl-3"
                  >Text Details</b
                >
                <!-- Image data -->
                <Editor
                  class="mt-5"
                  disableimage="true"
                  v-model="VideoMessagedata"
                  :image-provider="imageProvider"
                />
                <!-- Image data end -->
                <Schedule
                  ref="Schedule_ref"
                  v-if="tabs == 4"
                  typemessage="video"
                />
                <v-card elevation="0" class="d-flex flex-row-reverse" flat tile>
                  <v-card elevation="0" class="pa-2" tile>
                    <v-btn
                      class="d-flex flex-row"
                      color="green"
                      @click="saveVideoMessage"
                      >Save</v-btn
                    >
                  </v-card>
                </v-card>
              </a-col>
            </a-row>
          </a-tab-pane>
          <a-tab-pane key="5" tab="Combinational Message ">
            Content of Tab Pane 3
          </a-tab-pane>
          <a-tab-pane key="6" tab="Predefined Message">
            <!-- VMDS -->
            <div v-once>{{ LoadAllTestMessageData() }}</div>
            <div v-once>{{ LoadAllPredefinedData() }}</div>
            <b style="border-left: 5px solid blue" class="pl-3">Select VMD</b>
            <div class="pt-2">
              <v-autocomplete
                chips
                deletable-chips
                dense
                v-model="PredefinedModal"
                :rules="[rules.required]"
                label="VMD's*"
                auto-select-first
                item-text="VMDName"
                item-value="id"
                :items="GetVMDS"
              ></v-autocomplete>

              <b style="border-left: 5px solid blue" class="pl-3"
                >Message Details</b
              >
              <v-form>
                <div
                  class="pt-2"
                  v-bind:key="i.id"
                  v-for="i in predefinedListMessage"
                >
                  <v-autocomplete
                    v-model="i.modal"
                    dense
                    :rules="[rules.required]"
                    :label="`Select Predefined Message - ${i.id}`"
                    auto-select-first
                    item-text="Message"
                    item-value="id"
                    :items="AllMessagesDataobj"
                  ></v-autocomplete>
                  <!-- <p>Text</p>  <p @click="RemoveSequenceList(i)">Remove</p> -->
                </div>
              </v-form>
              <br />
              <!-- <v-btn small outlined @click="addSequence">+ Add Message</v-btn> -->
              <Schedule
                class="pt-5"
                ref="Schedule_ref"
                v-if="tabs == 6"
                typemessage="Predefined"
              />
              <v-card elevation="0" class="d-flex flex-row-reverse" flat tile>
                <v-card elevation="0" class="pa-2" tile>
                  <v-btn
                    class="d-flex flex-row"
                    color="green"
                    @click="PredefinedSequence"
                    >Save</v-btn
                  >
                </v-card>
              </v-card>
            </div>
          </a-tab-pane>
          <a-tab-pane key="7" tab="Sequence Management">
            <!-- VMDS -->
            <div v-once>{{ LoadAllTestMessageData() }}</div>
            <div v-once>{{ LoadAllSequenceData() }}</div>
            <b style="border-left: 5px solid blue" class="pl-3">Select VMD</b>
            <div class="pt-2">
              <v-autocomplete
                chips
                deletable-chips
                dense
                v-model="sequenceModal"
                :rules="[rules.required]"
                label="VMD's*"
                auto-select-first
                item-text="VMDName"
                item-value="id"
                :items="GetVMDS"
              ></v-autocomplete>

              <b style="border-left: 5px solid blue" class="pl-3"
                >Message Details</b
              >
              <v-form>
                <div
                  class="pt-2"
                  v-bind:key="i.id"
                  v-for="i in sequenceListMessage"
                >
                  <v-autocomplete
                    v-model="i.modal"
                    append-outer-icon="mdi-close-circle"
                    @click:append-outer="RemoveSequenceList(i)"
                    dense
                    :rules="[rules.required]"
                    :label="`Select Predefined Message - ${i.id}`"
                    auto-select-first
                    item-text="Message"
                    item-value="id"
                    :items="AllMessagesDataobj"
                  ></v-autocomplete>
                  <!-- <p>Text</p>  <p @click="RemoveSequenceList(i)">Remove</p> -->
                </div>
              </v-form>
              <br />
              <v-btn small outlined @click="addSequence">+ Add Message</v-btn>
              <Schedule
                class="pt-5"
                ref="Schedule_ref"
                v-if="tabs == 7"
                typemessage="Sequence"
              />
              <v-card elevation="0" class="d-flex flex-row-reverse" flat tile>
                <v-card elevation="0" class="pa-2" tile>
                  <v-btn
                    class="d-flex flex-row"
                    color="green"
                    @click="saveSequence"
                    >Save</v-btn
                  >
                </v-card>
              </v-card>
            </div>
          </a-tab-pane>
        </a-tabs>
        <!-- Tabs End -->
      </div>
    </v-app>
  </section>
</template>

<script>
// import { utility } from "../../mixins/utility";
// import VMD_List from "./VMD_List";
// import VMD_Groups_List from "./VMD_Groups_List";
// import Editor from '@baoshishu/vue-editor'
import Editor from "@/index.js";
import "@vueup/vue-quill/dist/vue-quill.snow.css";
import RegionDimension from "./RegionDimension";
import Schedule from "./Schedule";
import { MessagingMixins } from "../../mixins/MessagingMixins";
import { UsersMixins } from "../../mixins/UsersMixins";
import { VMDMixins } from "../../mixins/VMDMixins";

export default {
  mixins: [MessagingMixins, UsersMixins, VMDMixins],
  mounted() {
    this.get_VMDS();
  },
  data() {
    return {
      items: [
        {
          text: 'Dashboard',
          disabled: false,
          href: '/#/dashboard',
        },
        {
          text: 'Messaging',
          disabled: false,
        },

      ],
      tabs: "1",
      tab: null,
      sequenceModal: [],
      PredefinedModal: [],
      messagingType: null,
      SingleTextMessagedata: "",
      MultiTextMessagedata: "",
      ImageMessagedata: "",
      VideoMessagedata: "",
      dataObj: {},
      sequenceListMessage: [],
      predefinedListMessage: [{id: 1, modal: null}],
      multiDataobj: {},
      SequenceDataobj: {},
      PredefinedDataobj: {},
      AllMessagesDataobj: [],
      ImageDataobj: {},
      VideoDataobj: {},
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
        listreqired: (value) => {
          if (value.length >= 1) {
            return true;
          } else {
            return false || "Required.";
          }
        },
      },
    };
  },
  methods: {
    addSequence() {
      var len = this.sequenceListMessage.length;
      this.sequenceListMessage.push({ id: len + 1, modal: null });
    },
    RemoveSequenceList(item) {
      console.log(item);
      for (var i = 0; i < this.sequenceListMessage.length; i++) {
        if (this.sequenceListMessage[i].id === item.id) {
          this.sequenceListMessage.splice(i, 1);
        }
      }
    },
    LoadSingleLineData() {
      this.get_TextMessage(
        "?user=" + this.GetCurrentUser.id + "&type=single"
      ).then((data) => {
        if (data.data.length >= 1) {
          this.dataObj = data.data[0];
          this.SingleTextMessagedata = this.dataObj.text;
        }
      });
    },
    LoadMultiLineData() {
      this.get_TextMessage(
        "?user=" + this.GetCurrentUser.id + "&type=multi"
      ).then((data) => {
        if (data.data.length >= 1) {
          this.multiDataobj = data.data[0];
          this.MultiTextMessagedata = this.multiDataobj.text;
        }
      });
    },
    LoadAllTestMessageData() {
      this.get_TextMessage("?user=" + this.GetCurrentUser.id).then((data) => {
        if (data.data.length >= 1) {
          this.AllMessagesDataobj = data.data;
        }
      });
    },
    LoadAllSequenceData() {
      this.get_PublishManagement("?type=sequence&user=" + this.GetCurrentUser.id).then(
        (data) => {
          if (data.data.length >= 1) {
            console.log("LoadAllSequenceData");
            var loadedata = data.data[0];
            this.SequenceDataobj = loadedata;
            this.sequenceModal = loadedata.vmd;
            for (var i of loadedata.message) {
              var len = 0;
              this.sequenceListMessage.push({ id: len + 1, modal: i });
            }

            // this.AllMessagesDataobj = data.data;
          }
        }
      );
    },
    LoadAllPredefinedData() {
      this.get_PublishManagement("?type=Predefined&user=" + this.GetCurrentUser.id).then(
        (data) => {
          if (data.data.length >= 1) {
            console.log("LoadAllPredefinedData");
            var loadedata = data.data[0];
            this.PredefinedDataobj = loadedata;
            this.PredefinedModal = loadedata.vmd;
            this.predefinedListMessage = []
            for (var i of loadedata.message) {
              this.predefinedListMessage.push({ id: 1, modal: i });
            }

            // this.AllMessagesDataobj = data.data;
          }
        }
      );
    },
    LoadimageData() {
      this.get_TextMessage(
        "?user=" + this.GetCurrentUser.id + "&type=image"
      ).then((data) => {
        if (data.data.length >= 1) {
          this.ImageDataobj = data.data[0];
          this.ImageMessagedata = this.ImageDataobj.text;
        }
      });
    },
    LoadMediaData() {
      this.get_TextMessage(
        "?user=" + this.GetCurrentUser.id + "&type=video"
      ).then((data) => {
        if (data.data.length >= 1) {
          this.VideoDataobj = data.data[0];
          this.VideoMessagedata = this.VideoDataobj.text;
        }
      });
    },
    saveSingleLineMessage() {
      console.log("saveSingleLineMessage");
      this.$refs.RegionDimension_ref.validateFun();
      this.$refs.RegionDimension_ref.validateFun().then((data) => {
        console.log("One inside", data);
        console.log(this.$refs.RegionDimension_ref.dataObj);

        this.$refs.Schedule_ref.validateFun()
          .then((data1) => {
            console.log("Two inside", data1);
            console.log(this.$refs.Schedule_ref.dataObj);
            var payload = {
              text: this.SingleTextMessagedata,
              user: this.GetCurrentUser.id,
              type: "single",
              RegionDimensionAndCoOrdinates: this.$refs.RegionDimension_ref
                .dataObj.id,
              Schedule: this.$refs.Schedule_ref.dataObj.id,
            };
            console.log(payload);
            if (this.dataObj.id) {
              // Update
              payload.id = this.dataObj.id;
              this.patch_TextMessage(payload).then((data) => {
                console.log(data);
                this.$notification["success"]({
                  message: "Single Line Message",
                  description: "Single Line Message Updated",
                });
              });
            } else {
              //  Create
              this.post_TextMessage(payload).then((data) => {
                this.dataObj = data.data
                console.log(data);
                this.$notification["success"]({
                  message: "Single Line Message",
                  description: "Single Line Message Created",
                });
              });
            }
          })
          .catch((err) => {
            console.log(err);
          });
      });
    },
    saveMultiLineMessage() {
      console.log("saveMultiLineMessage");
      this.$refs.RegionDimension_ref.validateFun().then((data) => {
        console.log("One inside", data);
        console.log(this.$refs.RegionDimension_ref.dataObj);

        this.$refs.Schedule_ref.validateFun()
          .then((data1) => {
            console.log("Two inside", data1);
            console.log(this.$refs.Schedule_ref.dataObj);
            var payload = {
              text: this.MultiTextMessagedata,
              user: this.GetCurrentUser.id,
              type: "multi",
              RegionDimensionAndCoOrdinates: this.$refs.RegionDimension_ref
                .dataObj.id,
              Schedule: this.$refs.Schedule_ref.dataObj.id,
            };
            console.log(payload);
            if (this.multiDataobj.id) {
              // Update
              payload.id = this.multiDataobj.id;
              this.patch_TextMessage(payload).then((data) => {
                console.log(data);
                this.$notification["success"]({
                  message: "Multi Line Message",
                  description: "Multi Line Message Updated",
                });
              });
            } else {
              //  Create
              this.post_TextMessage(payload).then((data) => {
                console.log(data);
                this.multiDataobj = data.data
                this.$notification["success"]({
                  message: "Multi Line Message",
                  description: "Multi Line Message Updated",
                });
              });
            }
          })
          .catch((err) => {
            console.log(err);
          });
      });
    },
    saveImageMessage() {
      console.log("saveImageMessage");
      this.$refs.RegionDimension_ref.validateFun().then((data) => {
        console.log("One inside", data);
        console.log(this.$refs.RegionDimension_ref.dataObj);

        this.$refs.Schedule_ref.validateFun()
          .then((data1) => {
            console.log("Two inside", data1);
            console.log(this.$refs.Schedule_ref.dataObj);
            var payload = {
              text: this.ImageMessagedata,
              user: this.GetCurrentUser.id,
              type: "image",
              RegionDimensionAndCoOrdinates: this.$refs.RegionDimension_ref
                .dataObj.id,
              Schedule: this.$refs.Schedule_ref.dataObj.id,
            };
            console.log(payload);
            if (this.ImageDataobj.id) {
              // Update
              payload.id = this.ImageDataobj.id;
              this.patch_TextMessage(payload).then((data) => {
                console.log(data);
                this.$notification["success"]({
                  message: "Image Message",
                  description: "Image  Message Updated",
                });
              });
            } else {
              //  Create
              this.post_TextMessage(payload).then((data) => {
                this.ImageDataobj = data.data
                console.log(data);
                this.$notification["success"]({
                  message: "Image Message",
                  description: "Image Message Updated",
                });
              });
            }
          })
          .catch((err) => {
            console.log(err);
          });
      });
    },
    saveVideoMessage() {
      console.log("saveVideoMessage");
      this.$refs.RegionDimension_ref.validateFun().then((data) => {
        console.log("One inside", data);
        console.log(this.$refs.RegionDimension_ref.dataObj);

        this.$refs.Schedule_ref.validateFun()
          .then((data1) => {
            console.log("Two inside", data1);
            console.log(this.$refs.Schedule_ref.dataObj);
            var payload = {
              text: this.VideoMessagedata,
              user: this.GetCurrentUser.id,
              type: "video",
              RegionDimensionAndCoOrdinates: this.$refs.RegionDimension_ref
                .dataObj.id,
              Schedule: this.$refs.Schedule_ref.dataObj.id,
            };
            console.log(payload);
            if (this.VideoDataobj.id) {
              // Update
              payload.id = this.VideoDataobj.id;
              this.patch_TextMessage(payload).then((data) => {
                console.log(data);
                this.$notification["success"]({
                  message: "Video Message",
                  description: "Video  Message Updated",
                });
              });
            } else {
              //  Create
              this.post_TextMessage(payload).then((data) => {
                console.log(data);
                this.VideoDataobj = data.data
                this.$notification["success"]({
                  message: "Video Message",
                  description: "Video Message Updated",
                });
              });
            }
          })
          .catch((err) => {
            console.log(err);
          });
      });
    },
    PredefinedSequence(){
      console.log('called predeinfed fun')
      this.$refs.Schedule_ref.validateFun().then((data1) => {
        if (data1) {
          console.log("saveSequence Func called");
          var message = [];
          for (var i of this.predefinedListMessage) {
            message.push(i.modal);
          }
          var payload = {
            type: "Predefined",
            status: "Saved",
            vmd: this.PredefinedModal,
            Schedule: this.$refs.Schedule_ref.dataObj.id,
            user: this.GetCurrentUser.id,
            message: message,
          };
          if (this.PredefinedDataobj.id) {
            payload.id = this.PredefinedDataobj.id;

            this.patch_PublishManagement(payload).then((data) => {
              console.log(data);
              this.$notification["success"]({
                  message: "Predefined Message",
                  description: "Predefined Message Updated",
                });
            });
          } else {
            this.post_PublishManagement(payload).then((data) => {
              console.log(data);
              this.$notification["success"]({
                  message: "Predefined Message",
                  description: "Predefined Message Updated",
                });
            });
          }
        }
      });
    },
    saveSequence() {
      this.$refs.Schedule_ref.validateFun().then((data1) => {
        if (data1) {
          console.log("saveSequence Func called");
          console.log(this.sequenceModal);
          console.log(this.sequenceListMessage);
          var message = [];
          for (var i of this.sequenceListMessage) {
            message.push(i.modal);
          }
          var payload = {
            type: "Sequence",
            status: "Saved",
            vmd: this.sequenceModal,
            Schedule: this.$refs.Schedule_ref.dataObj.id,
            user: this.GetCurrentUser.id,
            message: message,
          };
          if (this.SequenceDataobj.id) {
            payload.id = this.SequenceDataobj.id;

            this.patch_PublishManagement(payload).then((data) => {
              console.log(data);
              this.$notification["success"]({
                  message: "Sequence Message",
                  description: "Sequence Message Updated",
                });
            });
          } else {
            this.post_PublishManagement(payload).then((data) => {
              console.log(data);
              this.$notification["success"]({
                  message: "Sequence Message",
                  description: "Sequence Message Updated",
                });
            });
          }
        }
      });
    },
  },
  components: {
    Editor,
    RegionDimension,
    Schedule,
    // QuillEditor
    // VMD_List,
    // VMD_Groups_List
  },
};
</script>