<template>
  <div class="home" :style="{ 'margin-left': sidebarWidth }">
    <NavBar></NavBar>
    <h1 class="page-heading">Give Feedback</h1>
    <div class="feedback-form">
      <form @submit.prevent="submitFeedback">
        <label for="rating">Rating (1-5):</label>
        <input
          type="number"
          id="rating"
          v-model="feedback.rating"
          min="1"
          max="5"
          required
        />

        <label for="remarks">Remarks:</label>
        <textarea id="remarks" v-model="feedback.remarks" rows="4"></textarea>

        <div class="button-container">
          <button type="button" @click="goBack">Back</button>
          <button type="submit">Submit Feedback</button>
        </div>
      </form>
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
      feedback: {
        rating: null,
        remarks: "",
      },
    };
  },
  methods: {
    async submitFeedback() {
      // Handle feedback submission logic
      console.log("Submitting Feedback:", this.feedback);

      // Perform API request or data handling as needed

      // Reset the form after submission
      this.feedback = {
        rating: null,
        remarks: "",
      };

      // Navigate back to the previous page
      this.$router.go(-1);
    },
    goBack() {
      // Navigate back to the previous page
      this.$router.go(-1);
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

<style scoped>
.page-heading {
  font-size: 2em;
  margin-bottom: 16px;
}

.feedback-form {
  max-width: 400px;
  margin: 0 auto;
}

label {
  display: block;
  margin-bottom: 8px;
}

input,
textarea {
  width: 100%;
  padding: 8px;
  margin-bottom: 16px;
}

.button-container {
  display: flex;
  justify-content: space-between;
}

button {
  background-color: #4caf50;
  color: white;
  padding: 8px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button[type="button"] {
  background-color: #333;
}
</style>
