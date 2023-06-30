import { useState, useEffect } from "react"
import "./App.css"
import Header from "./components/header"
import SolveButton from "./components/solve_button"
import SudokuGrid from "./components/sudoku_grid"

function ReadHello() {
    const [data, setData] = useState(null)

    useEffect(() => {
        fetch("/hello")
            .then((response) => response.json())
            .then((data) => setData(data.message))
    }, [])

    return (
        <div className="App">
            <header className="App-header">{data && <p>{data}</p>}</header>
        </div>
    )
}

function App() {
    return (
        <>
            <Header />
            <ReadHello />
            <SolveButton />
            <SudokuGrid />
        </>
    )
}

export default App
