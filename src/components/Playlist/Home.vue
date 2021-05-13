<template>
  <div>
    <v-breadcrumbs :items="items"></v-breadcrumbs>
    <div>
      <v-overlay :value="overlayMain">
        <div class="text-center">
          <v-progress-circular
            indeterminate
            color="primary"
          ></v-progress-circular>
          Searching
        </div>
      </v-overlay>
      <div v-once v-if="GetCurrentUser && GetCurrentUser.id">
        {{ GetPlaylist() }}
      </div>
      <div v-once v-if="GetCurrentUser && GetCurrentUser.id">
        {{ getQueryData() }}
      </div>
      <a-input-search
        style="width: 300px"
        class="ml-6"
        placeholder="Search Playlist OR Message Text"
        v-model="seachtext"
        enter-button
        @search="onSearch"
      />

      <a-timeline class="pt-5">
        <a-timeline-item v-bind:key="i.id" v-for="i in Playlist">
          Create at {{ i.createdDateFormat }} Playlist Name :
          <b><v-chip>{{ i.playlistname }}</v-chip></b>
          <br />
          <h3 style="border-left: 5px solid #394a59" class="mt-3 pl-3">
            Message Type :
            <template v-if="['Single', 'Multi'].includes(i.type)">{{i.type + " Line Message"}}</template>
            <template v-else-if="['Image', 'Video'].includes(i.type)">{{i.type + " Media Message"}}</template>
            <template v-else>{{i.type + " Message"}}</template>
            
          </h3>
          <a-collapse accordion >
            <a-collapse-panel key="1" header="Message Detail">
              <v-card>
                <v-card-text>
                  <v-window v-model="step">
                    <v-window-item :value="1">
                      <h3 v-if="i.type != 'Combine'" style="border-left: 5px solid #394a59" class="pl-3">
                        Region Dimension and Co-Ordinates
                      </h3>
                      <v-row v-if="i.type != 'Combine'" class="ml-2">
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
                      <v-row v-if="i.type != 'Combine'" class="ml-2">
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
                      <CombinationalPreview v-else-if="i.type == 'Combine'"  :PreviewData="i.CombineMessageData" />


                      <!-- VMD Selection -->
                      <h3
                        style="border-left: 5px solid #394a59"
                        class="mt-3 pl-3"
                      >
                        VMD/VMD Group Selection
                      </h3>
                      <br />
                      <a-radio-group class="ml-3" v-model="VmDSelectionValue">
                        <a-radio-button value="VMD" @click="vmd_or_Group = []">
                          VMD
                        </a-radio-button>
                        <a-radio-button
                          value="VMDGroup"
                          @click="vmd_or_Group = []"
                        >
                          VMD Group
                        </a-radio-button>
                      </a-radio-group>
                      <v-row class="pa-2">
                        <v-col
                          cols="12"
                          sm="6"
                          v-if="VmDSelectionValue == 'VMD'"
                        >
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
                <v-card-actions>
                  <v-btn text v-if="step == 2" @click="step--" outlined>
                    Back
                  </v-btn>
                  <v-spacer></v-spacer>
                  <v-btn
                    v-if="step != 2"
                    color="success"
                    outlined
                    depressed
                    :disabled="!vmd_or_Group.length >= 1"
                    @click="step++"
                  >
                    Send <v-icon color="success">mdi-send-circle</v-icon>
                  </v-btn>
                </v-card-actions>
              </v-card>
            </a-collapse-panel>
          </a-collapse>
          <!-- <template v-else>
            No Preview Available for Combine Message
          </template> -->
        </a-timeline-item>
      </a-timeline>
    </div>
  </div>
</template>

<script>
import { MessagingMixins } from "../../mixins/MessagingMixins";
import { UsersMixins } from "../../mixins/UsersMixins";
import { VMDMixins } from "../../mixins/VMDMixins";
import CombinationalPreview from "../Messaging/CombinationalPreview";

export default {
  mixins: [MessagingMixins, UsersMixins, VMDMixins],
  components: {CombinationalPreview},
  data() {
    return {
      vmd_or_Group: [],
      VmDSelectionValue: "VMD",
      step: 1,
      overlayMain: false,
      Playlist: [],
      seachtext: "",
      items: [
        {
          text: "Dashboard",
          disabled: false,
          href: "/#/dashboard",
        },
        {
          text: "Playlist",
          disabled: false,
        },
      ],
    };
  },
  mounted() {
    this.get_VMDS();
    this.get_VMDSGroups();

    
  },
  methods: {
    getQueryData(){
      if(this.$route.query.playlist){
      this.seachtext = this.$route.query.playlist
      this.onSearch()
    }
    },
    onSearch() {
      console.log("Searched called");
      this.Searchlist();
    },
    GetPlaylist() {
      this.get_Playlist("?ordering=-id&user=" + this.GetCurrentUser.id).then(
        (data) => {
          this.Playlist = data.data;
        }
      );
    },
    Searchlist() {
      this.overlayMain = true;
      this.get_Playlist(
        "?&user=" + this.GetCurrentUser.id + "&search=" + this.seachtext
      )
        .then((data) => {
          this.overlayMain = false;

          this.Playlist = data.data;
        })
        .catch(() => {
          this.overlayMain = false;
        });
    },
  },
};
</script>