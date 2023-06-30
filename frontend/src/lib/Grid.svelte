<script>
    let grid = new Array(9).fill("").map(() => new Array(9).fill(""))

    function setValue(rowIdx, colIdx, value) {
        grid[rowIdx][colIdx] = value
    }
</script>

<main>
    <p>Fill the grid</p>
</main>

<div class="grid">
    {#each grid as row, rowIdx}
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
        /* width: 200px; */
        /* height: 240px; */
        border: 1px solid white;
        /* display: flexbox; */
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
