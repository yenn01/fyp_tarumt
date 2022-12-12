<script>
    import {Jellyfish} from 'svelte-loading-spinners';
    import { fade } from 'svelte/transition';
    import {store_topic} from '../stores/topic';
    import Stopwatch from './Stopwatch.svelte';

    export let start;
    
</script>
<div class="tab_scrapping" transition:fade>
    <h3>{$store_topic}</h3>
    <div class="cont_loader">
        <Jellyfish size="18" color="rgb(255, 161, 120)" unit="rem" duration="3s"></Jellyfish>
    </div>
        <h1 id='txt_scrapping'>Analyzing...</h1>
    <div class="cont_scrapProgress">
        <Stopwatch bind:start={start}></Stopwatch>
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

</style>