<script setup lang="ts">
import { ref } from 'vue'

const value = ref<File[] | null>(null)
const isSending = ref(false)

function sendFiles() {
  console.log(value.value)

  if (!value.value) return

  const formData = new FormData()
  isSending.value = true
  value.value.forEach((file) => formData.append('files', file))
}
</script>

<template>
  <UForm class="flex flex-col gap-4 min-h-screen w-full items-center justify-center p-4">
    <UFileUpload
      m
      color="primary"
      highlight
      label="Перетащите свои изображения сюда"
      description="SVG, PNG, JPG, GIF"
      v-model="value"
      class="w-lg min-h-96 hover:cursor-pointer"
      accept="image/*"
      icon="i-tabler-photo-up"
    />
    <UButton
      size="sm"
      :loading="isSending"
      :disabled="value === null"
      color="primary"
      icon="i-tabler-upload"
      @click="sendFiles"
    >
      {{ isSending === false ? 'Отправить' : 'Загрузка' }}
    </UButton>
  </UForm>
</template>
