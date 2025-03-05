import React, { useState, useEffect, useMemo, useRef } from "react";
import axios from "axios";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";

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
    const [formData, setFormData] = useState({
        title: "",
        description: "",
        due_date: "",
        priority: 1,
    });
    const formRef = useRef<HTMLDivElement>(null); // Ref to track the form container

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
            setTasks(tasks.filter((task) => task.id !== id));
        } catch (error) {
            console.error("Error deleting task:", error);
        }
    };

    const handleTaskClick = (task: Task) => {
        setSelectedTask(task);
        setFormData({
            title: task.title,
            description: task.description,
            due_date: task.due_date,
            priority: task.priority,
        });
        setShowForm(true);
    };

    const handleInputChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
        const { name, value } = e.target;
        setFormData((prev) => ({
            ...prev,
            [name]: name === "priority" ? parseInt(value) || 1 : value,
        }));
    };

    const handleSubmit = async () => {
        if (!formData.title.trim()) {
            setShowForm(false);
            return;
        }

        try {
            if (selectedTask) {
                const response = await axios.put(
                    `http://127.0.0.1:8000/tasks/${selectedTask.id}`,
                    formData
                );
                setTasks(tasks.map((task) => (task.id === selectedTask.id ? response.data : task)));
            } else {
                const response = await axios.post("http://127.0.0.1:8000/tasks/", formData);
                setTasks([...tasks, response.data]);
            }
            setShowForm(false);
            setSelectedTask(null);
            setFormData({ title: "", description: "", due_date: "", priority: 1 });
        } catch (error) {
            console.error("Error submitting task:", error);
        }
    };

    const handleOutsideClick = (e: React.MouseEvent<HTMLDivElement>) => {
        if (formRef.current && !formRef.current.contains(e.target as Node)) {
            setShowForm(false);
            setSelectedTask(null);
            setFormData({ title: "", description: "", due_date: "", priority: 1 });
        }
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
                <Button
                    className="bg-blue-500 hover:bg-blue-600"
                    onClick={() => setSortBy("deadline")}
                >
                    Sort by Deadline
                </Button>
                <Button
                    className="bg-green-500 hover:bg-green-600"
                    onClick={() => setSortBy("priority")}
                >
                    Sort by Priority
                </Button>
            </div>
            <ul>
                {sortedTasks.map((task) => (
                    <li
                        key={task.id}
                        className="p-2 border-b cursor-pointer hover:bg-gray-100"
                        onClick={() => handleTaskClick(task)}
                    >
                        <h2 className="text-lg font-semibold">{task.title}</h2>
                        <p>
                            {task.description.length > 50
                                ? task.description.substring(0, 50) + "..."
                                : task.description}
                        </p>
                        <p className="text-sm text-gray-500">Due: {task.due_date}</p>
                        <p className="text-sm text-gray-700">Priority: {task.priority}</p>
                        <Button
                            variant="destructive"
                            className="mt-2"
                            onClick={(e) => {
                                e.stopPropagation();
                                handleDelete(task.id);
                            }}
                        >
                            Delete
                        </Button>
                    </li>
                ))}
            </ul>
            <Button
                className="fixed bottom-6 right-6 bg-blue-500 hover:bg-blue-600 rounded-full w-12 h-12 text-2xl"
                onClick={() => {
                    setSelectedTask(null);
                    setFormData({ title: "", description: "", due_date: "", priority: 1 });
                    setShowForm(true);
                }}
            >
                +
            </Button>
            {showForm && (
                <div
                    className="absolute top-0 left-0 w-full h-full bg-gray-600 bg-opacity-50 flex items-center justify-center"
                    onClick={handleOutsideClick}
                >
                    <div
                        ref={formRef}
                        className="bg-white p-4 shadow-lg rounded-md w-full max-w-md"
                    >
                        <h2 className="text-xl font-bold mb-2">
                            {selectedTask ? "Edit Task" : "New Task"}
                        </h2>
                        <Input
                            name="title"
                            placeholder="Title"
                            value={formData.title}
                            onChange={handleInputChange}
                            className="mb-2"
                        />
                        <Textarea
                            name="description"
                            placeholder="Description"
                            value={formData.description}
                            onChange={handleInputChange}
                            className="mb-2"
                        />
                        <Input
                            name="due_date"
                            type="date"
                            value={formData.due_date.split("T")[0]}
                            onChange={handleInputChange}
                            className="mb-2"
                        />
                        <Input
                            name="priority"
                            type="number"
                            min="1"
                            max="3"
                            value={formData.priority}
                            onChange={handleInputChange}
                            className="mb-2"
                        />
                        <div className="flex gap-2">
                            <Button onClick={handleSubmit}>
                                {selectedTask ? "Update" : "Create"}
                            </Button>
                            <Button
                                variant="secondary"
                                onClick={() => setShowForm(false)}
                            >
                                Cancel
                            </Button>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
};

export default TaskManager;