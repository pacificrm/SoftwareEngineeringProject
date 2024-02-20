<template>
  <div class="start">
    <StartPage v-show="t" />
    <LoginSignup
      v-show="!t"
      @signup="(signupData = $event), register()"
      @login="(loginData = $event), login()"
      :serror_1="signupData.error_1"
      :serror_2="signupData.error_2"
      :lerror_1="loginData.error_1"
      :lerror_2="loginData.error_2"
      :success="signupData.success"
    />
  </div>
</template>

<script>
import StartPage from "@/components/StartPage.vue";
import LoginSignup from "@/components/LoginSignup.vue";

const API_BASE_URL = "http://127.0.0.1:5000/api/user";
const LOGIN_URL = "http://127.0.0.1:5000/login?include_auth_token";

export default {
  name: "StartView",
  components: {
    StartPage,
    LoginSignup,
  },
  data() {
    return {
      t: true,
      signupData: {
        email: null,
        username: null,
        password1: null,
        password2: null,
        error_1: "",
        error_2: "",
        success: "",
      },
      loginData: {
        username: null,
        password: null,
        error_1: "",
        error_2: "",
        auth: null,
        is_authenticated: false,
      },
    };
  },
  async created() {
    setTimeout(() => (this.t = false), 7000);
    sessionStorage.clear();
    localStorage.clear();
  },
  async updated() {
    sessionStorage.clear();
    localStorage.clear();
  },
  methods: {
    async register() {
      this.clearSignupErrors();

      if (
        this.emailValidation(this.signupData.email) &&
        this.passValidation(this.signupData.password1) &&
        this.passConfirmation(
          this.signupData.password1,
          this.signupData.password2
        )
      ) {
        try {
          const res = await this.makeApiRequest("POST", API_BASE_URL, {
            email: this.signupData.email,
            username: this.signupData.username,
            password1: this.signupData.password1,
          });

          if (res.ok) {
            console.log("registered");
            this.signupData.success =
              "Signed up successfully!! Login to continue.";
          } else {
            this.handleRegistrationError(res.status);
          }
        } catch (error) {
          console.log("Registration Failed: ", error);
        }
      } else if (!this.emailValidation(this.signupData.email)) {
        this.signupData.error_1 = "Please enter a valid email";
      } else if (!this.passValidation(this.signupData.password1)) {
        this.signupData.error_1 = "Password requires at least 8 characters.";
      } else if (this.signupData.password1 !== this.signupData.password2) {
        this.signupData.error_1 = "Passwords do not match.";
      }
    },
    async login() {
      this.clearLoginErrors();

      try {
        const res = await this.makeApiRequest("POST", LOGIN_URL, {
          username: this.loginData.username,
          password: this.loginData.password,
          is_authenticated: true,
        });

        const data = await res.json();

        if (res.ok) {
          this.loginData.auth = data.response.user.authentication_token;
          sessionStorage.setItem("auth-token", this.loginData.auth);
          sessionStorage.setItem("username", this.loginData.username);

          if (this.loginData.username.toLowerCase() === "admin") {
            this.$router.push("/adminhome");
          } else {
            this.$router.push("/studenthome");
          }
        } else {
          this.handleLoginError(data.response.errors);
        }
      } catch (error) {
        console.log("Login Failed: ", error);
      }
    },
    async makeApiRequest(method, url, body) {
      return fetch(url, {
        mode: "cors",
        method: method,
        headers: {
          "Access-Control-Allow-Origin": "*",
          "Content-Type": "application/json",
        },
        body: JSON.stringify(body),
      });
    },
    clearSignupErrors() {
      this.signupData.error_1 = null;
      this.signupData.error_2 = null;
      this.signupData.success = null;
    },
    clearLoginErrors() {
      this.loginData.error_1 = null;
      this.loginData.error_2 = null;
    },
    handleRegistrationError(status) {
      if (status === 400) {
        this.signupData.error_1 = "Email already exists!! Try again.";
      } else if (status === 401) {
        this.signupData.error_1 = "Username already exists!! Try again.";
      } else {
        this.signupData.error_1 = "Registration Failed!! Try again.";
      }
    },
    handleLoginError(errors) {
      if (errors[1]) {
        this.loginData.error_1 = errors[1];
      }
      this.loginData.error_2 = errors[0];
    },
    emailValidation: function (email) {
      var result =
        /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,3}))$/;
      return result.test(email);
    },
    passValidation: function (passs) {
      var result = /.{8,}/;
      return result.test(passs);
    },
    passConfirmation: function (passs1, passs2) {
      return passs1 === passs2;
    },
  },
};
</script>
