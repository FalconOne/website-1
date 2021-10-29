<template>
    <nav class="main-nav shape">
        <router-link :to="{ name: 'home' }">
            <i class="fas fa-home"></i>
            <span class="link-text">Home</span>
        </router-link>
        <router-link :to="{ name: 'contact' }">
            <i class="fas fa-envelope"></i>
            <span class="link-text">Contact</span>
        </router-link>
        <router-link :to="{ name: 'about' }">
            <i class="fas fa-address-card"></i>
            <span class="link-text">About</span>
        </router-link>
    </nav>
</template>

<style scoped>
nav {
    @apply w-80 grid grid-cols-3 mb-4 mx-auto p-0 text-center sticky top-0 z-50;
}
nav:after {
    @apply absolute w-full h-full top-0 left-0
        rounded-none rounded-br-sm rounded-bl-sm bg-gradient-to-b
        from-gray-100 to-gray-200
        /* Dark Mode */
        dark:from-gray-600 dark:to-gray-500;
        
    content: "";
    z-index: -1;
    transform: perspective(100px) rotateX(355deg);
    transform-origin: center bottom;
    box-shadow: 0px 2px 10px 5px rgb(24, 25, 49);
    background: #212327;
    background: linear-gradient(90deg, rgb(43, 60, 83) 0%, rgb(24, 38, 58) 100%);
}
a {
    @apply mr-2 font-semibold p-1 rounded-sm no-underline;
}
a:last-child {
    @apply mr-0;
}
a > span.link-text {
    @apply ml-1.5 text-transparent bg-clip-text bg-gradient-to-r
        from-blue-800 to-blue-900
        /* Dark Mode */
        dark:from-gray-200 dark:to-gray-300;
}
a:hover,
a.router-link-active {
    @apply border-b-4
        border-blue-900
        /* Dark Mode */
        dark:border-yellow-700;
}
a > svg {
    @apply fill-current 
        text-indigo-800
        /* Dark Mode */
        dark:text-yellow-300;
}
</style>
