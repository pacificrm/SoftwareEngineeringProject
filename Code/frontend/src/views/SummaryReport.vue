<template>
  <div>
    <h1>Summary Report</h1>
    <canvas ref="barChart"></canvas>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
// eslint-disable-next-line no-unused-vars
import { Chart } from "chart.js/auto";

export default {
  setup() {
    const barChart = ref(null);

    onMounted(() => {
      // Data for the bar graph
      const data = {
        labels: ["Upload 1", "Upload 2", "Upload 3", "Upload 4"],
        datasets: [
          {
            label: "New Students Added",
            data: [400, 700, 673, 577],
            backgroundColor: "rgba(75, 192, 192, 0.2)",
            borderColor: "rgba(75, 192, 192, 1)",
            borderWidth: 1,
          },
          {
            label: "Pass Percentage",
            data: [87.88, 89.87, 86.56, 83.89],
            backgroundColor: "rgba(255, 99, 132, 0.2)",
            borderColor: "rgba(255, 99, 132, 1)",
            borderWidth: 1,
          },
        ],
      };

      // Chart configuration
      const config = {
        type: "bar",
        data: data,
        options: {
          scales: {
            y: {
              beginAtZero: true,
            },
          },
        },
      };

      // Create the bar chart
      // eslint-disable-next-line no-unused-vars
      const chart = new Chart(barChart.value, config);
    });

    return { barChart };
  },
};
</script>

<style scoped>
h1 {
  text-align: center;
  margin-bottom: 20px;
}
</style>
