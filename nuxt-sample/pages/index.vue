<template>
  <v-app>
    <!-- メインページ -->
    <v-main>
      <v-flex>
        <v-img src="~/assets/img/top.svg"></v-img>
      </v-flex>
    </v-main>
  </v-app>
</template>
<script>
export default {
  data: () => ({
    drawer: false,
    items: [
      { title: 'Home', icon: 'mdi-home', link: '#' },
      { title: 'About', icon: 'mdi-help-box', link: '#' },
    ],
  }),
}
</script>
