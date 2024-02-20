<template>
  <div class="home" :style="{ 'margin-left': sidebarWidth }">
    <NavBar></NavBar>
    <!-- <h1 class="section-heading">Welcome Learner!</h1> -->
    <h1 class="section-heading">Welcome Learner !!</h1>
    <div class="center-container">
      <div
        v-for="(card, index) in sortedLearningPathCards"
        :key="index"
        class="learning-path-card"
      >
        <img :src="card.image" :alt="card.title" class="card-image" />
        <div class="card-content">
          <h3 class="card-title">{{ card.title }}</h3>
          <div class="card-rating">Rating: {{ card.rating }}</div>
          <div class="card-created">
            Created: {{ formatDate(card.created) }}
          </div>
          <RouterLink to="/givefeedback">
            <button class="feedback-button" @click="showFeedbackForm(card)">
              Give Feedback
            </button>
          </RouterLink>
        </div>
      </div>
    </div>
    <FeedbackForm
      v-if="showForm"
      @submit="submitFeedback"
      @cancel="cancelFeedback"
    />
    <button class="create-learning-path" @click="openLearningPathCreator">
      Create New Learning Path
    </button>
  </div>
</template>

<script>
import NavBar from "../components/NavBar.vue";
import { sidebarWidth } from "../components/state";
import FeedbackForm from "@/components/FeedbackForm.vue";

export default {
  name: "CurrentLearningPath",
  components: { NavBar, FeedbackForm },
  setup() {
    return { sidebarWidth, showForm: false }; // Initialize showForm here
  },
  data() {
    return {
      username: "",
      auth_token: null,
      learningPathCards: [
        {
          image: require("@/assets/learning_path_1.png"),
          title: "Current Learning Path",
          rating: 4.5,
          created: "2023-01-01T12:00:00Z",
        },
      ],
    };
  },
  computed: {
    sortedLearningPathCards() {
      return [...this.learningPathCards].sort((a, b) => b.rating - a.rating);
    },
  },
  methods: {
    formatDate(dateString) {
      const options = { year: "numeric", month: "long", day: "numeric" };
      return new Date(dateString).toLocaleDateString(undefined, options);
    },
    showFeedbackForm(learningPath) {
      this.selectedLearningPath = learningPath;
      this.showForm = true;
    },
    submitFeedback(feedback) {
      // Handle feedback submission here
      console.log("Submitting feedback:", feedback);
      // Reset selected learning path and hide the form after submission
      this.selectedLearningPath = null;
      this.showForm = false;
    },
    cancelFeedback() {
      // Reset selected learning path and hide the form on cancel
      this.selectedLearningPath = null;
      this.showForm = false;
    },
    openLearningPathCreator() {
      window.open(
        "https://huggingface.co/spaces/GenAI-Warrior/course_recommender",
        "_blank"
      );
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
.center-container {
  display: flex;
  justify-content: center;
  align-items: center;
}

.learning-path-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  margin: 1px;
  padding: 1px;
  border-color: #f39c12;
  box-shadow: 0 0 10px rgba(18, 217, 243, 0.3);
  width: calc((100% - (2 * 8px) - {{sidebarWidth}}) / 3);
  box-sizing: border-box;
  height: 430px;
}

.card-image {
  width: 100%;
  height: 290px;
  object-fit: cover;
  border-radius: 8px;
}

.card-content {
  margin-top: 8px;
}

.card-title {
  font-size: 1.2em;
  margin-bottom: 4px;
}

.card-rating {
  margin-bottom: 4px;
}

.card-created {
  font-size: 0.8em;
  color: #666;
  margin-bottom: 4px;
}

.feedback-button {
  background-color: #4caf50;
  color: white;
  padding: 4px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
.section-heading {
  font-size: 2em;
  margin-bottom: 16px;
  text-align: center;
  color: #333;
  font-weight: bold;
  text-transform: uppercase;
}
.create-learning-path {
  background-color: #2196f3;
  color: white;
  padding: 10px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-bottom: 16px;
  margin-top: 16px;
  font-size: 1em;
}
</style>
