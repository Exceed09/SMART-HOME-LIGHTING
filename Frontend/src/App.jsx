import Button from "./components/Button"
import Card from "./components/Card"
import "./App.css"
import "./styles/Card.css"

function App() {

  return (
    <>
      <h1 class="webHead"> SMART-HOME LIGHT CONTROL</h1>
      <div className="card-list">
        <Card></Card>
        <Card></Card>
        <Card></Card>
      </div>
    </>
  )
}

export default App
