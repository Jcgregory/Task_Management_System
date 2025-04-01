import { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [tasks, setTasks] = useState([]);

  // Fetch tasks from Flask API
  useEffect(() => {
    axios.get("http://127.0.0.1:5000/tasks") // Flask API
      .then(response => {
        setTasks(response.data);
      })
      .catch(error => {
        console.error("Error fetching tasks:", error);
      });
  }, []);

  return (
    <div>
      <h1>Task Management System</h1>
      <ul>
        {tasks.map(task => (
          <li key={task.id}>{task.title} - {task.completed ? "✅" : "❌"}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
