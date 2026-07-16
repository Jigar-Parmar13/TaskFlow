from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date

db = SQLAlchemy()

class Task(db.Model):
    """Task model representing the task table in the database."""
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    priority = db.Column(db.String(20), nullable=False, default='Medium') # Low, Medium, High
    due_date = db.Column(db.Date, nullable=True)
    is_completed = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    @property
    def is_overdue(self):
        """Check if the task is overdue (past due date and not completed)."""
        if self.due_date and not self.is_completed:
            return self.due_date < date.today()
        return False

    def __repr__(self):
        return f'<Task {self.id}: {self.title}>'
