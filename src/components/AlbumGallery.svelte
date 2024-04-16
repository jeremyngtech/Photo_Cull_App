<script>

    export let albumThumbnails;
    // Function to get the path of each photo
    function getPhotoPath(filename) {
        //return './jeremy_lib/IMG_6657.jpg';
        let path = './src/lib/thumbnails/' + filename;
        console.log(path);
        return path; // Assuming photos are in the 'photos' directory inside the 'static' directory
    }


</script>


<div class="gallery">
    {#each Object.entries(albumThumbnails) as [name, filename]}
        <div class="img-container">
        <img src={getPhotoPath(filename)} alt={filename} /> <br>
        {name}
        <br>
        </div>
    {/each}
</div>


<style>

    .gallery {
        padding-top: 3px;
        padding-bottom: 3px;
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        grid-gap: 10px;
        height: 60%;
        width: 30%;
        overflow-y: auto;
        /*background-color: blue;*/
    }

    .gallery img {
        width: 125px;
        height: 125px; 
        overflow: hidden;
        object-fit: cover;
        border-radius: 2%;
    }

    

</style>