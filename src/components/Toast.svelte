<script>
    import { flip } from "svelte/animate";
    import { fly,fade } from "svelte/transition";
    import { notifications } from "../stores/notifications.js";
    import anime from 'animejs/lib/anime.es.js';

    let themes = {
        danger: "#E26D69",
        success: "#81e292",
        default: "#bfc2c7",
    };
  

</script>
<!-- Call notification sample code
        import {notifications} from './stores/notifications.js'
    <button on:click={() => notifications.success('Hi there :DD', 4000)}>info!</button> 
    Takes two params, msg, timeout. Supports :
    notifications.danger
    notifications.default
--> 
<div class="toasty-container">
    {#each $notifications as notification (notification.id)}
        <!-- {@const test = loading(notification.id,notification.timeout)} -->
        <div
            animate:flip
            class="toasty"
            style="background: #212529; border: 2px solid {themes[notification.type]}; border-radius: 6px;"
            transition:fly={{ y: 30 }}
            >
                <div class="inner-toast">
                {#if notification.type === "danger"}
                <div class="icon"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="{themes[notification.type]}" class="bi bi-exclamation-circle-fill" viewBox="0 0 16 16">
                    <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8 4a.905.905 0 0 0-.9.995l.35 3.507a.552.552 0 0 0 1.1 0l.35-3.507A.905.905 0 0 0 8 4zm.002 6a1 1 0 1 0 0 2 1 1 0 0 0 0-2z"/>
                </svg></div>
                {:else if notification.type === "success"}
                <div class="icon">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="{themes[notification.type]}" class="bi bi-check-circle-fill" viewBox="0 0 16 16">
                        <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z"/>
                    </svg>
                </div>
                {:else}
                    <div class="icon">
                        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="{themes[notification.type]}" class="bi bi-info-circle-fill" viewBox="0 0 16 16">
                            <path d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16zm.93-9.412-1 4.705c-.07.34.029.533.304.533.194 0 .487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703 0-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381 2.29-.287zM8 5.5a1 1 0 1 1 0-2 1 1 0 0 1 0 2z"/>
                        </svg>
                    </div>
                {/if}

                <div class="content" style="color:{themes[notification.type]};">{notification.message}</div>
              
            </div>
        </div>
    {/each}
    
</div>

<style>
    .toasty-container {
        position:fixed;
        top: 16vh;
        right: 3vw;
        margin: 0 auto;
        padding: 0;
        z-index: 999;
       display:flex;
       align-items: flex-end;
        pointer-events: none;
        flex-direction: column;
        justify-content: flex-start;
    }

    .inner-toast {
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: flex-start;
        align-self: center;
    }

    .square {
        height:1vh;
        width:1%;
        z-index: 99;
    }

    .icon svg {
        z-index: 99;
    }

    .toasty {
        flex: 0 0 auto;
        display:flex;
        flex-direction: column;
        margin-bottom: 10px;
        width:15rem;
        align-items: flex-start;
        justify-content: space-evenly;
    }

    .content {
        padding: 10px;
        display: block;
        color: white;
        font-weight: 500;
        text-align: right;
    }

    

</style>