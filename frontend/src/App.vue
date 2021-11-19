<script setup lang="ts">
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup
import MainNav from "./components/navigation/MainNav.vue";
import Footer from "./components/Footer.vue";
</script>

<template>
    <header class="main-header"></header>
    <MainNav />
    <router-view v-slot="{ Component }">
        <transition name="fade" mode="out-in">
            <component :is="Component" />
        </transition>
    </router-view>
    <transition name="fade" mode="out-in">
        <Footer />
    </transition>
</template>

<style>
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}
/* Transitions */
.fade-enter-from {
    /* @apply opacity-0 transform translate-x-28; */
    @apply opacity-0;
}
.fade-enter-active {
    transition: 0.3s ease-out;
}
.fade-leave-to {
    /* @apply opacity-100 transform -translate-y-28; */
    @apply opacity-100;
}
.fade-leave-active {
    transition: all 0.3s ease-in;
}
</style>
