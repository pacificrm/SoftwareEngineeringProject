<template>
  <div class="feedback-form">
    <h2 class="form-heading">Give Feedback</h2>
    <label for="rating">Rating:</label>
    <input
      type="number"
      id="rating"
      v-model="feedback.rating"
      min="1"
      max="5"
    />
    <label for="remarks">Remarks:</label>
    <textarea id="remarks" v-model="feedback.remarks"></textarea>
    <div class="buttons">
      <button @click="submitFeedback">Submit</button>
      <button @click="cancelFeedback">Cancel</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      feedback: {
        rating: 1,
        remarks: "",
      },
    };
  },
  methods: {
    submitFeedback() {
      this.$emit("submit", this.feedback);
      this.resetForm();
    },
    cancelFeedback() {
      this.$emit("cancel");
      this.resetForm();
    },
    resetForm() {
      this.feedback = { rating: 1, remarks: "" };
    },
  },
};
</script>

<style scoped>
/* Add your styles if needed */
.feedback-form {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 16px;
  width: 300px;
  background-color: #fff;
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.form-heading {
  font-size: 1.5em;
  margin-bottom: 16px;
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
  border: 1px solid #ddd;
  border-radius: 4px;
}

.buttons {
  display: flex;
  justify-content: space-between;
}

button {
  padding: 8px 16px;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #45a049;
}
</style>
