<script lang="ts" setup>
let isSending = false;
let hasError = false;


</script>
<template>
    <div class="contact">
        <h1>Contact Me</h1>
        
        <form action="" method="post" class="contact-form">
            <div class="error-message">
                <p v-show="hasError">Oh, please enter a valid email address.</p>
            </div>
            <div v-show="isSending" class="loading">Sendig...</div>
            <fieldset>
                <div class="form-group">
                    <label for="first_name" class="required">First Name<span>*</span>                    
                        <input type="text" name="first_name" id="first_name" placeholder="First Name"> 
                    </label>
                    <label for="last_name">Last Name
                        <input type="text" name="last_name" id="last_name" placeholder="Last Name">
                    </label>
                </div>
                <div class="form-group">
                    <label label for="email" class="required">Email<span>*</span>
                        <input type="text" name="email" id="email" placeholder="Email">
                    </label>
                    <label for="phone">Phone
                        <input type="tel" name="phone" id="phone" placeholder="Phone">
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
                        <input type="text" name="subject" id="subject" placeholder="Subject">
                    </label>
                </div>
                <div class="form-group">
                    <label for="comment" class="required">Comment<span>*</span>                    
                        <textarea name="comment" id="comment" cols="30" rows="10" placeholder="Your message here!"></textarea>
                    </label>
                </div>
                <div class="form-group ">
                    <input type="button" value="Submit" class="submit-btn">
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
        .error-message,
        .loading {
            @apply w-full;
        }
        .form-group {
            @apply flex flex-row gap-x-2 justify-start items-stretch mt-4;
            label,
            input,
            select,
            textarea {
                @apply  w-full text-sm text-gray-300;
            }
            label {
                @apply mb-1 w-full;
                span {
                    @apply ml-1
                }
                &.required {
                    @apply border-b-2 border-red-500;
                    span {
                        @apply text-red-500
                    }
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