<template>
  <div class="pt-2">
    <div v-if="this.GetCurrentUser.id" v-once>{{ LoadData() }}</div>
    <h3 style="border-left: 5px solid #394a59" class="pl-3"
      >Region Dimension and Co-Ordinates</h3
    >
    <div class="pl-4 pt-2">
      <v-form v-model="form" ref="formmodal">
        <v-row>
          <v-col>
            <v-text-field
              v-model="dataObj.XCoOrdinates"
              :rules="[rules.required]"
              dense
              label="X Co-Ordinates "
            ></v-text-field>
          </v-col>
          <v-col>
            <v-text-field
              v-model="dataObj.YCoOrdinates"
              :rules="[rules.required]"
              dense
              label="Y Co-Ordinates "
            ></v-text-field>
          </v-col>
          <v-col>
            <v-text-field
              v-model="dataObj.Width"
              :rules="[rules.required]"
              dense
              label="Width "
            ></v-text-field>
          </v-col>
          <v-col>
            <v-text-field
              v-model="dataObj.Height"
              :rules="[rules.required]"
              dense
              label="Height "
            ></v-text-field>
          </v-col>
        </v-row>
        <v-row>
          <v-dialog v-model="dialog" scrollable max-width="400px">
            <v-card>
              <v-card-text style="height: 270px">
                <b>Pick Color</b>
                <v-color-picker v-model="color" class="ma-2"></v-color-picker>
              </v-card-text>
              <v-divider></v-divider>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="dialog = false"
                  >Close</v-btn
                >
                <v-btn
                  color="blue darken-1"
                  text
                  @click="
                    dialog = false;
                    dataObj.BorderLine = showColor;
                  "
                  >Select - {{ showColor }}</v-btn
                >
              </v-card-actions>
            </v-card>
          </v-dialog>
          <v-dialog v-model="dialog1" scrollable max-width="400px">
            <v-card>
              <v-card-text style="height: 270px">
                <b>Pick Color</b>
                <v-color-picker v-model="color1" class="ma-2"></v-color-picker>
              </v-card-text>
              <v-divider></v-divider>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="dialog1 = false"
                  >Close</v-btn
                >
                <v-btn
                  color="blue darken-1"
                  text
                  @click="
                    dialog1 = false;
                    dataObj.BackGroundColor = showColor;
                  "
                  >Select - {{ showColor }}</v-btn
                >
              </v-card-actions>
            </v-card>
          </v-dialog>

          <v-col>
            <v-text-field
              :rules="[rules.required]"
              :color="`${dataObj.BorderLine}`"
              append-outer-icon="mdi-select-color"
              @click:append-outer="opencolorpicker"
              v-model="dataObj.BorderLine"
              dense
              label="Border Line"
            ></v-text-field>
          </v-col>
          <v-col>
            <v-text-field
              :rules="[rules.required]"
              dense
              :color="`${dataObj.BackGroundColor}`"
              append-outer-icon="mdi-select-color"
              @click:append-outer="opencolorpickerBackground"
              v-model="dataObj.BackGroundColor"
              label="Back Ground Color"
            ></v-text-field>
          </v-col>
        </v-row>
      </v-form>
    </div>
  </div>
</template>

<script>
import { MessagingMixins } from "../../mixins/MessagingMixins";
import { UsersMixins } from "../../mixins/UsersMixins";

export default {
  mixins: [MessagingMixins, UsersMixins],
  props: {
    typemessage: { default: "single" },
    loaddata: { default: "true" }
  },
  data() {
    return {
      border: "",
      background: "",
      dialog: false,
      dialog1: false,
      types: ["hex", "hexa", "rgba", "hsla", "hsva"],
      type: "hex",
      hex: "#FF00FF",
      hexa: "#FF00FFFF",
      dataObj: {
        XCoOrdinates: "",
        YCoOrdinates: "",
        Width: "",
        Height: "",
        BorderLine: "",
        BackGroundColor: "",
      },
      rgba: { r: 255, g: 0, b: 255, a: 1 },
      hsla: { h: 300, s: 1, l: 0.5, a: 1 },
      hsva: { h: 300, s: 1, v: 1, a: 1 },
      form: false,
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
  mounted() {},
  computed: {
    color: {
      get() {
        return this[this.type];
      },
      set(v) {
        this[this.type] = v;
      },
    },
    color1: {
      get() {
        return this[this.type];
      },
      set(v) {
        this[this.type] = v;
      },
    },
    showColor() {
      if (typeof this.color === "string") return this.color;

      return JSON.stringify(
        Object.keys(this.color).reduce((color, key) => {
          color[key] = Number(this.color[key].toFixed(2));
          return color;
        }, {}),
        null,
        2
      );
    },
  },
  methods: {
    opencolorpicker() {
      this.dialog = true;
      console.log("open color picker");
    },
    opencolorpickerBackground() {
      this.dialog1 = true;
      console.log("open color picker");
    },
    LoadData() {
      if(this.loaddata){
          this.get_RegionDimensionAndCoOrdinates(
        "?user=" + this.GetCurrentUser.id + "&type=" + this.typemessage
      ).then((data) => {
        if (data.data.length >= 1) {
          this.dataObj = data.data[0];
        }
      });
      }
    
    },
    validateFun() {
      return new Promise((resolve, reject) => {
        if (this.$refs.formmodal.validate()) {
         if (this.loaddata){
            if (this.dataObj.id) {
            // Update
            this.patch_RegionDimensionAndCoOrdinates(this.dataObj)
              .then(() => {
                resolve(true);
              })
              .catch(() => {
                resolve(false);
              });
          } else {
            // Create
            this.dataObj.user = this.GetCurrentUser.id;
            this.dataObj.type = this.typemessage;

            this.post_RegionDimensionAndCoOrdinates(this.dataObj)
              .then(() => {
                this.LoadData();
                resolve(true);
              })
              .catch(() => {
                resolve(false);
              });
          }
         }

          console.log(reject);
        } else {
                resolve(false);
        }
      });
    },
  },
};
</script>