<script>

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
    }

    export let showSelectedOnly = false;

    export let editMode;

</script>


<div class="gallery">
    {#each photoFilenames as filename, index}
        {#if !showSelectedOnly || buttonStates[index]}
            <div class="img-container">
                <img src={getPhotoPath(filename)} alt={filename} />
                {#if editMode}
                    <button class:clicked={buttonStates[index]} on:click={() => handleClick(index)} class="toggle-button">
                        {#if buttonStates[index]}
                            <span class="check-text">✓</span>
                        {/if}
                    </button>
                {/if}
            </div>
        {/if}
    {/each}
</div>


<style>

    .gallery {
        padding-bottom: 3px;
        display: grid;
        grid-template-columns: 315px 315px 315px;
        grid-gap: 8px;
        height: 95%;
        width: 983px; /*don't like how this is hard coded... fix later*/
        overflow-y: auto;
        /*background-color: blue;*/
    }

    .gallery::-webkit-scrollbar {
        width: 1px; /* Adjust as needed */
        
    }

    .gallery::-webkit-scrollbar-thumb {
        background-color: #ccc; /* Adjust as needed */
        border-radius: 3%;
    }

    .gallery img {
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

    .checkmark-icon {
        position: absolute;
        top: 0px;
        left: 0px;
        width: 10px;
        height: 10px;
    }
</style>