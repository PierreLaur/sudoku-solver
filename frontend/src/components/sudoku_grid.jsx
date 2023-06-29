import { useState } from "react"
import "../App.css"

// eslint-disable-next-line react/prop-types
function Cell({ id }) {
    const [value, setValue] = useState("")

    const handleChange = (e) => {
        setValue(e.target.value)
    }
    console.log(id)

    return <input type="text" id={id} className="cell" value={value} onChange={handleChange} maxLength={1} />
}

export default function SudokuGrid() {
    const rows = Array(9).fill(null)
    const cols = Array(9).fill(null)

    return (
        <div className="grid">
            {rows.map((row, rowIdx) => (
                <div key={rowIdx} className="row">
                    {cols.map((col, colIdx) => (
                        <Cell key={colIdx} id={rowIdx * 9 + colIdx} />
                    ))}
                </div>
            ))}
        </div>
    )
}
