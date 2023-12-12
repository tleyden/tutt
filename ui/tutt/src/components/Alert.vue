<template>
  <a href="#" @click.prevent="showAlert" class="text-blue-500 hover:text-blue-700">
    {{ display }}
  </a>

  </template>
  
  <script lang="ts">

  import { defineComponent } from 'vue';
  import type { PropType } from 'vue';

  export default defineComponent({
    name: 'AlertButton',
    props: {
      message: {
        type: String as PropType<string>,
        required: true,
      },
      display: {
        type: String as PropType<string>,
        required: true,
      },
    },
    methods: {
      showAlert() {
        alert(this.message);
      },
    },
  });
  </script>
  