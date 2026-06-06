<template>
  <UForm class="flex min-h-screen w-full items-center justify-center p-4" @submit="addToDocs">
    <UPageCard title="Добавление записи в базу знаний" class="w-full max-w-3xl">
      <div class="grid w-full grid-cols-2 gap-6">
        <UFormField label="Категория" required>
          <UInputMenu
            v-model="form.category"
            :items="categories"
            :ui="{ item: 'mb-2 last:mb-0' }"
            placeholder="Выберите Категорию"
            :reset-search-term-on-select="false"
            @update:search-term="preventSearchTermUpdate"
          />
        </UFormField>

        <UFormField label="Раздел" required>
          <UInputMenu
            v-model="form.section"
            :items="sections"
            placeholder="Выберите раздел"
            :reset-search-term-on-select="false"
            @update:search-term="preventSearchTermUpdate"
            :disabled="!form.category"
          />
        </UFormField>

        <UFormField label="Форматирование" class="col-span-2">
           <div class="flex items-center gap-4">
             <UInput
             v-model="form.code"
             placeholder="Метка языка"
             :disabled="form.isNote"
             />
             <USwitch
               v-model="form.isNote"
               label="Режим заметки"
             />
           </div>
         </UFormField>
        <UFormField label="Заголовок" required>
          <UInput v-model="form.title" placeholder="Введите заголовок" />
        </UFormField>


        <UFormField label="Текст" required class="col-span-2">
          <UTextarea
            v-model="form.text"
            placeholder="Введите текст записи"
            :rows="5"
            class="w-full"
          />
        </UFormField>
      </div>

      <div class="mt-6 flex justify-end">
        <UButton
          class="hover:cursor-pointer"
          type="submit"
          label="Сохранить запись"
          color="primary"
          size="lg"
          :loading="isSubmitting"
        />
      </div>
    </UPageCard>
  </UForm>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'
import axios from 'axios'
import { useToast } from '@nuxt/ui/runtime/composables/useToast.js'

const toast = useToast()
const selectedCategory = ref<any>(null)
const selectedSection = ref<any>(null)
const categories = ref([])
const sections = ref([])

const isSubmitting = ref(false)

const form = ref({
  category: null,
  section: null,
  title: '',
  code: '',
  text: '',
  isNote: false
})

const preventSearchTermUpdate = (): void => {}

axios
  .get('http://127.0.0.1:8000/api/v1/docs/categories')
  .then((res) => (categories.value = res.data))
  .catch((err) => {
    console.error(err)
    toast.add({
      title: 'Ошибка загрузки категорий',
      description: err.message,
      icon: 'i-tabler-alert-circle',
      color: 'error',
    })
  })

watch(
  () => form.value.category,
  async (newCat) => {
    form.value.section = null
    if (!newCat) {
      sections.value = []
      return
    }
    try {
      const res = await axios.get(`http://127.0.0.1:8000/api/v1/docs/sections?category=${newCat}`)
      sections.value = res.data
    } catch (err: any) {
      console.error(err)
      sections.value = []
      toast.add({
        title: 'Ошибка загрузки разделов',
        description: err.message,
        icon: 'i-tabler-alert-circle',
        color: 'error',
      })
    }
  },
  { immediate: true },
)

const addToDocs = async () => {
  if (!form.value.category || !form.value.section || !form.value.title || !form.value.text) {
    toast.add({
      title: 'Ошибка валидации',
      description: 'Заполните все обязательные поля',
      icon: 'i-tabler-alert-circle',
      color: 'error',
    })
    return
  }

  isSubmitting.value = true
  try {
    const payload = {
      category: form.value.category,
      section: form.value.section,
      title: form.value.title,
      text: form.value.text,
      code: form.value.isNote ? '' : (form.value.code || ''),
      is_note: form.value.isNote,
    }

    const response = await axios.post('http://127.0.0.1:8000/api/v1/docs/add', payload, {
      headers: { 'Content-Type': 'application/json' },
    })

    toast.add({
      title: 'Успешно!',
      description: 'Запись добавлена в базу знаний',
      icon: 'i-tabler-file-check',
      color: 'success',
    })

    form.value = {
      category: form.value.category,
      section: form.value.section,
      title: '',
      code: form.value.code,
      text: '',
      isNote: form.value.isNote,

    }
  } catch (err: any) {
    console.error(err)
    toast.add({
      title: 'Ошибка при сохранении',
      description: err.response?.data?.detail || err.message,
      icon: 'i-tabler-alert-circle',
      color: 'error',
    })
  } finally {
    isSubmitting.value = false
  }
}
</script>
