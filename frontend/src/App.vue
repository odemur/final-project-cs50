<template>
  <div id="app" class="flex flex-col min-h-screen">
    <AppHeader />
    <main class="flex-1 p-4">
      <router-view />
    </main>
    <AppFooter />
  </div>
</template>

<script>
import AppHeader from '@/components/AppHeader.vue';
import AppFooter from './components/AppFooter.vue';

export default {
  components: {
    AppHeader,
    AppFooter
},
};
</script>

<style>
html, body {
  height: 100%;
}

body {
  margin: 0;
}

#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}
</style>
