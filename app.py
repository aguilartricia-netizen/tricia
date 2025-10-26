from flask import Flask, jsonify, request

app = Flask(__name__)

# -----------------------------
# Temporary In-Memory Database
# -----------------------------
students = [
    {"id": 1, "name": "Tricia Aguilar", "grade": 10, "section": "Zechariah"},
    {"id": 2, "name": "Jomarie Lapasaran", "grade": 9, "section": "Matthew"},
    {"id": 3, "name": "Angel Dela Cruz", "grade": 11, "section": "Mark"}
]

# -----------------------------
# Home Route
# -----------------------------
@app.route('/')
def home():
    return "🎓 Welcome to the Student Management System API! Use /students to view all students."

# -----------------------------
# Get All Students
# -----------------------------
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify({
        "message": "List of all students",
        "total": len(students),
        "students": students
    })

# -----------------------------
# Get Single Student by ID
# -----------------------------
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = next((s for s in students if s["id"] == student_id), None)
    if student:
        return jsonify(student)
    return jsonify({"message": "Student not found"}), 404

# -----------------------------
# Add New Student
# -----------------------------
@app.route('/students', methods=['POST'])
def add_student():
    new_student = request.get_json()
    
    if not new_student or "name" not in new_student or "grade" not in new_student or "section" not in new_student:
        return jsonify({"message": "Invalid data. Please include name, grade, and section."}), 400

    new_student["id"] = len(students) + 1
    students.append(new_student)

    return jsonify({
        "message": "✅ Student added successfully!",
        "student": new_student
    }), 201

# -----------------------------
# Update Existing Student
# -----------------------------
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = next((s for s in students if s["id"] == student_id), None)
    if not student:
        return jsonify({"message": "Student not found"}), 404

    data = request.get_json()
    student.update(data)

    return jsonify({
        "message": "✅ Student updated successfully!",
        "student": student
    })

# -----------------------------
# Delete a Student
# -----------------------------
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    global students
    student = next((s for s in students if s["id"] == student_id), None)
    if not student:
        return jsonify({"message": "Student not found"}), 404

    students = [s for s in students if s["id"] != student_id]
    return jsonify({"message": "🗑️ Student deleted successfully!"})

# -----------------------------
# Run the Flask App
# -----------------------------
if __name__ == '__main__':
    app.run(debug=True)
