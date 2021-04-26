<template>
  <div>
          <div v-if="GetCurrentUser && GetCurrentUser.username">{{setUser(GetCurrentUser.username)}}</div>

    <v-row justify="center" class="mt-2 mr-2">
      <v-dialog scrollable v-model="dialog" persistent max-width="600px">
        <template v-slot:activator="{}">
          <v-spacer></v-spacer>
          <v-btn small outlined color="primary" dark @click="openModal">
            Add New VMD Group
          </v-btn>
        </template>
        <v-card :disabled="userformloader">
          <v-card-title>
            <span class="headline">{{
              !isEdit ? "Add VMD Group" : "Edit VMD Group"
            }}</span>
          </v-card-title>
          <v-divider></v-divider>
          <v-card-text style="height: 250px">
            <!-- <v-container> -->
            <v-alert dense v-if="userError" outlined type="error">
              {{ userError }}
            </v-alert>
            <v-form ref="userfrom" v-model="formmodal">
              <v-row>
                <v-col cols="12" sm="12">
                  <v-text-field
                    v-model="VMDGroupObj.GroupName"
                    :rules="[rules.required]"
                    label="VMD Group Name*"
                    required
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="12">
                  <v-autocomplete
                  chips
                  deletable-chips
                  multiple
                    v-model="VMDGroupObj.VMDS"
                    :rules="[rules.required, rules.listreqired]"
                    label="VMD's*"
                    auto-select-first
                    item-text="VMDName"
                    item-value="id"
                    :items="GetVMDS"
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
              >Update VMD Group</v-btn
            >
            <v-btn
              v-else
              color="primary"
              @click="AddVMD"
              :loading="userformloader"
              >Add VMD Group</v-btn
            >
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-row>

    <v-data-table
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
          :title="`Are you sure delete this ${item.GroupName}?`"
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
        { text: "Group Name", value: "GroupName" },
        { text: "Created By", value: "CreatedBy" },
        { text: "Created Date", value: "createdDateFormat" },
        { text: "No of VMD's", value: "NoOfVmds" },
        { text: "Actions", value: "actions" },
      ],
      loading: false,
      userformloader: false,
      UsersList: [],
      dialogm1: "",
      dialog: false,
      formmodal: false,
      userError: null,
      isEdit: false,
      readonly: true,
      VMDGroupObj: {
        GroupName: "",
        VMDS: [],
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
          if (value.length >=1) {
            return true;
          } else {
            return false || "Required.";
          }
        },
      },
    };
  },
  mounted() {
    console.log("Mounted called");
    this.getUsersList();
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
    setUser(user){
      this.VMDGroupObj.CreatedBy = user
    },
    editItem(item) {
      this.isEdit = true;
      this.VMDGroupObj = Object.assign({}, item);
      this.dialog = true;
    },
    deleteItem(item) {
      this.delete_VMDGroups(item).then((data) => {
        console.log(data);
        this.getUsersList();
        this.$notification["success"]({
          message: "VMD Group Deleted",
          description: "VMD Group deleted successfully ",
        });
      });
      // this.userObj = item
    },
    getUsersList() {
      this.loading = true;
      this.get_VMDGroups().then((data) => {
        this.loading = false;
        // this.UsersList = data.data.results;
        this.UsersList = data.data;
      });
    },
    openModal() {
      console.log('Calling open modal')
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
        this.post_VMDGroups(this.VMDGroupObj)
          .then((data) => {
            console.log(data);
            this.$notification["success"]({
              message: "VMD Group Added",
              description:
                "VMD Group : " + data.data.GroupName + " Added successfully ",
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
        this.patch_VMDGroups(this.VMDGroupObj)
          .then((data) => {
            console.log(data);
            this.userformloader = false;
            this.closeModal();
            this.getUsersList();
            this.userError = null;
            this.$notification["success"]({
              message: "VMD Group Updated",
              description:
                "VMD Group: " + data.data.GroupName + " Updated successfully ",
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