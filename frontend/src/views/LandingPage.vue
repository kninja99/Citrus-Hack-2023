<script>
    import Header from "../components/Header.vue";
    import NavBar from "../components/NavBar.vue";
    export default {
        name: 'Landing',
        components: {
            Header, NavBar
        }
    }
</script>

<template>
    <div class = "landingPage-body">
        <Header />
        <NavBar />
    <div class = "message">Plan your workout split with AI</div>
    </div>
</template>


