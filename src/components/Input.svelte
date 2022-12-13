
<script>
    import {router} from 'tinro';
import {createEventDispatcher} from 'svelte';
import { fade } from 'svelte/transition';

//import {Button,Modal,ModalBody,ModalHeader,ModalFooter} from 'sveltestrap';
import Modal from './Modal.svelte';

import {store_topic} from '../stores/topic'



import Settings from './Settings.svelte';
    import { notifications } from '../stores/notifications';

const dispatch = createEventDispatcher();



let userInput = "";
let open = false;
const toggle = () => (open = !open)


 function send() {
    if(userInput.split(' ').length > 6) {
        notifications.danger("You can only input 6 words or less.",3000)
        return
    }
    $store_topic = userInput
    dispatch('evt_submit',userInput);  
    router.goto("/scrapping")
    console.log("wtf"+userInput)
 }

 //$: userInput, console.log(userInput)
 
 
</script>
<!-- <Modal isOpen={open} {toggle}>
    <ModalHeader {toggle}>Modal title</ModalHeader>
    <ModalBody><Settings></Settings></ModalBody>
    <ModalFooter>
        <Button color="secondary" on:click={toggle}>Back</Button>
    </ModalFooter>
</Modal> -->
{#if open}
	<Modal on:close="{() => open = false}">
        <h2 slot="header">
			Settings
		</h2>
		<Settings></Settings>
	</Modal>
{/if}

<div class="tab_input" transition:fade>
    <h1 class="cont_topic">What topics' sentiment would you like to know about?</h1>
    <form>
    <div class="cont_input">
        <input type="text" 
        id="in_topic" 
        placeholder="Type here..." bind:value={userInput}>
        {#if userInput.split(' ').length > 6}
        <small transition:fade>
            Please input less than 6 words
        </small>
        {/if}
    </div>
    <div class="cont_submit">
        <button class="btn_submit" on:click|preventDefault={send} >
            Submit
        </button>
    </div>
    </form>
    <div class="cont_settings">
        <button on:click={toggle} class="btn_settings">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-gear-fill" viewBox="0 0 16 16">
                <path d="M9.405 1.05c-.413-1.4-2.397-1.4-2.81 0l-.1.34a1.464 1.464 0 0 1-2.105.872l-.31-.17c-1.283-.698-2.686.705-1.987 1.987l.169.311c.446.82.023 1.841-.872 2.105l-.34.1c-1.4.413-1.4 2.397 0 2.81l.34.1a1.464 1.464 0 0 1 .872 2.105l-.17.31c-.698 1.283.705 2.686 1.987 1.987l.311-.169a1.464 1.464 0 0 1 2.105.872l.1.34c.413 1.4 2.397 1.4 2.81 0l.1-.34a1.464 1.464 0 0 1 2.105-.872l.31.17c1.283.698 2.686-.705 1.987-1.987l-.169-.311a1.464 1.464 0 0 1 .872-2.105l.34-.1c1.4-.413 1.4-2.397 0-2.81l-.34-.1a1.464 1.464 0 0 1-.872-2.105l.17-.31c.698-1.283-.705-2.686-1.987-1.987l-.311.169a1.464 1.464 0 0 1-2.105-.872l-.1-.34zM8 10.93a2.929 2.929 0 1 1 0-5.86 2.929 2.929 0 0 1 0 5.858z"/>
              </svg>
            Settings
        </button>    
    </div>
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

    .btn_submit {
        font-size: 1.2rem;
        border-radius: 10px;
        cursor: pointer;
        font-weight: 500;
        padding: 0.5rem 1rem;
    }

    .btn_submit:hover {
        background-color:var(--theme-default);
        transition: 0.3s ease-in-out;
    }

    .cont_settings{
        margin-top:2rem;
        display: flex;
    justify-content: center;
    }

    .btn_settings {
        font-size:1rem;
        border:none;
        background-color: var(--bg-color);
        color:lightgray;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .btn_settings:hover {
        cursor: pointer;
        color:gray;
    }

    .btn_settings > svg {
        padding-right: 7px;
    }

    small {
        font-size:1rem;
        color:var(--theme-negative)
    }

</style>