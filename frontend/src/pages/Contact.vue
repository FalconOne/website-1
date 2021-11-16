<script lang="ts" setup>
import { ref } from 'vue'
import axios from 'axios';

let first_name = ref(''),
    last_name  = ref(''),
    email      = ref(''),
    phone      = ref(''),
    subject    = ref(''),
    comment    = ref(''),

    is_sending = ref(false),
    has_error  = ref(false);
    

async function submitForm() {
    if ( !validateInput(first_name.value) ||
         !validateInput(email.value) ||
         !validateInput(subject.value) ||
         !validateInput(comment.value)) {
        has_error.value = true;
        const error_msg = document?.getElementById("error_msg")?.offsetTop;
        window.scrollTo({ 'top': error_msg+70});
        return
    }
    is_sending.value = true;

    const res = await axios.post('http://127.0.0.1:8000/api/contact', {
        first_name: first_name.value,
        last_name : last_name.value,
        email     : email.value,
        phone     : phone.value,
        subject   : subject.value,
        comment   : comment.value,
    }).then(function(response) {
        return response.data.msg;
    })
    .catch(function(error) {
        return error.response.data;
    })
    
    resetForm();
}

function validateInput(input: any):boolean {
    if ( input.length > 1 && input != '') {
        return true;
    }
    return false;
}

function resetForm() {
    is_sending.value = false;
    has_error.value = false;
}
</script>
<template>
    <div class="contact">
        <h1>Contact Me</h1>
        <form action="" method="post" class="contact-form">
            <div v-show="has_error" class="error-msg" id="error_msg">
                <p><span>* </span>Oh, please fill all required fields.</p>
            </div>
            <div v-show="is_sending" class="sending">Sendig...</div>
            <fieldset>
                <div class="form-group">
                    <label for="first_name" class="required">First Name<span>*</span>
                        <input v-model.trim="first_name" type="text" name="first_name" placeholder="First Name"> 
                    </label>
                    <label for="last_name">Last Name
                        <input v-model.trim="last_name" type="text" name="last_name" id="last_name" placeholder="Last Name">
                    </label>
                </div>
                <div class="form-group">
                    <label label for="email" class="required">Email<span>*</span>
                        <input v-model.trim="email" type="text" name="email" id="email" placeholder="Email">
                    </label>
                    <label for="phone">Phone
                        <input v-model.number.trim="phone" type="tel" name="phone" id="phone" placeholder="Phone">
                    </label>
                </div>
                <div class="form-group">
                    <!-- <label for="topic" class="required">Topic<span>*</span>
                        <select name="topic" id="topic">
                            <option value="" selected disabled hidden>Select one!</option>
                            <option value="suggest">Suggestions</option>
                            <option value="bussines">Project / Work</option>
                            <option value="testimony">Testimony</option>
                        </select>
                    </label> -->
                    <label for="subject" class="required">Subject
                        <input v-model.trim="subject" type="text" name="subject" id="subject" placeholder="Subject">
                    </label>
                </div>
                <div class="form-group">
                    <label for="comment" class="required">Comment<span>*</span>
                        <textarea v-model.trim="comment" name="comment" id="comment" cols="30" rows="10" placeholder="Your message here!"></textarea>
                    </label>
                </div>
                <div class="form-group ">
                    <input type="button" value="Submit" class="submit-btn" @click="submitForm">
                </div>
            </fieldset>
        </form>
    </div>
</template>
   
<style lang="scss" scoped>
.contact {
    @apply flex flex-col justify-center items-center relative;
    .contact-form {
        @apply flex flex-col justify-center items-center my-5 p-6 bg-gradient-to-r rounded-md from-indigo-900 to-pink-900 drop-shadow-2xl;
        .error-msg,
        .sending {
            @apply w-full h-full text-gray-200 bg-red-800 p-1 rounded-sm border-solid border border-red-600;
        }
        .form-group {
            @apply flex flex-row gap-x-2 justify-start items-stretch mt-4;
            label,
            input,
            select,
            textarea {
                @apply w-full text-sm text-gray-300;
            }
            label {
                @apply mb-1 w-full;
                span {
                    @apply ml-1
                }
                &.required {
                    input,
                    textarea,
                    select {
                        @apply border-b-2 border-red-500 pb-2;
                    }
                    span {
                        @apply text-red-500
                    }
                }
                &.required > textarea {
                    @apply pb-0
                }
            }
            input,
            textarea,
            select {
                @apply mt-1 py-1 px-2 rounded-sm bg-gray-800 placeholder-gray-400 placeholder-opacity-50 filter drop-shadow-md shadow-lg transform transition-all duration-300 ease-in-out ;
                &:focus {
                    @apply outline-none ring-2 ring-gray-400 scale-x-102;
                }
            }
            textarea {
                min-height: 200px;
            }
            .submit-btn {
                @apply bg-yellow-700;
                &:hover,
                &:focus {
                    @apply bg-indigo-400 text-gray-900 transform scale-105 cursor-pointer;
                }
            }
        }
    }
}
</style>