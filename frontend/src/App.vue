<script setup lang="ts">
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup
import { ref } from "vue";
import MainNav from "./components/navigation/MainNav.vue";
</script>

<template>
    <header class="main-heade">
        <p>This is header</p>
    </header>
    <nav class="main-nav">
        <MainNav />
    </nav>
    <div class="content">
        <router-view v-slot="{ Component }">
            <transition name="fade" mode="out-in">
                <component :is="Component"></component>
            </transition>
        </router-view>
    </div>
</template>

<style>
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}
header, nav {
    text-align: center;
}
.content {
    width: 40%;
    min-width: 502px;
    margin: 0 auto;
    position: relative;
    text-align: left;
}
.fade-enter-from {
    opacity: 0;
    transform: translateX(100px);
}
.fade-enter-active {
    transition: 0.3s ease-out;
}
.fade-leave-to {
    opacity: 1;
    transform: translateX(-100px);
}
.fade-leave-active {
    transition: all 0.3s ease-in;
}
</style>
