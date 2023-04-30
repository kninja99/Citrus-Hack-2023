<script>
import NavBtn from '../components/navbtn.vue'
export default {
    components: { NavBtn }
}
</script>



<template>
    <header class="header">
        <div class="title">
            <div class="AI-title1">AI|want</div>
            <div class="AI-title2">2</div>
            <div class="AI-title3">workout</div>
            <div class="AI-logo"></div>
        </div>
        <NavBtn />
        <div class="nav-bar">
            <router-link to="/" custom v-slot="{ navigate }">
                <button class = "nav-link" @click="navigate" role="link">
                    Home
                </button>
            </router-link>
            <router-link to="/" custom v-slot="{ navigate }">
                <button class = "nav-link" @click="navigate" role="link">
                    Workout Generator
                </button>
            </router-link>
            <router-link to="/" custom v-slot="{ navigate }">
                <button class = "nav-link" @click="navigate" role="link">
                    Exercise History
                </button>
            </router-link>
            <router-link to="/onboarding" custom v-slot="{ navigate }">
                <button class = "nav-link" @click="navigate" role="link">
                    Profile
                </button>
            </router-link>
        </div>
    </header>
</template>