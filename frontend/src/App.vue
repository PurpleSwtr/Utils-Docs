<script setup lang="ts">
import { computed, ref } from 'vue'
import type { NavigationMenuItem, StepperItem } from '@nuxt/ui'
import { useToast } from '@nuxt/ui/runtime/composables/useToast.js'
import axios from 'axios'

const toast = useToast()
const isSyncing = ref(false)
const modalOpen = ref(false)
const currentStep = ref(0)

const commitMessage = ref('')

const steps = computed<StepperItem[]>(() => [
  {
    title: 'Подготовка изменений',
    icon: currentStep.value > 0 ? 'i-tabler-check' : 'i-tabler-alert-circle',
  },
  {
    title: 'Отправка на GitHub',
    icon: currentStep.value > 1 ? 'i-tabler-check' : 'i-tabler-refresh',
  },
  {
    title: 'Данные успешно обновлены',
    icon: 'i-tabler-brand-github',
  },
])

const sync = async () => {
  if (isSyncing.value) return

  if (!commitMessage.value.trim()) {
    toast.add({
      title: 'Ошибка валидации',
      description: 'Введите сообщение коммита перед синхронизацией',
      icon: 'i-tabler-alert-circle',
      color: 'error',
    })
    return
  }

  isSyncing.value = true
  currentStep.value = 1

  try {
    const response = await axios.post(
      'http://127.0.0.1:8000/api/v1/sync/sync',
      {},
      {
        params: {
          msg: commitMessage.value.trim(),
        },
        headers: {
          accept: 'application/json',
          'Content-Type': 'application/json',
        },
      },
    )
    if (response.data.status === 'error') {
      throw new Error(response.data.message)
    }
    if (response.data.status === 'skipped') {
      toast.add({
        title: 'Пропущено',
        description: 'Нет изменений для синхронизации',
        icon: 'i-tabler-info-circle',
        color: 'warning',
      })
      return
    }
    await new Promise((resolve) => setTimeout(resolve, 800))

    currentStep.value = 2

    toast.add({
      title: 'Успешно!',
      description: 'Синхронизация запущена в фоновом режиме',
      icon: 'i-tabler-file-check',
      color: 'success',
    })
  } catch (err: any) {
    console.error(err)
    currentStep.value = 0

    toast.add({
      title: 'Ошибка синхронизации',
      description: err.response?.data?.detail || err.message,
      icon: 'i-tabler-alert-circle',
      color: 'error',
    })
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
        <UColorModeButton class="hover:cursor-pointer" />
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

        <UModal v-model:open="modalOpen">
          <UButton
            class="hover:cursor-pointer"
            label="Синхронизация"
            icon="i-tabler-refresh"
            color="neutral"
            variant="subtle"
          />

          <template #content>
            <div class="p-4 flex flex-col gap-4">
              <UStepper v-model="currentStep" :items="steps" orientation="vertical" />

              <div v-if="currentStep < 2" class="flex flex-col gap-1.5">
                <label class="text-sm font-medium text-gray-700 dark:text-gray-300">
                  Сообщение для коммита Git
                </label>
                <UInput v-model="commitMessage" :disabled="isSyncing" />
              </div>

              <div class="flex justify-end">
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
