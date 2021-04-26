<template>
  <section >
    <!--overview start-->
             <v-breadcrumbs :items="items"></v-breadcrumbs>

    <v-app>
      <div class="pa-2">
        <!-- Tabs -->
        <a-tabs v-model="tabs" default-active-key="6">

          <!-- <a-tab-pane key="5" tab="Combinational Message ">
            Content of Tab Pane 3
          </a-tab-pane> -->
          <a-tab-pane key="6" tab="Predefined Message">
            <!-- VMDS -->
            <div v-once>{{ LoadAllTestMessageData() }}</div>
            <div v-once>{{ LoadAllPredefinedData() }}</div>
            <h3 style="border-left: 5px solid #394a59" class="pl-3">Select VMD</h3>
            <div class="pt-2">
              <v-autocomplete
                chips
                deletable-chips
                dense
                multiple
                v-model="PredefinedModal"
                :rules="[rules.required]"
                label="VMD's*"
                auto-select-first
                item-text="VMDName"
                item-value="id"
                :items="GetVMDS"
              ></v-autocomplete>
            <h3 style="border-left: 5px solid #394a59" class="pl-3">Select VMD Groups</h3>
              <v-autocomplete
              class="pt-2"
                chips
                deletable-chips
                dense
                multiple
                v-model="PredefinedVMDGroupModal"
                :rules="[rules.required]"
                label="VMD Group"
                auto-select-first
                item-text="GroupName"
                item-value="id"
                :items="GetVMDGroups"
              ></v-autocomplete>

              <h3 style="border-left: 5px solid #394a59" class="pl-3"
                >Message Details</h3
              >
              <v-form>
                <v-text-field v-model="predefinesinglelineMessage" label="Single Line Message"></v-text-field>
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
// import Editor from "@/index.js";
import "@vueup/vue-quill/dist/vue-quill.snow.css";
// import RegionDimension from "./RegionDimension";
import Schedule from "./Schedule";
import { MessagingMixins } from "../../mixins/MessagingMixins";
import { UsersMixins } from "../../mixins/UsersMixins";
import { VMDMixins } from "../../mixins/VMDMixins";

export default {
  mixins: [MessagingMixins, UsersMixins, VMDMixins],
  mounted() {
    this.get_VMDS();
    this.get_VMDSGroups()
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
          href: '/#/SendMessage',
        },
        {
          text: 'Predefined  Message',
          disabled: false,
        },

      ],
      tabs: "6",
      tab: null,
      sequenceModal: [],
      PredefinedModal: [],
      PredefinedVMDGroupModal: [],
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
      predefinesinglelineMessage: '',
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
    LoadAllPredefinedData() {
      this.get_PublishManagement("?type=Predefined&user=" + this.GetCurrentUser.id).then(
        (data) => {
          if (data.data.length >= 1) {
            console.log("LoadAllPredefinedData");
            var loadedata = data.data[0];
            this.PredefinedDataobj = loadedata;
            this.predefinesinglelineMessage = loadedata.message
            this.PredefinedModal = loadedata.vmd;
            this.PredefinedVMDGroupModal = loadedata.vmdGroups;
            

            // this.AllMessagesDataobj = data.data;
          }
        }
      );
    },

    PredefinedSequence(){
      console.log('called predeinfed fun')
      this.$refs.Schedule_ref.validateFun().then((data1) => {
        if (data1) {
          console.log("saveSequence Func called");
          var payload = {
            type: "Predefined",
            status: "Saved",
            vmd: this.PredefinedModal,
            vmdGroups: this.PredefinedVMDGroupModal,
            Schedule: this.$refs.Schedule_ref.dataObj.id,
            user: this.GetCurrentUser.id,
            message: this.predefinesinglelineMessage,
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
    // Editor,
    // RegionDimension,
    Schedule,
    // QuillEditor
    // VMD_List,
    // VMD_Groups_List
  },
};
</script>