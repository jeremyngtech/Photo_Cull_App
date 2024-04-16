<script>
  // @ts-nocheck
  import PhotoGallery from './components/PhotoGallery.svelte';
  import AlbumGallery from './components/AlbumGallery.svelte';

  let photoFilenames = ['IMG_3752.jpg', 'IMG_6604.jpg', 'IMG_6606.jpg', 'IMG_6590.jpg', 'IMG_6657.jpg', 'IMG_6666.jpg', 'IMG_6801.jpg', 'IMG_6836.jpg', 'IMG_7065.jpg', 'IMG_7278.jpg', 'IMG_7304.jpg', 'IMG_7348.jpg', 'IMG_7358.jpg', 'IMG_7530.jpg' ]; // Array of photo filenames

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
      <span id="title">Photo Manager</span> <br>

      <AlbumGallery {albumThumbnails}/>

      <p id="view-title">View Options <br></p>
      
      <div class="toggle">
        <input type="checkbox" on:click={toggleShowSelectedOnly}/>
        <label> Culled View</label>
      </div>

      <br>
      
      <div class="toggle">
        <input type="checkbox" on:click={toggleEditMode}/>
        <label> Edit Mode</label>
      </div>

      {#if editMode}
        <p>
          Edit Cull: <br>
          <button on:click={() => setButtonStatesCull([0, 2, 4, 6, 7])}>Apply Cull</button>
          <button on:click={() => undoCull()}>Undo Cull</button>
          <button on:click={() => deselectAll()}>Deselect All</button>
        </p>
      {/if}
      
      <div class="right-half">
        <PhotoGallery {buttonStates} {photoFilenames} {showSelectedOnly} {editMode}/>
      </div> 
    </div>
      
  </body>
</html>
