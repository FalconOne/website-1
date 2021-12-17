<script setup lang="ts">
</script>

<template>
    <div class="about">
        <section class="content">
            <h1>About me</h1>
            <article>
                <img class="profile-pic" src="../assets/img/ant-profile-pic.jpg" alt="">      
                <p class="max-w-lg text-center p-2">My name is Antenh. I've been programming web for 11+ years.<br> I specializing in Back-end development, eCommerce websites, and front-end development.</p>

                <div class="section">
                    <h2>Application Deployment</h2>
                    <p>
                        Application deployment on Linux server.
                        Ubuntu, CentOS of my development enviroments are currently run with Docker
                    </p>    
                </div>

                <div class="section">
                    <h2>Server Technologies</h2>
                    <p>I'm well versed in all aspects of application setup and deployment to production and creating development enviroments.</p>
                    <ul>
                        <li>Cloud providors: AWS / AWS CLI, Linode</li>
                        <li>OS: Linux, Ubuntu, CentOS</li>
                        <li>Apache, NGINX</li>
                        <li>SSL Certificates, Cypher, SSL Labs</li>
                    </ul>
                </div>
                <div class="section">
                    <h2>Backend</h2>
                    <ul>
                        <li>PHP (OOP), Python, Bash Script</li>
                        <li>Database Arcitecture, Modeiling, Programming</li>
                        <li>RESTful API</li>
                        <li>Frameworks: Laraval, Magento, Symfony, Django</li>
                    </ul>
                </div>
                <div class="section">
                    <h2>Frontend Technologies</h2>
                    <p>I'm well versed in all aspects of application setup and deployment to production and creating development enviroments.</p>

                    <ul>
                        <li>HTML, JavaScript, CSS / SASS</li>
                        <li>Frameworks: Vue.js, Backbone.js, Bootstrap, <span><img src="../assets/icons/tailwind-css-2.svg" alt="Tailwindcss">Tailwindcss</span></li>
                    </ul>
                </div>
                <div class="section">
                    <h2>eCommerece</h2>
                    <p>
                        From development to deployment and everything in between.<br>
                        <span class="svg-container"><img src="../assets/icons/magento-2.svg" alt="Magento">Magento</span>
                    </p>
                    <ul>
                        <li>Design & Build web UI components</li>
                    </ul>
                    <h4>Other</h4>
                    <ul>
                        <li>Magento</li>
                        <li>Authorize.NET</li>
                        <li>Spreedly</li>
                        <li>MailChimp</li>
                        <li>SendGrid</li>
                        <li>Twilio</li>
                        <li>Google Analytcs</li>
                    </ul>                    
                </div>
                <div class="section">
                    <h2>eCommerece</h2>
                    <p>
                        eCommerce(eComm) has been my career for past 8+ years. My experience in eCommerce is in backend development primarly, but not limited to. I've an extensive knowledge on Integrating payment systems, Content Management Systems (CMS) like MailChimp and Twilio. As well coding UI.
                    </p>
                    <h3>Contact</h3>
                </div>
                <div class="section">
                    <h2>My Philosophy</h2>
                    <p>
                        As programmer my goal is to write, clean, simple, efficient & readable code. Now it's probably every programmers goal. For me it can be the metric that will allow my clients to be productive and spend less time & money.
                    </p>
                    <p>
                        # # #<br>
                        Bussiness sense, every business will have to make the decisions that make sense to them. Every business is different and it needs attention in different arias of production. Weather there are budget constraints, level of talent, or special needs, it's import to able to establish the needs of the client first.
                    </p>
                </div>
                <div class="section">
                    <h2>Security</h2>
                    Security is very important part of an application, espcially now more than ever. It's at most impornce to me, as I work with client that utilize various technologies to obtain & store customer data. The security measures & patterns must be sound and secure, and make business sense.
                    <br>
                    <br>
                    <ul>
                        <li>Tech. SSL Labs.</li>
                        <li>Installing SSL Certificates</li>
                        <li>Aquairing, Configuring, Apache Communication Cypher
                        </li>
                        <li>application configurations.</li>
                    </ul>                    
                </div>
            </article>
            <article>
                <div class="section">
                    <h2>About this site</h2>
                    <p>
                        Built with: <br>
                        <span><img src="../assets/icons/vue-9.svg" alt="Vue.js">Vue.js</span> with  <span><img src="../assets/icons/typescript.svg" alt="TypeScript">TypeScript</span>, <span class="svg-container"><img src="../assets/icons/vitejs.svg" alt="Vite JS">Vite</span>, 
                        <span class="svg-container"><img src="../assets/icons/django.svg" alt="Django">Django</span>, <span><img src="../assets/icons/nginx-svgrepo-com.svg" alt="NGINX">NGINX</span>, <span><img src="../assets/icons/tailwind-css-2.svg" alt="Tailwindcss">Tailwindcss</span>.
                    </p>
                </div>
                <div class="section">
                    <h3>Site feature:</h3>
                    <ul>
                        <li>Secure Contact Form</li>
                        <li>Auto Dark Mode, using <code>--prefed-color-scheme</code> feature</li>
                        <li>Accessablity. Lighthouse report score<img src="../assets/img/accessibility-score-callmeant.com.png" alt=""></li>
                        <li>SEO</li>
                        <li>SSL Certifcate from <a href="https://letsencrypt.org/">Let's Encrypt</a> </li>
                    </ul>
                </div>
                <div class="section">
                    <h3>SVG icons obtained from these website:</h3>
                    <ul>
                        <li><a href="https://icon-icons.com/">https://icon-icons.com/</a></li>
                        <li><a href="https://worldvectorlogo.com/">https://worldvectorlogo.com/</a></li>
                        <li><a href="https://www.svgrepo.com/">https://www.svgrepo.com/</a></li>
                        <li><a href="https://freeicons.io/">https://freeicons.io/</a></li>
                    </ul>
                </div>

            </article>
        </section>
    </div>
</template>

<style lang="scss" scoped>
.about {
    @apply w-full ;
    h1 {
        @apply text-center;
    }
    article {
        @apply flex flex-wrap flex-row justify-center items-center text-left;
        h1, h2 {
            @apply w-full;
        }
        figure {
            @apply text-left;
        }
        h2, h3 {
            @apply mt-5 pb-2 border-b-2 border-purple-500 rounded-sm;
        }
        .section {
            @apply w-full;
            ul {
                @apply pl-10;
            }
        }
        p {
            @apply mt-5;
            img {
                @apply mr-5;
            }
        }
        ul {
            @apply w-full list-disc mt-4 float-left;
            list-style-type: square;
        }
        span {
            img {
                @apply inline-block h-5 mr-1
            }
        }
    }    
    a {
        @apply text-blue-300 underline
    }
}
</style>