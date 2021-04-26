<template>
  <div>
    <a-page-header
      style="border: 1px solid rgb(235, 237, 240)"
      sub-title="Configure VMD "
    >
      <template slot="extra">
        <!-- <a-button key="3"> Operation </a-button> -->
      </template>
      <template slot="footer">
        <center>
          <a-button class="mr-2"> Cancel </a-button>
          <a-button type="primary" v-if="!edit" @click="saveConfig">
            Submit
          </a-button>
          <a-button type="primary" v-else @click="UpdateConfig">
            Update
          </a-button>
        </center>
      </template>
      <div class="content">
        <div class="main">
          <v-alert dense v-if="userError" outlined type="error">
            {{ userError }}
          </v-alert>
          <a-descriptions bordered>
            <a-descriptions-item :span="12" label="Select VMD">
              <a-select
                v-model="config.VMDS"
                mode="multiple"
                style="width: 500px"
                placeholder="Please select"
              >
                <a-select-option
                  v-for="i in GetVMDS"
                  :value="i.id"
                  :key="i.VMDName"
                >
                  {{ i.VMDName }}({{ i.VMDResolutionwidth }}x{{
                    i.VMDResolutionHeight
                  }})
                </a-select-option>
              </a-select>
            </a-descriptions-item>
            <a-descriptions-item :span="12" label="ON/OFF Scheduling">
              <a-row>
                <a-col :span="2" class="pr-2">
                  <a-switch v-model="config.ON_OFF_Scheduling" />
                </a-col>
                <template v-if="config.ON_OFF_Scheduling">
                  <a-col :span="6">
                    <a-time-picker
                      v-model="config.wakeUptime"
                      class="pr-2"
                      placeholder="Wake Up Time"
                      use12-hours
                    />
                  </a-col>
                  <a-col :span="6">
                    <a-time-picker
                      v-model="config.Sleeptime"
                      class="pr-2"
                      placeholder="Sleep Time"
                      use12-hours
                    />
                  </a-col>
                  <a-col :span="6">
                    <a-time-picker
                      v-model="config.Reboottime"
                      class="pr-2"
                      placeholder="Reboot Time"
                      use12-hours
                    />
                  </a-col>
                </template>
              </a-row>
            </a-descriptions-item>
            <a-descriptions-item :span="12" label="VMD Brightness">
              <a-row>
                <a-col :span="2">
                  <a-switch v-model="config.VMD_Brightness" default-checked />
                </a-col>
                <!-- <a-col :span="2">
                  <v-icon class="pt-2">mdi-brightness-5</v-icon>
                </a-col> -->
                <template v-if="config.VMD_Brightness">
                  <a-col :span="9" class="mt-0 pt-0">
                    <a-slider v-model="config.Brightness" :min="1" :max="100" />
                  </a-col>
                  <a-col :span="4">
                    <a-alert
                      size="small"
                      class="ml-2 pa-1"
                      style="width: 45px"
                      :message="`${config.Brightness}%`"
                      type="success"
                    />
                  </a-col>
                </template>
              </a-row>
            </a-descriptions-item>
            <a-descriptions-item label="Resolution">
              <a-row>
                <a-col :span="2" class="pr-2">
                  <a-switch v-model="config.Resolution" default-checked />
                </a-col>
                <template v-if="config.Resolution">
                  <a-col :span="11" class="pr-2">
                    <a-input v-model="config.width" placeholder="Width" />
                  </a-col>
                  <a-col :span="11" class="pr-2">
                    <a-input v-model="config.height" placeholder="Height" />
                  </a-col>
                </template>
              </a-row>
            </a-descriptions-item>
          </a-descriptions>
        </div>
        <div class="extra"></div>
      </div>
    </a-page-header>
  </div>
</template>

<script>
import { VMDMixins } from "../../mixins/VMDMixins";
import { UsersMixins } from "../../mixins/UsersMixins";
import moment from "moment";

export default {
  mixins: [VMDMixins, UsersMixins],
  mounted() {
    this.get_VMDS();
    this.get_Config();
  },
  methods: {
    get_Config() {
      this.get_VMDConfig().then((data) => {
        // this.UsersList = data.data.results;

        console.log(data.data);
        if (data.data.length == 1) {
          this.config = data.data[0];
          this.config.wakeUptime = moment(this.config.wakeUptime, "hh:mm:ss");
          this.config.Sleeptime = moment(this.config.Sleeptime, "hh:mm:ss");
          this.config.Reboottime = moment(this.config.Reboottime, "hh:mm:ss");
          this.edit = true;
        } else {
          this.edit = false;
        }
      });
    },
    saveConfig() {
      this.config.wakeUptime = this.config.wakeUptime.format('hh:mm');
      this.config.Sleeptime = this.config.Sleeptime.format('hh:mm');
      this.config.Reboottime = this.config.Reboottime.format('hh:mm');
      this.post_VMDConfig(this.config)
        .then((data) => {
          console.log(data);
              

          this.$notification["success"]({
            message: "VMD Config Created",
            description: "VMD Config Created successfully ",
          });
        })
        .catch((error) => {
          if (error.response) {
            this.userError = error.response.data.Error;
          }
          this.userformloader = false;
        });
    },
    UpdateConfig() {
      try{
        this.config.wakeUptime = this.config.wakeUptime.format('hh:mm');
      this.config.Sleeptime = this.config.Sleeptime.format('hh:mm');
      this.config.Reboottime = this.config.Reboottime.format('hh:mm');
      }
      catch(err){console.log(err)}
      this.patch_VMDConfig(this.config)
        .then((data) => {
          console.log(data);
          this.$notification["success"]({
            message: "VMD Config Updated",
            description: "VMD Config Updated successfully ",
          });
          this.get_Config()
        })
        .catch((error) => {
          if (error.response) {
            this.userError = error.response.data.Error;
          }
          this.userformloader = false;
        });
    },
    //  onChangeWake(time) {
    //    console.log(time.format('hh:mm'))
    //    console.log()
    //   //  hh:mm[:ss[.uuuuuu]]
    //     this.config.wakeUptime = time.format('hh:mm');
    //   },
    //  onChangeSleep(time) {
    //     this.config.Sleeptime = time.format('hh:mm');
    //   },
    //  onChangeReboot(time) {
    //     this.config.Reboottime = time.format('hh:mm');
    //   },
  },
  data() {
    return {
      userError: null,
      inputValue1: 0,
      onoff: true,
      vmdbrigth: true,
      resolution: true,
      edit: false,
      config: {
        ON_OFF_Scheduling: true,
        VMD_Brightness: true,
        Resolution: true,
        wakeUptime: null,
        Sleeptime: null,
        Reboottime: null,
        Brightness: 0,
        width: null,
        height: null,
        VMDS: [],
      },
    };
  },
};
</script>
<style>
tr:last-child td {
  padding-bottom: 0;
}
#components-page-header-demo-responsive .content {
  display: flex;
}
#components-page-header-demo-responsive .ant-statistic-content {
  font-size: 20px;
  line-height: 28px;
}
@media (max-width: 576px) {
  #components-page-header-demo-responsive .content {
    display: block;
  }

  #components-page-header-demo-responsive .main {
    width: 100%;
    margin-bottom: 12px;
  }

  #components-page-header-demo-responsive .extra {
    width: 100%;
    margin-left: 0;
    text-align: left;
  }
}
</style>
