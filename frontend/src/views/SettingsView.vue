<script setup lang="ts">
import axios from 'axios'
import { ref } from 'vue'
import { useToast } from '@nuxt/ui/runtime/composables/useToast.js'

const toast = useToast()
const content = ref(``)

axios
  .get('http://127.0.0.1:8000/api/v1/settings/mkdocs_yml')
  .then((res) => (content.value = res.data))
  .catch((err) => {
    console.error(err)
    toast.add({
      title: 'Ошибка загрузки категорий',
      description: err.message,
      icon: 'i-tabler-alert-circle',
      color: 'error',
    })
  })
</script>

<template>
  <div>
    <UCodeBlock :code="content" lang="yaml" show-line-numbers />
  </div>
</template>
