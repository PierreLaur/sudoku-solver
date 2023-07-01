<script lang="ts">
    import { grid } from "./grid_store"

    function process_result(data) {
        if (data.status == 1) {
        } else {
            grid.set(data.grid)
        }
    }

    function callBackend() {
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
</main>

<style>
    button {
        width: 200px;
        font-size: 30px;
    }
</style>
