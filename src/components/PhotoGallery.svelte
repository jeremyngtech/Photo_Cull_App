<script>

    export let photoFilenames;
    // Function to get the path of each photo
    function getPhotoPath(filename) {
        //return './jeremy_lib/IMG_6657.jpg';
        let path = './src/lib/jeremy_lib/' + filename;
        console.log(path);
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
                            <!--<img src="./src/assets/checkmark.svg" alt="Checkmark" class="checkmark-icon">-->
                        {/if}
                    </button>
                {/if}
            </div>
        {/if}
    {/each}
</div>


<style>

    .gallery {
        padding-top: 3px;
        padding-bottom: 3px;
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        grid-gap: 1px;
        height: 95vh;
        overflow-y: auto;
        /*background-color: blue;*/
    }

    .gallery img {
        width: 375px;
        height: 375px; 
        overflow: hidden;
        object-fit: cover;
        border-radius: 2%;
    }

    .img-container {
        position: relative;
    }

    .toggle-button {
        position: absolute; /* Position the toggle button relative to its containing image */
        top: 17px; /* Position at the top */
        right: 23px; /* Position at the right */
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