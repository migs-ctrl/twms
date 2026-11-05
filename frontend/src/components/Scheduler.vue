<template>
    <q-dialog v-model="alert" persistent @before-show="resetForm">
    <q-card style="width: 520px; max-width: 95vw">
      <q-form @submit.prevent="onSubmit">
        <q-card-section>
          <div class="text-h6">{{ $t('appointment.title') }}</div>
        </q-card-section>
 
        <q-card-section class="q-pt-none q-gutter-y-md">
          <!-- Client details -->
          <div class="row q-col-gutter-md">
            <div class="col-12 col-sm-6">
              <q-input
                v-model="form.firstName"
                :label="$t('appointment.firstName')"
                outlined
                autocomplete="given-name"
                :rules="[(v) => !!v?.trim() || t('validation.firstName')]"
              />
            </div>
            <div class="col-12 col-sm-6">
              <q-input
                v-model="form.lastName"
                :label="$t('appointment.lastName')"
                outlined
                autocomplete="family-name"
                :rules="[(v) => !!v?.trim() || t('validation.lastName')]"
              />
            </div>
          </div>
 
          <q-input
            v-model="form.email"
            :label="$t('appointment.email')"
            type="email"
            outlined
            autocomplete="email"
            :rules="[(v) => !!v?.trim() || t('validation.emailRequired'), validEmail]"
          >
            <template #prepend><q-icon name="mail" /></template>
          </q-input>
 
          <q-input
            v-model="form.phone"
            :label="$t('appointment.phone')"
            type="tel"
            outlined
            autocomplete="tel"
            :rules="[(v) => !!v?.trim() || t('validation.phoneRequired'), validPhone]"
          >
            <template #prepend><q-icon name="call" /></template>
          </q-input>

                    <!-- Date and time -->
          <div class="row q-col-gutter-md">
            <div class="col-12 col-sm-7">
              <q-input
                v-model="form.date"
                :label="$t('appointment.date')"
                mask="####-##-##"
                :placeholder="$t('appointment.datePlaceholder')"
                outlined
                :rules="[(v) => !!v || t('validation.dateRequired'), validDate]"
              >
                <template #append>
                  <q-icon name="event" class="cursor-pointer">
                    <q-popup-proxy cover transition-show="scale" transition-hide="scale">
                      <q-date v-model="form.date" mask="YYYY-MM-DD" :options="futureDates">
                        <div class="row justify-end">
                          <q-btn v-close-popup :label="$t('appointment.done')" color="primary" flat />
                        </div>
                      </q-date>
                    </q-popup-proxy>
                  </q-icon>
                </template>
              </q-input>
            </div>
 
            <div class="col-12 col-sm-5">
              <q-input
                v-model="form.time"
                :label="$t('appointment.startTime')"
                mask="##:##"
                :placeholder="$t('appointment.timePlaceholder')"
                outlined
                :rules="[(v) => !!v || t('validation.timeRequired'), validTime]"
              >
                <template #append>
                  <q-icon name="schedule" class="cursor-pointer">
                    <q-popup-proxy cover transition-show="scale" transition-hide="scale">
                      <q-time v-model="form.time" format24h>
                        <div class="row justify-end">
                          <q-btn v-close-popup :label="$t('appointment.done')" color="primary" flat />
                        </div>
                      </q-time>
                    </q-popup-proxy>
                  </q-icon>
                </template>
              </q-input>
            </div>
          </div>
        </q-card-section>

        <q-card-actions align="right" class="q-pa-md">
          <q-btn v-close-popup :label="$t('appointment.cancel')" flat :disable="loading" />
          <q-btn
            type="submit"
            :label="$t('appointment.schedule')"
            color="primary"
            unelevated
            :loading="loading"
          />
        </q-card-actions>
      </q-form>
    </q-card>
  </q-dialog>
</template>


<script setup>
import { ref,onMounted,  reactive } from 'vue'
import { useI18n } from 'vue-i18n'
import { date } from 'quasar'
const { t } = useI18n()
const alert = ref(false)

const props = defineProps({
  /** Optional prefill: { firstName, lastName, email, phone } */
  client: { type: Object, default: null },
  /** Show a spinner on the Schedule button while the parent saves */
  loading: { type: Boolean, default: false },
  /** Error message from the parent (for example, a failed API call) */
  error: { type: String, default: '' }
})

const emit = defineEmits(['save'])

// Let a parent open or close the dialog through a template ref (for example after a successful save)
defineExpose({
  open: () => (alert.value = true),
  close: () => (alert.value = false)
})


onMounted(() => {
  // Trigger dialog to open as soon as the component loads
  alert.value = true
})

const form = reactive({
  firstName: '',
  lastName: '',
  email: '',
  phone: '',
  date: '',
  time: '',
  sendReminder: true
})

// ---- Validation helpers ----
const todayKey = () => date.formatDate(Date.now(), 'YYYY-MM-DD')
// q-date passes dates to this function as YYYY/MM/DD
const futureDates = (d) => d >= todayKey().replaceAll('-', '/')

function validEmail(v) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v.trim()) || t('validation.emailInvalid')
}
 
function validPhone(v) {
  const digits = v.replace(/\D/g, '')
  return (digits.length >= 10 && digits.length <= 15) || t('validation.phoneInvalid')
}
 
function validDate(v) {
  return /^\d{4}-\d{2}-\d{2}$/.test(v) && !isNaN(new Date(`${v}T00:00`)) && v >= todayKey()
    ? true
    : t('validation.dateInvalid')
}
 
function validTime(v) {
  if (!/^([01]\d|2[0-3]):[0-5]\d$/.test(v)) return t('validation.timeInvalid')
  if (form.date === todayKey() && new Date(`${form.date}T${v}`) <= new Date()) {
    return t('validation.timePast')
  }
  return true
}

// ---- Actions ----
function resetForm() {
  form.firstName = props.client?.firstName ?? ''
  form.lastName = props.client?.lastName ?? ''
  form.email = props.client?.email ?? ''
  form.phone = props.client?.phone ?? ''
  form.type = null
  form.date = ''
  form.time = ''
  form.sendReminder = true
}
 
function onSubmit() {
  const start = new Date(`${form.date}T${form.time}`)
  //const end = date.addToDate(start, { minutes: form.duration })
 
  emit('save', {
    client: {
      firstName: form.firstName.trim(),
      lastName: form.lastName.trim(),
      email: form.email.trim(),
      phone: form.phone.trim()
    },
    start: start.toISOString(),
    //end: end.toISOString(),
    sendReminder: form.sendReminder
  })
}

</script>