<script>
import SidebarLink from "./SidebarLink";
import { collapsed, toggleSidebar, sidebarWidth } from "./state";

export default {
  props: {},
  components: { SidebarLink },
  setup() {
    return { collapsed, toggleSidebar, sidebarWidth };
  },
  data() {
    return {
      username: "",
    };
  },
  async created() {
    this.auth_token = sessionStorage.getItem("auth-token");
    this.username = sessionStorage.getItem("username");
    console.log(this.username);
    if (!this.auth_token) {
      alert("Please Login to see your dashboard.");
      this.$router.push("/");
    }
  },
};
</script>

<template>
  <div class="sidebar" :style="{ width: sidebarWidth }">
    <h1>
      <span v-if="collapsed">
        <div style="font-family: Rubik Vinyl">R</div>
        <div style="font-family: Rubik Vinyl">S</div>
      </span>
      <span v-else class="recommender-text">Recommender System</span>
    </h1>

    <SidebarLink
      v-if="username.toLowerCase() === 'admin'"
      to="/adminhome"
      icon="fas fa-home"
      >Home</SidebarLink
    >
    <SidebarLink
      v-if="username.toLowerCase() === 'admin'"
      to="/studentdata"
      icon="fas fa-user-graduate"
      >Student Data</SidebarLink
    >
    <SidebarLink
      v-if="username.toLowerCase() === 'admin'"
      to="/coursedata"
      icon="fas fa-book"
      >Course Data</SidebarLink
    >
    <SidebarLink
      v-if="username.toLowerCase() === 'admin'"
      to="/alllearningpaths"
      icon="fas fa-map-signs"
      >Learning Paths</SidebarLink
    >

    <SidebarLink
      v-if="username.toLowerCase() !== 'admin'"
      to="/studenthome"
      icon="fas fa-home"
      >Home</SidebarLink
    >
    <SidebarLink
      v-if="username.toLowerCase() !== 'admin'"
      to="/courses"
      icon="fas fa-book"
      >Courses</SidebarLink
    >

    <SidebarLink
      v-if="username.toLowerCase() !== 'admin'"
      to="/popularlearningpaths"
      icon="fas fa-fire"
      >Learning Paths</SidebarLink
    >

    <SidebarLink
      v-if="username.toLowerCase() !== 'admin'"
      to="/mylearningpaths"
      icon="fas fa-history"
      >History</SidebarLink
    >

    <div class="spacer"></div>
    <SidebarLink to="" icon="fas fa-user-circle">{{ username }}</SidebarLink>
    <SidebarLink to="/" icon="fas fa-sign-out-alt">Logout</SidebarLink>
    <div class="spacers"></div>
    <span
      class="collapse-icon"
      :class="{ 'rotate-180': collapsed }"
      @click="toggleSidebar"
    >
      <i class="fas fa-angle-double-left" />
    </span>
  </div>
</template>

<style>
:root {
  --sidebar-bg-color: #2f3385;
  --sidebar-item-hover: #384da1;
  --sidebar-item-active: #272867;
  --font-family: Rubik Vinyl;
}
</style>

<style scoped>
.sidebar {
  color: white;
  background-color: var(--sidebar-bg-color);

  float: left;
  position: fixed;
  z-index: 1;
  top: 0;
  left: 0;
  bottom: 0;
  padding: 0.5em;

  transition: 0.3s ease;

  display: flex;
  flex-direction: column;
}

.sidebar h1 {
  height: 2.5em;
}

.collapse-icon {
  position: absolute;
  bottom: 0;
  padding: 0.75em;

  color: rgba(255, 255, 255, 0.7);

  transition: 0.2s linear;
}

.rotate-180 {
  transform: rotate(180deg);
  transition: 0.2s linear;
}

.recommender-text {
  font-family: var(--font-family);
  font-size: 0.76em;
}
.spacer {
  flex-grow: 1;
}
.spacers {
  flex-grow: 0.25;
}
</style>
