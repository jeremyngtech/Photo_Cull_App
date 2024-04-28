<script>
    import { createEventDispatcher } from 'svelte';

    export let photoFilenames;
    // Function to get the path of each photo
    function getPhotoPath(filename) {
        //return './jeremy_lib/IMG_6657.jpg';
        let path = './src/lib/jeremy_lib/' + filename;
        //console.log(path);
        return path; // Assuming photos are in the 'photos' directory inside the 'static' directory
    }

    // Array to track click state of each button
    export let buttonStates;
    // Function to toggle the click state of a specific button
    function handleClick(index) {
        buttonStates[index] = !buttonStates[index];
        console.log(buttonStates)
    }

    export let showSelectedOnly = false;

    export let editMode;

    export let moments;

    export let momentsView = false;


    //Expanding image code - help from chatGPT
    // Define the initial state
    let expandedImage = null;

    $: masterIndex = 0;

    // Function to determine if the left button should be disabled
    let isLeftDisabled = false;

    // Function to determine if the right button should be disabled
    let isRightDisabled = false;
    
    function checkDisabled() {
        isLeftDisabled = masterIndex == 0;
        isRightDisabled = masterIndex == photoFilenames.length - 1;
    }

    // Function to toggle the expanded state for a specific image
    function toggleExpanded(image) {
        expandedImage = image === expandedImage ? null : image;
        masterIndex = photoFilenames.indexOf(expandedImage.toUpperCase());
        checkDisabled();
    }

    // Create an event dispatcher to handle clicks on the background
    const dispatch = createEventDispatcher();

    // Function to navigate to the previous image
    function goToPrevious() {
        masterIndex = photoFilenames.indexOf(expandedImage.toUpperCase());
        if (masterIndex != 0) {
            expandedImage = photoFilenames[masterIndex - 1];
            masterIndex -= 1;
        }
        checkDisabled();
    }

    // Function to navigate to the next image
    function goToNext() {
        masterIndex = photoFilenames.indexOf(expandedImage.toUpperCase());
        if (masterIndex != photoFilenames.length - 1) {
            expandedImage = photoFilenames[masterIndex + 1];
            masterIndex += 1;
        }
        checkDisabled();
    }

    
    

</script>

{#if expandedImage !== null}
    <div class="expanded-overlay">
        <button class="overlay-buttons" id="close-button" on:click={() => toggleExpanded(null)}>×</button>
        <img class="expanded-image" src={getPhotoPath(expandedImage)} alt="Expanded Image" />
        {#if !showSelectedOnly}
            <button class="overlay-buttons" id="nav-button-left" on:click={goToPrevious} class:disabled={isLeftDisabled}>&lt;</button>
            <button class="overlay-buttons" id="nav-button-right" on:click={goToNext} class:disabled={isRightDisabled}>&gt;</button>
        {/if}
    </div>
{/if}

<div class="display-container">
    {#if momentsView == false}
        <div class="gallery">
            {#each photoFilenames as filename, index}
                {#if !showSelectedOnly || buttonStates[index]}
                    <div class="img-container">
                        <img class="image" src={getPhotoPath(filename)} alt={filename} />
                        {#if editMode}
                            <button class:clicked={buttonStates[index]} on:click={() => handleClick(index)} class="toggle-button">
                                {#if buttonStates[index]}
                                    <span class="check-text">✓</span>
                                {/if}
                            </button>
                        {:else}
                            <!--<button class="expand-button" on:click={() => toggleExpanded(getPhotoPath(filename))}>
                                <img class="expand-icon" src="./src/assets/expand.png" alt="expand">
                            </button>-->
                            <img class="expand-button" src="./src/assets/expand-5.png" alt="expand" 
                                on:click={() => toggleExpanded(filename)}>
                        {/if}
                    </div>
                {/if}
            {/each}
        </div>
    {:else}
        <div class="moments">
            {#each moments as moment, mom_index}
            <div class="moment" id="moment_{mom_index}">
                <div class="moment-title">Moment {mom_index + 1}</div>
                <div class="gallery" id="moment-photos">
                {#each moment.photos as filename, index}
                    {#if !showSelectedOnly || buttonStates[photoFilenames.indexOf(filename.toUpperCase())]}
                    <div class="img-container">
                        <img class="image" src={getPhotoPath(filename)} alt={filename} />
                        {#if editMode}
                            <button class:clicked={buttonStates[photoFilenames.indexOf(filename.toUpperCase())]}
                                on:click={() => handleClick(photoFilenames.indexOf(filename.toUpperCase()))} 
                                class="toggle-button">

                                {#if buttonStates[photoFilenames.indexOf(filename.toUpperCase())]}
                                    <span class="check-text">✓</span>
                                {/if}
                            </button>
                        {:else}
                            <img class="expand-button" src="./src/assets/expand-5.png" alt="expand" 
                                on:click={() => toggleExpanded(filename)}>
                        {/if}
                    </div>
                    {/if}
                {/each}
                </div>
            </div>
            {/each}
        </div>
    {/if}

</div>


<style>

    .gallery {
        padding-bottom: 3px;
        display: grid;
        grid-template-columns: 315px 315px 315px;
        grid-gap: 8px;
        height: 607px;
        width: 983px; /*don't like how this is hard coded... fix later*/
        overflow-y: auto;
    }

    .gallery::-webkit-scrollbar {
        width: 1px; /* Adjust as needed */  
    }

    .gallery::-webkit-scrollbar-thumb {
        background-color: #ccc; /* Adjust as needed */
        border-radius: 3%;
    }

    .image {
        width: 315px;
        height: 315px; 
        overflow: hidden;
        object-fit: cover;
        border-radius: 3%;
    }

    .img-container {
        position: relative;
        width: 315px;
        height: 315px; /*was 375 with 2 columns*/
       /*background-color: red;*/
    }

    .moments {
        height: 607px;
        width: 984px;
        overflow-y: auto;
        padding-top: 0px;
    }

    .moments::-webkit-scrollbar {
        width: 1px; /* Adjust as needed */  
    }

    .moments::-webkit-scrollbar-thumb {
        background-color: #ccc; /* Adjust as needed */
        border-radius: 3%;
    }

    .moment {
        margin-bottom: 20px;
    }

    #moment_0 {
        margin-top: 0px;
    }

    .moment-title {
        font-family: Didot;
        font-size: 17px;
        font-weight: 600;
        margin-bottom: 10px;
    }

    #moment-photos {
        padding-bottom: 3px;
        display: grid;
        grid-template-columns: 315px 315px 315px;
        grid-gap: 8px;
        width: 983px;
        height: auto;
        overflow-y: visible;
    }

    .toggle-button {
        position: absolute; /* Position the toggle button relative to its containing image */
        top: 17px; 
        right: 23px;
        background-color: rgba(255, 255, 255, 0.7); /* Semi-transparent background */
        border: 2px solid white;
        width: 31px; /* Set width */
        height: 31px; /* Set height */
        border-radius: 50%; /* Make it circular */
        padding: 0; /* Remove padding */
        cursor: pointer;
    }

    .toggle-button.clicked {
        background-color: #007AFF; /* Change background to blue when clicked */
    }

    .check-text {
        font-size: 15px;
        color: white;
    }

    .display-container {
        position: relative;
    }

    .expand-button {
        position: absolute; 
        top: 17px; 
        right: 17px;
        cursor: pointer;
        width: 16px;
        height: 16px;
        filter: invert(1);
    }

    .expanded-overlay {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.85); /* Semi-transparent black background */
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 999; /* Ensure it's above other content */
    }

    .expanded-image {
        max-width: 90%; /* Adjust as needed */
        max-height: 90%; /* Adjust as needed */
    }

    .overlay-buttons {
        background-color: transparent;
        border: none;
        color: white;
        font-size: 30px;
        font-family: 'Gill Sans';
        font-weight: 350;
        cursor: pointer;
        z-index: 1000; /* Ensure it's above the overlay */
    }

    #close-button {
        position: absolute;
        top: 15px;
        right: 19px;
    }

    #nav-button-left {
        font-size: 20px;
        position: absolute;
        top: 50%;
        left: 35px;
    }

    #nav-button-right {
        font-size: 20px;
        font-size: 20px;
        position: absolute;
        top: 50%;
        right: 35px;
    }

    .disabled {
        color: gray;
        pointer-events: none; /* Disable clicks */
    }
</style>