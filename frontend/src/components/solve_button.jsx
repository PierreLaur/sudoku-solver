function SolveButton() {
    function call_solver() {
        fetch("/solve", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: null, // data can be `string` or {object}!
        })
            .then((response) => response.json())
            .then((data) => console.log(data))
    }

    return <button onClick={call_solver}>Solve</button>
}

export default SolveButton
