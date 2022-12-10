<script>

    export let tweet;

    $: tweet, console.log(tweet)

</script>
    <div class="cont_tweet">
        <div class="cont_top_tweet">
            {tweet.tweet}
        </div>
        <div class="cont_bot_tweet">

           <div> Likes: {tweet.nlikes}</div>
           <div> Replies: {tweet.nreplies}</div>
           <div> Retweets: {tweet.nretweets}</div>
           
        </div>
        <div class="cont_label">
            <div>{tweet.sentiment}</div>
        </div>
    </div>


<style>

    .cont_tweet {
        border-radius: 6px;
        margin:1rem;
        background-color: lightgray;
        justify-content: space-around;
    }

    .cont_bot_tweet {
        display:flex;
        flex-direction: row;
        padding:0.5rem;
    }

</style>