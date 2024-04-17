<script>
  // @ts-nocheck
  import PhotoGallery from './components/PhotoGallery.svelte';
  import AlbumGallery from './components/AlbumGallery.svelte';

  let photoFilenames = [
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
  ]; // Array of photo filenames

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

  // Initialize buttonStates in App.svelte
  let fixedCull = [0, 2, 3, 4, 5, 8, 9, 10, 11, 22, 25, 26, 27, 30, 31, 34, 36, 40, 43, 45, 47];

  let buttonStates = new Array(photoFilenames.length).fill(false);

  let previousStates = new Array(photoFilenames.length).fill(false);
  
  // Note: a cull will override all current selections
  function setButtonStatesCull(indices_arr) {
    //previousStates = buttonStates;
    for (let i = 0; i < photoFilenames.length; i++) {
      previousStates[i] = buttonStates[i];
    }
    console.log(previousStates);
    for (let i = 0; i < photoFilenames.length; i++) {
      if (indices_arr.includes(i)){
        buttonStates[i] = true;
      } else {
        buttonStates[i] = false;
      }
    }
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
  function toggleShowSelectedOnly() {
    showSelectedOnly = !showSelectedOnly;
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
      <span id="title">Cullify <span id="subtitle">&nbsp;Automated Photo Manager</span> </span> <br>

      <div class="rounded-bar" id="title-sep"></div>

      <AlbumGallery {albumThumbnails}/>

      <div class="rounded-bar" id='view-sep'></div>

      

      <div class="view-scroll">

        <p id="view-title">View Options <br></p>

        <div class="toggle">
          <input type="checkbox" on:click={toggleEditMode}/> 
          <label>&nbsp;&nbsp;Edit Mode&nbsp;&nbsp;
            <div class="tooltip">
              <img class="question" src='./src/assets/question.png'>
              <span class="tooltiptext">
                Edit Mode allows you to cull your photos and adjust cull settings. <br>
                <br>
                Culling is the process of reducing the number of photos by only selecting the best ones.
              </span>
            </div>
          </label>
        </div>

        {#if editMode}
          <p>
            <button on:click={() => setButtonStatesCull(fixedCull)}>Apply Cull</button>
            <button on:click={() => undoCull()}>Undo Cull</button>
            <button on:click={() => deselectAll()}>Deselect All</button>
          </p>
          <p>
            Adjust Cull Settings: <br>
            Blurriness Scroll Bar <br>
            Brightness Scroll Bar <br>
            Sharpness Scroll Bar
          </p>
        {/if}

        <br>

        <div class="toggle">
          <input type="checkbox" on:click={toggleShowSelectedOnly}/> 
          <label>&nbsp;&nbsp;Culled View</label>
        </div>
      </div>

      <div class="right-half">
        <PhotoGallery {buttonStates} {photoFilenames} {showSelectedOnly} {editMode}/>
      </div> 

        
      
    </div>
      
  </body>
</html>
