<script setup lang="ts">
import { computed, ref } from 'vue'
import type { NavigationMenuItem, StepperItem } from '@nuxt/ui'
import { useToast } from '@nuxt/ui/runtime/composables/useToast.js'

const toast = useToast()
const isSyncing = ref(false)
const modalOpen = ref(false)
const currentStep = ref(0)
const step1Status = ref<'pending' | 'current' | 'completed'>('current')
const step2Status = ref<'pending' | 'current' | 'completed'>('pending')

const steps = computed<StepperItem[]>(() => [
  {
    title: 'Отслеживание изменений',
    icon: step1Status.value === 'completed' ? 'i-tabler-check' : 'i-tabler-alert-circle',
  },
  {
    title: 'Синхронизация данных',
    icon: step2Status.value === 'completed' ? 'i-tabler-check' : 'i-tabler-refresh',
  },
  {
    title: 'Данные обновлены',
    icon: 'i-tabler-brand-github',
  },
])

const sync = async () => {
  if (isSyncing.value) return

  currentStep.value = 1
  isSyncing.value = true

  try {
    await new Promise((resolve) => setTimeout(resolve, 2000))
    currentStep.value = 2

    toast.add({ title: 'Синхронизация завершена', color: 'success' })
  } catch {
    currentStep.value = 0
    toast.add({ title: 'Ошибка', color: 'error' })
  } finally {
    isSyncing.value = false
  }
}

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
        <UTooltip text="GitHub">
          <UButton
            color="neutral"
            variant="ghost"
            to="https://purpleswtr.github.io/Utils-Docs/"
            target="_blank"
            aria-label="GitHub"
            icon="i-tabler-brand-github"
          />
        </UTooltip>

        <UModal v-model:open="modalOpen">
          <UButton label="Синхронизация" icon="i-tabler-refresh" color="neutral" variant="subtle" />

          <template #content>
            <div class="p-4">
              <UStepper v-model="currentStep" :items="steps" orientation="vertical" />
              <!-- steps теперь только title/description, status не нужен -->
              <div class="mt-4 flex justify-end">
                <UButton
                  size="sm"
                  :loading="isSyncing"
                  :disabled="currentStep === 2"
                  color="primary"
                  icon="i-tabler-refresh"
                  @click="sync"
                >
                  {{ currentStep === 2 ? 'Синхронизировано' : 'Синхронизировать' }}
                </UButton>
              </div>
            </div>
          </template>
        </UModal>
      </template>
    </UHeader>

    <main>
      <RouterView />
    </main>
  </UApp>
</template>
