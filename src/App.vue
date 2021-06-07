<template>

    <router-view/>
</template>

<script>

export default {
  name: "App",
  watch: {
        $route(to,) {
            document.title = 'VMSS - ' +to.meta.title || 'VMSS';
        },
    },
  data: () => ({
    list: "",
    dialog: false,
    drawer: null,
  }),
};
</script>
