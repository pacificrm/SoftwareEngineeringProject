<template>
  <div>
    <h1>Student Information Upload</h1>
  </div>

  <div
    class="btn-toolbar d-flex justify-content-center"
    role="toolbar"
    aria-label="Toolbar with button groups"
  >
    <div
      class="btn-group mr-2 mb-2"
      role="group"
      aria-label="First group"
      style="margin: 10px"
    >
      <button
        type="button"
        class="btn btn-secondary"
        @click="showUploadModal(1, 'offline_education')"
      >
        Upload Offline Education Details
      </button>
    </div>
    <div
      class="btn-group mr-2 mb-2"
      role="group"
      aria-label="Second group"
      style="margin: 10px"
    >
      <button
        type="button"
        class="btn btn-secondary"
        @click="showUploadModal(2, 'gpa_details')"
      >
        Upload GPA Details
      </button>
    </div>
    <div
      class="btn-group mb-2"
      role="group"
      aria-label="Third group"
      style="margin: 10px"
    >
      <button
        type="button"
        class="btn btn-secondary"
        @click="showUploadModal(3, 'student_academic_info')"
      >
        Upload Student Academic Info
      </button>
    </div>
  </div>

  <div class="container d-flex justify-content-center mt-5">
    <div
      class="card"
      style="max-width: 1000px; padding: 20px; min-width: 600px"
    >
      <div class="card-body">
        <!-- <h5 class="card-title">Data Collection Form</h5> -->

        <form v-if="fromToShow === 1">
          <div class="form-group justify-content-start">
            <label for="rollNumber" style="margin-bottom: 10px"
              >Roll Number</label
            >
            <input
              type="text"
              class="form-control"
              id="rollNumber"
              placeholder="Enter Roll Number"
            />
          </div>

          <div class="form-group">
            <label for="degree" style="margin: 10px">Degree</label>
            <input
              type="text"
              class="form-control"
              id="degree"
              placeholder="Enter Degree"
            />
          </div>

          <div class="form-group">
            <label for="major" style="margin: 10px">Major</label>
            <input
              type="text"
              class="form-control"
              id="major"
              placeholder="Enter Major"
            />
          </div>

          <div class="form-group">
            <label for="endYear" style="margin: 10px">End Year</label>
            <input
              type="text"
              class="form-control"
              id="endYear"
              placeholder="Enter End Year"
              style="margin-bottom: 10px"
            />
          </div>
          <div class="form-group">
            <label for="csvFile" style="margin: 10px; color: red">
              OR Upload CSV
            </label>
            <input
              type="file"
              accept=".csv"
              @change="handleFileUpload"
              class="form-control"
              id="csvFile"
            />
          </div>
          <span></span>
          <RouterLink to="/studentdata">
            <button type="submit" class="btn btn-primary" style="margin: 10px">
              Submit
            </button>
          </RouterLink>
        </form>

        <form v-if="fromToShow === 2">
          <div class="form-group">
            <label for="termId" style="margin-bottom: 10px">Term ID</label>
            <input
              v-model="formData.term_id"
              type="text"
              class="form-control"
              id="termId"
              placeholder="Enter Term ID"
            />
          </div>

          <div class="form-group">
            <label for="rollNumber" style="margin: 10px">Roll Number</label>
            <input
              v-model="formData.roll_number"
              type="text"
              class="form-control"
              id="rollNumber"
              placeholder="Enter Roll Number"
            />
          </div>

          <div class="form-group">
            <label for="sgpa" style="margin: 10px">SGPA</label>
            <input
              v-model="formData.sgpa"
              type="number"
              step="0.1"
              class="form-control"
              id="sgpa"
              placeholder="Enter SGPA"
            />
          </div>

          <div class="form-group">
            <label for="cgpa" style="margin: 10px">CGPA</label>
            <input
              v-model="formData.cgpa"
              type="number"
              step="0.1"
              class="form-control"
              id="cgpa"
              placeholder="Enter CGPA"
            />
          </div>
          <div class="form-group">
            <label for="csvFile" style="margin: 10px; color: red">
              OR Upload CSV
            </label>
            <input
              type="file"
              accept=".csv"
              @change="handleFileUpload"
              class="form-control"
              id="csvFile"
            />
          </div>
          <RouterLink to="/studentdata">
            <button type="submit" class="btn btn-primary" style="margin: 10px">
              Submit
            </button>
          </RouterLink>
        </form>

        <form v-if="fromToShow === 3">
          <div class="form-group">
            <label for="termId" style="margin-bottom: 10px">Term ID</label>
            <input
              v-model="formData.term_id"
              type="text"
              class="form-control"
              id="termId"
              placeholder="Enter Term ID"
            />
          </div>

          <div class="form-group">
            <label for="rollNumber" style="margin: 10px">Roll Number</label>
            <input
              v-model="formData.roll_number"
              type="text"
              class="form-control"
              id="rollNumber"
              placeholder="Enter Roll Number"
            />
          </div>

          <div class="form-group">
            <label for="courseId" style="margin: 10px">Course ID</label>
            <input
              v-model="formData.course_id"
              type="text"
              class="form-control"
              id="courseId"
              placeholder="Enter Course ID"
            />
          </div>

          <div class="form-group">
            <label for="avgGa" style="margin: 10px">Average GA Score</label>
            <input
              v-model="formData.avg_ga"
              type="number"
              step="0.1"
              class="form-control"
              id="avgGa"
              placeholder="Enter Average GA"
            />
          </div>

          <div class="form-group">
            <label for="quiz1" style="margin: 10px">Quiz 1 Score</label>
            <input
              v-model="formData.quiz1"
              type="number"
              step="0.1"
              class="form-control"
              id="quiz1"
              placeholder="Enter Quiz 1"
            />
          </div>

          <div class="form-group">
            <label for="quiz2" style="margin: 10px">Quiz 2 Score</label>
            <input
              v-model="formData.quiz2"
              type="number"
              step="0.1"
              class="form-control"
              id="quiz2"
              placeholder="Enter Quiz 2"
            />
          </div>

          <div class="form-group">
            <label for="endTerm" style="margin: 10px">End Term Score</label>
            <input
              v-model="formData.end_term"
              type="number"
              step="0.1"
              class="form-control"
              id="endTerm"
              placeholder="Enter End Term"
            />
          </div>

          <div class="form-group">
            <label for="oppe1" style="margin: 10px">OPPE 1 Score</label>
            <input
              v-model="formData.oppe1"
              type="number"
              step="0.1"
              class="form-control"
              id="oppe1"
              placeholder="Enter OPPE 1"
            />
          </div>

          <div class="form-group">
            <label for="oppe2" style="margin: 10px">OPPE 2 Score</label>
            <input
              v-model="formData.oppe2"
              type="number"
              step="0.1"
              class="form-control"
              id="oppe2"
              placeholder="Enter OPPE 2"
            />
          </div>

          <div class="form-group">
            <label for="project" style="margin: 10px">Project Score</label>
            <input
              v-model="formData.project"
              type="number"
              step="0.1"
              class="form-control"
              id="project"
              placeholder="Enter Project"
            />
          </div>

          <div class="form-group">
            <label for="finalScore" style="margin: 10px"
              >Final Score Score</label
            >
            <input
              v-model="formData.final_score"
              type="number"
              step="0.1"
              class="form-control"
              id="finalScore"
              placeholder="Enter Final Score"
            />
          </div>
          <div class="form-group">
            <label for="csvFile" style="margin: 10px; color: red">
              OR Upload CSV
            </label>
            <input
              type="file"
              accept=".csv"
              @change="handleFileUpload"
              class="form-control"
              id="csvFile"
            />
          </div>
          <RouterLink to="/studentdata">
            <button type="submit" class="btn btn-primary" style="margin: 10px">
              Submit
            </button>
          </RouterLink>
        </form>
      </div>
    </div>
  </div>

  <div v-if="responseMessage">{{ responseMessage }}</div>
  <!-- </div> -->
</template>

<script>
export default {
  components: {},
  data() {
    return {
      fromToShow: 1,
      uploadModalVisible: false,
      uploadModalType: "",
      formData: {},
      responseMessage: "",
    };
  },
  methods: {
    showUploadModal(formNo, type) {
      this.fromToShow = formNo;
      this.uploadModalType = type;
      this.formData = {};
      this.responseMessage = "";
    },
    handleFileUpload(event) {
      const file = event.target.files[0];

      // You can now use 'file' to handle the CSV file upload.
      console.log("Uploaded CSV File:", file);
    },
    closeUploadModal() {
      this.uploadModalVisible = false;
    },
    async submitForm() {
      this.$router.push("/studentdata");
      // let url = "";
      // switch (this.uploadModalType) {
      //   case "offline_education":
      //     url = "http://127.0.0.1:5000/api/add_offline_education";
      //     break;
      //   case "gpa_details":
      //     url = "http://127.0.0.1:5000/api/add_gpa";
      //     break;
      //   case "student_academic_info":
      //     url = "http://127.0.0.1:5000/api/add_student_acamdemic_info";
      //     break;
      // }
      // console.log("sending fetch POST");
      // fetch(url, {
      //   mode: "cors",
      //   method: "POST",
      //   headers: {
      //     "Access-Control-Allow-Origin": "*",
      //     "Content-Type": "application/json",
      //   },
      //   body: JSON.stringify(this.formData),
      // })
      //   .then((response) => {
      //     // Log the response code to the console
      //     console.log("Response Code:", response.status);
      //     return response.json();
      //   })
      //   .then((data) => {
      //     this.responseMessage = data.message;
      //     this.closeUploadModal();
      //   })
      //   .catch((error) => {
      //     this.responseMessage = "Error: " + error.message;
      //   });
    },
  },
};
</script>

<style>
form label {
  text-align: left;
}
</style>
