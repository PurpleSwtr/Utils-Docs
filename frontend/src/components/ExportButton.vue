<script setup lang="ts">
import { useExport } from '@/composables/useExport';

const { isDownloading, downloadExport } = useExport()
</script>

<template>
  <UTooltip text="Скачать выгрузку" class="hover:cursor-pointer">
    <UButton
      color="neutral"
      variant="ghost"
      :loading="isDownloading"
      :disabled="isDownloading"
      aria-label="Скачать выгрузку"
      icon="i-tabler-file-zip"
      @click="downloadExport"
    />
  </UTooltip>
</template>
