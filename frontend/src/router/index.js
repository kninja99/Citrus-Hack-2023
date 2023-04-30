import { createRouter, createWebHistory } from 'vue-router';
import LoginView from '../views/LoginView.vue';
import OnBoarding from '../views/OnBoardingView.vue';
import LandingPage from '../views/LandingPage.vue';
import GenerateWorkoutPage from '../views/GenerateWorkoutView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: LandingPage,
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
    },
    {
      path: '/onboarding',
      name: 'onBoarding',
      component: OnBoarding,
    },
    {
      path: '/generate-workout',
      name: 'generateWorkout',
      component: GenerateWorkoutPage,
    },
  ],
});

export default router;
