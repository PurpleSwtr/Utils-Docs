<script setup lang="ts">
import { computed} from 'vue'
import type { NavigationMenuItem} from '@nuxt/ui'
import ModalSync from './components/ModalSync.vue';



const items = computed<NavigationMenuItem[]>(() => [
  {
    label: 'Добавить запись',
    to: '/',
    icon: 'i-tabler-plus',
  },
  {
    label: 'Добавить файл',
    to: '/add_file',
    icon: 'i-tabler-file-upload',
  },
  {
    label: 'Настройки',
    to: '/settings',
    icon: 'i-tabler-settings',
  },
  {
    label: 'База знаний',
    to: 'https://purpleswtr.github.io/Utils-Docs/',
    target: '_blank',
    icon: 'i-tabler-database-share',
  },
])
</script>

<template>
  <UApp>
    <UHeader>
      <template #title>
        <Logo class="h-6 w-auto" />
      </template>
      <UNavigationMenu :items="items" />
      <template #right>
        <UColorModeButton class="hover:cursor-pointer" text="Сменить тему"/>
        <ExportButton />
        <UTooltip text="GitHub">
          <UButton
            color="neutral"
            variant="ghost"
            to="https://github.com/PurpleSwtr/Utils-Docs"
            target="_blank"
            aria-label="GitHub"
            icon="i-tabler-brand-github"
          />
        </UTooltip>
        <ModalSync/>
      </template>
    </UHeader>
    <main>
      <RouterView />
    </main>
  </UApp>
</template>
