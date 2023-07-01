<script lang="ts">
    import SolveButton from "./lib/SolveButton.svelte"
    import Grid from "./lib/Grid.svelte"
    import ClearButton from "./lib/ClearButton.svelte"
    import GenerateButton from "./lib/GenerateButton.svelte"
</script>

<main>
    <div class="card">
        <div class="main-panel">
            <Grid />
            <br />
            <SolveButton />
        </div>
        <div class="control-panel">
            <ClearButton />
            <GenerateButton />
        </div>
    </div>
</main>

<style>
    .card {
        display: flex;
    }

    .control-panel {
        display: flex;
        flex-direction: column;
        justify-content: center;
        margin: 0;
        height: auto;
    }
</style>
