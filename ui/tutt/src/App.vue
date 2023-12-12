<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
import AlertButton from './components/Alert.vue'; 
import ImageModal from './components/ImageModal.vue'; 

const datasetDirectory = '../../../dataset';

// TODO: figure out how to use datasetDirectory here
import userData from '../../../dataset/dataset.json'


// function groupDatasetByDay(dataset: any) {

//   const groupedByDay = {};

//   dataset.entries.forEach(entry => {
//       // Assuming item.day exists and is a valid key
//       const dayMonthYear = getDayMonthYear(getFileName(entry.screenshot_filename))

//       // Check if the array for this day already exists; if not, create it
//       if (!groupedByDay[day]) {
//           groupedByDay[day] = [];
//       }

//       // Add the current item to the array for this day
//       groupedByDay[day].push(item);
//   });

// }

function getFileName(fullPath: string) {
    // Split the path by the directory separator
    const parts = fullPath.split(/[/\\]/);
    // Return the last part of the array (the filename)
    const filename_or_undefined = parts.pop();
    if (filename_or_undefined === undefined) {
        return "undefined";
    } else {
        return filename_or_undefined.trim();
    }
}

function getPathToDataFile(filename: string) {
    // contcat the datasetDirectory with the filename to get the full path
    return `${datasetDirectory}/${filename}`;
}

// function getDateFromFilename(filename: string) {

// }

function getTimestamp(filename: string) {
    // Given a filename like "foo_1702050969.11921.png"
    // extract the timestamp in python format and 
    // return it as a friendly string like "8:13 am"

    // Extract the timestamp from the filename
    // The filename is in the format "foo_1702050969.11921.png"
    const timestamp = filename.substring(
        filename.lastIndexOf('_') + 1, 
        filename.lastIndexOf('.')
    );

    // Convert the extracted timestamp to a Date object
    // The timestamp is in seconds, JavaScript Date requires milliseconds
    const date = new Date(parseFloat(timestamp) * 1000);

    // Format the date into a friendly string like "8:13 am"
    let hours = date.getHours();
    const minutes = date.getMinutes();
    const month = date.getMonth() + 1;
    const dateOfMonth = date.getDate();
    const ampm = hours >= 12 ? 'pm' : 'am';
    hours = hours % 12;
    hours = hours ? hours : 12; // the hour '0' should be '12'
    const minutesStr = minutes < 10 ? '0' + minutes : minutes;

    return `${hours}:${minutesStr} ${ampm} on ${month}/${dateOfMonth}`;

}

</script>

<template>
  <body>
    <!-- <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" /> -->

    <div class="wrapper">

        <div class="block max-w-xl p-6 bg-white border border-gray-200 rounded-lg shadow hover:bg-gray-100 dark:bg-gray-800 dark:border-gray-700 dark:hover:bg-gray-700">
            
          <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white text-left">All entries</h5>
        
            <div class="grid grid-cols-3 gap-4">
        
              <!-- row 0 -->
              <!-- <div class="text-center border-2 col-span-3">Key</div>  -->

              <template v-for="item in userData.entries">
                <!-- row n -->
                <div class="text-center border-0 flex justify-center items-center"> <ImageModal :image-url="getPathToDataFile(item.screenshot_filename)" :message="item.llm_response" :display="getTimestamp(getPathToDataFile(item.screenshot_filename))" /> </div>
                <div class="text-center border-0 flex justify-center items-center">{{ item.actual_category }}  </div>
                <div class="text-center border-0">
                  <!-- Note this loads from the public folder.  It requires a symlink from the dataset subdir into the public dir -->
                  <img :src="`dataset/${getPathToDataFile(item.screenshot_filename)}`" alt="Thumbnail" class="max-h-14 border-2">
                </div>
              </template>
      
        
            </div>
        </div>    


      <!-- old exmaple stuff .. 
        <HelloWorld msg="You did it!" />
      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
      </nav> -->
    
    
    </div>
  </body>

  <!-- old example stuff <RouterView /> -->
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
