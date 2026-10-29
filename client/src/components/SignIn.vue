<template>
  <div class="auth">
    <h2 class="text-center">Buenvenida</h2>
    <form @submit.prevent="signIn">
      <b-input square filled color="teal" label="Usario" v-model="form.username"/>
      <b-input square filled color="teal" label="Contrasena" type="password" v-model="form.password"/>
      <div class="row">
        <b-button @click="signIn"> Inciar Session </b-button>
      </div>
    </form>
  </div>
</template>


<style>
.auth {
  margin: 0 auto;
  width: 460px;
}
</style>