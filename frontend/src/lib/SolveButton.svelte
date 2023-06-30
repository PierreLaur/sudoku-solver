<script lang="ts">
    let apiOutput: string = ""
    function callBackend() {
        fetch("/hello")
            .then((res) => res.json())
            .then((data) => (apiOutput = data.message))
    }
</script>

<main>
    <button on:click={callBackend}> Call backend </button>
    <p>{apiOutput}</p>
</main>
