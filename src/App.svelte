<script>
  // @ts-nocheck
  import PhotoGallery from './components/PhotoGallery.svelte';
  import AlbumGallery from './components/AlbumGallery.svelte';
  //import jsonLibrary from './jeremy-library.JSON';

  let jsonLibrary;
  let photoFilenames = []; //needs to be all upper case
  let bestPhotos = []; // needs to be all upper case
  let moments = [];

  // Fetch JSON data when the component is mounted - code from ChatGPT
  async function fetchData() {
  try {
    const response = await fetch('src/jeremy-library.JSON');
    if (!response.ok) {
      throw new Error('Failed to fetch JSON');
    }
    const data = await response.json();
    //console.log(data); // Log the response data
    jsonLibrary = data; // Assign the data to jsonLibrary
    //console.log("second", jsonLibrary);
    moments = jsonLibrary.Moments;

    jsonLibrary.Moments.forEach(moment => {
      //console.log("success loop");
      photoFilenames = photoFilenames.concat(moment.photos);
      photoFilenames = photoFilenames.map(name => name.toUpperCase());
      bestPhotos = bestPhotos.concat(moment.best_photos);
      bestPhotos = bestPhotos.map(name => name.toUpperCase());
    });
    console.log(bestPhotos);
  } catch (error) {
    console.error('There was a problem with the fetch operation:', error);
  }
}
  // Call the function to fetch data
  fetchData();

  /*let photoFilenames = [
    'IMG_3752.jpg', 'IMG_3753.jpg', //jeremy maggie michelle
    'IMG_6604.jpg', 'IMG_6606.jpg', 'IMG_6590.jpg', 
    'IMG_6655.jpg', 'IMG_6656.jpg', 'IMG_6657.jpg', //jeremy on cannon
    'IMG_6658.jpg', 'IMG_6666.jpg', 'IMG_6801.jpg', 'IMG_6836.jpg', 
    'IMG_3986.jpg', 'IMG_3988.jpg', 'IMG_3989.jpg', 'IMG_3990.jpg', 'IMG_3991.jpg', 'IMG_3992.jpg', 
    'IMG_3993.jpg', 'IMG_3994.jpg', 'IMG_3995.jpg', 'IMG_3996.jpg', 'IMG_3997.jpg', 'IMG_3998.jpg', //all on cannon
    'IMG_6932.jpg', 'IMG_6933.jpg', //church
    'IMG_7065.jpg', 
    'IMG_7177.jpg', 'IMG_7178.jpg', 'IMG_7179.jpg', //street sunset
    'IMG_7278.jpg', 'IMG_7304.jpg', 
    'IMG_7348.jpg', 'IMG_7349.jpg', 'IMG_7350.jpg', 'IMG_7351.jpg', //skygarden
    'IMG_7358.jpg', 
    'IMG_6393.jpg', 'IMG_6394.jpg', 'IMG_6395.jpg', 'IMG_6396.jpg', 'IMG_6397.jpg', 'IMG_6398.jpg', //tea
    'IMG_7530.jpg',
    'IMG_7475.jpg', 'IMG_7476.jpg','IMG_7477.jpg', //cocktail
    'IMG_7466.jpg' 
  ]; // Array of photo filenames*/
  

  let albumThumbnails = {
    'Austria': 'IMG_6196.jpg',
    'Cesky Krumlov': 'IMG_5440.JPG',
    'Hawaii': 'IMG_5765.jpg',
    'Italy': 'IMG_2648.jpg', 
    'Los Angeles': 'IMG_0772.jpg', 
    'Paris': 'IMG_0929.jpg', 
    'Prague': 'IMG_7991.jpg',
    'Puerto Rico': 'IMG_4271.jpg', 
    'Troja Chateau': 'IMG_6455.jpg',
  }

  //array of cutton "indices", based on indices in photoFilenames - there has to be better data structures but later problem
  let buttonStates = new Array(photoFilenames.length).fill(false); 

  let previousStates = new Array(photoFilenames.length).fill(false);

  // Note: a cull will override all current selections - help from ChatGPT
  function setButtonStatesCull() {
    // Store previous button states
    previousStates = buttonStates.slice();

    // Reset all button states to false
    buttonStates = buttonStates.map(() => false);
    
    //console.log("test best", bestPhotos)
    // Set button state to true for photos in bestPhotos
    photoFilenames.forEach((filename, index) => {
      const photo = jsonLibrary.Photos.find(photo => photo.filename === filename);
      //console.log(filename); 
      //console.log("photo fn", photo); 
      
      if (photo && bestPhotos.includes(photo.filename)) {
        buttonStates[index] = true;
      }
    });

    //console.log("prev", previousStates);
    //console.log("new", buttonStates);
  }

  function deselectAll() {
    for (let i = 0; i < photoFilenames.length; i++) {
      buttonStates[i] = false;
    }
  }

  //Can only go back one cull
  function undoCull() {
    for (let i = 0; i < photoFilenames.length; i++) {
      buttonStates[i] = previousStates[i];
    }
  }

  let showSelectedOnly = false;
  function handleChangeShow(event) {
    let selectedOption = event.target.value;
    if (selectedOption == "show_chosen"){
      showSelectedOnly = true;
    } else {
      showSelectedOnly = false;
    }
  }

  let momentsView = false;
  function handleChangeDisplay(event) {
    let selectedOption = event.target.value;
    if (selectedOption == "moments_view"){
      momentsView = true;
    } else {
      momentsView = false;
    }
  }

  let editMode = false;
  function toggleEditMode() {
    editMode = !editMode;
  }
</script>

<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Photo Manager</title>
    <link rel="stylesheet" href="./style.css">
  </head>
  <body>
    <div class="container">
      <span id="title">Moments <span id="subtitle">&nbsp;Automated Photo Manager</span> </span> <br>

      <div class="rounded-bar" id="title-sep"></div>

      <AlbumGallery {albumThumbnails}/>

      <div class="rounded-bar" id='view-sep'></div>

      <div class="view-scroll">

        <div id="view-title">
          Cull Your Photos &nbsp;
          <div class="tooltip">
            <img class="question" src='./src/assets/question.png'>
            <span class="tooltiptext">
              Culling is the process of choosing your best photos, reducing the number of photos in your library/album. <br>
              <br>
              Switch to Edit Mode to automatically or manually cull your photos.
            </span>
          </div>
          <br>
        </div>

        <div class="toggle">
          <input type="checkbox" on:click={toggleEditMode}/> 
          <label>&nbsp;&nbsp;Edit Mode
            
          </label>
        </div>

        {#if editMode}
          <p>
            <button class="option-button" on:click={() => setButtonStatesCull()}>Apply Auto-Cull</button>
            <button class="option-button" on:click={() => undoCull()}>Undo Auto-Cull</button>
            <button class="option-button" on:click={() => deselectAll()}>Deselect All </button>
          </p>
          <p id="cull-settings">
            Adjust Auto-Cull Settings: <br>
            Blurriness Scroll Bar <br>
            Brightness Scroll Bar <br>
            Sharpness Scroll Bar
          </p>
        {/if}

        <br>

        
      </div>

      <div class="right-half">
        <div id="gallery-banner">

          <div id="gallery-title">
            Library
          </div>

          <div id="gallery-dropdowns-container">
            <select class="gallery-dropdown" on:change={handleChangeShow}>
              <option value="show_all">Show All</option>
              <option value="show_chosen">Show Chosen ({buttonStates.filter(state => state === true).length})</option>
            </select>

            <select class="gallery-dropdown" on:change={handleChangeDisplay}>
              <option value="gallery_view">Gallery View</option>
              <option value="moments_view">Moments View</option>
            </select>
          </div>
        </div>

        <PhotoGallery bind:buttonStates={buttonStates} {photoFilenames} {moments} {showSelectedOnly} {momentsView} {editMode}/>
      </div> 

        
      
    </div>
      
  </body>
</html>
