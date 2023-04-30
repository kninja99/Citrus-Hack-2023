<script>
import axios from 'axios';
import Header from "../components/Header.vue";
export default {
    data: function () {
        return {
            workout: null
        };
    },
    components: {
        Header
    },
    methods: {
        generateWorkout: async function () {
            await axios.get('http://localhost:5000/generate')
                .then((res) => {
                    this.workout = res.data;
                })
                .catch((err) => {
                    console.log(err);
                })
        }
    }
}
</script>

<template>
    <div class="container">
        <Header />
        <div class="generate-workout">
            <div class="workout"><button @click="this.generateWorkout" class="form-btn">Generate Workout</button></div>
            <table v-if="this.workout" class="workout-table">
                <tr>
                    <th>Workout Name</th>
                    <th>Muscle Group</th>
                    <th>Difficulty</th>
                    <th>sets</th>
                    <th>reps</th>
                </tr>
                <tr v-for="workout in this.workout">
                    <td v-for="data in workout">{{ data }}</td>
                </tr>
            </table>
        </div>
    </div>
</template>