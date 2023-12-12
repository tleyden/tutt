<template>
    <div>
        <!-- Link to open modal -->
        <a href="#" @click="toggleModal(true)" class="text-blue-500 hover:text-blue-700">
        {{ display }}
        </a>

        <!-- Modal -->
        <div v-if="isModalOpen" class="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto flex justify-center items-center">
            <div class="bg-white p-5 rounded shadow-lg max-w-lg mx-auto">
                <!-- Image -->
                <img :src="`dataset/${imageUrl}`" alt="Modal Image" class="max-w-full h-auto mb-4" />
                
                <!-- Text -->
                <p>{{ message }}</p>

                <!-- Close button -->
                <button @click="toggleModal(false)" class="mt-4 px-4 py-2 bg-red-500 text-white rounded hover:bg-red-700">
                Close
                </button>
            </div>
        </div>


    </div>
</template>

<script lang="ts">

    import { defineComponent, ref } from 'vue';
    import type { PropType } from 'vue';

    export default defineComponent({
    name: 'ImageModal',
    props: {
        message: {
            type: String as PropType<string>,
            required: true,
        },
        display: {
            type: String as PropType<string>,
            required: true,
        },
        imageUrl: {
            type: String as PropType<string>,
            required: true,
        },
    },
    setup() {
        const isModalOpen = ref(false);

        function toggleModal(open: boolean) {
        isModalOpen.value = open;
        }

        return { isModalOpen, toggleModal };
    },
    });

</script>

<style>
/* Add any additional styling for your modal here */
</style>
