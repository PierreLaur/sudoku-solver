<script>
    import { grid } from "./grid_store"
    import { fade } from "svelte/transition"
    let myGrid = new Array(9).fill("").map(() => new Array(9).fill(""))
    grid.set(myGrid)
    grid.subscribe((value) => (myGrid = value))

    $: myGrid = myGrid.map((row) => row.map(setValue))

    function setValue(cell) {
        const result = cell.replace(/[^1-9]/g, "")
        grid.set(myGrid)
        return result
    }

    function clearValue(rowIdx, colIdx) {
        myGrid[rowIdx][colIdx] = ""
        grid.set(myGrid)
    }
</script>

<main>
    <h2>Fill the grid</h2>
</main>

<div class="grid">
    {#each myGrid as row, rowIdx}
        <div class="row">
            {#each row as value, colIdx (value + (rowIdx * 9).toString() + colIdx.toString())}
                <div class="cell">
                    <input bind:value on:click={() => clearValue(rowIdx, colIdx)} />
                </div>
            {/each}
            <br />
        </div>
    {/each}
</div>

<style>
    .grid {
        display: grid;
        border: 1px solid black;
    }

    @keyframes slideFadeIn {
        0% {
            transform: scale(0.1);
        }
        30% {
            transform: scale(1.2);
        }
        60% {
            transform: scale(0.8);
        }
        100% {
            transform: scale(1);
        }
    }

    input {
        box-sizing: border-box;
        width: 100%;
        height: 100%;
        text-align: center;
        margin: 0;
        background-color: transparent;
        color: black;
        font-size: 30px;
        border: none;
        transition: background-color 0.4s;
        animation: slideFadeIn 0.5s;
    }

    input:hover {
        cursor: pointer;
    }
    .cell {
        width: 50px;
        height: 50px;
        display: inline-block;
        border-radius: 0;
        background-color: darkgrey;
        border: 1px solid whitesmoke;
    }

    input:focus {
        outline: none;
        background-color: lightsalmon;
        caret-color: transparent;
    }

    input:hover {
        background-color: lightcyan;
    }

    .cell:first-child {
        border-left: 3px solid black;
    }

    .row:first-child {
        border-top: 3px solid black;
    }

    .cell:nth-child(3n) {
        border-right: 3px solid black;
    }

    .row:nth-child(3n) {
        border-bottom: 3px solid black;
    }
</style>
