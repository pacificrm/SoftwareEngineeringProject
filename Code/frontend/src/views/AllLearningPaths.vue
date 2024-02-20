<template>
  <div class="home" :style="{ 'margin-left': sidebarWidth }">
    <NavBar></NavBar>
    <h1 class="section-heading">Learning Paths</h1>
    <div class="learning-path-cards">
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
            <button class="feedback-button">Give Feedback</button>
          </RouterLink>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import NavBar from "../components/NavBar.vue";
import { sidebarWidth } from "../components/state";

export default {
  name: "AllLearningPaths",
  components: { NavBar },
  setup() {
    return { sidebarWidth };
  },
  data() {
    return {
      username: "",
      auth_token: null,
      learningPathCards: [
        {
          image: require("@/assets/learning_path_1.png"),
          title: "Learning Path 1",
          rating: 4.5,
          created: "2021-12-01T12:00:00Z",
        },
        {
          image: require("@/assets/learning_path_2.png"),
          title: "Learning Path 2",
          rating: 3.8,
          created: "2021-12-15T12:00:00Z",
        },
        {
          image: require("@/assets/learning_path_3.png"),
          title: "Learning Path 3",
          rating: 4.2,
          created: "2021-12-30T12:00:00Z",
        },
        {
          image: require("@/assets/learning_path_4.png"),
          title: "Learning Path 4",
          rating: 4.0,
          created: "2022-01-10T12:00:00Z",
        },
        {
          image: require("@/assets/learning_path_5.png"),
          title: "Learning Path 5",
          rating: 3.5,
          created: "2022-05-05T12:00:00Z",
        },
        {
          image: require("@/assets/learning_path_6.png"),
          title: "Learning Path 6",
          rating: 4.8,
          created: "2022-05-20T12:00:00Z",
        },
        {
          image: require("@/assets/learning_path_7.png"),
          title: "Learning Path 7",
          rating: 4.3,
          created: "2022-05-31T12:00:00Z",
        },
        {
          image: require("@/assets/learning_path_8.png"),
          title: "Learning Path 8",
          rating: 3.9,
          created: "2022-08-15T12:00:00Z",
        },
        {
          image: require("@/assets/learning_path_9.png"),
          title: "Learning Path 9",
          rating: 4.7,
          created: "2022-09-20T12:00:00Z",
        },
        {
          image: require("@/assets/learning_path_10.png"),
          title: "Learning Path 10",
          rating: 4.1,
          created: "2022-09-30T12:00:00Z",
        },
        {
          image: require("@/assets/learning_path_1.png"),
          title: "Learning Path 11",
          rating: 3.6,
          created: "2023-06-10T12:00:00Z",
        },
        {
          image: require("@/assets/learning_path_2.png"),
          title: "Learning Path 12",
          rating: 4.4,
          created: "2023-07-01T12:00:00Z",
        },
        {
          image: require("@/assets/learning_path_3.png"),
          title: "Learning Path 13",
          rating: 3.9,
          created: "2023-07-15T12:00:00Z",
        },
        {
          image: require("@/assets/learning_path_4.png"),
          title: "Learning Path 14",
          rating: 4.2,
          created: "2023-07-30T12:00:00Z",
        },
        {
          image: require("@/assets/learning_path_5.png"),
          title: "Learning Path 15",
          rating: 4.6,
          created: "2023-08-10T12:00:00Z",
        },
      ],
    };
  },
  computed: {
    sortedLearningPathCards() {
      return [...this.learningPathCards].sort(
        (a, b) => new Date(b.created) - new Date(a.created)
      );
    },
  },
  methods: {
    formatDate(dateString) {
      const options = { year: "numeric", month: "long", day: "numeric" };
      return new Date(dateString).toLocaleDateString(undefined, options);
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
.section-heading {
  font-size: 1.5em;
  margin-bottom: 16px;
}

.learning-path-cards {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  margin: 0 -8px;
}

.learning-path-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  margin: 3px;
  padding: 1px;
  /* border-color: #8d0579;
  box-shadow: 0 0 10px rgba(18, 217, 243, 0.3); */
  width: calc((100% - (2 * 8px) - {{sidebarWidth}}) / 3);
  box-sizing: border-box;
  height: 400px; /* Adjust the height as needed */
}

.card-image {
  width: 100%;
  height: 250px; /* Adjust the height as needed */
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
</style>
