<template>
  <div>
    <v-breadcrumbs :items="items"></v-breadcrumbs>
    <div v-once v-if="GetCurrentUser && GetCurrentUser.id">
      {{ LoadAllTestMessageData() }}
      {{ LoadSequenceList() }}
    </div>
     <a-tabs class="ma-2" default-active-key="1" >
      <a-tab-pane key="1" tab="Sequence List">
        <a-timeline>
          <a-timeline-item v-for="j in AllSequenceMessage" v-bind:key="j.id">
            Create at {{ j.createdDateFormat }}
          <br />
          
          <template v-if="j.vmd_list.length >=1">  Target VMD : <a-tag v-for="k in j.vmd_list" v-bind:key="k.id"><a :href="`/#/VmdInfo/${k.id}`">{{k.VMDName}}</a></a-tag></template>
          <template v-if="j.vmdGroups_list.length >=1">Target VMD Group: <a-tag v-for="k in j.vmdGroups_list" v-bind:key="k.id">{{k.GroupName}}</a-tag></template>
          <a-timeline-item class="mt-2" v-bind:key="i.id" v-for="i in j.playlistData">
           Playlist Name :
          <b><v-chip>{{ i.playlistname }}</v-chip></b>
          <br />
          <h3 style="border-left: 5px solid #394a59" class="mt-3 pl-3">
            Message Type :
            {{
              ["Single", "Multi"].includes(i.type)
                ? i.type + " Line Message"
                : "Media Message"
            }}
          </h3>
          <a-collapse accordion>
            <a-collapse-panel key="1" header="Message Detail">
              <v-card>
                <v-card-text>
                  <v-window >
                    <v-window-item :value="1">
                      <h3 style="border-left: 5px solid #394a59" class="pl-3">
                        Region Dimension and Co-Ordinates
                      </h3>
                      <v-row class="ml-2">
                        <v-col>
                          <v-text-field
                            readonly
                            v-model="i.XCoOrdinates"
                            dense
                            label="X Co-Ordinates "
                          ></v-text-field>
                        </v-col>
                        <v-col>
                          <v-text-field
                            readonly
                            v-model="i.YCoOrdinates"
                            dense
                            label="Y Co-Ordinates "
                          ></v-text-field>
                        </v-col>
                        <v-col>
                          <v-text-field
                            readonly
                            v-model="i.Width"
                            dense
                            label="Width "
                          ></v-text-field>
                        </v-col>
                        <v-col>
                          <v-text-field
                            readonly
                            v-model="i.Height"
                            dense
                            label="Height "
                          ></v-text-field>
                        </v-col>
                      </v-row>
                      <v-row class="ml-2">
                        <v-col>
                          <v-text-field
                            readonly
                            v-model="i.BorderLine"
                            dense
                            label="Border Line "
                          ></v-text-field>
                        </v-col>
                        <v-col>
                          <v-text-field
                            readonly
                            v-model="i.BorderLine"
                            dense
                            label="Back Ground Color "
                          ></v-text-field>
                        </v-col>
                      </v-row>
                      <h3
                        style="border-left: 5px solid #394a59"
                        class="mt-3 pl-3"
                      >
                        Message Preview
                      </h3>
                      <iframe
                        v-if="i.type == 'Single'"
                        class="ml-2"
                        :style="`background-color:${i.BackGroundColor};border: 4px solid ${i.BorderLine}`"
                        :srcdoc="i.singleLineMessage"
                        :height="i.Height"
                        :width="i.Width"
                        title="Iframe Example"
                      >
                      </iframe>
                      <iframe
                        v-else-if="i.type == 'Multi'"
                        class="ml-2"
                        :style="`background-color:${i.BackGroundColor};border: 4px solid ${i.BorderLine}`"
                        :srcdoc="i.multilineMessage"
                        :height="i.Height"
                        :width="i.Width"
                        title="Iframe Example"
                      >
                      </iframe>
                      <img   v-else-if="i.type == 'Image'"  :src="i.imageMessage" alt="">
                      <video width="400" v-else-if="i.type == 'Video'" controls>
                        <source :src="i.videoMessage" type="video/mp4">
                        Your browser does not support HTML video.
                      </video>

                      
                    </v-window-item>
                    <v-window-item :value="2">
          <a-result status="success" title="Successfully Message Send to VMD">
            <template #extra>
              
              <!-- <a-button key="buy">
                Buy Again
              </a-button> -->
            </template>
          </a-result>
        </v-window-item>

                  </v-window>
                </v-card-text>
                
              </v-card>
            </a-collapse-panel>
          </a-collapse>
          </a-timeline-item>
          </a-timeline-item>
        </a-timeline>
      </a-tab-pane>
      <a-tab-pane key="2" tab="New Sequence Message" force-render>
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
                  :label="`Select Sequence Message - ${i.id}`"
                  auto-select-first
                  item-text="playlistname"
                  item-value="id"
                  :items="AllMessagesDataobj"
                ></v-autocomplete>
                <!-- <p>Text</p>  <p @click="RemoveSequenceList(i)">Remove</p> -->
              </div>
              <v-btn small outlined @click="addSequence">+ Add Playlist</v-btn>
            </v-form>
          </v-col>
          <v-col cols="12" sm="6">
            <h3 style="border-left: 5px solid #394a59" class="mt-3 pl-3">
              Message Preview
            </h3>
            <!-- <b>{{sequenceListMessage}}</b> -->
            <v-simple-table       :height="300">
                  <template v-slot:default>
            <div v-bind:key="i.id" v-for="i in sequenceListMessage">
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
            </div>
            </template>
                </v-simple-table>
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
export default {
  mixins: [MessagingMixins, UsersMixins, VMDMixins],
  mounted() {
    this.get_VMDS();
    this.get_VMDSGroups();
  },
  methods: {
    sendMesage() {
      if (
        this.$refs.sequenceModal.validate() &&
        this.sequenceListMessage.length >= 1 &&
        this.vmd_or_Group.length >= 1
      ) {
        var payload = {
            "StartDate": null,
            "StartTime": null,
            "Duration": "",
            "RepeatCount": null,
            "type": "Sequence",
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
    LoadSequenceList() {
      this.get_PublishManagement("?ordering=-id&type=Sequence&user=" + this.GetCurrentUser.id).then((data) => {
        if (data.data.length >= 1) {
          this.AllSequenceMessage = data.data;
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
      sequenceListMessage: [],

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
          text: "Sequence  Message",
          disabled: false,
        },
      ],
    };
  },
};
</script>