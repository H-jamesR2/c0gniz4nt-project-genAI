import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import { FaHome, FaTasks, FaChartBar } from "react-icons/fa"; // Icons for TaskManager and scoreApplication
import TaskManager from "./pages/TaskManager";
import Home from "./pages/Home"; // We'll create this
import "./App.css";

const icon_size = 24;

function App() {
  return (
    <Router>
      <div className="flex min-h-screen">
        {/* Vertical Toolbar (Top-Left) */}
        <nav className="fixed top-0 left-0 h-full w-16 bg-gray-800 flex flex-col items-center py-4 space-y-6">
          <Link to="/" className="text-white hover:text-blue-300" title="Home">
            <FaHome size={icon_size} /> {/* Placeholder for Home or scoreApplication */}
          </Link>
          <Link to="/tasks" className="text-white hover:text-blue-300" title="Task Manager">
            <FaTasks size={icon_size} /> {/* TaskManager Icon */}
          </Link>
          <Link to="/" className="text-white hover:text-blue-300" title="Score Tracker">
            <FaChartBar size={icon_size} /> {/* Placeholder for Home or scoreApplication */}
          </Link>
        </nav>

        {/* Main Content */}
        <div className="flex-1 p-4">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/tasks" element={<TaskManager />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;