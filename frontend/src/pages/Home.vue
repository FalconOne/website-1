<template>
    <div class="home">
        <div class="hero">
            <div class="content">
                <img src="../assets/img/ant-profile-pic.jpg" alt="Antenh" width="100" height="100" />
                <h1>
                    Hello,
                    <br />Name is Antenh
                </h1>
                <p>
                    I'm a Full Stack Web Developer and eCommerce Specifalist.
                    <br />Backend systems arcitect and front-end prefectionist.
                </p>
            </div>
        </div>
        <div class="summary hidden">
            <div class="content">
                <h2>Technical Summary</h2>
                <p>10+ years of experience</p>
                <p></p>
                <p></p>
            </div>
        </div>
        <div class="experience">
            <div class="content">
                <div class="section">
                    <h3>Summary</h3>
                </div>
                <div class="section">
                    <h3>Frontend</h3>
                </div>
            </div>
            <div class="experience-wave-devider">
                <svg
                    data-name="Layer 1"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 1200 120"
                    preserveAspectRatio="none"
                >
                    <path
                        d="M321.39,56.44c58-10.79,114.16-30.13,172-41.86,82.39-16.72,168.19-17.73,250.45-.39C823.78,31,906.67,72,985.66,92.83c70.05,18.48,146.53,26.09,214.34,3V0H0V27.35A600.21,600.21,0,0,0,321.39,56.44Z"
                        class="shape-fill"
                    />
                </svg>
            </div>
        </div>
    </div>
</template>

<style scoped>
.hero {
    @apply w-full p-2;
}
.hero > .content > img {
    @apply rounded-full w-32 mx-auto;
}
.hero > .content > h1 {
    @apply mt-10 text-5xl;
}
.hero > .content > p {
    @apply mt-10;
}
.experience {
    @apply relative w-full bg-gradient-to-r from-blue-900 to-blue-600 mt-10 pt-7 ;
}
.experience > .content {
    @apply grid grid-cols-2;
}
.experience > .content > .section {
    @apply w-full p-4;
}
.experience-wave-devider {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    overflow: hidden;
    line-height: 0;
}
.experience-wave-devider svg {
    position: relative;
    display: block;
    width: calc(100% + 1.3px);
    height: 50px;
}

.experience-wave-devider .shape-fill {
    @apply fill-current text-gray-800
}         
</style>