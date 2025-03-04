import { useState } from "react";

type Task = {
    id: string;
    title: string;
    description: string;
    dueDate: string;
    priority: "low" | "medium" | "high";
    completed: boolean;
};

export default function TaskManager() {
    const [tasks, setTasks] = useState<Task[]>([]);
    const [selectedTasks, setSelectedTasks] = useState<Set<string>>(new Set());

    const toggleSelectTask = (id: string) => {
        setSelectedTasks((prev) => {
            const newSet = new Set(prev);
            newSet.has(id) ? newSet.delete(id) : newSet.add(id);
            return newSet;
        });
    };

    return (
        <div className="p-6 max-w-4xl mx-auto">
            <h1 className="text-2xl font-bold mb-4">Task Manager</h1>
            <TaskInputForm setTasks={setTasks} />
            <TaskList tasks={tasks} toggleSelectTask={toggleSelectTask} selectedTasks={selectedTasks} />
        </div>
    );
}

function TaskInputForm({ setTasks }: { setTasks: React.Dispatch<React.SetStateAction<Task[]>> }) {
    const [title, setTitle] = useState("");
    const [description, setDescription] = useState("");
    const [dueDate, setDueDate] = useState("");
    const [priority, setPriority] = useState<"low" | "medium" | "high">("medium");

    const addTask = () => {
        if (!title.trim()) return;
        const newTask: Task = {
            id: crypto.randomUUID(),
            title,
            description,
            dueDate,
            priority,
            completed: false,
        };
        setTasks((prev) => [...prev, newTask]);
        setTitle("");
        setDescription("");
        setDueDate("");
    };

    return (
        <div className="mb-4 p-4 border rounded-lg bg-gray-100">
            <input
                type="text"
                placeholder="Task Title"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
                className="p-2 border rounded w-full mb-2"
            />
            <textarea
                placeholder="Description"
                value={description}
                onChange={(e) => setDescription(e.target.value)}
                className="p-2 border rounded w-full mb-2"
            ></textarea>
            <input
                type="date"
                value={dueDate}
                onChange={(e) => setDueDate(e.target.value)}
                className="p-2 border rounded w-full mb-2"
            />
            <select
                value={priority}
                onChange={(e) => setPriority(e.target.value as "low" | "medium" | "high")}
                className="p-2 border rounded w-full mb-2"
            >
                <option value="low">Low</option>
                <option value="medium">Medium</option>
                <option value="high">High</option>
            </select>
            <button onClick={addTask} className="bg-blue-500 text-white p-2 rounded w-full">
                Add Task
            </button>
        </div>
    );
}

function TaskList({
    tasks,
    toggleSelectTask,
    selectedTasks,
}: {
    tasks: Task[];
    toggleSelectTask: (id: string) => void;
    selectedTasks: Set<string>;
}) {
    return (
        <ul className="space-y-2">
            {tasks.map((task) => (
                <li key={task.id} className="flex items-center justify-between p-4 border rounded-lg bg-white">
                    <input
                        type="checkbox"
                        checked={selectedTasks.has(task.id)}
                        onChange={() => toggleSelectTask(task.id)}
                        className="mr-2"
                    />
                    <div>
                        <h2 className="text-lg font-semibold">{task.title}</h2>
                        <p className="text-sm text-gray-600">{task.description}</p>
                        <p className="text-xs text-gray-500">Due: {task.dueDate} | Priority: {task.priority}</p>
                    </div>
                </li>
            ))}
        </ul>
    );
}
