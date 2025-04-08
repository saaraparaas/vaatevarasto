import db

def add_item(title, size, color, description, user_id):
    sql = """INSERT INTO items (title, size, color, description, user_id)
             VALUES (?, ?, ?, ?, ?)"""
    db.execute(sql, [title, size, color, description, user_id])

def get_items():
    sql = "SELECT id, title, size FROM items ORDER BY id DESC"
    return db.query(sql)

def get_item(item_id):
    sql = """SELECT items.id,
                    items.title,
                    items.size,
                    items.color,
                    items.description,
                    users.id user_id,
                    users.username
             FROM items, users
             WHERE items.user_id = users.id AND
                    items.id = ?"""
    result = db.query(sql, [item_id])
    return result[0] if result else None

def update_item(item_id, title, size, color, description):
    sql = """UPDATE items SET title = ?,
                                size = ?,
                                color = ?,
                                description = ?
                            WHERE id = ?"""
    db.execute(sql, [title, size, color, description, item_id])


def remove_item(item_id):
    sql = "DELETE FROM items WHERE id = ?"
    db.execute(sql, [item_id])
