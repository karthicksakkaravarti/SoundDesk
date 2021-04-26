<template>
  <aside>
    <div id="sidebar" class="nav-collapse">
      <!-- sidebar menu start-->
      <ul class="sidebar-menu">
        <li class="active ">
          <a class="cursor"  @click="routing('dashboard')">
            <i class="icon_house_alt"></i>
            <span>Dashboard</span>
          </a>
        </li>
        <li >
          <a @click="showMessagingOption=!showMessagingOption"  class="cursor">
            <i class="fa fa-comment"></i>
            <span>Messaging</span>
            <span :class="`menu-arrow ${showMessagingOption ? 'arrow_carrot-down' : 'arrow_carrot-right' }`"></span>
          </a>
          <ul v-if="showMessagingOption">
            <li><a class="active" @click="routing('SendMessage')">Send Message</a></li>
            <li><a class="" @click="routing('MessagingConfig')">Messaging Config</a></li>
          </ul>
        </li>
        

        <li>
          <a class="" >
            <i class="fa-file"></i>
            <span>Reports</span>
          </a>
        </li>

        <li >
          <a @click="showVMDMgmtOption=!showVMDMgmtOption"  class="cursor">
            <i class="fa fa-desktop"></i>
            <span>VMD</span>
            <span :class="`menu-arrow ${showVMDMgmtOption ? 'arrow_carrot-down' : 'arrow_carrot-right' }`"></span>
          </a>
          <ul v-if="showVMDMgmtOption">
            <li><a class="active" @click="routing('VmdManagement')">VMD Management</a></li>
            <li><a class="" @click="routing('VmdConfiguration')">VMD Configuration</a></li>
          </ul>
        </li>

        
        <li>
          <a class="cursor" @click="routing('Usermanagement')">
            <i class="fa fa-users"></i>
            <span>User Management</span>
          </a>
        </li>
        <!-- <li >
          <a href="javascript:;" class="">
            <i class="icon_documents_alt"></i>
            <span>Pages</span>
            <span class="menu-arrow arrow_carrot-right"></span>
          </a>
          <ul class="sub">
            <li><a class="" href="profile.html">Profile</a></li>
            <li>
              <a class="" href="login.html"><span>Login Page</span></a>
            </li>
            <li>
              <a class="" href="contact.html"><span>Contact Page</span></a>
            </li>
            <li><a class="" href="blank.html">Blank Page</a></li>
            <li><a class="" href="404.html">404 Error</a></li>
          </ul>
        </li> -->
      </ul>
      <!-- sidebar menu end-->
    </div>
  </aside>
</template>

<script>
import { utility } from "../mixins/utility";
export default {
  mixins: [utility],
  data(){
      return{
          showMessagingOption: false,
          showVMDMgmtOption: false,
          
      }
  }
};
</script>

<style scoped>
.cursor{
    cursor:pointer
}
</style>