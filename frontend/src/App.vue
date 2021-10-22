<script setup lang="ts">
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup
import { ref } from "vue";
import MainNav from "./components/navigation/MainNav.vue";
</script>

<template>
    <header class="main-header"></header>
    <MainNav />
    <article class="content">
        <router-view v-slot="{ Component }">
            <transition name="fade" mode="out-in">
                <component :is="Component" />
            </transition>
        </router-view>
    </article>
</template>

<style>
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}
.content {
    margin: 0 auto;
    position: relative;
    text-align: left;
}

/* Transitions */
.fade-enter-from {
    opacity: 0;
    @apply transform translate-x-28;
}
.fade-enter-active {
    transition: 0.3s ease-out;
}
.fade-leave-to {
    opacity: 1;
    @apply transform -translate-x-28;
}
.fade-leave-active {
    transition: all 0.3s ease-in;
}
</style>
