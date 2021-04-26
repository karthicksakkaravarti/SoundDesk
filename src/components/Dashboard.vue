<template>
  <section class="pa-2">
    <v-breadcrumbs :items="items"></v-breadcrumbs>
  </section>
</template>

<script>
export default {
  data() {
    return {
      items: [
        {
          text: "Home",
          disabled: true,
        },
        {
          text: "Dashboard",
          disabled: true,
        },
      ],
    };
  },
};
</script>