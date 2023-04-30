<script>
export default {
    data() {
        return {
            questions: ["Please Enter Your First and Last Name", "Please Enter Your Phone Number", "Please Enter your Height in Inches and Weight in Pounds", "How many times would you like to workout per week?", "What is your experiance in the gym?", "Congradulations, you can now generate your first workout!"],
            questionIndex: 0,
            form: {}
        }
    },
    methods: {
        advanceQuestion: function () {
            console.log(this.form)
            this.questionIndex += 1;
        },
        /**
         * Event handler for check boxed to record data of the equipment avliable for users
         * @param {Event} e 
         */
        radioEvent: function (e) {
            if (!this.form['equipment']) {
                this.form['equipment'] = [];
                console.log("array created")
            }
            let target = e.target;
            if (target.checked) {
                this.form['equipment'].push(e.target.value);
            }
            else {
                let indexValue = this.form['equipment'].indexOf(e.target.value);
                if (indexValue > -1) { // only splice array when item is found
                    this.form['equipment'].splice(indexValue, 1); // 2nd parameter means remove one item only
                }
            }
        }
    }
}
</script>

<template>
    <div class="login-body">
        <div class="on-boarding-questionair">
            <p class="on-boarding-header">Please Answer The Following Questions</p>
            <div class="question-container">
                <div class="question">{{ this.questions[this.questionIndex] }}</div>
                <form v-if="questionIndex == 0" class="question-inputs">
                    <input v-model="form['firstName']" type="text" placeholder="First Name" maxlength="50">
                    <input v-model="form['lastName']" type="text" placeholder="Last Name" maxlength="50">
                </form>
                <form v-if="questionIndex == 1" class="question-inputs">
                    <input v-model="form['phoneNumber']" type="tel" placeholder="10 digit Phone Number" maxlength="10">
                </form>
                <form v-if="questionIndex == 2" class="question-inputs">
                    <label for="height">Height in Inches</label>
                    <input v-model="form['height']" name="height" id="height" type="number" min='0' max='96'>
                    <label for="weight">Weight in lb's</label>
                    <input v-model="form['weight']" name="weight" id="weight" type="number" min='50' max='500'>
                </form>
                <form v-if="questionIndex == 3">
                    <select v-model="form['workoutFrequency']" class="form-select" default="1">
                        <option value="1" selected>Workout once a week</option>
                        <option value="2">Workout twice a week</option>
                        <option value="3">Workout three times a week</option>
                        <option value="4">Workout four times a week</option>
                        <option value="5">Workout five times a week</option>
                        <option value="6">Workout six times a week</option>
                        <option value="7">Workout seven times a week</option>
                    </select>
                </form>
                <form v-if="questionIndex == 4">
                    <select v-model="form['workoutExperiance']" class="form-select" default="1">
                        <option value="1" selected>Beginner</option>
                        <option value="2">Intermediate</option>
                        <option value="3">Experianced</option>
                    </select>
                </form>
                <form v-if="questionIndex == 5">
                    <label for="body-weight">Body Weight Only</label>
                    <input @click="this.radioEvent" type="checkbox" name="body-weight" id="body-weight" value="Body Only">
                    <label for="full-gym">Full Gym</label>
                    <input @click="this.radioEvent" type="checkbox" name="full-gym" id="full-gym" value="Full Gym">
                    <label for="kettlebells">Kettlebells</label>
                    <input @click="this.radioEvent" type="checkbox" name="kettlebells" id="kettlebells" value="Kettlebells">
                    <label for="bands">Resistance Bands</label>
                    <input @click="this.radioEvent" type="checkbox" name="bands" id="bands" value="Bands">
                </form>
            </div>
            <button @click="this.advanceQuestion" class="form-btn">Next</button>
        </div>
    </div>
</template>