<template>
    <div>
      <h2 class="text-2xl font-bold mb-4">Export Properties</h2>

      <button @click="exportProperties" class="bg-green-500 text-white p-2">Export Properties</button>
    </div>
  </template>
  
  <script>
  import api from '@/services/api';
  
  export default {
    methods: {
      async fetchProperties() {
        try {
          const response = await api.get('/properties');
          return response.data;
        } catch (error) {
          console.error('Error fetching properties:', error);
          throw error;
        }
      },
  
      async exportProperties() {
        try {
          const properties = await this.fetchProperties();
          const jsonData = JSON.stringify(properties, null, 2);
          const blob = new Blob([jsonData], { type: 'application/json' });
          const link = document.createElement('a');
          link.href = URL.createObjectURL(blob);
          link.download = 'properties.json';
          link.click();
        } catch (error) {
          console.error('Error exporting properties:', error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  /* Add your scoped styles here */
  </style>
  