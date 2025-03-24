import db

def add_item(title, size, color, description, user_id):
    sql = """INSERT INTO items (title, size, color, description, user_id)
             VALUES (?, ?, ?, ?, ?)"""
    db.execute(sql, [title, size, color, description, user_id])
