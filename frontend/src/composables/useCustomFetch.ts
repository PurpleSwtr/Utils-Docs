import { ref } from 'vue'
import axios from 'axios'

import { useToast } from '@nuxt/ui/runtime/composables/useToast.js'

export function useCustomFetch(url: string | null) {
  const toast = useToast()
  const data = ref(null)
  const error = ref(null)

  const fetchData = async () => {
    try {
      if (url) {
        const response = await axios.get(url)
        data.value = response.data
      }
      error.value = null
    } catch (err: any) {
      const errorMessage = err.message || String(err)
      error.value = errorMessage
      data.value = null
      toast.add({
        title: 'Ошибка при получении данных от сервера',
        description: errorMessage,
        icon: 'i-tabler-alert-circle',
        color: 'error',
      })
    }
  }

  fetchData()

  return { data, error }
}
