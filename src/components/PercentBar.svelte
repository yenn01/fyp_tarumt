<script>
import { fade, fly } from 'svelte/transition';
import {store_results} from '../stores/results';
import anime from 'animejs/lib/anime.es.js';

let textColor = '#000000'
let text = ''

export const change = () => {
    console.log("Percent bar called.")
    let pos = isNaN($store_results.positive) ? 0 : $store_results.positive
    let neu = isNaN($store_results.neutral) ? 0 : $store_results.neutral
    let neg = isNaN($store_results.negative) ? 0 : $store_results.negative
    let total = pos + neu + neg
    let posPercent = Math.round(pos/total * 100 * 100) / 100
    let neuPercent = Math.round(neu/total * 100 * 100) / 100
    let negPercent = Math.round(neg/total * 100 * 100) / 100

    anime({
            targets: '#progress',
            width: `${posPercent}%`,
            easing: 'easeOutExpo',
            duration:4000
        })
    anime({
        targets: '#progressMid',
        width: `${neuPercent+posPercent}%`,
        easing: 'easeOutExpo',
        duration:4000
    })
    anime({
        targets: '#neuPercent',
        innerHTML: [0,neuPercent],
        easing: 'easeOutExpo',
        round:100,
        duration:3000,
        
    })
    anime({
        targets: '#posPercent',
        innerHTML: [0,posPercent],
        easing: 'easeOutExpo',
        round:100,
        duration:3000,
        
    })
    anime({
        targets: '#negPercent',
        innerHTML: [0,negPercent],
        easing: 'easeOutExpo',
        round:100,
        duration:3000,
        
    })

    if(neuPercent>posPercent && neuPercent > negPercent) {
        text = "Neutral"
        textColor = "rgb(120, 224, 255)"
    } else if (posPercent>negPercent && posPercent > neuPercent) {
        text = "Mostly Positive"
        textColor = "rgb(172, 255, 120)"
    } else if (negPercent>posPercent && negPercent > neuPercent) {
        text = "Mostly Negative"
        textColor = "rgb(255, 127, 120)"
    }
}


</script>
<div class="conclusion">
    <div class="progress-text" style="color:{textColor}"><strong transition:fade>{text}</strong></div>
</div>
<div class="progress-holder" transition:fly="{{ y: 50, duration: 500 }}" on:introend={change}>
    <div class="progress-bar progress-mid" id="progressMid"></div>
    <div class="progress-bar progress-background"></div>
    <div class="progress-bar progress-front" id="progress"></div>
    <div class="progress-positive"><strong id="posPercent">0</strong> %</div>
    <div class="progress-neutral" ><strong id="neuPercent">0</strong> %</div>
    <div class="progress-negative"><strong id="negPercent">0</strong> %</div>
</div>



<style>
 .progress-holder {
        display:grid;
        grid-template-columns: repeat(3, 2fr);
        grid-template-rows: repeat(2, 3fr);
        width:80%;
        height:50px;
        margin: 0 auto;
        font-size: 1.2rem;
    }

    .progress-bar {
        
        grid-column: 1/4;
        grid-row: 1/2;
    }

    .progress-positive {
        grid-column: 1/2;
        grid-row: 2/3;
        color :var(--theme-positive);
        text-align: left;
    }

    .progress-negative {
        grid-column: 3/4;
        grid-row: 2/3;
        color :var(--theme-negative);
        text-align:right;
    }

    .progress-neutral {
        grid-column: 2/3;
        grid-row: 2/3;    
        color:var(--theme-neutral);    
    }

    .progress-front {
        background-color: var(--theme-positive);
        border-radius: 20px;
        height:12px;
        width:1%;
        z-index:5;
    }

    .progress-mid {
        background-color: var(--theme-neutral);
        border-radius: 20px;
        height:12px;
        width:1%;
        z-index:2;
    }

    .progress-background {
        background-color: var(--theme-negative);
        border-radius: 20px;
        height:12px;
    }

    .conclusion {
        display:flex;
        justify-content: center;
        font-size:1.45rem;
        
    }
</style>