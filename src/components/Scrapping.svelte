<script>
    import {Jellyfish} from 'svelte-loading-spinners';
    import { fade } from 'svelte/transition';
    import {store_topic} from '../stores/topic';
    
    export let topic = "";
    
</script>
<div class="tab_scrapping" transition:fade>
    <h3>{$store_topic}</h3>
    <Jellyfish size="18" color="rgb(255, 161, 120)" unit="rem" duration="3s"></Jellyfish>
    <h1 id='txt_scrapping'>Scrapping...</h1>
    <div class="cont_scrapProgress">

    </div>
</div>
<style>

.wrapper {
    width:none;
}



.tab-scrapping {
    
}

</style>