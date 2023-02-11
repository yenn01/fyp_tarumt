<script>
    import {Jellyfish, Circle3} from 'svelte-loading-spinners';
    import { fade,fly } from 'svelte/transition';
    import {store_topic} from '../stores/topic';
    import Stopwatch from './Stopwatch.svelte';
    import { store_processing } from '../stores/processing';
    import { store_numTweets } from '../stores/numTweets';
    export let start;
    
</script>
<div class="tab_scrapping" transition:fade>
    <h3>{$store_topic}</h3>
    <div class="cont_loader" transition:fade>
        {#if $store_processing === "scrapping"}
        <Jellyfish size="18" color="rgb(255, 161, 120)" unit="rem" duration="3s"></Jellyfish>
        {:else if $store_processing === "analysing"}
        <Circle3 size="180" ballTopLeft="rgb(120, 224, 255)" ballTopRight="rgb(255, 127, 120)" ballBottomLeft="rgb(172, 255, 120)" ballBottomRight="rgb(255, 161, 120)" unit="px" duration="1.35s"></Circle3>
        {/if}
    </div>
        {#if $store_processing === "scrapping"}
            <h1 id='txt_scrapping' transition:fly>Scrapping...</h1>
        {:else if $store_processing === "analysing"}
            
            <h1 id='txt_scrapping' transition:fly>Analysing...</h1>
            {#if $store_numTweets != 0}
                <h4 transition:fly>Number of usable tweets</h4>
                <h2 transition:fly>{$store_numTweets}</h2>
            {/if}
        {/if}
    <div class="cont_scrapProgress">
        <Stopwatch bind:start={start}></Stopwatch>
        <small>Please do not refresh or leave this page</small>
    </div>
</div>
<style>

.cont_scrapProgress {
    margin-top:2rem;
}

.cont_loader {
    display:flex;
   justify-content: center;
}


.tab_scrapping {
   min-height: 500px;
}

h4 {
    margin-top:0px;
}

small {
    font-size: 0.9rem;
}

</style>