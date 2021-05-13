<template>
  <div>
    <v-breadcrumbs :items="items"></v-breadcrumbs>
    <div v-once v-if="GetCurrentUser && GetCurrentUser.id">
      {{ LoadAllTestMessageData() }}
            {{ LoadSequenceList() }}

    </div>

    <a-tabs class="ma-2" default-active-key="1" >
      <a-tab-pane key="1" tab="Schedule List">
        <v-data-table
        :items="AllSequenceMessage"
        :headers="[
        {text: '#Id', value: 'id'},
        {text: 'Start Date', value: 'StartDate'},
        {text: 'Endt Date', value: 'EndDate'},
        {text: 'Start Time', value: 'StartTime'},
        {text: 'End Time', value: 'EndTime'},
        {text: 'Target VMD/Group', value: 'vmdlist'},
        {text: 'Playlist', value: 'playlistData'},
        {text: 'Acton', value: 'action'},
        ]"
        >
<template v-slot:item.vmdlist="{ item }" >
              <template v-if="item.vmd_list.length >=1">   <a-tag v-for="k in item.vmd_list" v-bind:key="k.id"><a :href="`/#/VmdInfo/${k.id}`">{{k.VMDName}}</a></a-tag></template>
          <template v-if="item.vmdGroups_list.length >=1"> <a-tag v-for="k in item.vmdGroups_list" v-bind:key="k.id">{{k.GroupName}}</a-tag></template>
    </template>
    
<template v-slot:item.playlistData="{ item }" >
              <a :href="`/#/playlist?playlist=${item.playlistData[0].playlistname}`">{{item.playlistData[0].playlistname}}</a>
    </template>
<template v-slot:item.action="{ item }" >
  <a-button @click="deleteRecord(item)">Delete</a-button>
    </template>

        </v-data-table>
      </a-tab-pane>
      <a-tab-pane key="2" tab="Setup New Schedule" force-render>
        <v-card>
      <v-card-text>
        <!-- VMD Selection -->
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
              :rules="[rules.required]"
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
              :rules="[rules.required]"
              dense
              label="VMD Group*"
              auto-select-first
              item-text="GroupName"
              item-value="id"
              :items="GetVMDGroups"
            ></v-autocomplete>
          </v-col>
        </v-row>

        <v-row>
          <v-col cols="12" sm="6">
            <h3 style="border-left: 5px solid #394a59" class="mt-3 pl-3">
              Playlist Detials
            </h3>
            <v-form ref="sequenceModal">
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
                  return-object
                  :rules="[rules.required]"
                  :label="`Select Playlist`"
                  auto-select-first
                  item-text="playlistname"
                  item-value="id"
                  :items="AllMessagesDataobj"
                ></v-autocomplete>
                <!-- <p>Text</p>  <p @click="RemoveSequenceList(i)">Remove</p> -->
              </div>
              <!-- <v-btn small outlined @click="addSequence">+ Add Playlist</v-btn> -->
            </v-form>
          </v-col>
          <v-col cols="12" sm="6">
            <h3 style="border-left: 5px solid #394a59" class="mt-3 pl-3">
              Message Preview
            </h3>
            <!-- <b>{{sequenceListMessage}}</b> -->

            <div v-bind:key="i.id" v-for="i in sequenceListMessage">
              <center>
                <template v-if="i && i.modal">
                  <iframe
                    v-if="i.modal.type == 'Single'"
                    class="ml-2"
                    :style="`background-color:${i.modal.BackGroundColor};border: 4px solid ${i.modal.BorderLine}`"
                    :srcdoc="i.modal.singleLineMessage"
                    :height="i.modal.Height"
                    :width="i.modal.Width"
                    title="Iframe Example"
                  >
                  </iframe>
                  <iframe
                    v-else-if="i.modal.type == 'Multi'"
                    class="ml-2"
                    :style="`background-color:${i.modal.BackGroundColor};border: 4px solid ${i.modal.BorderLine}`"
                    :srcdoc="i.modal.multilineMessage"
                    :height="i.modal.Height"
                    :width="i.modal.Width"
                    title="Iframe Example"
                  >
                  </iframe>
                  <img
                    v-else-if="i.modal.type == 'Image'"
                    :src="i.modal.imageMessage"
                    alt=""
                  />
                  <video
                    width="400"
                    v-else-if="i.modal.type == 'Video'"
                    controls
                  >
                    <source :src="i.modal.videoMessage" type="video/mp4" />
                    Your browser does not support HTML video.
                  </video>
                </template>
              </center>
            </div>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <ScheduleForm :loaddata="false" ref="ScheduleForm_ref" />
          </v-col>
        </v-row>
      </v-card-text>
      <v-divider></v-divider>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="success" outlined depressed @click="sendMesage">
          Send <v-icon color="success">mdi-send-circle</v-icon>
        </v-btn>
      </v-card-actions>
    </v-card>
      </a-tab-pane>
      
    </a-tabs>

    
  </div>
</template>

<script>
import { MessagingMixins } from "../../mixins/MessagingMixins";
import { UsersMixins } from "../../mixins/UsersMixins";
import { VMDMixins } from "../../mixins/VMDMixins";
import ScheduleForm from "./ScheduleForm";

export default {
  mixins: [MessagingMixins, UsersMixins, VMDMixins],
  mounted() {
    this.get_VMDS();
    this.get_VMDSGroups();
  },
  components: { ScheduleForm },
  methods: {
    LoadSequenceList() {
            this.AllSequenceMessage = []

      this.get_PublishManagement("?ordering=-id&type=Schedule&user=" + this.GetCurrentUser.id).then((data) => {
        if (data.data.length >= 1) {
          this.AllSequenceMessage = data.data;
        }
      });
    },
    deleteRecord(payload){
      this.delete_PublishManagement(payload)
      this.$notification["success"]({
            message: "Schedule Message Deleted successfully",
            // description: "Predefined Message Updated",
          });
      this.LoadSequenceList()
    },
    sendMesage() {
      this.$refs.sequenceModal.validate();
      this.$refs.ScheduleForm_ref.validateFun().then(() => {
        if (
          this.$refs.sequenceModal.validate() &&
          this.sequenceListMessage.length >= 1 &&
          this.vmd_or_Group.length >= 1
        ) {
          var payload = {
            "StartDate": this.$refs.ScheduleForm_ref.dataObj.StartDate,
            "EndDate": this.$refs.ScheduleForm_ref.dataObj.EndDate,
            "StartTime": this.$refs.ScheduleForm_ref.dataObj.StartTime,
            "EndTime": this.$refs.ScheduleForm_ref.dataObj.EndTime,
            "type": "Schedule",
            "status": "Active",
            "user": this.GetCurrentUser.id,
            "vmd": [],
            "vmdGroups": [],
            "playlist": []
        }
        if (this.VmDSelectionValue == 'VMD'){payload.vmd = this.vmd_or_Group}
        if (this.VmDSelectionValue == 'VMDGroup'){payload.vmdGroups = this.vmd_or_Group}
        for (var i of this.sequenceListMessage){
            payload.playlist.push(i.modal.id)
        }
                console.log(payload)

        this.post_PublishManagement(payload)
        .then(data => {
          console.log(data)
        })

          this.$notification["success"]({
            message: "Sequence Message Send successfully",
            // description: "Predefined Message Updated",
          });
        } else {
          this.$notification["warn"]({
            message: "Please fill all the required field",
            // description: "Predefined Message Updated",
          });
        }
      });
    },
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
    LoadAllTestMessageData() {
      this.get_Playlist("?user=" + this.GetCurrentUser.id).then((data) => {
        if (data.data.length >= 1) {
          this.AllMessagesDataobj = data.data;
        }
      });
    },
  },
  data() {
    return {
      AllMessagesDataobj: [],
      AllSequenceMessage: [],
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
      sequenceListMessage: [{ id: 1, modal: null }],

      VmDSelectionValue: "VMD",
      vmd_or_Group: [],
      items: [
        {
          text: "Dashboard",
          disabled: false,
          href: "/#/dashboard",
        },
        {
          text: "Messaging",
          disabled: false,
          href: "/#/SendMessage",
        },
        {
          text: "Schedule Message",
          disabled: false,
        },
      ],
    };
  },
};
</script>