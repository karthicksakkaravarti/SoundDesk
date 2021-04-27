<template>
    <!-- container section start -->
    <div id="app">
  <v-app id="inspire">
    <v-app id="inspire">
      <v-navigation-drawer
        v-model="drawer"
        color="#394a59"
        :clipped="$vuetify.breakpoint.lgAndUp"
        app
        expand-on-hover
      >
        <v-list dense>
          <template v-for="item in items">
            <v-row
              v-if="item.heading"
              :key="item.heading"
              align="center"
            >
              <v-col cols="6">
                <v-subheader v-if="item.heading">
                  {{ item.heading }}
                </v-subheader>
              </v-col>
              <v-col
                cols="6"
                class="text-center"
              >
                <a
                  href="#!"
                  class="body-2 black--text"
                >EDIT</a>
              </v-col>
            </v-row>
            <v-list-group
              v-else-if="item.children"
              :key="item.text"
              v-model="item.model"
              :prepend-icon="item.model ? item.icon : item['icon-alt']"
              append-icon=""
            >
              <template v-slot:activator>
                <v-list-item-content>
                  <v-list-item-title>
                    {{ item.text }}
                  </v-list-item-title>
                </v-list-item-content>
              </template>
              <v-list-item
                v-for="(child, i) in item.children"
                :key="i"
                link
              >
                <v-list-item-action v-if="child.icon">
                  <v-icon>{{ child.icon }}</v-icon>
                </v-list-item-action>
                <v-list-item-content>
                  <v-list-item-title>
                    {{ child.text }}
                  </v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list-group>
            <v-list-item
            color="white"
            :to="item.to"
              v-else
              :key="item.text"
              link
            >
              <v-list-item-action>
                <v-icon>{{ item.icon }}</v-icon>
              </v-list-item-action>
              <v-list-item-content>
                <v-list-item-title>
                  {{ item.text }}
                </v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </template>
        </v-list>
      </v-navigation-drawer>
  
      <v-app-bar
      
      dense
        :clipped-left="$vuetify.breakpoint.lgAndUp"
        app
      color="#1a2732"
        dark
      >
        <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
        <v-toolbar-title
          style="width: 300px"
          class="ml-0 pl-4"
        >
          <span class="hidden-sm-and-down">VMSS</span>
        </v-toolbar-title>
        
        <v-spacer></v-spacer>
        <v-btn icon>
          <v-icon>mdi-apps</v-icon>
        </v-btn>
        <v-btn icon>
          <v-icon>mdi-bell</v-icon>
        </v-btn>
        <v-menu
      v-model="menu"
      :close-on-content-click="false"
      :nudge-width="100"
      offset-x
    >
      <template v-slot:activator="{ on, attrs }">
        <!-- <v-btn
          color="indigo"
          dark
       
        >
          Menu as Popover
        </v-btn> -->
        <v-avatar size=35 color="grey"    v-bind="attrs"
          v-on="on">
            <span v-if="GetCurrentUser && GetCurrentUser.username" >{{GetCurrentUser.username ? GetCurrentUser.username.charAt(0).toUpperCase(): 'anonymous'}}{{GetCurrentUser.username ? GetCurrentUser.username.charAt(1).toUpperCase(): "User"}}</span>
        </v-avatar>
      </template>

      <v-card>
        <v-list>
          <v-list-item>
            <v-list-item-avatar>
                 <v-avatar size=35 color="grey" >
                        <span  v-if="GetCurrentUser && GetCurrentUser.username" >{{GetCurrentUser.username ? GetCurrentUser.username.charAt(0).toUpperCase(): 'anonymous'}}{{GetCurrentUser.username ? GetCurrentUser.username.charAt(1).toUpperCase(): "User"}}</span>
                    </v-avatar>
            </v-list-item-avatar>

            <v-list-item-content>
              <v-list-item-title v-if="GetCurrentUser && GetCurrentUser.username" >{{GetCurrentUser.username.toUpperCase()}}</v-list-item-title>
              <v-list-item-subtitle v-if="GetCurrentUser">{{GetCurrentUser.email}}</v-list-item-subtitle>
            </v-list-item-content>

            <v-list-item-action>
              <v-form >
                <input name="logout" value="true"  type="hidden"/>
                <v-btn small color="primary" type="submit"   >Logout</v-btn>
              </v-form>
             
            </v-list-item-action>
          </v-list-item>
        </v-list>

        <!-- <v-divider></v-divider> -->

        <!-- <v-list>
          <v-list-item>
            <v-list-item-action>
              <v-switch v-model="message" color="purple"></v-switch>
            </v-list-item-action>
            <v-list-item-title>Enable messages</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-action>
              <v-switch v-model="hints" color="purple"></v-switch>
            </v-list-item-action>
            <v-list-item-title>Enable hints</v-list-item-title>
          </v-list-item>
        </v-list> -->

        <v-card-actions>
          <v-spacer></v-spacer>

          <!-- <v-btn text @click="menu = false">Cancel</v-btn>
          <v-btn color="primary" text @click="menu = false">Save</v-btn> -->
        </v-card-actions>
      </v-card>
    </v-menu>
      </v-app-bar>
      <v-main>
        
          <router-view></router-view>  

      </v-main>
    </v-app>
  </v-app>
</div>


</template>


<script>
// import sidebar from '../components/sidebar';
import { UsersMixins } from "../mixins/UsersMixins";

export default {
  mixins: [UsersMixins],
  data(){
    return{
      dialog: false,
      menu: '',
    drawer: null,
    items: [
      { icon: 'mdi-view-dashboard', text: 'Dashboard' , to: "dashboard"},
      { icon: 'mdi-message', text: 'Messaging' , to: "SendMessage"},
      { icon: 'mdi-message', text: 'PlayList' , to: "playlist"},
      { icon: 'mdi-file-chart', text: 'Reports' , to: "reports"},
      { icon: 'mdi-desktop-tower', text: 'VMDS' , to: "VmdManagement"},
      { icon: 'mdi-account-group-outline', text: 'User Management', to: "Usermanagement" },
    ],
    }
  },
  components: {
    // sidebar,
  },
  mounted(){
    this.get_Curentuser()
  }
}
</script>