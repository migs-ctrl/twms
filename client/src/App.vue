<template>
    <div class="container">
        <div class="column">
            <main>
                <RouterView />
            </main>
        </div>
    </div>
</template>

<style scoped>

.main {
    padding-top: 25vh;
}
.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
  }

  .logo {
    margin: 0 2rem 0 0;
  }


}
</style>
