<script>
    import {router} from 'tinro';
    import {fade} from 'svelte/transition';
</script>

{#key $router.path}
    <div transition:fade>
        <slot></slot>
    </div>
{/key}