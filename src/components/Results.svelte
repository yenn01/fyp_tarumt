<script>
    import {store_results} from '../stores/results';
    import {store_elapsedTime} from '../stores/elapsedTime'
    import Tweet from '../components/Tweet.svelte'
    import { fade } from 'svelte/transition';
    import PercentBar from '../components/PercentBar.svelte'
    import {chart} from 'svelte-apexcharts'
    import {store_topic} from '../stores/topic';

    export let tweets
    $:show = false;

    const loadedTweets = () => {
        console.log("loaded")
        console.log($store_results)
        show = true
        transform()
    }

    let results = [];
    let colLabels = ['positive','neutral','negative']
    const transform = () => {
        results.push($store_results.positive)
        results.push($store_results.neutral)
        results.push($store_results.negative)
    }
    // let data = {
    //     labels: colLabels,
    //     datasets: [
    //         {
    //             values: results
    //         }
    //     ]

    // }

    let options = {
        chart: {
            type:"bar",
        },
        series: [
            {
                name:"sales",
                data:results,
            },
        ],
        plotOptions: {
            bar: {
                distributed: true,
                horizontal:true,
                barHeight: '50%',
            },
        },
        dataLabels:{
            style:{
                colors: "#000000"
            }
        },
        xaxis: {
            categories: colLabels
        },
        colors: [
            "#acff78","#78e0ff","#ff7f78"
        ]
    }
    let progressBar

    $: tweets && loadedTweets()
    $: results && console.log(results)
</script>

<div class="cont_results" transition:fade>
    <div class="cont_r_left">
        
        <h3>High Activity Tweets</h3>
        {#if show == true}
            {#each tweets as post}
                <Tweet tweet={post}></Tweet>
            {/each}
        {/if}
            

    </div>
    <div class="cont_r_right">

        <h4 class="runtime">Total Runtime  <b>{$store_elapsedTime}</b></h4>
        <h2>{$store_topic}</h2>
        {#if show == true}
            <PercentBar bind:this={progressBar}></PercentBar>
        {/if}
        <div class="cont_graph">
            <div use:chart={options}/>
            <!-- <Chart data={data} type="bar"></Chart> -->
        </div>
        
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
        padding:1rem;
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
        padding:1rem;
        background-color: rgb(240, 240, 240);
    }

    .runtime {
        text-align: right;
    }

    b {
        font-size: 1.3rem;
    }

    .cont_graph {
        padding: 5vh;
    }
</style>
