<template>
  <section class="pa-2">
    
    <v-breadcrumbs :items="items"></v-breadcrumbs>
    <a-card class="rounded-lg mt-0" style="background-color: #dae1ed">
      <a-row>
        <a-row>
          <a-col :lg="{ span: 8 }" :xs="{ span: 8 }" :md="{ span: 8 }">
            <h3>Dashboard Data</h3>
          </a-col>
        </a-row>
        <a-col cols="12" sm="12">
          <a-col :lg="{ span: 8 }" :xs="{ span: 8 }" :md="{ span: 8 }">
            <a-tooltip placement="bottom">
              <template slot="title">
                <span>Total VMD </span>
              </template>
              <a>
                <a-statistic
                  title="Total VMD "
                  :value="GetVMDS.length"
                  style="color: white; margin-right: 50px"
                >
                  <template #suffix>
                    <a-icon
                      :style="{ fontSize: '16px', color: 'green' }"
                      type="desktop"
                    />
                  </template>
                </a-statistic>
              </a>
            </a-tooltip>
          </a-col>
          <a-col :lg="{ span: 8 }" :xs="{ span: 8 }" :md="{ span: 8 }">
            <a-tooltip placement="bottom">
              <template slot="title">
                <span>Online VMD's </span>
              </template>
              <a>
                <a-statistic title="Online VMD's" :value="GetVMDS.filter(obj => {return obj.VMDStatus == 'Active'}).length" class="demo-class">
                  <template #suffix>
                    <a-icon
                      :style="{ fontSize: '16px', color: 'green' }"
                      type="like"
                    />
                  </template>
                </a-statistic>
              </a>
            </a-tooltip>
          </a-col>
          <a-col :lg="{ span: 8 }" :xs="{ span: 8 }" :md="{ span: 8 }">
            <a-tooltip placement="bottom">
              <template slot="title">
                <span>Offiline VMD's </span>
              </template>
              <a>
                <a-statistic
                  title="Offiline VMD's"
                  :value="GetVMDS.filter(obj => {return obj.VMDStatus == 'InActive'}).length"
                  class="demo-class"
                >
                  <template #suffix>
                    <a-icon
                      :style="{ fontSize: '16px', color: 'red' }"
                      type="dislike"
                    />
                  </template>
                </a-statistic>
              </a>
            </a-tooltip>
          </a-col>
        </a-col>
        <!-- <template v-else>
                      <div class="text-center">
                          <v-skeleton-loader
                          elevation="0"
                          ref="skeleton"
                          type="table-thead"
                          class="mx-auto"
                        ></v-skeleton-loader>
                      </div>

                  </template> -->
      </a-row>
      
    </a-card>
    <v-row class="mt-2">
      <v-col cols="12" sm="7">
          <v-card outlined>
            <GoogleMap/>
          </v-card>
      </v-col>
      <v-col cols="12" sm="5">
        <!-- <b>{{GetVMDS}}</b> -->
          <v-card outlined>
            <v-data-table
            class="mt-2"
          :headers="[
          {'text': 'VMD ID', 'value': 'id'},
          {'text': 'VMD Name', 'value': 'VMDName'},
          {'text': 'VMD Ip', 'value': 'VMDIPAddress'},
          {'text': 'VMD Status', 'value': 'VMDStatus'},
          {'text': 'Screen Shot', 'value': 'Screen Shot'}
          ]"
          :items="GetVMDS">
            <template v-slot:item.VMDStatus= {item} class="mt-2">
                  <a-tag type="success">{{item.VMDStatus}}</a-tag>
                </template>
          </v-data-table>
          </v-card>
      </v-col>
    </v-row>
  </section>
</template>

<script>
import { VMDMixins } from "../mixins/VMDMixins";
import GoogleMap from './GoogleMap.vue'

export default {
    mixins: [VMDMixins],
  mounted(){
        this.get_VMDS();

  },
  components:{
    GoogleMap
  },
  data() {
    return {
      items: [
        {
          text: "Home",
          disabled: true,
        },
        {
          text: "Dashboard",
          disabled: true,
        },
      ],
    };
  },
};
</script>