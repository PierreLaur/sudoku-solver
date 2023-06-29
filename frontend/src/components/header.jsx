import sudoku_img from "../assets/1.png"

export default function Header() {
    return (
        <nav>
            <ul className="myNavbar">
                <img src={sudoku_img}></img>
                <li>1</li>
                <li>2</li>
                <li className="specialLi">3</li>
            </ul>
        </nav>
    )
}
