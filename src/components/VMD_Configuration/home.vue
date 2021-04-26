<template>
  <section class="pa-2">
    <!--overview start-->
    
    <v-tabs v-model="tab">
      <v-tab>VMD Configuration</v-tab>
    </v-tabs>

    <v-tabs-items v-model="tab">
      <v-app>
      <v-tab-item>
        <v-card color="basil" flat>
          
            <VMD_ConfigurationListt />
          
        </v-card>
      </v-tab-item>
      
      </v-app>
    </v-tabs-items>
  </section>
</template>

<script>
import { utility } from "../../mixins/utility";
import VMD_ConfigurationListt from "./VMD_ConfigurationListt";

export default {
  mixins: [utility],
  data() {
    return {
      tab: null,
    };
  },
  components: {
    VMD_ConfigurationListt,
  },
};
</script>