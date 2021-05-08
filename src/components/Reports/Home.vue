<template>
  <div>
          <v-breadcrumbs :items="items"></v-breadcrumbs>
 <a-card class="rounded-lg ma-2" style="background-color: #dae1ed">
      <a-row>
        
        <a-col cols="12" sm="12">
          <a-col :lg="{ span: 6 }" :xs="{ span: 6 }" :md="{ span: 6 }">
            <a-tooltip placement="bottom">
              <template slot="title">
                <span>Live Status </span>
              </template>
              <a>
                <a-statistic
                  title="Live Status "
                  :value="10"
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
          <a-col :lg="{ span: 6 }" :xs="{ span: 6 }" :md="{ span: 6 }">
            <a-tooltip placement="bottom">
              <template slot="title">
                <span>Up Time </span>
              </template>
              <a>
                <a-statistic
                  title="Up Time"
                  :value="
                    10
                  "
                  class="demo-class"
                >
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
          <a-col :lg="{ span: 6 }" :xs="{ span: 6 }" :md="{ span: 6 }">
            <a-tooltip placement="bottom">
              <template slot="title">
                <span>Funcational History </span>
              </template>
              <a>
                <a-statistic
                  title="Funcational History"
                  :value="
                    10
                  "
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
          <a-col :lg="{ span: 6 }" :xs="{ span: 6 }" :md="{ span: 6 }">
            <a-tooltip placement="bottom">
              <template slot="title">
                <span>Message Logs </span>
              </template>
              <a>
                <a-statistic
                  title="Message Logs"
                  :value="
                    reports.length
                  "
                  class="demo-class"
                >
                  <template #suffix>
                    <a-icon
                      :style="{ fontSize: '16px', color: 'red' }"
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

    <!-- Information -->
     <h3 style="border-left: 5px solid #394a59" class="mt-3 pl-3">
            Message Logs
          </h3>
    <v-data-table
    :items="reports"
   :headers="[
    {'text': 'ID', 'value': 'id' },
    {'text': 'User', 'value': 'user.username' },
    {'text': 'Message', 'value': 'message' },
    {'text': 'VMD', 'value': 'VMDS' },
    {'text': 'VMD Group', 'value': 'VMDGroups' }
    ]"
    >

    <template v-slot:item.VMDGroups="{ item }" >
              <v-chip v-for="i in item.VMDGroups " v-bind:key="i.id" >{{
                i.VMDName
              }}</v-chip>
            </template>
    <template v-slot:item.VMDS="{ item }" >
              <v-chip v-for="i in item.VMDS " v-bind:key="i.id" >{{
                i.VMDName
              }}</v-chip>
            </template>
    </v-data-table>
  </div>
</template>

<script>
import { MessagingMixins } from "../../mixins/MessagingMixins";

export default {
    mixins: [MessagingMixins],
    data(){
        return{
            reports : [],
            items: [
        {
          text: "Home",
          disabled: true,
        },
        {
          text: "Reposrts",
          disabled: true,
        },
      ],
        }
    },
    mounted(){
        this.get_Reports('?')
        .then(data => {
                this.reports = data.data
        })
    }
}
</script>

<style>

</style>