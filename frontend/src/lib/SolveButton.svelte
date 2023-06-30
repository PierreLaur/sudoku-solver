<script lang="ts">
    import { grid } from "./stores"
    let apiOutput: string = ""

    function process_result(data) {
        if (data.status == 1) {
            apiOutput = "solve failed"
        } else {
            grid.set(data.grid)
            apiOutput = ""
        }
    }

    function callBackend() {
        // fetch("/hello")
        //     .then((res) => res.json())
        //     .then((data) => (apiOutput = data.message))

        fetch("/solve", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ grid: $grid }),
        })
            .then((res) => res.json())
            .then((data) => process_result(data))
    }
</script>

<main>
    <button on:click={callBackend}> Solve </button>
    <p>{apiOutput}</p>
</main>
