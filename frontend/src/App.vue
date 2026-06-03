<script setup lang="ts">
import { computed } from 'vue'
import type { NavigationMenuItem } from '@nuxt/ui'
import { useRoute } from 'vue-router'

const route = useRoute()

const items = computed<NavigationMenuItem[]>(() => [
  {
    label: 'Добавить запись',
    to: '/',
    icon: 'i-tabler-plus',
  },
  {
    label: 'База знаний',
    to: '/docs',
    icon: 'i-tabler-file',
  },
  {
    label: 'Синхронизировать',
    to: '/sync',
    icon: 'i-tabler-refresh',
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
        <UColorModeButton />

        <UTooltip text="Open on GitHub" :kbds="['meta', 'G']">
          <UButton
            color="neutral"
            variant="ghost"
            to="https://github.com/nuxt/ui"
            target="_blank"
            icon="i-sim"
            aria-label="GitHub"
          />
        </UTooltip>
      </template>
    </UHeader>
    <main>
      <RouterView />
    </main>
  </UApp>
</template>
