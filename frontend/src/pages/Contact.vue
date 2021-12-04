<script setup>
import { ref } from "vue";
import axios from "axios";
import VueHcaptcha from '@hcaptcha/vue3-hcaptcha';

let first_name = ref(''),
    last_name  = ref(''),
    email      = ref(''),
    phone      = ref(''),
    subject    = ref(''),
    comment    = ref(''),
    is_sending = ref(false),
    has_error  = ref(false),
    thank_you  = ref(false);

const captcha_verified = ref(false),
      captcha_expired  = ref(false),
      captcha_token    = ref(""),
      captcha_eKey     = ref(""),
      captcha_error    = ref(false);

const isDarkMode = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;

async function submitForm() {
    resetForm();

    if (
        !validateInput(first_name.value) ||
        !validateInput(email.value) ||
        !validateInput(subject.value) ||
        !validateInput(comment.value)
    ) {
        has_error.value = true;
        return;
    }

    if ( !captcha_verified.value || !captcha_token.value || !captcha_eKey.value) {
        captcha_error.value = true;
        return;
    }

    is_sending.value = true;

    const res = await axios.post('/app/api/contact', {
        first_name: first_name.value,
        last_name : last_name.value,
        email     : email.value,
        phone     : phone.value,
        subject   : subject.value,
        comment   : comment.value,
    }).then(function (response) {
        is_sending.value = false;

        if ( response.data.msg == 'success' ) {
            thank_you.value = true;
        }
    })
    .catch(function (error) {
        return error.response;
    })
    
    resetForm();
}

function validateInput(input) {
    if (input.length > 1 && input != '') {
        return true;
    }
    return false;
}

function resetForm() {
    is_sending.value = false;
    has_error.value  = false;
}

function captchaVerify(token, eKey) {
    captcha_verified.value = true;
    captcha_token.value    = token;
    captcha_eKey.value     = eKey;
    captcha_error.value    = false;
}

function captchaExpired() {
    captcha_verified.value = false;
    captcha_token.value    = '';
    captcha_eKey.value     = '';
    captcha_expired.value  = true;
}

function captchaError(error) {
    captcha_token.value = '';
    captcha_eKey.value  = '';
    captcha_error.value = error;
}
</script>
<template>
    <div class="contact">
        <h1>Contact Me</h1>
        <form action="#" method="post" class="contact-form">
            <div v-show="has_error" class="error-msg" id="error_msg">
                <p><span>*</span>Oh, please fill all required fields.</p>
            </div>
            <fieldset>
                <div class="form-group">
                    <label for="first_name" class="required">
                        First Name
                        <span>*</span>
                        <input
                            v-model.trim="first_name"
                            type="text"
                            name="first_name"
                            placeholder="First Name"
                        />
                    </label>
                    <label for="last_name">
                        Last Name
                        <input
                            v-model.trim="last_name"
                            type="text"
                            name="last_name"
                            id="last_name"
                            placeholder="Last Name"
                        />
                    </label>
                </div>
                <div class="form-group">
                    <label label for="email" class="required">
                        Email
                        <span>*</span>
                        <input
                            v-model.trim="email"
                            type="text"
                            name="email"
                            id="email"
                            placeholder="Email"
                        />
                    </label>
                    <label for="phone">
                        Phone
                        <input
                            v-model.number.trim="phone"
                            type="tel"
                            name="phone"
                            id="phone"
                            placeholder="Phone"
                        />
                    </label>
                </div>
                <div class="form-group">
                    <!-- <label for="topic" class="required">Topic<span>*</span>
                        <select name="topic" id="topic">
                            <option value='' selected disabled hidden>Select one!</option>
                            <option value="suggest">Suggestions</option>
                            <option value="bussines">Project / Work</option>
                            <option value="testimony">Testimony</option>
                        </select>
                    </label>-->
                    <label for="subject" class="required">
                        Subject
                        <input
                            v-model.trim="subject"
                            type="text"
                            name="subject"
                            id="subject"
                            placeholder="Subject"
                        />
                    </label>
                </div>
                <div class="form-group">
                    <label for="comment" class="required">
                        Comment
                        <span>*</span>
                        <textarea
                            v-model.trim="comment"
                            name="comment"
                            id="comment"
                            cols="30"
                            rows="10"
                            placeholder="Your message here!"
                        ></textarea>
                    </label>
                </div>
                <vue-hcaptcha 
                    sitekey="9f0c5779-b36e-414c-9e7f-a56d10094413"
                    :theme="isDarkMode ? 'dark' : 'light'"
                    @verify="captchaVerify"
                    @expired="captchaExpired"
                    @challenge-expired="captchaExpired"
                    @error="captchaError"
                >
                </vue-hcaptcha>
                <div v-show="captcha_error" class="captcha-error">
                    <p>Please check "I am human" checkbox.</p>
                </div>
                <div class="form-group">
                    <input
                        type="button"
                        value="Submit"
                        class="submit-btn"
                        @click="submitForm"
                    />
                </div>
            </fieldset>
            <div v-show="is_sending" class="sending">
                <div class="lds-ripple">
                    <div></div>
                    <div></div>
                </div>
                Sending...<br />
            </div>
            <div v-show="thank_you" class="thank-you">
                <img src="../assets/icons/check-solid.svg" alt="Check Mark">
                <h3>Thank you for reaching out.</h3>
                <p>I'm looking forward to reading your message.<br>
                </p>
            </div>
        </form>
    </div>
</template>

<style lang="scss" scoped>
.contact {
    @apply flex flex-col justify-center items-center relative;
    .contact-form {
        @apply flex flex-col justify-center items-center relative my-5 p-6 bg-gradient-to-r rounded-md drop-shadow-2xl
        from-indigo-200 to-red-200        
        /* Dark */
        dark:from-indigo-900 dark:to-pink-900;
        .error-msg {
            @apply w-full h-full bg-gradient-to-r p-1 rounded-sm filter drop-shadow-md
            text-black from-red-400 to-red-300
            /* Dark */
            dark:text-gray-200 dark:from-red-800 dark:to-red-700;
        }
        .captcha-error {
            @apply w-full h-full mt-4 bg-gradient-to-r p-1 rounded-sm filter 
            text-black from-red-400 to-red-300
            /* Dark */
            dark:text-gray-200 dark:from-red-800 dark:to-red-700;
        }
        .sending,
        .thank-you {
            @apply w-full h-full absolute flex flex-col justify-center items-center bg-gradient-to-r rounded-sm
            text-gray-900 from-indigo-200 to-green-200
            /* Dark */
            dark:text-gray-200 dark:from-indigo-800 dark:to-green-800;
        }
        .thank-you {
            img {
                @apply w-16
            }
            h3, p {
                @apply mt-3
            }

        }
        .form-group {
            @apply flex flex-row gap-x-2 justify-start items-stretch mt-4;
            label,
            input,
            select,
            textarea {
                @apply w-full text-sm
                text-gray-800
                /* Dark */
                dark:text-gray-300;
            }
            label {
                @apply mb-1 w-full;
                span {
                    @apply ml-1;
                }
                &.required {
                    input,
                    textarea,
                    select {
                        @apply border-b-2 pb-2
                        border-red-500
                        /* Dark */
                        dark:border-red-500;
                    }
                    span {
                        @apply text-red-500;
                    }
                }
                &.required > textarea {
                    @apply pb-0;
                }
            }
            input,
            textarea,
            select {
                @apply mt-1 py-1 px-2 rounded-sm placeholder-opacity-50 filter drop-shadow-md shadow-lg transform transition-all duration-300 ease-in-out
                bg-gray-200 placeholder-gray-600
                /* Dark */
                dark:bg-gray-800 dark:placeholder-gray-400;
                &:focus {
                    @apply outline-none ring-2 scale-x-102
                    ring-gray-800
                    /* Dark */
                    dark:ring-gray-400 ;
                }
            }
            textarea {
                min-height: 200px;
            }
            .submit-btn {
                @apply bg-indigo-600 text-gray-100 
                dark:bg-yellow-700;
                &:hover,
                &:focus {
                    @apply transform scale-105 cursor-pointer
                    text-gray-900 bg-yellow-100
                    /* Dark */
                    dark:bg-indigo-300 dark:text-gray-900;
                }
            }
        }
    }
}

.lds-ripple {
    display: inline-block;
    position: relative;
    width: 80px;
    height: 80px;
}
.lds-ripple div {
    position: absolute;
    border: 4px solid #fff;
    opacity: 1;
    border-radius: 50%;
    animation: lds-ripple 1s cubic-bezier(0, 0.2, 0.8, 1) infinite;
}
.lds-ripple div:nth-child(2) {
    animation-delay: -0.5s;
}
@keyframes lds-ripple {
    0% {
        top: 36px;
        left: 36px;
        width: 0;
        height: 0;
        opacity: 1;
    }
    100% {
        top: 0px;
        left: 0px;
        width: 72px;
        height: 72px;
        opacity: 0;
    }
}
</style>
