<template>
  <header class="bg-blue-500 p-4 text-white">
    <div class="inline">
      <h1 class="text-2xl font-bold inline">Real Estate System</h1>
    </div>
    <nav class="inline ml-4">
      <router-link to="/add-property" class="ml-4">Add Property</router-link>
      <router-link to="/list-properties" class="ml-4">List Properties</router-link>
      <router-link to="/export-properties" class="ml-4">Export Properties</router-link>
    </nav>
  </header>
</template>

<script>
export default {
  name: 'AppHeader',
};
</script>

<style scoped>
/* Add your scoped styles here */
</style>
