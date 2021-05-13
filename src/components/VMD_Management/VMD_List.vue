<template>
  <div>
    <v-row justify="center" class="mt-2 mr-2">
      <v-dialog scrollable v-model="dialog" persistent max-width="600px">
        <template v-slot:activator="{}">
          <v-spacer></v-spacer>
          <v-btn small outlined color="primary" dark @click="openModal">
            Add New VMD
          </v-btn>
        </template>
        <v-card :disabled="userformloader">
          <v-card-title>
            <span class="headline">{{ !isEdit ? "Add VMD" : "Edit VMD" }}</span>
          </v-card-title>
          <v-divider></v-divider>
          <v-card-text style="height: 400px">
            <!-- <v-container> -->
            <v-alert dense v-if="userError" outlined type="error">
              {{ userError }}
            </v-alert>
            <v-form ref="userfrom" v-model="formmodal">
              <v-row>
                <v-col cols="12" sm="6">
                  <v-text-field
                    v-model="VMDObj.VMDName"
                    :rules="[rules.required]"
                    label="VMD Name*"
                    required
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="6">
                  <v-text-field
                    v-model="VMDObj.VMDLocation"
                    :rules="[rules.required]"
                    label="VMD Location*"
                    required
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="6">
                  <v-text-field
                    v-model="VMDObj.VMDLatitude"
                    :rules="[rules.required]"
                    label="VMD Latitude*"
                    required
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="6">
                  <v-text-field
                    v-model="VMDObj.VMDLongitude"
                    :rules="[rules.required]"
                    label="VMD Longitude*"
                    required
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="6">
                  <v-text-field
                    v-model="VMDObj.VMDIPAddress"
                    :rules="[rules.required]"
                    label="VMD IP Address*"
                    required
                  ></v-text-field>
                </v-col>
                <!-- <v-col cols="12" sm="6">
                  <v-text-field
                    v-model="VMDObj.VMDPort"
                    :rules="[rules.required]"
                    label="VMD Port*"
                    required
                  ></v-text-field>
                </v-col> -->
                <v-col cols="12" sm="6">
                  <v-text-field
                    v-model="VMDObj.VMDResolutionHeight"
                    :rules="[rules.required]"
                    label="VMD Resolution Height*"
                    required
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="6">
                  <v-text-field
                    v-model="VMDObj.VMDResolutionwidth"
                    :rules="[rules.required]"
                    label="VMD Resolution width*"
                    required
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="6">
                  <v-autocomplete
                    v-model="VMDObj.VMDStatus"
                    label="VMD Status"
                    auto-select-first
                    :items="['Active',  'InActive']"
                  ></v-autocomplete>
                </v-col>
                <v-col cols="12" sm="6" class="pt-0">
                  <v-subheader>VMD Brightness</v-subheader>

                  <v-slider
                    v-model="VMDObj.VMDBrightness"
                    hide-details
                    thumb-label
                    color="yellow"
                    prepend-icon="mdi-brightness-5"
                  ></v-slider>
                  <a-switch size="small" /> Automatic adjust brightness
                </v-col>
                <v-col cols="12" sm="6">
                  <v-autocomplete
                    v-model="VMDObj.AssigneUser"
                    label="Assigne User"
                    auto-select-first
                    item-text="username"
                    item-value="username"
                    :items="UsersListActaul"
                  ></v-autocomplete>
                </v-col>
              </v-row>
            </v-form>
            <!-- </v-container> -->
            <small>*indicates required field</small>
          </v-card-text>
          <v-divider></v-divider>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" text @click="closeModal">Close</v-btn>
            <v-btn
              v-if="isEdit"
              color="primary"
              @click="UpdateVMD"
              :loading="userformloader"
              >Update VMD</v-btn
            >
            <v-btn
              v-else
              color="primary"
              @click="AddVMD"
              :loading="userformloader"
              >Add VMD</v-btn
            >
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-row>

    <v-data-table
    class="mt-4"
      :loading="loading"
      :items="UsersList"
      loading-text="Loading... Please wait"
      :headers="header"
    >
      <template class="pt-4" v-slot:progress>
        <div class="text-center">
          <v-progress-circular
            class="pt-4"
            indeterminate
            color="primary"
          ></v-progress-circular>
        </div>
      </template>
      <template v-slot:item.actions="{ item }">
        <v-icon small class="mr-2" @click="editItem(item)"> mdi-pencil </v-icon>
        <a-popconfirm
          :title="`Are you sure delete this ${item.VMDName}?`"
          ok-text="Yes"
          cancel-text="No"
          @confirm="deleteItem(item)"
        >
          <v-icon small> mdi-delete </v-icon>
        </a-popconfirm>
      </template>
    </v-data-table>
  </div>
</template>

<script>
import { VMDMixins } from "../../mixins/VMDMixins";
import { UsersMixins } from "../../mixins/UsersMixins";

export default {
  mixins: [VMDMixins, UsersMixins],
  data() {
    return {
      header: [
        { text: "#", value: "id" },
        { text: "Name", value: "VMDName" },
        { text: "Location", value: "VMDLocation" },
        { text: "Latitude", value: "VMDLatitude" },
        { text: "Longitude", value: "VMDLongitude" },
        { text: "IPAddress", value: "VMDIPAddress" },
        { text: "width", value: "VMDResolutionwidth" },
        { text: "Height", value: "VMDResolutionHeight" },
        { text: "Action", value: "actions" },
      ],
      loading: false,
      userformloader: false,
      UsersList: [],
      UsersListActaul: [],
      
      dialogm1: "",
      dialog: false,
      formmodal: false,
      userError: null,
      isEdit: false,
      VMDObj: {
        VMDName: "",
        VMDLocation: "",
        VMDLatitude: "",
        VMDLongitude: "",
        VMDIPAddress: "",
        VMDPort: null,
        VMDResolutionHeight: null,
        VMDResolutionwidth: null,
        VMDStatus: "",
        VMDBrightness: null,
        AssigneUser: "",
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
      },
    };
  },
  mounted() {
    console.log("Mounted called");
    this.getUsersList();
    this.getUsers1List();
  },
  computed: {
    progress() {
      try {
        return Math.min(100, this.userObj.password.length * 10);
      } catch (err) {
        return 0;
      }
    },
    color() {
      try {
        return ["error", "warning", "success"][Math.floor(this.progress / 40)];
      } catch (err) {
        return [];
      }
    },
  },
  methods: {
    editItem(item) {
      this.isEdit = true;
      this.VMDObj = Object.assign({}, item);
      this.dialog = true;
    },
    deleteItem(item) {
      this.delete_VMDS(item).then((data) => {
        console.log(data);
        this.getUsersList();
        this.$notification["success"]({
          message: "VMD Deleted",
          description: "VMD deleted successfully ",
        });
      });
      // this.userObj = item
    },
    getUsers1List() {
      this.loading = true;
      this.get_Users().then((data) => {
        this.loading = false;
        // this.UsersList = data.data.results;
        this.UsersListActaul = data.data;
      });
    },
    getUsersList() {
      this.loading = true;
      this.get_VMDS().then((data) => {
        this.loading = false;
        // this.UsersList = data.data.results;
        this.UsersList = data.data;
      });
    },
    openModal() {
      this.isEdit = false;
      this.dialog = true;
    },
    closeModal() {
      this.$refs.userfrom.reset();
      this.dialog = false;
      this.userError = null;
      this.isEdit = false;
    },
    AddVMD() {
      if (this.$refs.userfrom.validate()) {
        this.userformloader = true;
        this.post_VMDS(this.VMDObj)
          .then((data) => {
            console.log(data);
            this.$notification["success"]({
              message: "VMD Added",
              description:
                "VMD : " + data.data.VMDName + " Added successfully ",
            });
            this.userformloader = false;
            this.closeModal();
            this.getUsersList();
            this.userError = null;
          })
          .catch((error) => {
            if (error.response) {
              this.userError = error.response.data.Error;
            }
            this.userformloader = false;
          });
      }
    },
    UpdateVMD() {
      if (this.$refs.userfrom.validate()) {
        this.userformloader = true;
        this.patch_VMDS(this.VMDObj)
          .then((data) => {
            console.log(data);
            this.userformloader = false;
            this.closeModal();
            this.getUsersList();
            this.userError = null;
            this.$notification["success"]({
              message: "VMD Updated",
              description:
                "VMD : " + data.data.VMDName + " Updated successfully ",
            });
          })
          .catch((error) => {
            if (error.response) {
              this.userError = error.response.data.Error;
            }
            this.userformloader = false;
          });
      }
    },
  },
};
</script>