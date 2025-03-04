import React, { useState, useEffect, useMemo } from "react";
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
    const [showForm, setShowForm] = useState<boolean>(false);
    const [selectedTask, setSelectedTask] = useState<Task | null>(null);

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

    const handleDelete = async (id: string) => {
        try {
            await axios.delete(`http://127.0.0.1:8000/tasks/${id}`);
            setTasks(tasks.filter(task => task.id !== id));
        } catch (error) {
            console.error("Error deleting task:", error);
        }
    };

    const handleTaskClick = (task: Task) => {
        setSelectedTask(task);
        setShowForm(true);
    };

    const sortedTasks = useMemo(() => {
        return [...tasks].sort((a, b) => {
            if (sortBy === "deadline") {
                return new Date(a.due_date).getTime() - new Date(b.due_date).getTime();
            } else if (sortBy === "priority") {
                return b.priority - a.priority;
            }
            return 0;
        });
    }, [tasks, sortBy]);

    return (
        <div className="p-4 relative">
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
                    <li key={task.id} className="p-2 border-b cursor-pointer" onClick={() => handleTaskClick(task)}>
                        <h2 className="text-lg font-semibold">{task.title}</h2>
                        <p>{task.description.length > 50 ? task.description.substring(0, 50) + "..." : task.description}</p>
                        <p className="text-sm text-gray-500">Due: {task.due_date}</p>
                        <p className="text-sm text-gray-700">Priority: {task.priority}</p>
                        <button
                            className="text-red-500 mt-2"
                            onClick={(e) => {
                                e.stopPropagation();
                                handleDelete(task.id);
                            }}
                        >
                            Delete
                        </button>
                    </li>
                ))}
            </ul>
            <button
                className="fixed bottom-6 right-6 bg-blue-500 text-white rounded-full w-12 h-12 flex items-center justify-center text-2xl"
                onClick={() => {
                    setSelectedTask(null);
                    setShowForm(true);
                }}
            >
                +
            </button>
            {showForm && (
                <div className="absolute top-0 left-0 w-full h-full bg-white p-4 shadow-lg">
                    <h2 className="text-xl font-bold mb-2">{selectedTask ? "Edit Task" : "New Task"}</h2>
                    <input
                        type="text"
                        placeholder="Title"
                        className="w-full p-2 border mb-2"
                        defaultValue={selectedTask?.title || ""}
                    />
                    <textarea
                        placeholder="Description"
                        className="w-full p-2 border mb-2"
                        defaultValue={selectedTask?.description || ""}
                    />
                    <button
                        className="px-4 py-2 bg-gray-400 text-white rounded"
                        onClick={() => setShowForm(false)}
                    >
                        Cancel
                    </button>
                </div>
            )}
        </div>
    );
};

export default TaskManager;
