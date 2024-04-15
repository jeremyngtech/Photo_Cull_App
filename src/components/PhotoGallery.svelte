<script>
    let photoFilenames = ['IMG_3752.jpg', 'IMG_6604.jpg', 'IMG_6606.jpg', 'IMG_6590.jpg', 'IMG_6657.jpg', 'IMG_6666.jpg', 
    'IMG_6801.jpg', 'IMG_6836.jpg', 'IMG_7065.jpg', 'IMG_7278.jpg', 'IMG_7304.jpg', 'IMG_7348.jpg', 'IMG_7358.jpg', 'IMG_7530.jpg' ]; // Array of photo filenames

    // Function to get the path of each photo
    function getPhotoPath(filename) {
        //return './jeremy_lib/IMG_6657.jpg';
        let path = './src/lib/jeremy_lib/' + filename;
        console.log(path);
        return path; // Assuming photos are in the 'photos' directory inside the 'static' directory
    }

    // Array to track click state of each button
    let buttonStates = new Array(photoFilenames.length).fill(false);

    // Function to toggle the click state of a specific button
    function handleClick(index) {
        buttonStates[index] = !buttonStates[index];
    }
</script>


<div class="gallery">
    {#each photoFilenames as filename, index}
        <div class="img-container">
            <img src={getPhotoPath(filename)} alt={filename} />
            <button class:clicked={buttonStates[index]} on:click={() => handleClick(index)} class="toggle-button"></button>
        </div>
    {/each}
</div>


<style>

    .gallery {
        padding-top: 3px;
        padding-bottom: 3px;
        display: grid;
        grid-template-columns: 380px 380px;
        grid-gap: 3px;
        height: 95%;
        overflow-y: auto;
        /*background-color: blue;*/
    }

    .gallery img {
        width: 375px;
        height: 375px; 
        overflow: hidden;
        object-fit: cover;
    }

    .img-container {
        position: relative;
    }

    .toggle-button {
        position: absolute; /* Position the toggle button relative to its containing image */
        top: 17px; /* Position at the top */
        right: 20px; /* Position at the right */
        background-color: rgba(255, 255, 255, 0.7); /* Semi-transparent background */
        border: 2px solid white;
        width: 31px; /* Set width */
        height: 31px; /* Set height */
        border-radius: 50%; /* Make it circular */
        padding: 0; /* Remove padding */
        cursor: pointer;
    }

    .toggle-button.clicked {
        background-color: rgba(42, 79, 245, 0.95); /* Change background to blue when clicked */
    }
</style>