<template>
    <nav class="main-nav shape">
        <router-link :to="{ name: 'home' }">
            <i class="fas fa-home"></i>
            <span class="link-text">About</span>
        </router-link>
        <router-link :to="{ name: 'contact' }">
            <i class="fas fa-envelope"></i>
            <span class="link-text">Contact</span>
        </router-link>
        <!-- <router-link :to="{ name: 'about' }">
            <i class="fas fa-address-card"></i>
            <span class="link-text">About</span>
        </router-link> -->
    </nav>
</template>

<style lang="scss" scoped>
nav {
    @apply w-80 grid grid-cols-2 mb-4 mx-auto p-0 text-center sticky top-0 z-50;
    &::after {
        @apply absolute w-full h-full top-0 left-0
            rounded-none rounded-br-sm rounded-bl-sm bg-gradient-to-b
            from-gray-100 to-gray-200
            /* Dark Mode */
            dark:from-gray-600 dark:to-gray-500;
            
        content: "";
        z-index: -1;
        transform: perspective(100px) rotateX(355deg);
        transform-origin: center bottom;
    }
    
    a {
        @apply mr-2 font-semibold p-1 rounded-sm no-underline;
        &:last-child {
            @apply mr-0;
        }
        > span.link-text {
            @apply ml-1.5 text-transparent bg-clip-text bg-gradient-to-r
                text-gray-900
                /* Dark Mode */
                dark:text-gray-100 dark:from-gray-200 dark:to-gray-300;
        }
        &:hover,
        &.router-link-active {
            @apply border-b-4
                border-blue-800
                /* Dark Mode */
                dark:border-yellow-700;
        }
        > svg {
            @apply fill-current 
                text-indigo-800
                /* Dark Mode */
                dark:text-yellow-300;
        }
    }
}

@media(prefers-color-scheme: light) {
    nav {
        &::after {
            box-shadow: 0px 2px 10px 5px rgb(138, 138, 146);
            background: #babbbe;
            background: linear-gradient(135deg, rgb(197, 198, 199) 0%, rgb(215, 221, 228) 100%);
        }
    }
}

@media(prefers-color-scheme: dark) {
    nav {
        &::after {
            box-shadow: 0px 2px 10px 5px rgb(24, 25, 49);
            background: #212327;
            background: linear-gradient(135deg, rgb(43, 60, 83) 0%, rgb(24, 38, 58) 100%);
        }
    }
}


@media (max-width: 640px) {
    nav {
        @apply w-full;
        &::after { 
            transform: none;
        }
    }
}
</style>
