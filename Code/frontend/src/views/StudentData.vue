<template>
  <div class="home" :style="{ 'margin-left': sidebarWidth }">
    <NavBar></NavBar>

    <!-- Students Data Page -->
    <div class="students-data">
      <h1 class="page-heading">Students Data</h1>

      <!-- List of Previous Uploads -->
      <div v-if="previousUploads.length > 0">
        <h2 class="section-heading">Previous Uploads</h2>
        <ul class="upload-list">
          <li
            v-for="upload in previousUploads"
            :key="upload.id"
            class="upload-row"
          >
            <span class="upload-label">Upload {{ upload.id }}:</span>
            <span>{{ upload.uploadDate }}</span>
            <span @click="editUpload(upload.id)" class="icon edit-icon">
              <i class="fas fa-edit"></i>
            </span>
            <span @click="deleteUpload(upload.id)" class="icon delete-icon">
              <i class="fas fa-trash-alt"></i>
            </span>
          </li>
        </ul>
      </div>

      <!-- Upload Data Button -->
      <RouterLink to="/uploaddata">
        <button @click="uploadData" class="upload-button">
          <i class="fas fa-cloud-upload-alt"></i> Upload Data
        </button>
      </RouterLink>
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
      auth_token: null,
      previousUploads: [
        { id: 6, uploadDate: "03/05/2023" },
        { id: 5, uploadDate: "29/12/2022" },
        { id: 4, uploadDate: "30/08/2022" },
        { id: 3, uploadDate: "30/04/2022" },
        { id: 2, uploadDate: "03/01/2022" },
        { id: 1, uploadDate: "01/09/2021" },
      ],
    };
  },
  methods: {
    async uploadData() {
      // Handle upload data logic
      console.log("Uploading Data");

      // Navigate to the upload data page or perform API request as needed
    },
    editUpload(uploadId) {
      // Handle edit upload logic
      console.log("Editing Upload:", uploadId);
    },
    deleteUpload(uploadId) {
      // Handle delete upload logic
      console.log("Deleting Upload:", uploadId);
    },
  },
  async created() {
    this.auth_token = sessionStorage.getItem("auth-token");
    this.username = sessionStorage.getItem("username");
    console.log(this.username);

    // Fetch previous uploads data
    // You can replace the URL and headers with your actual API endpoint
    try {
      const response = await fetch(
        "http://127.0.0.1:5000/api/previous-uploads",
        {
          method: "GET",
          mode: "cors",
          headers: {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Authentication-Token": `${this.auth_token}`,
          },
        }
      );

      const data = await response.json();
      this.previousUploads = data; // Update previousUploads with the fetched data
    } catch (error) {
      console.log("Error fetching previous uploads:", error);
    }
  },
};
</script>

<style scoped>
.page-heading {
  font-size: 2em;
  margin-bottom: 16px;
}

.section-heading {
  font-size: 1.5em;
  margin-bottom: 12px;
}

.upload-list {
  list-style: none;
  padding: 0;
}

.upload-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 8px;
  margin-bottom: 8px;
  margin-left: 10px;
  margin-right: 10px;
  transition: box-shadow 0.3s ease;
}

.upload-row:hover {
  box-shadow: 0 4px 8px #00274e;
}

.upload-label {
  margin-right: 8px;
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

.upload-button {
  background-color: #4caf50;
  color: white;
  padding: 8px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.upload-button i {
  margin-right: 8px;
}

.upload-button:hover {
  background-color: #45a049;
}
</style>
