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

<div id="library-album">
    <p id="library-title">Library<br></p>
    <div class="img-containter">
        <img class="gallery-img" src='./src/lib/thumbnails/IMG_3752.jpg' alt='library image' /> <br>
    </div>

    <p id="album-title">Albums<br></p>
    <div class="gallery">
        {#each Object.entries(albumThumbnails) as [name, filename]}
            <div class="img-container">
                <img class="gallery-img" src={getPhotoPath(filename)} alt={filename} /> <br>
                {name}
                <br>
            </div>
        {/each}
    </div>
</div>

<style>
    #library-title{
        margin-top: 0px;
        margin-bottom: 8px;
        font-size: 15px;
    }

    #album-title{
        font-size: 15px;
        margin-bottom: 8px;
    }

    #library-album{
        height: 55vh;
        overflow-y: auto;
        margin-top: 5px;
        margin-bottom: 30px;
        /*border-bottom: white solid 3px;*/
    }

    .gallery {
        padding-top: 3px;
        padding-bottom: 3px;
        margin-bottom: 20px;
        display: grid;
        grid-template-columns: 95px 95px 95px;
        grid-gap: 20px;
        /*height: 60%;*/
        
        /*background-color: aqua;*/
        /*background-color: blue;*/
    }

    .img-container{
        font-size: 12px;
    }
    .gallery-img {
        width: 95px;
        height: 95px; 
        overflow: hidden;
        object-fit: cover;
        border-radius: 3%;
    }

    

</style>