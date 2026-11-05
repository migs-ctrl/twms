import { createI18n } from 'vue-i18n'
import { Quasar } from 'quasar'
import { languages, messages, DEFAULT_LOCALE, STORAGE_KEY } from '@/i18n'

function initialLocale() {
  try {
    const saved = localStorage.getItem(STORAGE_KEY)
    if (languages.some((l) => l.code === saved)) return saved
  } catch {
    /* storage unavailable */
  }
  // Fall back to the browser language if we support it
  const browser = navigator.language?.split('-')[0]
  return languages.find((l) => l.code.split('-')[0] === browser)?.code ?? DEFAULT_LOCALE
}

export const i18n = createI18n({
  legacy: false,
  locale: initialLocale(),
  fallbackLocale: DEFAULT_LOCALE,
  messages
})

/** Switch the whole site: app text, Quasar's built-in text (calendar, etc.), <html lang>, and remember it. */
export function setLocale(code) {
  const lang = languages.find((l) => l.code === code)
  if (!lang) return
  i18n.global.locale.value = code
  Quasar.lang.set(lang.quasarLang)
  document.documentElement.setAttribute('lang', code)
  try {
    localStorage.setItem(STORAGE_KEY, code)
  } catch {
    /* ignore */
  }
}

export default ({ app }) => {
  app.use(i18n)
  setLocale(i18n.global.locale.value)
}