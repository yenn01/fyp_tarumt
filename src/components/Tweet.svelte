<script>

    export let tweet;

    $: tweet, console.log(tweet)

</script>
    <div class="cont_tweet">
        <div class="cont_top_tweet">
            {tweet.tweet}
        </div>
        <div class="cont_bot_tweet">

           <div> Likes: <b>{tweet.nlikes}</b></div>
           <div> Replies: <b>{tweet.nreplies}</b></div>
           <div> Retweets: <b>{tweet.nretweets}</b></div>
           
        </div>
        <div class="cont_label">
            <div class="label" style="background-color: {
                tweet.sentiment === 'negative' ? "rgb(255, 127, 120)" 
                : tweet.sentiment === 'positive' ? "rgb(172, 255, 120)"
                : tweet.sentiment === 'neutral' ? "rgb(120, 224, 255)" 
                :"rgb(255, 161, 120)"}
            ">{tweet.sentiment.toUpperCase()}</div>
        </div>
    </div>


<style>

    .cont_top_tweet {
        font-weight:800;
    }

    .cont_tweet {
        border-radius: 6px;
        margin:1rem;
        background-color: rgb(240, 240, 240);
       padding:1rem;
    }

    .cont_bot_tweet {
        display:flex;
        flex-direction: row;
        justify-content: space-around;
        padding:0.5rem;
    }

    .label {
        border-radius: 5px;
        padding: 0.2rem 0.6rem;
        width: 5rem;
        font-weight:1000;
    }

    .cont_label {
        display:flex;
        justify-content: center;
    }

</style>