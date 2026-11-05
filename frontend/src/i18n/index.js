import enUS from './en-US'
import es from './es'
import quasarEn from 'quasar/lang/en-US'
import quasarEs from 'quasar/lang/es'
 
// To add a language: create src/i18n/<code>.js and add one entry here.
export const languages = [
  { code: 'en-US', label: 'English', short: 'EN', messages: enUS, quasarLang: quasarEn },
  { code: 'es', label: 'Español', short: 'ES', messages: es, quasarLang: quasarEs }
]
 
export const messages = Object.fromEntries(languages.map((l) => [l.code, l.messages]))
 
export const DEFAULT_LOCALE = 'en-US'
export const STORAGE_KEY = 'locale'

