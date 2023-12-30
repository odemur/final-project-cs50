import { createRouter, createWebHistory } from 'vue-router';
import AddProperty from '@/views/AddProperty.vue';
import ListProperties from '@/views/ListProperties.vue';
import ExportProperties from '@/views/ExportProperties.vue';

const routes = [
  { path: '/add-property', component: AddProperty },
  { path: '/list-properties', component: ListProperties },
  { path: '/export-properties', component: ExportProperties },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
