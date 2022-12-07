
<script>
import {createEventDispatcher} from 'svelte';
import {store_topic} from '../stores/topic'
import { fade } from 'svelte/transition';
import {router} from 'tinro';
let userInput = "";

const dispatch = createEventDispatcher();


 function send() {
    $store_topic = userInput
    dispatch('evt_submit',userInput);  
    router.goto("/scrapping")
    console.log("wtf"+userInput)
 }

 $: userInput, console.log(userInput)
 

</script>


<div class="tab_input" transition:fade>
    <h1 class="cont_topic">What topics' sentiment would you like to know about?</h1>
    <form>
    <div class="cont_input">
        <input type="text" 
        id="in_topic" 
        placeholder="Type here..." bind:value={userInput}>
        <small></small>
        
    </div>
    <div class="cont_submit">
        <button class="btn_submit" on:click|preventDefault={send} >
            Submit
        </button>
    </div>
    </form>
</div>

<style>
    
    .cont_topic {
        display: flex;
        align-items: center;
        min-height: 15vh;
        font-family: monospace;
    }

    .cont_input {
        font-size: 1.5rem;
        width:100%;
    }

    input {
        outline: none;
        border:none;
        width: 100%;
        text-align: center;
        background-color: var(--bg-color);
        border-bottom: 1px solid darkgrey;
        transition: 0.2s ease-in-out;
    }

    input:hover {
        border-bottom: 2px solid black;
        transition: 0.2s ease-in-out;
    }

    input:focus {
        border-bottom: 2px solid black;
        transition: 0.2s ease-in-out;
    }

    button {
        font-size: 1.2rem;
        border-radius: 10px;
        cursor: pointer;
        font-weight: 500;
        padding: 0.5rem 1rem;
    }

    button:hover {
        background-color:var(--theme-default);
        transition: 0.3s ease-in-out;
    }

</style>