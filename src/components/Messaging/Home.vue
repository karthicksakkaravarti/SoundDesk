<template>
  <div class="pa-1">
    <v-breadcrumbs :items="items"></v-breadcrumbs>

    <b style="border-left: 5px solid #394a59" class="pl-3">Avialable VMD's</b>
    <v-btn x-small outlined @click="routing('predefined')" class="ml-3">Set Predefined Messages</v-btn>
    <div class="pa-2">
      <v-row>
        <v-col cols="12" sm="4" v-bind:key="i.id" v-for="i in GetVMDS">
          <v-hover v-slot:default="{ hover }">
            <v-card elevation="5" hover>
              <v-card-title> {{ i.VMDName }} </v-card-title>
              <v-card-subtitle>
                Status : <a-tag color="green">{{ i.VMDStatus }}</a-tag>
              </v-card-subtitle>
              <v-divider></v-divider>
              <v-card-text class="fixedheigh">
                <v-expand-transition>
                  <v-overlay :absolute="true" :value="hover">
                    <v-row>
                      <center>
                        <v-col class="mr-15" cols="12" sm="6">
                          <a-tooltip placement="top">
                            <template slot="title">
                              Single Line Message
                            </template>
                            <v-btn
                              color="#394a59"
                              @click="
                                dialog = true;
                                messageType = 'Single Line Message';
                                selectedVmd = i;
                              "
                              small
                              >Single Line Message</v-btn
                            >
                          </a-tooltip>
                        </v-col>
                        <v-col class="mr-15" cols="12" sm="6">
                          <a-tooltip placement="top">
                            <template slot="title">
                              Multi Line Message
                            </template>
                            <v-btn
                              color="#394a59"
                              small
                              @click="
                                dialog = true;
                                messageType = 'Multi Line Message';
                                selectedVmd = i;
                              "
                              >Multi Line Message</v-btn
                            >
                          </a-tooltip>
                        </v-col>
                        <v-col class="mr-15" cols="12" sm="6">
                          <a-tooltip placement="top">
                            <template slot="title"> Image Message </template>
                            <v-btn
                              color="#394a59"
                              small
                              @click="
                                dialog = true;
                                messageType = 'Image Message';
                                selectedVmd = i;
                              "
                              >Image Message</v-btn
                            >
                          </a-tooltip>
                        </v-col>
                        <v-col class="mr-15" cols="12" sm="6">
                          <a-tooltip placement="top">
                            <template slot="title"> Video Message </template>
                            <v-btn
                              color="#394a59"
                              small
                              @click="
                                dialog = true;
                                messageType = 'Video Message';
                                selectedVmd = i;
                              "
                              >Video Message</v-btn
                            >
                          </a-tooltip>
                        </v-col>
                      </center>
                    </v-row>
                  </v-overlay>
                </v-expand-transition>
                <ul>
                  <li>
                    Location : <b>{{ i.VMDLocation }}</b>
                  </li>
                  <li>
                    Latitude : <b>{{ i.VMDLatitude }}</b>
                  </li>
                  <li>
                    Longitude : <b>{{ i.VMDLongitude }}</b>
                  </li>
                  <li>
                    IPAddress : <b>{{ i.VMDIPAddress }}</b>
                  </li>
                  <li>
                    Port : <b>{{ i.VMDPort }}</b>
                  </li>
                  <li>
                    ResolutionHeight : <b>{{ i.VMDResolutionHeight }}</b>
                  </li>
                  <li>
                    Resolutionwidth : <b>{{ i.VMDResolutionwidth }}</b>
                  </li>
                  <li>
                    Brightness : <b>{{ i.VMDBrightness }}</b>
                  </li>
                </ul>
              </v-card-text>
              <v-card-actions> </v-card-actions>
            </v-card>
          </v-hover>
        </v-col>
      </v-row>

      <!-- Dialog -->
      <v-row justify="center">
        <v-dialog v-model="dialog" scrollable max-width="900px">
          <v-card>
            <v-card-title
              >{{ messageType }} to
              <a-tag v-if="selectedVmd" class="ml-2"
                >{{ selectedVmd.VMDName }}({{
                  selectedVmd.VMDResolutionHeight
                }}x{{ selectedVmd.VMDResolutionwidth }})</a-tag
              ></v-card-title
            >
            <v-divider></v-divider>
            <v-card-text style="height: 300px">
              <RegionDimension
                v-if="dialog"
                ref="RegionDimension_ref"
                :loaddata="false"
              ></RegionDimension>
              <h3 style="border-left: 5px solid #394a59" class="pl-3">
                Message Details
              </h3>
              <v-form ref="messageForm" v-if="dialog">
                <template v-if="messageType === 'Single Line Message'">
                  <v-text-field
                    :rules="[rules.required]"
                    outlined
                    label="Single Line Message"
                  ></v-text-field>
                </template>
                <template v-else-if="messageType === 'Multi Line Message'">
                  <v-textarea
                    outlined
                    :rules="[rules.required]"
                    rows="2"
                    label="Multi Line Message"
                  ></v-textarea>
                </template>
                <template v-else-if="messageType === 'Image Message'">
                  <v-file-input
                    :rules="[rules.required]"
                    label="Upload Image"
                  ></v-file-input>
                </template>
                <template v-else-if="messageType === 'Video Message'">
                  <v-file-input
                    :rules="[rules.required]"
                    label="Upload Video"
                  ></v-file-input>
                </template>
              </v-form>
            </v-card-text>
            <v-divider></v-divider>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                color="blue darken-1"
                text
                @click="
                  dialog = false;
                  selectedVmd = null;
                "
                >Close</v-btn
              >
              <v-btn color="success" @click="SendMessage">Send</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-dialog v-model="dialog1" scrollable max-width="900px">
          <v-card>
            <v-card-title
              >{{ messageType }}</v-card-title
            >
            <v-divider></v-divider>
            <v-card-text style="height: 300px">
              <RegionDimension
                v-if="dialog1"
                ref="RegionDimension_ref"
              ></RegionDimension>
              <h3 style="border-left: 5px solid #394a59" class="pl-3">
                Message Details
              </h3>
                          </v-card-text>
            <v-divider></v-divider>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                color="blue darken-1"
                text
                @click="
                  dialog = false;
                  selectedVmd = null;
                "
                >Close</v-btn
              >
              <v-btn color="success" @click="SendMessage">Send</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-row>
    </div>
  </div>
</template>
<script>
import { VMDMixins } from "../../mixins/VMDMixins";
import { utility } from "../../mixins/utility";
import RegionDimension from "./RegionDimension";

export default {
  components: {
    RegionDimension,
  },
  mixins: [VMDMixins, utility],
  mounted() {
    this.get_VMDS();
  },
  methods: {
    SendMessage() {
      this.$refs.RegionDimension_ref.validateFun().then((data) => {
        console.log(data);
        this.$refs.messageForm.validate();
      });
    },
  },
  data() {
    return {
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
