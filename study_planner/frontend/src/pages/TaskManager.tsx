import React, { useState, useEffect } from "react";
import axios from "axios";

interface Task {
    id: string;
    title: string;
    description: string;
    due_date: string;
    priority: number;
    completed: boolean;
}

const TaskManager: React.FC = () => {
    const [tasks, setTasks] = useState<Task[]>([]);
    const [sortBy, setSortBy] = useState<string>("deadline");

    useEffect(() => {
        fetchTasks();
    }, []);

    const fetchTasks = async () => {
        try {
            const response = await axios.get("http://127.0.0.1:8000/tasks/");
            setTasks(response.data);
        } catch (error) {
            console.error("Error fetching tasks:", error);
        }
    };

    const sortedTasks = [...tasks].sort((a, b) => {
        if (sortBy === "deadline") {
            return new Date(a.due_date).getTime() - new Date(b.due_date).getTime();
        } else if (sortBy === "priority") {
            return b.priority - a.priority;
        }
        return 0;
    });

    return (
        <div className="p-4">
            <h1 className="text-2xl font-bold mb-4">Task Manager</h1>
            <div className="flex gap-4 mb-4">
                <button
                    className="px-4 py-2 bg-blue-500 text-white rounded"
                    onClick={() => setSortBy("deadline")}
                >
                    Sort by Deadline
                </button>
                <button
                    className="px-4 py-2 bg-green-500 text-white rounded"
                    onClick={() => setSortBy("priority")}
                >
                    Sort by Priority
                </button>
            </div>
            <ul>
                {sortedTasks.map((task) => (
                    <li key={task.id} className="p-2 border-b">
                        <h2 className="text-lg font-semibold">{task.title}</h2>
                        <p>{task.description}</p>
                        <p className="text-sm text-gray-500">Due: {task.due_date}</p>
                        <p className="text-sm text-gray-700">Priority: {task.priority}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default TaskManager;
