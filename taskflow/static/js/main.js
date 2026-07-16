document.addEventListener('DOMContentLoaded', () => {
    // 1. Auto-dismiss flash messages after 5 seconds
    const flashMessages = document.querySelectorAll('.flash-message');
    flashMessages.forEach((message) => {
        // Set timeout to dismiss
        setTimeout(() => {
            dismissMessage(message);
        }, 5000);

        // Add close button event listener
        const closeBtn = message.querySelector('.flash-close');
        if (closeBtn) {
            closeBtn.addEventListener('click', () => {
                dismissMessage(message);
            });
        }
    });

    function dismissMessage(message) {
        message.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
        message.style.opacity = '0';
        message.style.transform = 'translateY(-10px)';
        setTimeout(() => {
            message.remove();
        }, 500);
    }

    // 2. Delete Confirmation Dialog
    const deleteForms = document.querySelectorAll('.delete-task-form');
    deleteForms.forEach((form) => {
        form.addEventListener('submit', (event) => {
            const taskTitle = form.dataset.taskTitle || 'this task';
            const confirmed = confirm(`Are you sure you want to delete "${taskTitle}"? This action cannot be undone.`);
            if (!confirmed) {
                event.preventDefault();
            }
        });
    });

    // 3. Client-Side Input Form Validation
    const taskForms = document.querySelectorAll('.task-form');
    taskForms.forEach((form) => {
        form.addEventListener('submit', (event) => {
            const titleInput = form.querySelector('#title');
            if (titleInput && titleInput.value.trim() === '') {
                event.preventDefault();
                alert('Task title is required.');
                titleInput.focus();
                return;
            }

            const dueDateInput = form.querySelector('#due_date');
            if (dueDateInput && dueDateInput.value) {
                const selectedDate = new Date(dueDateInput.value);
                const today = new Date();
                // Set hours to 0 to compare dates only
                today.setHours(0, 0, 0, 0);
                selectedDate.setHours(0, 0, 0, 0);

                // We can warn the user if the due date is in the past, but still allow it
                if (selectedDate < today) {
                    const proceed = confirm('Warning: The selected due date is in the past. Do you want to proceed?');
                    if (!proceed) {
                        event.preventDefault();
                    }
                }
            }
        });
    });

    // 4. Auto-submit search/filter form on select change
    const filterSelects = document.querySelectorAll('.auto-submit-select');
    filterSelects.forEach((select) => {
        select.addEventListener('change', () => {
            const form = select.closest('form');
            if (form) {
                form.submit();
            }
        });
    });
});
