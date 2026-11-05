<template>
  <q-btn flat dense no-caps icon="translate" :label="current.short" :aria-label="$t('language.label')">
    <q-menu>
      <q-list style="min-width: 140px">
        <q-item
          v-for="lang in languages"
          :key="lang.code"
          v-close-popup
          clickable
          :active="lang.code === locale"
          @click="setLocale(lang.code)"
        >
          <q-item-section>{{ lang.label }}</q-item-section>
          <q-item-section v-if="lang.code === locale" side>
            <q-icon name="check" />
          </q-item-section>
        </q-item>
      </q-list>
    </q-menu>
  </q-btn>
</template>

<script setup>
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'
import { languages } from '@/i18n'
import { setLocale } from '@/boot/i18n'

const { locale } = useI18n()
const current = computed(() => languages.find((l) => l.code === locale.value) ?? languages[0])
</script>