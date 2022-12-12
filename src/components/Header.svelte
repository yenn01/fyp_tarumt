<script>
import {router} from 'tinro'
$: src = './logo_b.png'

</script>

<div class="header-container">
    <img class="logo" src="./logo_b.png">
    {#if !($router.path === "/scrapping" || $router.path === "/")}
        <a href="/"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-up-left-circle-fill" viewBox="0 0 16 16">
            <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-5.904 2.803a.5.5 0 1 0 .707-.707L6.707 6h2.768a.5.5 0 1 0 0-1H5.5a.5.5 0 0 0-.5.5v3.975a.5.5 0 0 0 1 0V6.707l4.096 4.096z"/>
          </svg> Back home</a>
    {/if}
    
    
</div>

<style>

    .header-container {
        display:flex;
        justify-content: space-between;
        margin-top:3vh;
        padding:0 2rem;
        align-items: center;
        font-size: 1.2rem;
    }

    .logo {
        width:10vw;
    }

    a{
        color:black;
        text-decoration: none;
    }

    a:hover {
        color:var(--theme-default);
        text-decoration:none;
    }

</style>