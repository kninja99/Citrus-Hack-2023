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
            <button class="nav-link">Home</button>
            <button class="nav-link">Workout Generator</button>
            <button class="nav-link">Profile</button>
            <button class="nav-link">Exercise History</button>
        </div>
    </header>
</template>