<template>
  <div class="home" :style="{ 'margin-left': sidebarWidth }">
    <NavBar></NavBar>
    <h1 class="page-heading">Course Data</h1>
    <div class="course-list">
      <div v-for="course in courses" :key="course.id" class="course-item">
        <div class="course-header">
          <h3>{{ course.name }}</h3>
          <div class="icons">
            <span
              @click="editCourse(course.id)"
              class="icon edit-icon"
              title="Edit"
            >
              <i class="fas fa-pencil-alt"></i>
            </span>
            <span
              @click="deleteCourse(course.id)"
              class="icon delete-icon"
              title="Delete"
            >
              <i class="fas fa-trash-alt"></i>
            </span>
          </div>
        </div>
        <div class="course-details">
          <div><strong>ID:</strong> {{ course.id }}</div>
          <div><strong>Level:</strong> {{ course.level }}</div>
          <div>
            <strong>Prerequisites:</strong>
            {{ course.prerequisites.join(", ") }}
          </div>
          <div>
            <strong>Corequisites:</strong> {{ course.corequisites.join(", ") }}
          </div>
        </div>
      </div>
    </div>
    <div class="add-course-button">
      <router-link to="/addcourse">
        <button @click="addCourse">Add Course</button>
      </router-link>
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
      courses: [
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
    };
  },
  methods: {
    editCourse(courseId) {
      // Handle course edit
      console.log("Edit Course:", courseId);

      // Find the course with the given ID
      const courseToEdit = this.courses.find(
        (course) => course.id === courseId
      );

      // Assuming /editcourse is the route for editing a course
      this.$router.push({
        path: "/editcourse",
        query: {
          courseId: courseToEdit.id,
          courseName: courseToEdit.name,
          courseCorequisites: courseToEdit.corequisites.join(", "),
          coursePrerequisites: courseToEdit.prerequisites.join(", "),
          courseLevel: courseToEdit.level,
          // ... add other fields as needed
        },
      });
    },

    deleteCourse(courseId) {
      // Find the course with the given ID
      const courseToDelete = this.courses.find(
        (course) => course.id === courseId
      );

      // Display a confirmation dialog
      const isConfirmed = window.confirm(
        `Do you want to delete the course "${courseToDelete.name}"?`
      );

      if (isConfirmed) {
        // Handle course deletion
        console.log("Delete Course:", courseId);

        // Find the index of the course with the given ID
        const index = this.courses.findIndex(
          (course) => course.id === courseId
        );

        // Remove the course from the courses array
        if (index !== -1) {
          this.courses.splice(index, 1);
        }
      } else {
        // User clicked "Cancel," do nothing or add additional logic
        console.log("Course deletion canceled");
      }
    },

    addCourse() {
      // Handle adding a new course
      console.log("Add Course", this.course);

      // Assuming this.course is the newly added course
      this.courses.push(this.course);

      // Reset the form or create a new course object
      this.course = {
        name: "",
        id: "",
        corequisites: "",
        prerequisites: "",
        level: "",
      };

      // Navigate to /coursedata
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

.course-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.course-item {
  border: 1px solid #ddd;
  border-radius: 8px;
  margin: 10px;
  padding: 10px;
  width: calc(33.33% - 20px);
  box-sizing: border-box;
  margin-bottom: 16px;
  transition: box-shadow 0.3s ease;
}

.course-item:hover {
  box-shadow: 0 4px 8px #00274e;
}

.course-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px;
  background-color: #f2f2f2;
  border-bottom: 1px solid #ddd;
}

.icons {
  display: flex;
  gap: 8px;
}

.icon {
  cursor: pointer;
}

.edit-icon {
  color: green;
}

.delete-icon {
  color: red;
}

.course-details {
  padding: 8px;
}

.add-course-button {
  position: absolute;
  top: 0;
  right: 0;
  margin: 16px;
}

button {
  background-color: #4caf50;
  color: white;
  padding: 8px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}
</style>
