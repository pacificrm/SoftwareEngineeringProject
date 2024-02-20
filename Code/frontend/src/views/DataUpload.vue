<template>
  <div class="home" :style="{ 'margin-left': sidebarWidth }">
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD"
      crossorigin="anonymous"
    />
    <NavBar></NavBar>
    <upLoad></upLoad>
  </div>
</template>

<script>
import NavBar from "../components/NavBar.vue";
import { sidebarWidth } from "../components/state";
import upLoad from "../components/upLoad.vue";

export default {
  name: "UploadData",
  components: { NavBar, upLoad },
  setup() {
    return { sidebarWidth };
  },
  data() {
    return {
      username: "",
      email: null,
      auth_token: null,
      users: null,
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
    return fetch("http://127.0.0.1:5000/api/user", {
      method: "GET",
      mode: "cors",
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Authentication-Token": `${this.auth_token}`,
      },
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(this.blogs);
        console.log(data);
      })
      .catch((error) => console.log("1st", error));
  },
};
</script>
