from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# In-memory list (acts as a temporary database)
students = []

@app.route('/')
def home():
    return render_template('index.html', students=students)

@app.route('/add', methods=['POST'])
def add_student():
    name = request.form['name']
    grade = request.form['grade']
    section = request.form['section']

    new_student = {
        "id": len(students) + 1,
        "name": name,
        "grade": grade,
        "section": section
    }

    students.append(new_student)
    return render_template('index.html', students=students, message="✅ Student added successfully!")

@app.route('/api/students', methods=['GET'])
def get_students():
    return jsonify(students)

if __name__ == '__main__':
    app.run(debug=True)
