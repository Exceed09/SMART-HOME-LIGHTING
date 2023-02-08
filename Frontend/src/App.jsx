import Button from "./components/Button"
import Card from "./components/Card"
import "./App.css"
import "./styles/Card.css"

function App() {

  return (
    <>
      <h1 className="webHead"> SMART-HOME LIGHT CONTROL</h1>
      <div className="card-list">
        <Card id={1}></Card>
        <Card id={2}></Card>
        <Card id={3}></Card>
      </div>
    </>
  )
}

export default App
