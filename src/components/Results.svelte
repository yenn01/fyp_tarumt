<script>
    import {store_results} from '../stores/results';
    import {store_tractions} from '../stores/tractions'
    import Tweet from '../components/Tweet.svelte'

    export let tweets
    $:show = false;

    const loadedTweets = () => {
        console.log("loaded")
        show = true
    }

    $: tweets && loadedTweets()

</script>

<div class="cont_results">
    <div class="cont_r_left">
        
            
        {#if show == true}
            {#each tweets as post}
                <Tweet tweet={post}></Tweet>
            {/each}
        {/if}
            

    </div>
    <div class="cont_r_right">
        <h1>BIGG</h1>
    </div>

</div>

<style>
    .cont_results {
        
        display:flex;
        flex-wrap: wrap;
        flex-direction: row;
        justify-content: space-around;
        margin:1rem 0;
        width:100%;
        

    }

    .cont_r_left {
        display:flex;
        flex-direction: column;
        flex-grow:2;
        flex-shrink: 0;
        flex-basis: 200px;
    }

    .cont_r_right {
        display:flex;
        flex-direction: column;
        flex-grow:3;
        background-color: var(--theme-color-darker-bg);
        border-radius: 10px;
        min-height: 40vh;
        flex-shrink: 0;
        flex-basis: 400px;
        padding:2rem;
    }

</style>
