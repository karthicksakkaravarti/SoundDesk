<template>

    <router-view/>
</template>

<script>

export default {
  name: "App",
  data: () => ({
    list: "",
    dialog: false,
    drawer: null,
  }),
};
</script>
