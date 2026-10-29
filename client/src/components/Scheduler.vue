<template>
    <div class="container">
        <h3 class="text-center"> Sistema de Citas</h3>



        <label for="datepicker">Fecha</label>
        <b-form-datepicker id="datepicker" v-model="selectedDate" :date-disabled-fn="dateDisabled" class="mb-2">
        </b-form-datepicker>

        <label for="pickEmployee">Empleado</label>
        <b-form-select id="pickEmployee" v-model="selectedEmployee">
            <option v-for="(employee, id) in options"
                    :value="employee.employee_id"
                    :key="id"
                    @click="onChangeEmployee(employee.employee_id)">
                {{ employee.employee_name }}
            </option>
        </b-form-select>

        <div v-if="selectedDate && selectedEmployee">
            <label for="timepicker">Hora</label>
            <b-form-select  v-model="selected2" id="timepicker">
                <option v-if="options2" v-for="(time, id) in options2"
                        :value="time.id"
                        :key="id">
                    {{ time.start_time  }}
                </option>
            </b-form-select>
        </div>
        <b-btn style='margin-top:1vh;background-color:#c1eeaa;'> Confirmar </b-btn>
    </div>
</template>

<script setup>
    import { ref } from 'vue'

    const options = ref([])
    const options2 = ref([])
    
    const selectedEmployee = ref(null)
    const selectedDate = ref(null)

    async function getEmployees() {
        var response = await fetch("http://localhost/api/employees/").then(res => res.json())
            .then(data => options.value = data)
    }
    async function getTimes(id) {
        const appointmentDay = new Date(selectedDate._value)
        var response = await fetch("localhost/api/timeslots/?id=" + id + "&start_time=" + appointmentDay.toISOString())
            .then(res => res.json())
            .then(data => {
                if (data) {
                    options2.value = data
                }
            })
    }

    function dateDisabled(ymd, date) {
        // Disable weekends (Sunday = `0`, Saturday = `6`) and
        // disable days that fall on the 13th of the month
        const now = new Date()
        const today = new Date(now.getFullYear(), now.getMonth(), now.getDate())
        // Return `true` if the date should be disabled
        return date < today
    }

    getEmployees()

    function onChangeEmployee(id) {
        getTimes(id)
    }
</script>

<style scoped>
    .custom-select {
        width: 100%;
        padding: 10px 5px 10px 5px;
    }
</style>