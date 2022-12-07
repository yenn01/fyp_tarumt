<script>
    import anime from 'animejs/lib/anime.es.js';
    import Toast from "./components/Toast.svelte";
    import {notifications} from './stores/notifications.js'
    import { fade, fly } from 'svelte/transition';
    import Footer from './components/Footer.svelte';
    import Header from './components/Header.svelte';
    import {Route} from 'tinro'; 
    import Input from './components/Input.svelte'
    import RouteTransition from './components/RouteTransition.svelte';
    import Scrapping from './components/Scrapping.svelte';
    import {store_topic} from './stores/topic'

    var socket = io();
    socket.on('connect', function() {
        console.log("Connected to WebSocket.")
    });

    const handleSubmission = (eventMsg) => {
        console.log(eventMsg.detail)
        getResults(eventMsg.detail)
       
        
    }

    async function getResults(passed) {
        let temp = $store_topic
        if (!$store_topic) {
             notifications.danger('No topics given.',4000)
             return;        
        }
        console.log(temp)
        console.log(encodeURI(temp))
        let url = "/scrape?text="+encodeURI(temp)
        const res = await fetch(url).then(res => res.json()).then(
            parsed => {
                console.log(parsed)
                //response = arrMerge(parsed.labels,parsed.scores)
                //console.log(JSON.stringify(response))
            }
        ).catch((e)=> {
            console.error(e)
        })
    }

    function arrMerge(k, v) {

        var obj = {};

        for (var i = 0; i < k.length; i++) {
            obj[k[i]] = v[i];
        }

        return obj;
    }


</script>

<svelte:head>
    <title>sens</title>
</svelte:head>

<Header></Header>
<main>
    <Toast/>
    
    <div class="cont_main">
        <div class="cont_body">
                <div><Route path="/">
                    <Input on:evt_submit={handleSubmission}></Input>
                </Route></div>
                <div><Route path="/scrapping"><Scrapping></Scrapping></Route>
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
		padding: 0.2em;
		max-width: 500px;
		margin: 0 auto;
        min-width: 500px;
        min-height: 60vh;
        font-family: monospace;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}

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
    }

    .cont_body > * {
        grid-column: 1/2;
        grid-row: 1/2;
    }



</style>