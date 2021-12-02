<template>
    <div class="home">
        <div class="hero">
            <div class="content">
                <div class="heading">
                    <figure>
                        <img
                            class="profile-pic"
                            src="../assets/img/ant-profile-pic.jpg"
                            alt="Antenh"
                            width="100"
                            height="100"
                        />
                    </figure>
                    <h1>
                        Hello,<br />My name is Antenh
                    </h1>
                </div>
                <h2>Full Stack Web Developer and eCommerce Specifalist.</h2>
                <div class="btn-container">
                    <router-link :to="{ name: 'about' }" class="btn learn-more">Learn More</router-link>
                    <router-link :to="{ name: 'contact' }" class="btn contact">Contact Me</router-link>
                </div>
            </div>
        </div>
        <svg xmlns:xlink="http://www.w3.org/1999/xlink" id="wave" style="transform:rotate(0deg); transition: 0.3s" viewBox="0 0 1440 110" version="1.1" xmlns="http://www.w3.org/2000/svg"><defs><linearGradient id="sw-gradient-0" x1="0" x2="0" y1="1" y2="0"><stop stop-color="#1e40af" offset="0%"/><stop stop-color="#1e40af" offset="100%"/></linearGradient></defs><path style="transform:translate(0, 0px); opacity:1" fill="url(#sw-gradient-0)" d="M0,11L60,18.3C120,26,240,40,360,40.3C480,40,600,26,720,29.3C840,33,960,55,1080,60.5C1200,66,1320,55,1440,51.3C1560,48,1680,51,1800,60.5C1920,70,2040,84,2160,86.2C2280,88,2400,77,2520,77C2640,77,2760,88,2880,93.5C3000,99,3120,99,3240,99C3360,99,3480,99,3600,86.2C3720,73,3840,48,3960,33C4080,18,4200,15,4320,18.3C4440,22,4560,33,4680,38.5C4800,44,4920,44,5040,51.3C5160,59,5280,73,5400,67.8C5520,62,5640,37,5760,22C5880,7,6000,4,6120,14.7C6240,26,6360,51,6480,56.8C6600,62,6720,48,6840,49.5C6960,51,7080,70,7200,78.8C7320,88,7440,88,7560,82.5C7680,77,7800,66,7920,64.2C8040,62,8160,70,8280,71.5C8400,73,8520,70,8580,67.8L8640,66L8640,110L8580,110C8520,110,8400,110,8280,110C8160,110,8040,110,7920,110C7800,110,7680,110,7560,110C7440,110,7320,110,7200,110C7080,110,6960,110,6840,110C6720,110,6600,110,6480,110C6360,110,6240,110,6120,110C6000,110,5880,110,5760,110C5640,110,5520,110,5400,110C5280,110,5160,110,5040,110C4920,110,4800,110,4680,110C4560,110,4440,110,4320,110C4200,110,4080,110,3960,110C3840,110,3720,110,3600,110C3480,110,3360,110,3240,110C3120,110,3000,110,2880,110C2760,110,2640,110,2520,110C2400,110,2280,110,2160,110C2040,110,1920,110,1800,110C1680,110,1560,110,1440,110C1320,110,1200,110,1080,110C960,110,840,110,720,110C600,110,480,110,360,110C240,110,120,110,60,110L0,110Z"/></svg>
        <div class="summary">
            <div class="content">
                <h2>Summary</h2>
                <p>11+ years of experience, specializing in eCommerce for past 8+ years</p>
                <p>Backend web application; Responsive websites for Mobile and Tablet devices with Accessablity in mind</p>
                <p>API Integrations: Payment Systems & Content Management System (CMS)</p>
            </div>
        </div>
        <svg xmlns:xlink="http://www.w3.org/1999/xlink" id="wave" style="transform:rotate(180deg); transition: 0.3s" viewBox="0 0 1440 100" version="1.1" xmlns="http://www.w3.org/2000/svg"><defs><linearGradient id="sw-gradient-0" x1="0" x2="0" y1="1" y2="0"><stop stop-color="rgba(30, 64, 175, 1)" offset="0%"/><stop stop-color="rgba(30, 64, 175, 1)" offset="100%"/></linearGradient></defs><path style="transform:translate(0, 0px); opacity:1" fill="url(#sw-gradient-0)" d="M0,10L60,20C120,30,240,50,360,51.7C480,53,600,37,720,30C840,23,960,27,1080,33.3C1200,40,1320,50,1440,55C1560,60,1680,60,1800,53.3C1920,47,2040,33,2160,25C2280,17,2400,13,2520,25C2640,37,2760,63,2880,63.3C3000,63,3120,37,3240,26.7C3360,17,3480,23,3600,33.3C3720,43,3840,57,3960,58.3C4080,60,4200,50,4320,48.3C4440,47,4560,53,4680,50C4800,47,4920,33,5040,28.3C5160,23,5280,27,5400,31.7C5520,37,5640,43,5760,40C5880,37,6000,23,6120,28.3C6240,33,6360,57,6480,63.3C6600,70,6720,60,6840,61.7C6960,63,7080,77,7200,68.3C7320,60,7440,30,7560,23.3C7680,17,7800,33,7920,43.3C8040,53,8160,57,8280,56.7C8400,57,8520,53,8580,51.7L8640,50L8640,100L8580,100C8520,100,8400,100,8280,100C8160,100,8040,100,7920,100C7800,100,7680,100,7560,100C7440,100,7320,100,7200,100C7080,100,6960,100,6840,100C6720,100,6600,100,6480,100C6360,100,6240,100,6120,100C6000,100,5880,100,5760,100C5640,100,5520,100,5400,100C5280,100,5160,100,5040,100C4920,100,4800,100,4680,100C4560,100,4440,100,4320,100C4200,100,4080,100,3960,100C3840,100,3720,100,3600,100C3480,100,3360,100,3240,100C3120,100,3000,100,2880,100C2760,100,2640,100,2520,100C2400,100,2280,100,2160,100C2040,100,1920,100,1800,100C1680,100,1560,100,1440,100C1320,100,1200,100,1080,100C960,100,840,100,720,100C600,100,480,100,360,100C240,100,120,100,60,100L0,100Z"/></svg>
        <div class="experience">
            <div class="content">
                <h2 class="title">Technical Experience</h2>
                <div class="section">
                    <h3>Backend</h3>
                    <span><img src="../assets/icons/aws-logo.svg" alt="AWS">AWS</span>
                    <span><img src="../assets/icons/linode-1.svg" alt="Linode">Linode</span>
                    <hr>
                    <span><img src="../assets/icons/ubuntu-icon.svg" alt="Ubuntu">Ubuntu</span>
                    <span><img src="../assets/icons/centos-1.svg" alt="CentOS">CentOS</span>
                    <span><img src="../assets/icons/microsoft-windows-22.svg" alt="Windows">Windows</span>
                    <span><img src="../assets/icons/apple.svg" alt="Mac OS">Mac OS</span>
                    <span><img src="../assets/icons/command-line_115191.svg" alt="Command Line">Command Line</span>
                    <hr>
                    <span><img src="../assets/icons/apache-seeklogo.com.svg" alt="Apache">Apache</span>
                    <span><img src="../assets/icons/nginx-svgrepo-com.svg" alt="NGINX">NGINX</span>
                    <span><img src="../assets/icons/mysql-svgrepo-com.svg" alt="MySQL">MySQL</span>
                    <span><img src="../assets/icons/sqlite_logo_icon_169724.svg" alt="SQLite">SQLite</span>
                    <span><img src="../assets/icons/nodejs-icon.svg" alt="Node.js">Node.js</span>
                    <hr>
                    <span><img src="../assets/icons/php-1.svg" alt="PHP">PHP</span>
                    <span><img src="../assets/icons/python-svgrepo-com.svg" alt="Python">Python</span>
                    <span><img src="../assets/icons/java-14.svg" alt="Java">Java</span>
                    <hr>
                    <span><img src="../assets/icons/laravel-svgrepo-com.svg" alt="Laravel">Laravel</span>
                    <span><img src="../assets/icons/symfony-svgrepo-com.svg" alt="Symfony">Symfony</span>
                    <span><img src="../assets/icons/magento-2.svg" alt="Magento">Magento</span>
                    <span><img src="../assets/icons/wordpress-icon-1.svg" alt="WordPress">WordPress</span>
                    <span><img src="../assets/icons/django.svg" alt="Django">Django</span>
                    <span><img src="../assets/icons/yii.svg" alt="Yii">Yii</span>
                    <hr>
                    <span><img src="../assets/icons/docker.svg" alt="Docker">Docker</span>
                    <span><img src="../assets/icons/vagrant.svg" alt="Vagrant">Vagrant</span>
                    <span><img src="../assets/icons/virtualbox.svg" alt="VirtualBox">VirtualBox</span>
                    <span><img src="../assets/icons/vmware.svg" alt="VMWare">VMWare</span>
                    <hr>
                </div>
                <div class="section">
                    <h3>Frontend</h3>
                    <span><img src="../assets/icons/logo-javascript.svg" alt="JavaScript">JavaScript</span>
                    <span><img src="../assets/icons/vue-9.svg" alt="Vue.js">Vue.js</span>
                    <span><img src="../assets/icons/jquery-4.svg" alt="jQuery">jQuery</span>
                    <span><img src="../assets/icons/backbone-js.svg" alt="Backbone.js">Backbone.js</span>
                    <hr>
                    <span><img src="../assets/icons/html-1.svg" alt="HTML 5">HTML 5</span>
                    <span><img src="../assets/icons/css-3.svg" alt="CSS">CSS</span>
                    <span><img src="../assets/icons/sass-1.svg" alt="SASS">SASS</span>
                    <hr>
                    <span><img src="../assets/icons/tailwind-css-2.svg" alt="Tailwindcss">Tailwindcss</span>
                    <span><img src="../assets/icons/bootstrap-5-1.svg" alt="Bootstrap">Bootstrap</span>
                    <hr>
                    <h3>Development Tools</h3>
                    <span><img src="../assets/icons/phpstorm-1.svg" alt="PhpStorm">PhpStorm</span>
                    <span><img src="../assets/icons/vscode_icon_130084.svg" alt="VS Code">VS Code</span>
                    <span><img src="../assets/icons/sublime-text.svg" alt="Sublime Text">Sublime Text</span>
                    <span><img src="../assets/icons/mysqlworkbench_93532.svg" alt="MySQL Workbench">MySQL Workbench</span>
                    <span><img src="../assets/icons/git-icon.svg" alt="Git, Version Control System">Git</span>
                    <span><img src="../assets/icons/bitbucket-icon.svg" alt="BitBucket">BitBucket</span>
                    <span><img src="../assets/icons/postman.svg" alt="Postman">Postman</span>
                    <hr>
                </div>
            </div>
        </div>
    </div>
</template>

<style lang="scss">
.home {
    @apply flex flex-col justify-center items-center relative;
    * {
        @apply z-30;
    }
}
.hero {
    @apply flex flex-col justify-center items-center w-full p-0;
    .content {
        @apply flex flex-row flex-wrap justify-center items-center p-6;
        .heading {
            @apply flex flex-row flex-wrap justify-evenly items-center w-full;
            h1 {
                @apply text-5xl text-center bg-gradient-to-r bg-clip-text text-transparent
                from-pink-800 to-purple-900
                /* Dark */
                dark:from-pink-200 dark:to-purple-300;
            }
        }
        h2 {
            @apply w-full mt-10 text-center rounded;
        }
        .btn-container {
            @apply mt-10;
            a {
                @apply py-2 px-4 relative text-sm rounded-sm shadow-md 
                    transition transform-gpu duration-150 ease-in-out scale-110
                    bg-purple-300
                    /* Dark */
                    dark:bg-blue-900;
                &::before {
                    content: "";
                    @apply absolute top-0 left-0 w-full h-full z-10 bg-opacity-5 transition-all duration-300
                    bg-gray-200
                    /* Dark */
                    dark:bg-gray-700;
                }
                &::after {
                    content: "";
                    @apply absolute top-0 left-0 w-full h-full z-10 opacity-0 transition-all duration-300 border-2 rounded-sm transform-gpu scale-110
                    border-indigo-600
                    /* Dark */
                    dark:border-indigo-400;
                }
                &:hover,
                &:focus {
                    @apply transform scale-110  underline
                    bg-indigo-700 text-indigo-100
                    /* Dark */
                    dark:bg-pink-100 dark:text-indigo-900;
                    transform: scale(1, 1);
                }
                &:hover::before,
                &:focus::before {
                    @apply opacity-0 transform-gpu scale-50;
                }
                &:hover::after,
                &:focus::after {
                    @apply opacity-100 transform-gpu scale-100;
                }
                &:last-child {
                    @apply ml-3;
                }
            }
        }
    }
}
.summary {
    @apply flex flex-col justify-center items-center w-full bg-gradient-to-r
    from-blue-100 to-blue-200
    /* Dark */
    dark:from-blue-800 dark:to-blue-800;
    .content {
        @apply flex flex-col flex-wrap justify-center items-center pt-0;
        p {
            @apply h-full mt-2 text-center leading-6;
        }        
    }
}
.experience {
    @apply flex flex-col justify-center items-center relative w-full;
    .content {
        @apply flex flex-row flex-wrap justify-around items-start pt-0;
        .section {
            @apply md:w-1/2 flex flex-row flex-wrap justify-center text-center;
            h3 {
                @apply w-full mt-5 p-2 ;
            }
            span {
                @apply flex items-center px-2 py-1;
            }
            hr {
                @apply w-full border-0;
                height: 2px;
                background-image: linear-gradient(to right, rgba(0, 0, 0, 0), rgb(180, 83, 9, 42%), rgba(0, 0, 0, 0));
            }
            p {
                @apply text-left mt-5;
            }
            img {
                @apply inline-block h-5 mr-1
            }
        }
    }
}
.content {
    @apply max-w-4xl p-6 mx-auto;
}
.title {
    @apply w-full text-center; 
}
</style>