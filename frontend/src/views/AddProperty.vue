<template>
  <div class="max-w-screen-md mx-auto mt-8 p-6 bg-white rounded-md shadow-md">
    <h2 class="text-3xl font-bold mb-6">Add Property</h2>

    <form @submit.prevent="submitForm" class="space-y-4">
      <div>
        <label for="title" class="block text-sm font-medium text-gray-700">Title:</label>
        <input v-model="property.title" type="text" id="title" class="mt-1 p-2 w-full border rounded-md">
      </div>

      <div>
        <label for="description" class="block text-sm font-medium text-gray-700">Description:</label>
        <textarea v-model="property.description" id="description" class="mt-1 p-2 w-full border rounded-md"></textarea>
      </div>

      <div>
        <label for="address" class="block text-sm font-medium text-gray-700">Address:</label>
        <input v-model="property.address" type="text" id="address" class="mt-1 p-2 w-full border rounded-md">
      </div>

      <div class="grid grid-cols-2 gap-4">
        <div>
          <label for="city" class="block text-sm font-medium text-gray-700">City:</label>
          <input v-model="property.city" type="text" id="city" class="mt-1 p-2 w-full border rounded-md">
        </div>

        <div>
          <label for="state" class="block text-sm font-medium text-gray-700">State:</label>
          <input v-model="property.state" type="text" id="state" class="mt-1 p-2 w-full border rounded-md">
        </div>
      </div>

      <div>
        <label for="price" class="block text-sm font-medium text-gray-700">Price:</label>
        <input v-model="property.price" type="number" id="price" class="mt-1 p-2 w-full border rounded-md">
      </div>

      <button type="submit" class="bg-blue-500 text-white p-2 mt-4 w-full rounded-md">Add Property</button>
    </form>
  </div>
</template>

<script>

import axios from 'axios';

export default {
  data() {
    return {
      property: {
        title: '',
        description: '',
        address: '',
        city: '',
        state: '',
        price: 0,
      },
    };
  },
  methods: {
    async submitForm() {
      // Simple validation
      if (!this.property.title || !this.property.description || !this.property.address || !this.property.city || !this.property.state || !this.property.price) {
        alert('Please fill in all required fields.');
        return;
      }

      try {
        const response = await axios.post('http://127.0.0.1:5000/properties', this.property);
        console.log('Property added successfully:', response.data);
        alert('Property added successfully!');
        this.clearForm();

      } catch (error) {
        console.error('Error adding property:', error);
        alert('Error adding property. Please try again.');
      }
    },
    clearForm() {
      this.property = {
        title: '',
        description: '',
        address: '',
        city: '',
        state: '',
        price: 0,
      };
    },
  },
};
</script>

<style scoped>
/* Add your scoped styles here */
</style>