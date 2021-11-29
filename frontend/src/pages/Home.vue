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
        <div class="summary">
            <div class="content">
                <h2>Summary</h2>
                <p>11+ years of experience, specializing in eCommerce for past 8+ years</p>
                <p>Backend web application; Responsive websites for Mobile and Tablet devices with Accessablity in mind</p>
                <p>API Integrations: Payment Systems & Content Management System (CMS)</p>
            </div>
        </div>
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
    dark:from-blue-700 dark:to-blue-800;
    .content {
        @apply flex flex-col flex-wrap justify-center items-center;
        p {
            @apply h-full mt-2 text-center leading-6;
        }        
    }
}
.experience {
    @apply flex flex-col justify-center items-center relative w-full;
    .content {
        @apply flex flex-row flex-wrap justify-around items-start;
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