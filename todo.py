from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Todo class for Todo items
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)

# Create the SQLite database
with app.app_context():
    db.create_all()

    from flask import render_template, request, redirect, url_for

# Route to display all todos
@app.route('/')
def show_todos():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)

# Route to add a new todo
@app.route('/add', methods=['POST'])
def add_todo():
    content = request.form['content']
    new_todo = Todo(content=content)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('show_todos'))

# Route to toggle todo completion status
@app.route('/toggle/<int:id>')
def toggle_complete(id):
    todo = Todo.query.get(id)
    todo.completed = not todo.completed
    db.session.commit()
    return redirect(url_for('show_todos'))

# Route to delete a todo
@app.route('/delete/<int:id>')
def delete_todo(id):
    todo = Todo.query.get(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('show_todos'))

@app.route('/completed')
def show_completed_todos():
    #print("Showing completed todos")   #added a print statement to ensure the new code was being accessed
    completed_todos = Todo.query.filter_by(completed=True).all()
    return render_template('completed.html', todos=completed_todos)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_todo(id):
    todo = Todo.query.get(id)
    if request.method == 'POST':
        todo.content = request.form['content']
        db.session.commit()
        return redirect(url_for('show_todos'))
    return render_template('edit.html', todo=todo)


if __name__ == '__main__':
    app.run(debug=True)