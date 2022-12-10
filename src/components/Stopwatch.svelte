<script>

let elapsedSeconds = 0
let elapsedMinutes = 0

export let start= new Date();

const elapsedTimeIntervalRef = setInterval(() => {
    console.log("time counting.")
    if(start!=null) {
        let endTime = new Date();
        let timeDiff = endTime.getTime() - start.getTime();
        timeDiff = timeDiff / 1000 //Convert from millisecond to seconds.
        elapsedSeconds = Math.floor(timeDiff % 60);
        let minTimeDiff = Math.floor(timeDiff / 60) //Convert from seconds to minutes.
        elapsedMinutes = minTimeDiff % 60;
    }
}, 1000);



</script>

<div class="cont_stopwatch">
    <h3>Elapsed Time</h3>
    <h2>{String(elapsedMinutes).padStart(2, '0')}:{String(elapsedSeconds).padStart(2, '0')}</h2>

</div>


<style>

h2 {
    margin: 0.2rem;
}

h3 {
    margin: 0.2rem;
}

</style>