<script lang="ts">
    import { grid } from "./grid_store"

    function clear_grid() {
        let myGrid = new Array(9).fill("").map(() => new Array(9).fill(""))
        grid.set(myGrid)
    }
</script>

<main>
    <button on:click={clear_grid}> Clear </button>
</main>

<style>
    button {
        width: 150px;
        font-size: 20px;
    }
</style>
