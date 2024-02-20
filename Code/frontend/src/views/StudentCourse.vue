<template>
  <div class="home" :style="{ 'margin-left': sidebarWidth }">
    <NavBar></NavBar>

    <!-- Completed Courses -->
    <div class="course-list">
      <h1 class="course-heading">Completed Courses</h1>
      <div class="courses">
        <div
          v-for="course in completedCourses"
          :key="course.id"
          class="course-item completed"
        >
          <div class="course-header">
            <h3>{{ course.name }}</h3>
            <RouterLink to="/givefeedback">
              <button @click="giveFeedback(course.id)" class="feedback-button">
                Give Feedback
              </button>
            </RouterLink>
          </div>
          <div class="course-details">
            <div><strong>ID:</strong> {{ course.id }}</div>
            <div><strong>Level:</strong> {{ course.level }}</div>
            <div>
              <strong>Prerequisites:</strong>
              {{ course.prerequisites.join(", ") }}
            </div>
            <div>
              <strong>Corequisites:</strong>
              {{ course.corequisites.join(", ") }}
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Upcoming Courses -->
    <div class="course-list">
      <h1 class="course-heading">Upcoming Courses</h1>
      <div class="courses">
        <div
          v-for="course in upcomingCourses"
          :key="course.id"
          class="course-item upcoming"
        >
          <div class="course-header">
            <h3>{{ course.name }}</h3>
          </div>
          <div class="course-details">
            <div><strong>ID:</strong> {{ course.id }}</div>
            <div><strong>Level:</strong> {{ course.level }}</div>
            <div>
              <strong>Prerequisites:</strong>
              {{ course.prerequisites.join(", ") }}
            </div>
            <div>
              <strong>Corequisites:</strong>
              {{ course.corequisites.join(", ") }}
            </div>
          </div>
        </div>
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
      completedCourses: [
        {
          id: 1,
          name: "BDM",
          prerequisites: [],
          corequisites: [],
          level: "L2",
        },
        {
          id: 2,
          name: "MAD1",
          prerequisites: [],
          corequisites: ["DBMS"],
          level: "L2",
        },
        {
          id: 3,
          name: "DBMS",
          prerequisites: [],
          corequisites: [],
          level: "L2",
        },
        {
          id: 4,
          name: "MAD1 Project",
          prerequisites: [],
          corequisites: ["MAD1"],
          level: "L2",
        },
        {
          id: 5,
          name: "PDSA",
          prerequisites: [],
          corequisites: [],
          level: "L2",
        },
        {
          id: 6,
          name: "MLF",
          prerequisites: [],
          corequisites: [],
          level: "L2",
        },
      ],
      upcomingCourses: [
        {
          id: 7,
          name: "MAD2",
          prerequisites: [],
          corequisites: ["MAD1"],
          level: "L2",
        },
        {
          id: 8,
          name: "MAD2 Project",
          prerequisites: [],
          corequisites: ["MAD2"],
          level: "L2",
        },
        {
          id: 9,
          name: "BA",
          prerequisites: ["BDM"],
          corequisites: [""],
          level: "L2",
        },
        {
          id: 10,
          name: "MLT",
          prerequisites: [""],
          corequisites: ["MLF"],
          level: "L2",
        },
        {
          id: 11,
          name: "JAVA",
          prerequisites: [""],
          corequisites: [""],
          level: "L2",
        },
        {
          id: 12,
          name: "TDS",
          prerequisites: [],
          corequisites: ["BDM"],
          level: "L2",
        },
        {
          id: 13,
          name: "MLP",
          prerequisites: ["MLT"],
          corequisites: [],
          level: "L2",
        },
        {
          id: 14,
          name: "SC",
          prerequisites: [""],
          corequisites: [""],
          level: "L2",
        },
        {
          id: 15,
          name: "BDM Project",
          prerequisites: [""],
          corequisites: ["BDM"],
          level: "L2",
        },
        {
          id: 16,
          name: "MLP Project",
          prerequisites: [],
          corequisites: ["MLP"],
          level: "L2",
        },
      ],
      courses: [
        {
          id: 1,
          name: "BDM",
          prerequisites: ["MAD1"],
          corequisites: [],
          level: "L2",
        },
        {
          id: 2,
          name: "MAD1",
          prerequisites: ["DBMS"],
          corequisites: ["BDM"],
          level: "L2",
        },
        {
          id: 3,
          name: "DBMS",
          prerequisites: [],
          corequisites: ["MAD1"],
          level: "L2",
        },
        {
          id: 4,
          name: "MAD1 Project",
          prerequisites: ["MAD1"],
          corequisites: [],
          level: "L2",
        },
        {
          id: 5,
          name: "PDSA",
          prerequisites: ["MLF"],
          corequisites: [],
          level: "L2",
        },
        {
          id: 6,
          name: "MLF",
          prerequisites: ["MAD2"],
          corequisites: ["PDSA"],
          level: "L2",
        },
        {
          id: 7,
          name: "MAD2",
          prerequisites: [],
          corequisites: ["MLF"],
          level: "L2",
        },
        {
          id: 8,
          name: "MAD2 Project",
          prerequisites: ["MAD2"],
          corequisites: [],
          level: "L2",
        },
        {
          id: 9,
          name: "BA",
          prerequisites: ["MLT"],
          corequisites: ["JAVA"],
          level: "L2",
        },
        {
          id: 10,
          name: "MLT",
          prerequisites: ["JAVA"],
          corequisites: ["BA"],
          level: "L2",
        },
        {
          id: 11,
          name: "JAVA",
          prerequisites: ["TDS"],
          corequisites: ["MLT", "BA"],
          level: "L2",
        },
        {
          id: 12,
          name: "TDS",
          prerequisites: [],
          corequisites: ["JAVA"],
          level: "L2",
        },
        {
          id: 13,
          name: "MLP",
          prerequisites: ["SC"],
          corequisites: [],
          level: "L2",
        },
        {
          id: 14,
          name: "SC",
          prerequisites: ["BDM Project"],
          corequisites: ["MLP"],
          level: "L2",
        },
        {
          id: 15,
          name: "BDM Project",
          prerequisites: ["MLP"],
          corequisites: ["SC"],
          level: "L2",
        },
        {
          id: 16,
          name: "MLP Project",
          prerequisites: ["MLP"],
          corequisites: [],
          level: "L2",
        },
      ],
    };
  },

  methods: {
    giveFeedback(courseId) {
      // Handle giving feedback for a specific course
      console.log("Give Feedback for Course:", courseId);
    },
    giveFeedbackForAll() {
      // Handle giving feedback for all completed courses
      console.log("Give Feedback for All Completed Courses");
    },
    shuffleArray(array) {
      // Shuffle array in place using Fisher-Yates algorithm
      for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
      }
      return array;
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
/* .page-heading {
  font-size: 2em;
  margin-bottom: 16px;
} */

.course-list {
  margin-bottom: 24px;
}

.course-heading {
  font-size: 2em;
  margin-bottom: 12px;
}

.courses {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  margin-left: 30px;
}

.course-item {
  border: 1px solid #ddd;
  border-radius: 8px;
  width: calc(33.33% - 20px);
  box-sizing: border-box;
  transition: box-shadow 0.3s ease;
}

.course-item:hover {
  box-shadow: 0 4px 8px #00274e;
}

.completed {
  background-color: #d3ffd3; /* Light green for completed courses */
}

.upcoming {
  background-color: #d0cece; /* Light gray for upcoming courses */
}

.course-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px;
  background-color: #f2f2f2;
  border-bottom: 1px solid #ddd;
}

.course-details {
  padding: 8px;
}

.feedback-button {
  background-color: #4285f4;
  color: white;
  padding: 8px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}
</style>
