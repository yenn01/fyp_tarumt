<script>

    import {store_elapsedTime} from "../stores/elapsedTime"    
    import {store_results} from "../stores/results"

let elapsedSeconds = 0
let elapsedMinutes = 0


export let start;

const stopwatch = () => {
    console.log("time counting.")
    if(start!=null) {
        let endTime = new Date();
        let timeDiff = endTime.getTime() - start.getTime();
        timeDiff = timeDiff / 1000 //Convert from millisecond to seconds.
        elapsedSeconds = Math.floor(timeDiff % 60);
        let minTimeDiff = Math.floor(timeDiff / 60) //Convert from seconds to minutes.
        elapsedMinutes = minTimeDiff % 60;
        $store_elapsedTime = String(elapsedMinutes).padStart(2, '0').concat(":",String(elapsedSeconds).padStart(2, '0'))
    }
}

let elapsedTimeIntervalRef = null;

export const stopElapse = () => {
    console.log("try stop")
    clearInterval(elapsedTimeIntervalRef);
    elapsedTimeIntervalRef = null;
    
}

const checkTimer = () => {
    console.log("Stopwatch Reset Try")
    if(elapsedTimeIntervalRef === null) {
        console.log("Stopwatch Reset Called")
        $store_elapsedTime = "";
        elapsedTimeIntervalRef = setInterval(stopwatch,1000)
    }
}

$: $store_results && stopElapse()
$: start && checkTimer()
 


</script>

<div class="cont_stopwatch">
    <h3>Elapsed Time</h3>
    <h2>{$store_elapsedTime}</h2>

</div>


<style>

h2 {
    margin: 0.2rem;
}

h3 {
    margin: 0.2rem;
}

</style>