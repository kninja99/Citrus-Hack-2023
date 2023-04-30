<script>
import Header from "../components/Header.vue";
export default {
    name: 'Landing',
    components: {
        Header
    }
}
</script>

<template>
    <div class="container">
        <Header />
        <div class="generate-workout">
            <div class="workout"></div>
        </div>
    </div>
</template>