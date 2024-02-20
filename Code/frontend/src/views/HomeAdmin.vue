<template>
  <div class="home" :style="{ 'margin-left': sidebarWidth }">
    <NavBar></NavBar>
    <h1 class="welcome-heading">Welcome, Admin !!</h1>

    <div class="card-container">
      <div
        class="card"
        style="
          border-color: #3498db;
          box-shadow: 0 0 10px rgba(52, 152, 219, 0.3);
        "
      >
        <h2>Total Students</h2>
        <p class="number">1023</p>
      </div>

      <div
        class="card"
        style="
          border-color: #2ecc71;
          box-shadow: 0 0 10px rgba(46, 204, 113, 0.3);
        "
      >
        <h2>Total Courses</h2>
        <p class="number">44</p>
      </div>
    </div>

    <div class="card-container">
      <div
        class="card"
        @click="openSummaryReport"
        style="
          border-color: #e74c3c;
          box-shadow: 0 0 10px rgba(231, 76, 60, 0.3);
        "
      >
        <h2>Student's Data Summary Report</h2>
        <p class="click-to-view">Click to view</p>
      </div>
      <div
        class="card"
        @click="openSatisfactionMetric"
        style="
          border-color: #f39c12;
          box-shadow: 0 0 10px rgba(243, 156, 18, 0.3);
        "
      >
        <h2>Student's Satisfaction Metric</h2>
        <p class="click-to-view">Click to view</p>
      </div>
    </div>
  </div>
</template>
<script>
import NavBar from "../components/NavBar.vue";
import { sidebarWidth } from "../components/state";

export default {
  components: { NavBar },
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
  methods: {
    openSummaryReport() {
      // Handle opening the summary report here
      // You can navigate to a new route or display a modal, for example
      console.log("Opening Student's Data Summary Report");
    },
    openSatisfactionMetric() {
      // Handle opening the satisfaction metric here
      // You can navigate to a new route or display a modal, for example
      console.log("Opening Student's Satisfaction Metric");
    },
  },
  async created() {
    this.auth_token = sessionStorage.getItem("auth-token");
    this.username = sessionStorage.getItem("username");
    console.log(this.username);
    if (!this.auth_token) {
      alert("Please Login to see your dashboard.");
      this.$router.push("/");
    }
    try {
      const response = await fetch("http://127.0.0.1:5000/api/user", {
        method: "GET",
        mode: "cors",
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*",
          "Authentication-Token": `${this.auth_token}`,
        },
      });

      const data = await response.json();
      console.log(data);
    } catch (error) {
      console.log("Error:", error);
    }
  },
};
</script>

<style scoped>
.welcome-heading {
  text-align: center;
  margin-top: 40px;
  font-size: 44px; /* Adjust the font size as needed */
  margin-bottom: 60px;
}

.card-container {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}

.card {
  border: 2px solid;
  border-radius: 8px;
  padding: 20px;
  margin: 0 15px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.card:hover {
  background-color: #ecf0f1;
}

.number {
  color: #3498db; /* Change the color as needed */
  font-weight: bold;
}

.click-to-view {
  color: #e74c3c; /* Change the color as needed */
  font-weight: bold;
}
</style>
