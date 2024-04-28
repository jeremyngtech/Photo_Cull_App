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
        console.log(buttonStates)
    }

    export let showSelectedOnly = false;

    export let editMode;

    export let moments;

    export let momentsView = false;

</script>


<!--<div class="gallery">
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
                {/if}
            </div>
        {/if}
    {/each}
</div>-->

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
                    {/if}
                </div>
            {/if}
        {/each}
    </div>
{:else}

    <div class="moments">
        {#each moments as moment, mom_index}
        <div class="moment">
            <h3>Moment {mom_index + 1}</h3>
            <div class="gallery" id="moment-photos">
            {#each moment.photos as filename, index}
                {#if !showSelectedOnly || buttonStates[index]}
                <div class="img-container">
                    <img class="image" src={getPhotoPath(filename)} alt={filename} />
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
        </div>
        {/each}
    </div>

{/if}


<style>

    .gallery {
        padding-bottom: 3px;
        display: grid;
        grid-template-columns: 315px 315px 315px;
        grid-gap: 8px;
        height: 87%;
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
        height: 87%;
        width: 984px;
        overflow-y: auto;
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

    .moment h3 {
        margin-bottom: 10px;
    }

    #moment-photos {
        padding-bottom: 3px;
        display: grid;
        grid-template-columns: 315px 315px 315px;
        grid-gap: 8px;
        width: 983px;
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

    .checkmark-icon {
        position: absolute;
        top: 0px;
        left: 0px;
        width: 10px;
        height: 10px;
    }
</style>