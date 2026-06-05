import MainView from '@/views/MainView.vue'
import FilesView from '@/views/FilesView.vue'
import { createRouter, createWebHistory } from 'vue-router'
import SyncView from '@/views/SyncView.vue'
import SettingsView from '@/views/SettingsView.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', component: MainView },
    { path: '/add_file', component: FilesView },
    { path: '/sync', component: SyncView },
    { path: '/settings', component: SettingsView },
  ],
})

export default router
