from flask import Blueprint, render_template, redirect, url_for, request, flash
from taskflow.models import db, Task
from datetime import datetime
from sqlalchemy import case

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@main_bp.route('/dashboard')
def dashboard():
    """Render dashboard with tasks list, search, filter, and sorting options."""
    q = request.args.get('q', '').strip()
    status = request.args.get('status', 'all').lower()
    priority = request.args.get('priority', 'all').lower()
    sort_by = request.args.get('sort_by', 'created_at').lower()
    order = request.args.get('order', 'desc').lower()

    query = Task.query

    # Search filter (by title or description)
    if q:
        query = query.filter(Task.title.contains(q) | Task.description.contains(q))

    # Status filter
    if status == 'completed':
        query = query.filter(Task.is_completed == True)
    elif status == 'pending':
        query = query.filter(Task.is_completed == False)

    # Priority filter
    if priority in ['low', 'medium', 'high']:
        query = query.filter(Task.priority.ilike(priority))

    # Sorting options
    if sort_by == 'due_date':
        if order == 'asc':
            query = query.order_by(Task.due_date.asc())
        else:
            query = query.order_by(Task.due_date.desc())
    elif sort_by == 'priority':
        # Define priority weights for sorting: High (1), Medium (2), Low (3)
        priority_case = case(
            (Task.priority == 'High', 1),
            (Task.priority == 'Medium', 2),
            (Task.priority == 'Low', 3),
            else_=4
        )
        if order == 'asc':
            query = query.order_by(priority_case.asc())
        else:
            query = query.order_by(priority_case.desc())
    else:  # Default sort_by is 'created_at'
        if order == 'asc':
            query = query.order_by(Task.created_at.asc())
        else:
            query = query.order_by(Task.created_at.desc())

    tasks = query.all()

    # Calculate overall task stats
    total_tasks = Task.query.count()
    completed_tasks = Task.query.filter_by(is_completed=True).count()
    pending_tasks = total_tasks - completed_tasks

    return render_template(
        'dashboard.html',
        tasks=tasks,
        total_tasks=total_tasks,
        completed_tasks=completed_tasks,
        pending_tasks=pending_tasks,
        q=q,
        status=status,
        priority=priority,
        sort_by=sort_by,
        order=order
    )

@main_bp.route('/task/new', methods=['GET', 'POST'])
def create_task():
    """Handle task creation form rendering and processing."""
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()
        priority = request.form.get('priority', 'Medium')
        due_date_str = request.form.get('due_date', '').strip()

        errors = []
        if not title:
            errors.append('Title is required.')
        if len(title) > 100:
            errors.append('Title must be 100 characters or less.')
        if priority not in ['Low', 'Medium', 'High']:
            errors.append('Invalid priority level selected.')

        due_date = None
        if due_date_str:
            try:
                due_date = datetime.strptime(due_date_str, '%Y-%m-%d').date()
            except ValueError:
                errors.append('Invalid due date format. Please use YYYY-MM-DD.')

        if errors:
            for error in errors:
                flash(error, 'danger')
            return render_template('create.html', title=title, description=description, priority=priority, due_date=due_date_str)

        new_task = Task(
            title=title,
            description=description,
            priority=priority,
            due_date=due_date
        )
        db.session.add(new_task)
        db.session.commit()
        flash('Task created successfully!', 'success')
        return redirect(url_for('main.dashboard'))

    return render_template('create.html')

@main_bp.route('/task/<int:task_id>/edit', methods=['GET', 'POST'])
def edit_task(task_id):
    """Handle editing an existing task."""
    task = Task.query.get_or_404(task_id)

    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()
        priority = request.form.get('priority', 'Medium')
        due_date_str = request.form.get('due_date', '').strip()

        errors = []
        if not title:
            errors.append('Title is required.')
        if len(title) > 100:
            errors.append('Title must be 100 characters or less.')
        if priority not in ['Low', 'Medium', 'High']:
            errors.append('Invalid priority level selected.')

        due_date = None
        if due_date_str:
            try:
                due_date = datetime.strptime(due_date_str, '%Y-%m-%d').date()
            except ValueError:
                errors.append('Invalid due date format. Please use YYYY-MM-DD.')

        if errors:
            for error in errors:
                flash(error, 'danger')
            return render_template('edit.html', task=task)

        task.title = title
        task.description = description
        task.priority = priority
        task.due_date = due_date
        db.session.commit()
        flash('Task updated successfully!', 'success')
        return redirect(url_for('main.dashboard'))

    return render_template('edit.html', task=task)

@main_bp.route('/task/<int:task_id>/toggle', methods=['POST'])
def toggle_task(task_id):
    """Toggle completion status of a task."""
    task = Task.query.get_or_404(task_id)
    task.is_completed = not task.is_completed
    db.session.commit()
    
    status_str = 'completed' if task.is_completed else 'pending'
    flash(f'Task "{task.title}" marked as {status_str}!', 'success')
    return redirect(request.referrer or url_for('main.dashboard'))

@main_bp.route('/task/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    """Delete a task from the database."""
    task = Task.query.get_or_404(task_id)
    title = task.title
    db.session.delete(task)
    db.session.commit()
    flash(f'Task "{title}" deleted successfully!', 'success')
    return redirect(url_for('main.dashboard'))
