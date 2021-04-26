<template>
  <div>
    <v-row justify="center" class="mt-2 mr-2">
      <v-dialog v-model="dialog" persistent max-width="600px">
        <template v-slot:activator="{}">
          <v-spacer></v-spacer>
          <v-btn small outlined color="primary" dark @click="openModal">
            Add User
          </v-btn>
        </template>
        <v-card :disabled="userformloader">
          <v-card-title>
            <span class="headline">{{!isEdit ? 'Add User' : 'Edit User'}}</span>
          </v-card-title>
          <v-divider></v-divider>
          <v-card-text>
            <v-container>
              <v-alert dense v-if="userError" outlined type="error">
                {{ userError }}
              </v-alert>
              <v-form ref="userfrom" v-model="formmodal">
                <v-row>
                  <v-col cols="12" sm="6">
                    <v-text-field
                      v-model="userObj.username"
                      :rules="[rules.required]"
                      label="Username*"
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6">
                    <v-autocomplete
                      v-model="userObj.role"
                      label="User Role"
                      auto-select-first
                      :items="['Admin', 'User']"
                    ></v-autocomplete>
                  </v-col>

                  <v-col cols="12">
                    <v-text-field
                      label="Email*"
                      v-model="userObj.email"
                      :rules="[rules.required, rules.email]"
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col v-if="!isEdit" cols="12" sm="6">
                    <v-text-field
                      label="Password*"
                      type="password"
                      loading
                      v-model="userObj.password"
                      :rules="[rules.required]"
                      required
                    >
                      <template v-slot:progress>
                        <v-progress-linear
                          :value="progress"
                          :color="color"
                          absolute
                          height="7"
                        ></v-progress-linear> </template
                    ></v-text-field>
                  </v-col>
                  <v-col v-if="!isEdit" cols="12" sm="6">
                    <v-text-field
                      label="Confirm Password*"
                      :rules="[rules.required, rules.confirmpassword]"
                      type="password"
                      required
                    ></v-text-field>
                  </v-col>
                </v-row>
              </v-form>
            </v-container>
            <small>*indicates required field</small>
          </v-card-text>
          <v-divider></v-divider>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" text @click="closeModal">Close</v-btn>
            <v-btn v-if="isEdit" color="primary" @click="UpdateUser" :loading="userformloader"
              >Update User</v-btn
            >
            <v-btn v-else color="primary" @click="saveUser" :loading="userformloader"
              >Add User</v-btn
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
      <v-icon
        small
        class="mr-2"
        @click="editItem(item)"
      >
        mdi-pencil
      </v-icon>
      <a-popconfirm
    :title="`Are you sure delete this ${item.username}?`"
    ok-text="Yes"
    cancel-text="No"
    @confirm="deleteItem(item)"
  >
    <v-icon
        small
      >
        mdi-delete
      </v-icon>
  </a-popconfirm>
      
    </template>
    </v-data-table>
  </div>
</template>

<script>
import { UsersMixins } from "../../mixins/UsersMixins";

export default {
  mixins: [UsersMixins],
  data() {
    return {
      header: [
        { text: "#", value: "id" },
        { text: "User Id", value: "email" },
        { text: "Name", value: "username" },
        { text: "Action", value: "actions" },
      ],
      loading: false,
      userformloader: false,
      UsersList: [],
      dialogm1: "",
      dialog: false,
      formmodal: false,
      userError: null,
      isEdit: false,
      userObj: {
        username: "",
        email: "",
        role: "Admin",
        password: "",
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
    editItem(item){
        this.isEdit = true
        this.userObj = Object.assign({}, item)
        this.dialog = true
    },
    deleteItem(item){
        this.delete_Users(item)
          .then((data) => {
            console.log(data);
            this.getUsersList();
            this.$notification['success']({message: 'User Deleted',description: "User deleted successfully ",});

          })
        // this.userObj = item
    },
    getUsersList() {
      this.loading = true;
      this.get_Users().then((data) => {
        this.loading = false;
        // this.UsersList = data.data.results;
        this.UsersList = data.data;
      });
    },
    openModal() {
      this.userObj.role = "Admin";
      this.isEdit = false
      this.dialog = true;
    },
    closeModal() {
      this.$refs.userfrom.reset();
      this.dialog = false;
      this.userError = null;
      this.isEdit = false
    },
    saveUser() {
      if (this.$refs.userfrom.validate()) {
        this.userformloader = true;
        this.post_Users(this.userObj)
          .then((data) => {
            console.log(data);
            this.$notification['success']({message: 'User Added',description: "User :"+data.data.username +' Added successfully ',});
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
    UpdateUser() {
      if (this.$refs.userfrom.validate()) {
        this.userformloader = true;
        this.patch_Users(this.userObj)
          .then((data) => {
            console.log(data);
            this.userformloader = false;
            this.closeModal();
            this.getUsersList();
            this.userError = null;
            this.$notification['success']({message: 'User Updated',description: "User :"+data.data.username +' Updated successfully ',});

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