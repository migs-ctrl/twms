<template>
	<div>
		<header class="col align-self-start">
                <b-dropdown class="m-2"
                            id="dropdownMenuButton1"
                            text="Language">
                    <b-dropdown-item-button> Spanish </b-dropdown-item-button>
                    <b-dropdown-item-button> English </b-dropdown-item-button>
                </b-dropdown>
                <b-button-group>
                    <b-button href="tel:2819991920">
                        <b-icon-telephone/>
                    </b-button>
                    <b-button href="https://goo.gl/maps/E7rTcP8bycMs3a7a9">
                        <b-icon-pin-map/>
                    </b-button>
                    <b-button href="https://www.facebook.com/3americas.srvcs/">
                        <b-icon-facebook style="color:white"/>
                    </b-button>
                </b-button-group>
                <b-button @click="toLogin"> SIGN IN </b-button>
            </header>
			<AddClient class="col-md-6 col-sm-12" />
			<Scheduler class="col-md-6 col-sm-12 mt-5"/>
	</div>
</template>

<script setup>
	import Scheduler from "./Scheduler.vue"
    import AddClient from "./AddClient.vue"
	import { useRouter } from 'vue-router'
	const routerP = useRouter()
	
	function toLogin() {
		routerP.push('signin')
	}

	function changeLanguage (selectedLanguage) {
	      // this.setLanguage(selectedLanguage)
	}
</script>