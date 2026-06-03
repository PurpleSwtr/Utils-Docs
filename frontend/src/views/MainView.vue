<template>
  <UForm class="flex min-h-screen w-full items-center justify-center p-4">
    <UPageCard title="Добавление записи в базу знаний" class="w-full max-w-3xl">
      <div class="grid w-full grid-cols-2 gap-6">
        <UFormField label="Категория" required>
          <UInputMenu
            v-model="selectedCategory"
            :items="categories"
            :ui="{ item: 'mb-2 last:mb-0' }"
            placeholder="Выберите Категорию"
            :reset-search-term-on-select="false"
            @update:search-term="preventSearchTermUpdate"
          />
        </UFormField>

        <UFormField label="Раздел" required>
          <UInputMenu
            v-model="value"
            :items="items"
            placeholder="Выберите раздел"
            :reset-search-term-on-select="false"
            @update:search-term="preventSearchTermUpdate"
          />
        </UFormField>

        <UFormField label="Заголовок" required>
          <UInput placeholder="Введите заголовок" />
        </UFormField>

        <UFormField label="Метка для кода">
          <UInput placeholder="Введите метку для кода" />
        </UFormField>

        <UFormField label="Текст" required class="col-span-2">
          <UTextarea placeholder="Введите текст записи" rows="5" class="w-full" />
        </UFormField>
      </div>

      <div class="mt-6 flex justify-end">
        <UButton
          class="hover:cursor-pointer"
          type="submit"
          label="Сохранить запись"
          color="primary"
          size="lg"
        />
      </div>
    </UPageCard>
  </UForm>
</template>

<script setup lang="ts">
const items = ref([])
const value = ref('')
const selectedCategory = ref(null)

const preventSearchTermUpdate = (): void => {}

import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useToast } from '@nuxt/ui/runtime/composables/useToast.js'

const categories = ref([])

const toast = useToast()

const fetchPosts = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/api/v1/docs/categories')
    categories.value = response.data
  } catch (err: any) {
    toast.add({
      title: 'Ошибка при получении данных от сервера',
      description: err.message || String(err),
      icon: 'i-tabler-alert-circle',
      color: 'error',
    })
  }
}

onMounted(fetchPosts)
</script>
