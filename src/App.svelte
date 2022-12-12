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
    import { store_elapsedTime } from './stores/elapsedTime';

    let socket = io();
    let start;

    socket.on('connect', function() {
        console.log("Connected to WebSocket.")
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
        start = new Date()
        console.log(start)
        getResults(eventMsg.detail)
        
        
    }

    async function getResults(passed) {
        let temp = $store_topic
        if (!$store_topic) {
             notifications.danger('No topics given.',4000)
             return;        
        }

        let url = "/scrape?text="+encodeURI(temp)
        const res = await fetch(url).then(res => res.json()).then(
            parsed => {
                console.log(parsed)
                $store_results = parsed


                router.goto("/results")
                
                //response = arrMerge(parsed.labels,parsed.scores)
                //console.log(JSON.stringify(response))
            }
        ).catch((e)=> {
            console.error(e)
        })
    }

</script>

<svelte:head>
    <title>trend</title>
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