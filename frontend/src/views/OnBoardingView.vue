<script>
export default {
    data() {
        return {
            questions: ["Please Enter Your First and Last Name", "Please Enter Your Phone Number", "Please Enter your Height in Inches and Weight in Pounds"],
            questionIndex: 0,
            form: {}
        }
    },
    methods: {
        advanceQuestion: function () {
            console.log(this.form)
            this.questionIndex += 1;
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
                    <input v-model="form['height']" name="height" type="number" min='0' max='96'>
                    <label for="weight">Weight in lb's</label>
                    <input v-model="form['weight']" name="weight" type="number" min='50' max='500'>
                </form>
            </div>
            <button @click="this.advanceQuestion" class="form-btn">Next</button>
        </div>
    </div>
</template>