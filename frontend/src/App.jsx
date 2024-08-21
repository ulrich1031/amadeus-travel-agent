import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Chat from "./pages/Chat"

function App() {

  return (
    <Router>
      <Routes>
        <Route path="/chat" element={<Chat />} />
      </Routes>
    </Router>
  )
}

export default App
