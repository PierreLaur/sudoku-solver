<script lang="ts">
    import { grid } from "./grid_store"

    function rand_digit(n) {
        let res = []
        for (let i = 0; i < n; i++) {
            res.push(Math.floor(Math.random() * 9))
        }
        return res
    }

    function generate_grid() {
        let myGrid = new Array(9).fill("").map(() => new Array(9).fill(""))

        const n = 16
        let i = 0

        let generated = new Set()
        while (i < n) {
            let [r, c, d] = rand_digit(3)
            // Generate unique r,c pairs
            while (generated.has(r * 9 + c)) {
                ;[r, c, d] = rand_digit(3)
            }
            generated.add(r * 9 + c)

            let valid = true

            // Check if no incompatible digits around
            for (let j = 0; j < 9; j++) {
                if (j == c) continue
                if (myGrid[r][j] == d) {
                    valid = false
                    break
                }
            }

            for (let j = 0; j < 9; j++) {
                if (j == r) continue
                if (myGrid[j][c] == d) {
                    valid = false
                    break
                }
            }

            let rBlockStart = r - (r % 3)
            let cBlockStart = c - (c % 3)

            for (let row = rBlockStart; row < rBlockStart + 3; row++) {
                for (let col = cBlockStart; col < cBlockStart + 3; col++) {
                    if (row == r && col == c) continue

                    if (myGrid[row][col] == d) {
                        valid = false
                        break
                    }
                }
            }

            if (valid) {
                myGrid[r][c] = d.toString()
                i += 1
            }
        }

        grid.set(myGrid)
    }
</script>

<main>
    <button on:click={generate_grid}> Generate </button>
</main>

<style>
    button {
        width: 150px;
        font-size: 20px;
        margin: 10px;
    }
</style>
