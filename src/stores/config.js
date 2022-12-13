import { writable } from 'svelte/store';

export const store_config = writable({
    model:"rb",
    limit:1000
});