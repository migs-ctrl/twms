<template>
    <div class="container">
        <h3 class="text-center">Cliente Nuevo</h3>
        <div class="row">
            <div class="col">
                <label>First Name</label>
                <b-form-input v-model="fName"></b-form-input>
            </div>
            <div class="col">
                <label>Last Name</label>
                <b-form-input v-model="lName"></b-form-input>
            </div>
        </div>
        <label>Fecha de Nacimiento</label>
        <b-form-input type="date" v-model="DOB" class="mb-2"></b-form-input>
        <label>Cell Phone</label>
        <b-form-input v-model="phone"></b-form-input>

        <label>Address</label>
        <b-form-input v-model="address"></b-form-input>
        <label>E-mail</label>
        <b-form-input v-model="email"></b-form-input>
        <b-btn style='margin-top:1vh;background-color:#c1eeaa;' @click="addClient"> Confirmar </b-btn>
    </div>
</template>

<script setup>
    import { useRouter } from 'vue-router'
    import { ref } from 'vue'
    import axios from 'axios'

    var fName = ref(null)
    var lName = ref(null)
    var DOB = ref(null)
    var phone = ref(null)
    var address = ref(null)
    var email = ref(null)
    const routerP = useRouter()
    async function addClient() {
        var data = {
            'first_name': fName._value,
            'last_name': lName._value,
            'dob': DOB._value,
            'phone': phone._value,
            'address': address._value,
            'email': email._value
        }

        await axios({
            method: 'post',
            url: 'http://localhost/api/clients/',
            data: data,
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
        }).then(arg => routerP.push('/'))
        
    }

</script>