<template>
  <section class="pa-2">
          <v-breadcrumbs :items="items"></v-breadcrumbs>

    <v-tabs dense v-model="tab">
      <v-tab>VMD List</v-tab>
      <v-tab>VMD Groups</v-tab>
    </v-tabs>

    <v-tabs-items v-model="tab">
      <v-app>
      <v-tab-item>
        <v-card color="basil" flat>
          
            <VMD_List />
          
        </v-card>
      </v-tab-item>
      <v-tab-item>
        <v-card color="basil" flat>
            <VMD_Groups_List />
        </v-card>
      </v-tab-item>
      </v-app>
    </v-tabs-items>
  </section>
</template>

<script>
import { utility } from "../../mixins/utility";
import VMD_List from "./VMD_List";
import VMD_Groups_List from "./VMD_Groups_List";

export default {
  mixins: [utility],
  data() {
    return {
      tab: null,
      items: [
        {
          text: 'Dashboard',
          disabled: false,
          href: '/#/dashboard',
        },
        {
          text: 'VMD Management',
          disabled: false,
        },

      ],
    };
  },
  components: {
    VMD_List,
    VMD_Groups_List
  },
};
</script>