<template>
  <div>
    <div v-if="this.GetCurrentUser.id" v-once>{{ LoadData() }}</div>
    <h3 style="border-left: 5px solid #394a59" class="pl-3">Schedule</h3>
    <div class="pl-4 pt-2">
      <v-form v-model="form" ref="formmodal">
        <v-row>
          <v-col>
            <v-menu
              ref="menu1"
              v-model="menu1"
              :close-on-content-click="false"
              transition="scale-transition"
              offset-y
              max-width="290px"
              min-width="290px"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  v-model="dateFormatted"
                  :rules="[rules.required]"
                  label="Start Date"
                  hint="MM/DD/YYYY format"
                  persistent-hint
                  append-icon="mdi-calendar"
                  v-bind="attrs"
                  @blur="date = parseDate(dateFormatted)"
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker
                v-model="date"
                @change="dataObj.StartDate = date"
                no-title
                @input="menu1 = false"
              ></v-date-picker>
            </v-menu>
            <!-- <p>
              Date in ISO format: <strong>{{ date }}</strong>
            </p> -->

            <!-- <v-text-field
              append-icon="mdi-calendar"
              dense
              label="Start Date"
            ></v-text-field> -->
          </v-col>
          <v-col>
            <v-menu
              ref="menu"
              v-model="menu3"
              :close-on-content-click="false"
              :nudge-right="40"
              :return-value.sync="time"
              transition="scale-transition"
              offset-y
              max-width="290px"
              min-width="290px"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  v-model="dataObj.StartTime"
                  :rules="[rules.required]"
                  label="Start Time"
                  append-icon="mdi-clock-time-eight"
                  readonly
                  v-bind="attrs"
                  v-on="on"
                ></v-text-field>
              </template>
              <v-time-picker
                v-if="menu3"
                v-model="dataObj.StartTime"
                full-width
                @click:minute="$refs.menu.save(dataObj.StartTime)"
              ></v-time-picker>
            </v-menu>

            <!-- <v-text-field
              append-icon="mdi-clock-time-eight"
              dense
              label="Start Time"
            ></v-text-field> -->
          </v-col>
          <v-col>
            <v-autocomplete
              label="Duration"
              auto-select-first
              v-model="dataObj.Duration"
              :rules="[rules.required]"
              append-icon="mdi-clock-end"
              :items="['1 Minites', '2 Minites']"
            ></v-autocomplete>

            <!-- <v-text-field
              append-icon="mdi-clock-end"
              dense
              label="Duration"
            ></v-text-field> -->
          </v-col>
          <v-col>
            <v-autocomplete
              label="Repeat Count"
              auto-select-first
              v-model="dataObj.RepeatCount"
              :rules="[rules.required]"
              append-icon="mdi-repeat"
              :items="[1, 2, 3, 4, 5]"
            ></v-autocomplete>
            <!-- <v-text-field
              append-icon="mdi-repeat"
              dense
              label="Repeat Count"
            ></v-text-field> -->
          </v-col>
        </v-row>
      </v-form>
    </div>
  </div>
</template>

<script>
import { UsersMixins } from "../../mixins/UsersMixins";
import { MessagingMixins } from "../../mixins/MessagingMixins";

export default {
  mixins: [MessagingMixins, UsersMixins],
  props: {
    typemessage: { default: "single" },
  },
  data: () => ({
    date: new Date().toISOString().substr(0, 10),
    dateFormatted: "",
    menu1: false,
    menu2: false,
    time: null,
    menu3: false,
    modal3: false,
    form: false,
    dataObj: {
      StartDate: null,
      StartTime: null,
      Duration: null,
      RepeatCount: null,
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
  }),
  computed: {
    computedDateFormatted() {
      return this.formatDate(this.date);
    },
  },
  watch: {
    date() {
      this.dateFormatted = this.formatDate(this.date);
    },
  },

  methods: {
    LoadData() {
      this.get_Schedule(
        "?user=" + this.GetCurrentUser.id + "&type=" + this.typemessage
      ).then((data) => {
        if (data.data.length >= 1) {
          this.dataObj = data.data[0];
          console.log('this.dataObj',this.dataObj)
          this.date = this.dataObj.StartDate;
        }
      });
    },
    formatDate(date) {
      if (!date) return null;

      const [year, month, day] = date.split("-");
      return `${month}/${day}/${year}`;
    },
    parseDate(date) {
      if (!date) return null;

      const [month, day, year] = date.split("/");
      return `${year}-${month.padStart(2, "0")}-${day.padStart(2, "0")}`;
    },
    validateFun() {
      return new Promise((resolve, reject) => {
        if (this.$refs.formmodal.validate()) {
          if (this.dataObj.id) {
            // Update
            this.patch_Schedule(this.dataObj)
              .then(() => {
                return resolve(true);
              })
              .catch(() => {
                return resolve(false);
              });
          } else {
            // Create
            this.dataObj.user = this.GetCurrentUser.id;
            this.dataObj.type = this.typemessage;

            this.post_Schedule(this.dataObj)
              .then((data) => {
                this.dataObj = data.data;
                this.LoadData();
                return resolve(true);
              })
              .catch(() => {
                return resolve(false);
              });
          }
          console.log(reject);
        } else {
          return false;
        }
      });
    },
  },
};
</script>