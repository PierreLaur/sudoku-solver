<script>
    import { grid } from "./stores"
    let myGrid = new Array(9).fill(null).map(() => new Array(9).fill(null))
    grid.set(myGrid)
    grid.subscribe((value) => (myGrid = value))

    function setValue(rowIdx, colIdx, value) {
        let input = parseInt(value)
        if (!isNaN(input) && input >= 1 && input <= 9) {
            myGrid[rowIdx][colIdx] = value
        } else {
            myGrid[rowIdx][colIdx] = null
        }
        grid.set(myGrid)
    }

    function clearValue(rowIdx, colIdx) {
        myGrid[rowIdx][colIdx] = null
        grid.set(myGrid)
    }
</script>

<main>
    <h2>Fill the grid</h2>
</main>

<div class="grid">
    {#each myGrid as row, rowIdx}
        <div class="row">
            {#each row as value, colIdx}
                <div class="cell">
                    <input
                        bind:value
                        on:change={() => setValue(rowIdx, colIdx, value)}
                        on:click={() => clearValue(rowIdx, colIdx)}
                    />
                </div>
            {/each}
            <br />
        </div>
    {/each}
</div>

<style>
    .grid {
        display: flexbox;
        border: 2px solid black;
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
        caret-color: lightsalmon;
    }

    .cell:nth-child(3n) {
        border-right: 3px solid black;
    }

    .row:nth-child(3n) {
        border-bottom: 3px solid black;
    }
</style>
