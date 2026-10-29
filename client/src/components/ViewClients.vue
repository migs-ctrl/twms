<template>
	<h3> Clientes </h3>
	<b-table :items="clients" :fields="fields" virtual-scroll>
	</b-table>
</template>

<script setup>
    import { ref } from 'vue'
    import axios from 'axios'

    const clients = ref([])
    const fields = [
    	{
    		key:'first_name'
    	}, 
    	{
    		key: 'last_name',
    		sortable: true
    	},
    	{
    		key: 'dob',
    		sortable: true,
    		label: 'DOB'
    	},
    	{
    		key: 'phone'
    	}, 
    	{
    		key: 'email'
    	}, 
    	{
    		key: 'address'
    	}]
    
    async function getClients(){
    	var response = await axios.get('http://localhost/api/clients/')
    	.then(res => clients.value = res.data )
    }

    getClients()

</script>

<style>
</style>