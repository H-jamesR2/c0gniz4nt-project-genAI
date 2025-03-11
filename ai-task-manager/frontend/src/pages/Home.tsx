import React from "react";
import { Link } from "react-router-dom";
import viteLogo from "../assets/vite.svg";
import reactLogo from "../assets/react.svg";

const Home: React.FC = () => {
    return (
        <div className="text-center">
            <h1 className="text-3xl font-bold mb-6">Welcome to My App</h1>
            <div className="flex justify-center gap-4 mb-6">
                <a href="https://vite.dev" target="_blank" rel="noopener noreferrer">
                    <img src={viteLogo} className="logo" alt="Vite logo" />
                </a>
                <a href="https://react.dev" target="_blank" rel="noopener noreferrer">
                    <img src={reactLogo} className="logo react" alt="React logo" />
                </a>
            </div>
            <p className="mb-4">Explore the app:</p>
            <div className="flex justify-center gap-4">
                <Link to="/tasks" className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">
                    Task Manager
                </Link>
                <Link to="/" className="px-4 py-2 bg-gray-500 text-white rounded hover:bg-gray-600">
                    Score Application (Coming Soon)
                </Link>
            </div>
            <p className="mt-6 text-gray-600">Edit <code>src/pages/Home.tsx</code> to customize this page.</p>
        </div>
    );
};

export default Home;