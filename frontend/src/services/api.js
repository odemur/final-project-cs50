import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:5000',  // Adjust the URL based on your Flask API
});

export default api;