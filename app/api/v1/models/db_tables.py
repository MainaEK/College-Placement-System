import os
from werkzeug.security import generate_password_hash

def drop_table_if_exists():
    """ Deletes all tables"""
    drop_users = """ DROP TABLE IF EXISTS users CASCADE"""
    drop_universities = """ DROP TABLE IF EXISTS universities CASCADE"""
    drop_courses = """ DROP TABLE IF EXISTS courses CASCADE"""
    drop_students = """ DROP TABLE IF EXISTS students CASCADE"""
    return [drop_users, drop_universities, drop_courses, drop_students]

def set_up_tables():
    create_users_table = """
        CREATE TABLE IF NOT EXISTS users (
        user_id SERIAL PRIMARY KEY,
        username VARCHAR(40) NOT NULL,
        password VARCHAR(200) NOT NULL,
        registered_on TIMESTAMP WITHOUT TIME ZONE \
        DEFAULT (NOW() AT TIME ZONE 'utc'),
        isAdmin BOOLEAN DEFAULT False);"""    
         
    create_universities_table = """
        CREATE TABLE IF NOT EXISTS universities (
        uni_id INTEGER PRIMARY KEY,
        uni_name VARCHAR(100) NOT NULL,
        email VARCHAR(200),
        password VARCHAR(200) NOT NULL,
        registered_on TIMESTAMP WITHOUT TIME ZONE \
        DEFAULT (NOW() AT TIME ZONE 'utc'));"""    
        
    create_courses_table = """
        CREATE TABLE IF NOT EXISTS courses (
        course_id SERIAL PRIMARY KEY,
        course_name VARCHAR(100) NOT NULL,
        requirements VARCHAR(20),
        uni_id INTEGER NOT NULL,
        FOREIGN KEY (uni_id) REFERENCES universities(uni_id) ON DELETE CASCADE,
        registered_on TIMESTAMP WITHOUT TIME ZONE \
        DEFAULT (NOW() AT TIME ZONE 'utc'));"""   
        
    create_students_table = """
        CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY,
        student_name VARCHAR(100) NOT NULL,
        grades VARCHAR(20) NOT NULL,
        course_id INTEGER NOT NULL,
        FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
        registered_on TIMESTAMP WITHOUT TIME ZONE \
        DEFAULT (NOW() AT TIME ZONE 'utc'));"""   
        
    return [create_users_table, create_universities_table,create_courses_table,create_students_table]

def create_admin(connect):
    query = """
        INSERT INTO users(username, password, isAdmin)
        VALUES('adminUser', '{}', 'True')
        """.format(generate_password_hash('Eric1234'))   
          
    # prevents trying duplicating admin if already exists
    get_admin = """SELECT * from users WHERE username = 'admin'"""
    cur = connect.cursor()
    get_admin = cur.execute(get_admin)
    get_admin = cur.fetchone()
    if get_admin:
        pass
    else:
        cur.execute(query)
        connect.commit()
        