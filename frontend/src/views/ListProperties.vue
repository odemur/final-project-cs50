<template>
  <div class="max-w-screen-md mx-auto mt-8 p-6 bg-white rounded-md shadow-md">
    <h2 class="text-3xl font-bold mb-6">List Properties</h2>

    <div class="mb-4">
      <label class="block text-sm font-medium text-gray-700">Search:</label>
      <input v-model="searchQuery" type="text" class="p-2 w-full border rounded-md">
    </div>

    <ul>
      <li v-for="property in filteredProperties" :key="property.id" class="border-b py-4">
        <div class="max-w-screen-md">
          <div class="mb-4">
            <label class="text-sm font-medium text-gray-700">Code:</label>
            {{ property.id }}
          </div>
          <div class="mb-4">
            <h3 class="text-xl font-bold">{{ property.title }}</h3>
          </div>
          <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700">Description:</label>
            <p class="text-gray-500">{{ property.description }}</p>
          </div>
          <div class="mb-4">
            <label class="text-sm font-medium text-gray-700">Price: </label> 
            <span class="text-blue-500 font-bold">{{ formatCurrency(property.price) }}</span>
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700">Address:</label>
            <p class="text-gray-600">{{ property.address }}, {{ property.city }}, {{ property.state }}</p>
          </div>
          <button @click="deleteProperty(property.id)" class="text-red-500 mt-4">Delete</button>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      properties: [],
      searchQuery: '',
    };
  },
  mounted() {
    this.fetchProperties();
  },
  computed: {
    filteredProperties() {
      return this.properties.filter(property => {
        const lowerCaseQuery = this.searchQuery.toLowerCase();
        return (
          property.title.toLowerCase().includes(lowerCaseQuery) ||
          property.description.toLowerCase().includes(lowerCaseQuery) ||
          property.address.toLowerCase().includes(lowerCaseQuery) ||
          property.city.toLowerCase().includes(lowerCaseQuery) ||
          property.state.toLowerCase().includes(lowerCaseQuery)
        );
      });
    },
  },
  methods: {
    async fetchProperties() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/properties');
        this.properties = response.data;
      } catch (error) {
        console.error('Error fetching properties:', error);
      }
    },
    async deleteProperty(propertyId) {
      try {
        await axios.delete(`http://127.0.0.1:5000/properties/${propertyId}`);
        this.properties = this.properties.filter(property => property.id !== propertyId);
        console.log('Property deleted successfully');
      } catch (error) {
        console.error('Error deleting property:', error);
      }
    },
    formatCurrency(amount) {
      return amount.toLocaleString('en-US', { style: 'currency', currency: 'USD' });
    },
  },
};
</script>

<style scoped>
/* Add your scoped styles here */
</style>
