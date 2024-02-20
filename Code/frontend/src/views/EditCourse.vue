<!-- EditCourse.vue -->
<template>
  <div class="home" :style="{ 'margin-left': sidebarWidth }">
    <NavBar></NavBar>
    <h1 class="page-heading">Edit Course</h1>
    <div class="course-form">
      <form @submit.prevent="submitForm">
        <!-- Populate the form fields with the provided query parameters -->
        <label for="courseName">Course Name:</label>
        <input type="text" id="courseName" v-model="course.name" required />

        <label for="courseId">Course ID:</label>
        <input type="text" id="courseId" v-model="course.id" required />

        <label for="corequisites">Corequisites (comma-separated):</label>
        <input type="text" id="corequisites" v-model="course.corequisites" />

        <label for="prerequisites">Prerequisites (comma-separated):</label>
        <input type="text" id="prerequisites" v-model="course.prerequisites" />

        <label for="level">Level (L1 to L4):</label>
        <input
          type="text"
          id="level"
          v-model="course.level"
          pattern="[Ll][1-4]"
        />

        <div class="button-container">
          <button type="button" @click="goBack">Back</button>
          <button type="submit">Update Course</button>
        </div>
      </form>
    </div>
  </div>
</template>

// EditCourse.vue
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
      course: {
        name: this.$route.query.courseName || "",
        id: this.$route.query.courseId || "",
        corequisites: this.$route.query.courseCorequisites || "",
        prerequisites: this.$route.query.coursePrerequisites || "",
        level: this.$route.query.courseLevel || "",
      },
    };
  },
  methods: {
    async submitForm() {
      // Handle form submission logic
      console.log("Editing Course:", this.course);

      // Perform API request or data handling as needed

      // Reset the form after submission
      this.course = {
        name: "",
        id: "",
        corequisites: "",
        prerequisites: "",
        level: "",
      };

      // Navigate back to /coursedata
      this.$router.push("/coursedata");
    },
    goBack() {
      // Navigate back to /coursedata
      this.$router.push("/coursedata");
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
.page-heading {
  font-size: 2em;
  margin-bottom: 16px;
}

.course-form {
  max-width: 400px;
  margin: 0 auto;
}

label {
  display: block;
  margin-bottom: 8px;
}

input {
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
