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
            <button class="nav1">Home</button>
            <button class="nav2">Workout Generator</button>
            <button class="nav3">Profile</button>
            <button class="nav4">Exercise History</button>
        </div>
    </header>
</template>