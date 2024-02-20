import { createRouter, createWebHistory } from "vue-router";
import HomeStudent from "../views/HomeStudent.vue";

const routes = [
  {
    path: "/studenthome",
    name: "studenthome",
    component: HomeStudent,
  },
  {
    path: "/adminhome",
    name: "adminhome",
    component: () => import("../views/HomeAdmin"),
  },
  {
    path: "/popularlearningpaths",
    name: "popularlearningpaths",
    component: () => import("../views/PopularLearningPaths"),
  },
  {
    path: "/learningpathfeedback",
    name: "learningpathfeedback",
    component: () => import("../views/LearningPathFeedback"),
  },
  {
    path: "/alllearningpaths",
    name: "alllearningpaths",
    component: () => import("../views/AllLearningPaths"),
  },
  {
    path: "/mylearningpaths",
    name: "mylearningpaths",
    component: () => import("../views/MyLearningPaths"),
  },
  {
    path: "/coursedata",
    name: "coursedata",
    component: () => import("../views/CourseData"),
  },
  {
    path: "/addcourse",
    name: "addcourse",
    component: () => import("../views/AddCourse"),
  },
  {
    path: "/editcourse",
    name: "editcourse",
    component: () => import("../views/EditCourse"),
  },
  {
    path: "/courses",
    name: "courses",
    component: () => import("../views/StudentCourse"),
  },
  {
    path: "/givefeedback",
    name: "givefeedback",
    component: () => import("../views/GiveFeedback"),
  },

  {
    path: "/loginsignup",
    name: "loginsignup",
    component: () => import("../components/LoginSignup.vue"),
  },
  {
    path: "/studentdata",
    name: "studentdata",
    component: () => import("../views/StudentData.vue"),
  },
  {
    path: "/summaryreport",
    name: "summaryreport",
    component: () => import("../views/SummaryReport.vue"),
  },
  {
    path: "/uploaddata",
    name: "uploaddata",
    component: () => import("../views/DataUpload.vue"),
  },
  {
    path: "/",
    name: "start",
    component: () => import("../views/StartView.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
