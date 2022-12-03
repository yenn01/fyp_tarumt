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

    const handleSubmission = (eventMsg) => {
        console.log(eventMsg)
        
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
            <RouteTransition>
                <Route path="/">
                    <Input on:evt_submit={handleSubmission}></Input>
                </Route>
                <Route path="/scrapping"><Scrapping></Scrapping></Route>
            </RouteTransition>
        </div>
    </div>

</main>
<Footer></Footer>

<style>

    :root {
        --bg-color:  rgb(250,250,250)
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
        justify-content: center;
    }

    .cont_body {
        display: flex;
        align-items: center;
        flex-direction: column;
        margin-bottom:1em;
    }



</style>