<script setup lang="ts">
</script>

<template>
    <div class="about">
        <section class="content">
            <h1>About me</h1>
            <article>
                <img class="profile-pic" src="../assets/img/ant-profile-pic.jpg" alt="">      
                <p class="max-w-lg text-center p-2">My name is Antenh. I'm experienced fullstack web developer with 11+ years.
                I specializing in backend and API development, eCommerce websites, and front-end development.</p>
                <h2>Backend</h2>
                <div class="section">
                    <p>I'm well versed in all aspects of application setup and deployment to production and creating development enviroments.</p>
                    <ul>
                        <li>Cloud: <span><img src="../assets/icons/aws-logo.svg" alt="AWS">AWS</span>, <span><img src="../assets/icons/linode-1.svg" alt="Linode">Linode</span></li>
                        <li>OS: <span><img src="../assets/icons/ubuntu-icon.svg" alt="Ubuntu">Ubuntu</span>, <span><img src="../assets/icons/centos-1.svg" alt="CentOS">CentOS</span></li>
                        <li>Web Server: <span><img src="../assets/icons/apache-seeklogo.com.svg" alt="Apache">Apache</span>, <span><img src="../assets/icons/nginx-svgrepo-com.svg" alt="NGINX">NGINX</span></li>
                        <li>Database: <span><img src="../assets/icons/mysql-svgrepo-com.svg" alt="MySQL">MySQL</span>, <span><img src="../assets/icons/sqlite_logo_icon_169724.svg" alt="SQLite">SQLite</span></li>
                        <li>Languages: <span><img src="../assets/icons/php-1.svg" alt="PHP">PHP</span>, <span><img src="../assets/icons/python-svgrepo-com.svg" alt="Python">Python</span>, <span><img src="../assets/icons/c-program.svg" alt="C"></span></li>
                        <li>Frameworks: <span><img src="../assets/icons/laravel-svgrepo-com.svg" alt="Laravel">Laravel</span>, <span><img src="../assets/icons/magento-2.svg" alt="Magento">Magento</span>, <span><img src="../assets/icons/symfony-svgrepo-com.svg" alt="Symfony">Symfony</span>, <span><img src="../assets/icons/django.svg" alt="Django">Django</span></li>
                    </ul>
                </div>
                <h2>Frontend</h2>
                <div class="section">
                    <ul>
                        <li><span><img src="../assets/icons/html-1.svg" alt="HTML">HTML</span>, <span><img src="../assets/icons/logo-javascript.svg" alt="JavaScript">JavaScript</span>, <span><img src="../assets/icons/typescript.svg" alt="TypeScript">TypeScript</span>, <span><img src="../assets/icons/css-3.svg" alt="CSS">CSS</span>, <span><img src="../assets/icons/sass-1.svg" alt="SASS">SASS</span></li>
                        <li>Frameworks: <span><img src="../assets/icons/vue-9.svg" alt="Vue.js">Vue.js</span>, <span><img src="../assets/icons/backbone-js.svg" alt="Backbone.js">Backbone.js</span>, <span><img src="../assets/icons/bootstrap-5-1.svg" alt="Bootstrap">Bootstrap</span>, <span><img src="../assets/icons/tailwind-css-2.svg" alt="Tailwindcss">Tailwindcss</span></li>
                    </ul>
                </div>
                <h2>eCommerece</h2>
                <div class="section">
                    <p>
                        From development to deployment and everything in between.
                    </p>
                    <ul>
                        <li>Design & Build web UI components</li>
                        <li>Payment System & Gateway Integration</li>
                        <li>Transactional emails integrations</li>
                        <li>Text Messaging integrations</li>
                        <li>UI & UX design</li>
                        <li>Analytcs integrations and Reporting</li>
                    </ul>                 
                </div>
                <h2>Security</h2>
                <div class="section">
                    <p>
                        Security is very important part of an application, espcially now more than ever. I work with client that utilize various technologies to obtain & store customer data. The security measures & patterns must be sound and secure, and make business sense.
                    </p>                  
                </div>
            </article>
            <article>
                <h2>About this site</h2>
                <div class="section">
                    <p>
                        Built with: <span><img src="../assets/icons/vue-9.svg" alt="Vue.js">Vue.js</span> with  <span><img src="../assets/icons/typescript.svg" alt="TypeScript">TypeScript</span>, <span class="svg-container"><img src="../assets/icons/vitejs.svg" alt="Vite JS">Vite</span>, 
                        <span class="svg-container"><img src="../assets/icons/django.svg" alt="Django">Django</span>, <span><img src="../assets/icons/nginx-svgrepo-com.svg" alt="NGINX">NGINX</span>, <span><img src="../assets/icons/tailwind-css-2.svg" alt="Tailwindcss">Tailwindcss</span>.
                    </p>
                    <h3>Site feature:</h3>
                    <ul>
                        <li>Secure Contact Form</li>                        
                        <li>SSL Certifcate from <a href="https://letsencrypt.org/">Let's Encrypt</a></li>
                        <li>Auto Dark Mode, using <code>--prefed-color-scheme</code> feature</li>
                        <li>Accessablity. Lighthouse report score<img src="../assets/img/accessibility-score-callmeant.com.png" alt=""></li>
                    </ul>
                    <h3>SVG Icons obtained from these website:</h3>
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
        h2 {
            @apply mt-5 pb-2 border-b-2 border-purple-500 rounded-sm;
        }
        h3 {
            @apply mt-3 pb-2 border-b-2 border-pink-500 rounded-sm;
        }
        .section {
            @apply w-full pl-3;
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
            @apply w-full list-disc mt-2 float-left;
            list-style-type: square;
            li {
                @apply mt-2;
            }
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