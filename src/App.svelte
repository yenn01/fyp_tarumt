<script>
    import anime from 'animejs/lib/anime.es.js';
    import { fade, fly } from 'svelte/transition';


    import {Route} from 'tinro'; 
    import {router} from 'tinro';

    import Toast from "./components/Toast.svelte";
    import {notifications} from './stores/notifications.js'
    import Footer from './components/Footer.svelte';
    import Header from './components/Header.svelte';
    import Input from './components/Input.svelte'
    import RouteTransition from './components/RouteTransition.svelte';
    import Scrapping from './components/Scrapping.svelte';
    import Results from './components/Results.svelte'
    
    import {store_topic} from './stores/topic'
    import {store_results} from './stores/results'  
    import { store_config } from './stores/config';
    import { store_numTweets} from './stores/numTweets'
    import { store_processing } from './stores/processing';


    let socket = io({
        timeout:300000
    });
    let start;

    socket.on('connect', function() {
        console.log("Connected to WebSocket.")
    });

    socket.on('disconnect', function() {
        console.log("Disconnected from WebSocket.")
    });

    socket.on('completed_scrape',() => {
        notifications.success('Scrape completed',4000)
        console.log("Scrape completed")
    })

    let instance;
    let tweets;
    
    socket.on('high_traction',(response) => {
        console.log(response)
        tweets = JSON.parse(response)
    })


    

    const handleSubmission = (eventMsg) => {
        //console.log(eventMsg.detail)
        $store_processing = "scrapping"
        start = new Date()
        console.log(start)
        //getResults(eventMsg.detail)
        beginAnalysis()
        
    }

    async function beginAnalysis(_topic) {
        let temp = $store_topic
        // let url = "/scrape?text="+encodeURI(temp)
        let url = "/scrape?text="+encodeURI(temp)+"&limit="+$store_config.limit
            try {
                //const scrapeProcess = await scrape(_topic)
                const scrapeProcess = await (await fetch(url)).json()
                //if(parsed.id != null) {
                    //console.log("Succeeded Scrape")
                    //console.log(scrapeProcess)
                const analyseResults = await analysis(scrapeProcess)
                //} 
                return analyseResults
            } catch (error) {
                console.log(error)
            }
    } 

    async function analysis(_process) {
        $store_processing = "analysing"
        console.log(_process)
        let url = "/analyse?id="+encodeURI(_process.id)+"&model="+$store_config.model
        $store_numTweets = _process.numRow
        const res = await fetch(url).then(res => res.json()).then(
        parsed => {
            console.log("Succeeded analysis")
            console.log(parsed)
            $store_results = parsed
            router.goto("/results")
            return parsed
        })
    }

    // async function scrape(topic) {
    //     if (!$store_topic) {
    //          notifications.danger('No topics given.',4000)
    //          return;        
    //     }
       
        
    //     const res = .then(res => res.json()).then(
    //     parsed => {
    //         console.log("internal parsed")
    //         console.log(parsed)
    //         return res
    //     })
    // }

    // async function getResults(passed) {
    //     let temp = $store_topic
    //     if (!$store_topic) {
    //          notifications.danger('No topics given.',4000)
    //          return;        
    //     }

    //     let url = "/scrape?text="+encodeURI(temp)

       

        
    //     const res = await fetch(url).then(res => res.json()).then(
    //         parsed => {
    //             console.log(parsed)
    //             //$store_results = parsed
    //             if (parsed.success) {
    //                 console.log("Scrape succeeded")
    //                 url = "/analyse?id="+encodeURI(parsed.id)
    //                 const analyseRes =  await fetch(url).then(res => res.json()).then({

    //                 })
    //             }

    //            // router.goto("/results")
                
    //             //response = arrMerge(parsed.labels,parsed.scores)
    //             //console.log(JSON.stringify(response))
    //         }
    //     ).catch((e)=> {
    //         console.error(e)
    //     })
    // }

</script>

<svelte:head>
    <title>trend</title>
    <link rel="icon" href="/favicon.ico" type="image/x-icon">
    <!-- <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"> -->
</svelte:head>

<Header></Header>
<main>
    <Toast/>
    
    <div class="cont_main">
        <div class="cont_body">
                <div><Route path="/">
                    <Input on:evt_submit={handleSubmission}></Input>
                </Route></div>
                <div><Route path="/scrapping"><Scrapping bind:start={start}></Scrapping></Route>
                </div>
                <div >
                    <Route path="/results"><Results {tweets}></Results></Route>
                </div>
        </div>
    </div>
    
</main>
<Footer></Footer>

<style>

    :root {
        --bg-color:  rgb(250,250,250);
        --theme-default: rgb(255, 161, 120);
        --theme-negative: rgb(255, 127, 120);
        --theme-positive: rgb(172, 255, 120);
        --theme-neutral:rgb(120, 224, 255);

    }

    :global(body) {
        background: var(--bg-color);
    }
    
	main {
		text-align: center;
		padding: 0.2rem 2rem;
        min-height: 60vh;
        font-family: monospace;
	}
/* 
	@media (min-width: 500px) {
		main {
			max-width: none;
            padding: 0.2rem 0rem;
		}
	} */

    .cont_main {
        display:flex;
        flex-direction: column;
        align-items: center;
        min-height:50vh;
        justify-content: flex-start;
    }

    .cont_body {
        display:grid;
        grid-template-columns: 1fr;
grid-template-rows: 1fr;
justify-items: center;
width:100%;
    }

    .cont_body > * {
        grid-column: 1/2;
        grid-row: 1/2;
    }



</style>