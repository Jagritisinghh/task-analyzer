document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('taskForm');
    const list = document.getElementById('taskList');

    // 1. Fetch Tasks on Load
    fetchTasks();

    // 2. Handle Form Submit
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const taskData = {
            title: document.getElementById('title').value,
            importance: document.getElementById('importance').value,
            effort: document.getElementById('effort').value,
            due_date: document.getElementById('dueDate').value
        };

        try {
            const res = await fetch('/api/tasks/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(taskData)
            });

            if (res.ok) {
                form.reset();
                fetchTasks(); // Reload list to see new ranking
            }
        } catch (err) {
            console.error('Error adding task:', err);
        }
    });

    // 3. Fetch and Render Function
    async function fetchTasks() {
        try {
            const res = await fetch('/api/tasks/');
            const data = await res.json();
            renderList(data.tasks);
        } catch (err) {
            console.error('Error fetching tasks:', err);
        }
    }

    // 4. Render Logic
    function renderList(tasks) {
        list.innerHTML = '';
        if (tasks.length === 0) {
            list.innerHTML = '<p style="text-align:center; color:#b2bec3;">No tasks found. Relax!</p>';
            return;
        }

        tasks.forEach(task => {
            const div = document.createElement('div');
            
            // Visual logic for border color based on score
            let priorityClass = 'priority-low';
            if (task.score > 80) priorityClass = 'priority-high';
            else if (task.score > 50) priorityClass = 'priority-med';

            div.className = `task-item ${priorityClass}`;
            div.innerHTML = `
                <div class="task-info">
                    <h3>${task.title}</h3>
                    <div class="task-meta">
                        Due: ${task.due_date || 'No Date'} | 
                        Imp: ${task.importance}/5 | 
                        Effort: ${task.effort}/5
                    </div>
                </div>
                <div class="task-actions">
                    <span class="score-badge" title="Smart Score">Score: ${task.score}</span>
                    <button onclick="deleteTask(${task.id})">✓ Done</button>
                </div>
            `;
            list.appendChild(div);
        });
    }

    // 5. Delete Action (Attached to window for global access)
    window.deleteTask = async (id) => {
        if(!confirm('Mark this task as complete?')) return;
        
        try {
            await fetch(`/api/tasks/${id}/`, { method: 'DELETE' });
            fetchTasks();
        } catch (err) {
            console.error('Error deleting:', err);
        }
    };
});