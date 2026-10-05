from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

DATABASE = "students.db"


# -----------------------------
# Database connection
# -----------------------------

def get_db():

    conn = sqlite3.connect(DATABASE)

    conn.row_factory = sqlite3.Row

    return conn


# -----------------------------
# Create database
# -----------------------------

def create_database():

    conn = get_db()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            admission_no TEXT,

            name TEXT NOT NULL,

            dob TEXT,

            age INTEGER,

            gender TEXT,

            father_name TEXT,

            mother_name TEXT,

            phone TEXT,

            email TEXT,

            address TEXT,

            department TEXT,

            course TEXT,

            year TEXT,

            blood_group TEXT

        )
    """)

    conn.commit()

    conn.close()


# -----------------------------
# Home page
# -----------------------------

@app.route("/")
def index():

    conn = get_db()

    students = conn.execute("""
        SELECT *
        FROM students
        ORDER BY id DESC
    """).fetchall()

    conn.close()

    return render_template(
        "index.html",
        students=students
    )


# -----------------------------
# Add student
# -----------------------------

@app.route(
    "/add",
    methods=["POST"]
)
def add_student():

    admission_no = request.form.get(
        "admission_no"
    )

    name = request.form.get(
        "name"
    )

    dob = request.form.get(
        "dob"
    )

    age = request.form.get(
        "age"
    )

    gender = request.form.get(
        "gender"
    )

    father_name = request.form.get(
        "father_name"
    )

    mother_name = request.form.get(
        "mother_name"
    )

    phone = request.form.get(
        "phone"
    )

    email = request.form.get(
        "email"
    )

    address = request.form.get(
        "address"
    )

    department = request.form.get(
        "department"
    )

    course = request.form.get(
        "course"
    )

    year = request.form.get(
        "year"
    )

    blood_group = request.form.get(
        "blood_group"
    )


    conn = get_db()

    conn.execute("""
        INSERT INTO students (

            admission_no,
            name,
            dob,
            age,
            gender,
            father_name,
            mother_name,
            phone,
            email,
            address,
            department,
            course,
            year,
            blood_group

        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)

    """, (

        admission_no,
        name,
        dob,
        age,
        gender,
        father_name,
        mother_name,
        phone,
        email,
        address,
        department,
        course,
        year,
        blood_group

    ))

    conn.commit()

    conn.close()

    return redirect("/")


# -----------------------------
# Delete student
# -----------------------------

@app.route(
    "/delete/<int:student_id>"
)
def delete_student(student_id):

    conn = get_db()

    conn.execute("""
        DELETE FROM students
        WHERE id = ?
    """, (student_id,))

    conn.commit()

    conn.close()

    return redirect("/")


# -----------------------------
# Start application
# -----------------------------

if __name__ == "__main__":

    create_database()

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False,
        use_reloader=False
    )