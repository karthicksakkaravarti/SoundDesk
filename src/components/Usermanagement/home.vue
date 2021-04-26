<template>
  <div class="pa-2">
        <v-breadcrumbs :items="items"></v-breadcrumbs>

    <v-tabs v-model="tab">
      <v-tab>Users List</v-tab>
      <v-tab>User Log Report</v-tab>
    </v-tabs>

    <v-tabs-items v-model="tab">
      <v-tab-item>
        <v-card color="basil" flat>
          <v-app>
            <users_list />
          </v-app>
        </v-card>
      </v-tab-item>
    </v-tabs-items>
  </div>
</template>

<script>
import { utility } from "../../mixins/utility";
import users_list from "./users_list";

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
          text: 'User Management',
          disabled: true,
          href: 'Usermanagement',
        },

      ],
    };
  },
  components: {
    users_list,
  },
};
</script>