<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TodoList App</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container">
        <h1 class="my-4">TodoList App</h1>
        <form id="todoForm" class="mb-4">
            <div class="input-group">
                <input type="text" id="newItem" class="form-control" placeholder="Enter a new item" required>
                <button type="submit" class="btn btn-primary">Add</button>
            </div>
        </form>
        <ul id="todoList" class="list-group"></ul>
    </div>

    <template id="itemTemplate">
        <li class="list-group-item">
            <div class="form-check">
                <input class="form-check-input" type="checkbox">
                <label class="form-check-label"></label>
                <input type="text" class="form-control d-none">
            </div>
            <div class="btn-group btn-group-sm float-end">
                <button type="button" class="btn btn-secondary edit-btn">Edit</button>
                <button type="button" class="btn btn-danger delete-btn">Delete</button>
            </div>
        </li>
    </template>

    <script>
        const todoForm = document.getElementById('todoForm');
        const newItem = document.getElementById('newItem');
        const todoList = document.getElementById('todoList');
        const itemTemplate = document.getElementById('itemTemplate');

        // Fetch and render existing items
        fetch('<?= base_url("item"); ?>/')
            .then(response => response.json())
            .then(items => {
                items.forEach(item => {
                    const li = createListItem(item);
                    todoList.appendChild(li);
                });
            });

        // Handle form submission
        todoForm.addEventListener('submit', event => {
            event.preventDefault();
            const item = { item: newItem.value, completed: false };
            fetch('<?= base_url("item"); ?>/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(item)
            })
            .then(response => response.json())
            .then(item => {
                const li = createListItem(item);
                todoList.appendChild(li);
                newItem.value = '';
            });
        });

        // Handle item actions
        todoList.addEventListener('click', event => {
            const li = event.target.closest('li');
            const checkbox = li.querySelector('.form-check-input');
            const label = li.querySelector('.form-check-label');
            const input = li.querySelector('input[type="text"]');
            const editBtn = li.querySelector('.edit-btn');
            const deleteBtn = li.querySelector('.delete-btn');
            const id = li.dataset.id;

            if (event.target === checkbox) {
                const completed = checkbox.checked;
                fetch(`<?= base_url("item"); ?>/${id}`, {
                    method: 'PUT',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ completed })
                });
            } else if (event.target === editBtn) {
                label.classList.add('d-none');
                input.classList.remove('d-none');
                input.value = label.textContent;
                input.focus();
            } else if (event.target === deleteBtn) {
                fetch(`<?= base_url("item"); ?>/${id}`, { method: 'DELETE' })
                    .then(() => li.remove());
            }
        });

        // Handle item editing
        todoList.addEventListener('keypress', event => {
            if (event.key === 'Enter') {
                const li = event.target.closest('li');
                const label = li.querySelector('.form-check-label');
                const input = li.querySelector('input[type="text"]');
                const id = li.dataset.id;
                const item = input.value;

                fetch(`<?= base_url("item"); ?>/${id}`, {
                    method: 'PUT',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ item })
                })
                .then(() => {
                    label.textContent = item;
                    label.classList.remove('d-none');
                    input.classList.add('d-none');
                });
            }
        });

        // Create list item from template
        function createListItem(item) {
            const li = itemTemplate.content.firstElementChild.cloneNode(true);
            li.dataset.id = item.id;
            const checkbox = li.querySelector('.form-check-input');
            checkbox.checked = item.completed === '1'; // Check the checkbox if completed is '1'
            const label = li.querySelector('.form-check-label');
            label.textContent = item.item;
            return li;
        }
    </script>
</body>
</html>