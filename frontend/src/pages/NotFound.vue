<template>
    <div class="not-found content">
        <img src="../assets/icons/error_window_icon_193961.svg" alt="Error: 404.Page Not Found">
        <h1>Sorry. This page doesn't exist.</h1>
    </div>
</template>

<style lang="scss" scoped>
    .not-found {
        @apply flex flex-col my-12 text-center rounded-md drop-shadow-lg shadow-lg
        bg-indigo-200 text-gray-800
        /* Dark */
        dark:bg-indigo-600 dark:text-white;

        img {
            @apply h-28;
        }

    }

</style>