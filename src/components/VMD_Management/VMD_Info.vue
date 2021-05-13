<template>
  <div>
    <!-- Breadcrumbs -->
    <v-breadcrumbs :items="items"></v-breadcrumbs>
    <!-- <b>{{ VMDInFO }}</b> -->
    <a-descriptions v-if="VMDInFO" size="small" class="ma-4" title="VMD Info" bordered>
      <a-descriptions-item label="VMD Name">
        {{VMDInFO.VMDName}}
      </a-descriptions-item>
      <a-descriptions-item label="VMD Location"> {{VMDInFO.VMDLocation}} </a-descriptions-item>
      <a-descriptions-item label="VMD Latitude"> {{VMDInFO.VMDLatitude}} </a-descriptions-item>
      <a-descriptions-item label="VMD Longitude">
        {{VMDInFO.VMDLongitude}}
      </a-descriptions-item>
      <a-descriptions-item label="VMD IPAddress" :span="2">
         {{VMDInFO.VMDIPAddress}}
      </a-descriptions-item>
      <a-descriptions-item label="Status" :span="3">
        <a-badge status="processing" :text="VMDInFO.VMDStatus" />
      </a-descriptions-item>
      <a-descriptions-item label="VMD Resolution Height">
        {{VMDInFO.VMDResolutionHeight}}
      </a-descriptions-item>
      <a-descriptions-item label="VMD Resolution width"> {{VMDInFO.VMDResolutionwidth}}</a-descriptions-item>
      <a-descriptions-item label="VMD Brightness">
        {{VMDInFO.VMDBrightness}}
      </a-descriptions-item>
      
    </a-descriptions>
    <a-result v-else status="warning" title="VMD Not Found">
    
  </a-result>
  </div>
</template>

<script>
import { VMDMixins } from "../../mixins/VMDMixins";

export default {
  mixins: [VMDMixins],
  mounted() {
    this.GetVMDINfo();
  },
  methods: {
    GetVMDINfo() {
      console.log(this.$route.params.id);
      this.loading = true;
      this.get_VMDS_ByID("?id=" + this.$route.params.id).then((data) => {
        this.loading = false;
        // this.UsersList = data.data.results;
        this.VMDInFO = data.data[0];
      });
    },
  },
  data() {
    return {
      loading: false,
      VMDInFO: "",
      items: [
        {
          text: "Dashboard",
          disabled: false,
          href: "/#/dashboard",
        },
        {
          text: "VMD Info",
          disabled: false,
        },
      ],
    };
  },
};
</script>

<style>
</style>