import { ref } from 'vue'
import axios from 'axios'
import { useToast } from '@nuxt/ui/runtime/composables/useToast.js'

export function useExport() {
  const toast = useToast()
  const isDownloading = ref(false)

  const downloadExport = async () => {
    if (isDownloading.value) return
    isDownloading.value = true

    try {
      const response = await axios.get('http://127.0.0.1:8000/api/v1/files/download_backup', {
        responseType: 'blob',
      })

      const blob = new Blob([response.data], { type: 'application/zip' })
      const url = window.URL.createObjectURL(blob)

      const link = document.createElement('a')
      link.href = url
      link.setAttribute('download', 'backup.zip')
      document.body.appendChild(link)
      link.click()

      link.remove()
      window.URL.revokeObjectURL(url)

      toast.add({
        title: 'Архив успешно скачан',
        icon: 'i-tabler-file-check',
        color: 'success',
      })
    } catch (err: any) {
      console.error('Ошибка скачивания:', err)
      toast.add({
        title: 'Ошибка скачивания',
        description: err.response?.data?.detail || err.message || 'Не удалось скачать файл',
        icon: 'i-tabler-alert-circle',
        color: 'error',
      })
    } finally {
      isDownloading.value = false
    }
  }

  return { isDownloading, downloadExport }
}
