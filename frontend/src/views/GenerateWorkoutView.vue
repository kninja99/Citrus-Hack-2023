<script>
import axios from 'axios';
import Header from "../components/Header.vue";
export default {
    data: function () {
        return {
            muscelTarget: "Chest",
            workout: null
        };
    },
    components: {
        Header
    },
    methods: {
        generateWorkout: async function () {
            console.log(this.muscelTarget);
            await axios.get('http://localhost:5000/generate')
                .then((res) => {
                    this.workout = res.data;
                })
                .catch((err) => {
                    console.log(err);
                });
        }
    }
}
</script>

<template>
    <div class="container">
        <Header />
        <div class="generate-workout">
            <div class="workout">
                <div class="generation-form">
                    <p class="ai-motivation-text">The only bad workout is the one that didn't happen. Generate your workout
                        now
                        using AI.</p>
                    <div class="workout-inputs">
                        <select v-model="muscelTarget" id="muscle-selector" aria-placeholder="Please Select a Workout">
                            <option value="Chest" selected>Chest</option>
                            <option value="Triceps">Triceps</option>
                            <option value="Biceps">Biceps</option>
                            <option value="Shoulders">Shoulders</option>
                            <option value="Quadriceps">Quads</option>
                        </select>
                        <button @click="this.generateWorkout" class="generate-workout-btn">Generate Workout</button>
                    </div>

                </div>

                <table v-if="this.workout" class="workout-table">
                    <tr class="workout-header-container">
                        <th>Workout Name</th>
                        <th>Muscle Group</th>
                        <th>Difficulty</th>
                        <th>sets</th>
                        <th>reps</th>
                    </tr>
                    <tr class="workout-data-container" v-for="workout in this.workout">
                        <td v-for="data in workout" class="workout-data">{{ data }}</td>
                        <td class="workout-data">4</td>
                        <td class="workout-data">10</td>
                    </tr>
                </table>
            </div>

        </div>
    </div>
</template>