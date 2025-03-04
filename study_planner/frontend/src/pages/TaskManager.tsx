import { useState, useEffect } from "react";
import { FaSortAmountUp, FaSortAmountDown, FaTasks } from "react-icons/fa";

interface Task {
    id: string;
    title: string;
    description: string;
    due_date: string;
    priority: number;
    completed: boolean;
}

export default function TaskManager() {
    const [tasks, setTasks] = useState<Task[]>([]);
    const [sortBy, setSortBy] = useState<"deadline" | "priority" | null>(null);

    useEffect(() => {
        fetch("http://localhost:8000/tasks")
            .then((res) => res.json())
            .then((data) => setTasks(data));
    }, []);

    const sortedTasks = [...tasks].sort((a, b) => {
        if (sortBy === "deadline") {
            return new Date(a.due_date).getTime() - new Date(b.due_date).getTime();
        }
        if (sortBy === "priority") {
            return b.priority - a.priority;
        }
        return 0;
    });

    return (
        <div className="p-4">
            {/* Navbar */}
            <nav className="flex items-center space-x-4 mb-4">
                <button className="text-xl" onClick={() => setSortBy("deadline")}>
                    <FaSortAmountUp className="inline mr-2" /> Sort by Deadline
                </button>
                <button className="text-xl" onClick={() => setSortBy("priority")}>
                    <FaSortAmountDown className="inline mr-2" /> Sort by Priority
                </button>
            </nav>

            {/* Task List */}
            <div className="grid gap-4">
                {sortedTasks.map((task) => (
                    <div key={task.id} className="p-4 border rounded shadow">
                        <h3 className="text-lg font-bold">{task.title}</h3>
                        <p>{task.description}</p>
                        <p>Due: {new Date(task.due_date).toLocaleDateString()}</p>
                        <p>Priority: {task.priority}</p>
                    </div>
                ))}
            </div>
        </div>
    );
}
