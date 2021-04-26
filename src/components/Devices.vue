<template>
  <div>
    <v-row>
      <v-col>
        <div v-bind:key="i.id" v-for="i in Device">
          <v-card class="mx-auto" max-width="344" outlined>
            <v-list-item three-line>
              <v-list-item-content>
                <div class="overline mb-4">{{ i.name }}</div>
                <v-list-item-title class="headline mb-1"
                  >Device Desc</v-list-item-title
                >
                <!-- <v-list-item-subtitle
                  >Greyhound divisely hello coldly
                  fonwderfully</v-list-item-subtitle> -->
              </v-list-item-content>

              <v-list-item-avatar
                tile
                size="80"
                color="grey"
              ></v-list-item-avatar>
            </v-list-item>

            <v-card-actions>
              <v-btn text>Action1</v-btn>
              <v-btn text>Action2</v-btn>
            </v-card-actions>
          </v-card>
         
        </div>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      env: process.env.VUE_APP_Backed_API,
      Device: [],
    };
  },
  mounted() {
    fetch(this.env + "Deveice/", {
      method: "GET",
    })
      .then((response) => {
        if (response.ok) {
          return response.json();
        } else {
          alert(
            "Server returned " + response.status + " : " + response.statusText
          );
        }
      })
      .then((response) => {
        console.log(response);
        this.Device = response;
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>