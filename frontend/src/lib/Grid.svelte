<script>
    import { grid } from "./stores"
    let myGrid = new Array(9).fill(null).map(() => new Array(9).fill(null))
    grid.set(myGrid)
    grid.subscribe((value) => (myGrid = value))

    function setValue(rowIdx, colIdx, value) {
        myGrid[rowIdx][colIdx] = value
        grid.set(myGrid)
    }
</script>

<main>
    <p>Fill the grid</p>
</main>

<div class="grid">
    {#each myGrid as row, rowIdx}
        {#each row as value, colIdx}
            <div class="cell">
                <input bind:value on:change={() => setValue(rowIdx, colIdx, value)} />
            </div>
        {/each}
        <br />
    {/each}
</div>

<style>
    .grid {
        /* width: 193px; */
        /* height: 240px; */
        border: 1px solid white;
        display: flexbox;
    }
    input {
        box-sizing: border-box;
        width: 100%;
        height: 100%;
        text-align: center;
        margin: 0;
        background-color: transparent;
        border: none;
    }

    input:hover {
        cursor: pointer;
    }
    .cell {
        width: 20px;
        height: 20px;
        /* margin: 1px; */
        display: inline-block;
        border-radius: 0;
        background-color: grey;
        border: 1px solid white;
        /* flex: 1; */
        /* display: flex; */
    }
</style>
