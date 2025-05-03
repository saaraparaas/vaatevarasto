import db

def get_all_classes():
    sql = "SELECT title, value FROM classes ORDER BY id"
    result = db.query(sql)

    classes = {}
    for title, value in result:
        classes[title] = []
    for title, value in result:
        classes[title].append(value)

    return classes

def add_item(title, size, color, description, user_id, classes):
    sql = """INSERT INTO items (title, size, color, description, user_id)
             VALUES (?, ?, ?, ?, ?)"""
    db.execute(sql, [title, size, color, description, user_id])

    item_id = db.last_insert_id()

    sql = "INSERT INTO item_classes (item_id, title, value) VALUES (?, ?, ?)"
    for title, value in classes:
        db.execute(sql, [item_id, title, value])

def get_images(item_id):
    sql = "SELECT id FROM images WHERE item_id = ?"
    return db.query(sql, [item_id])

def add_image(item_id, image):
    sql = "INSERT INTO images (item_id, image) VALUES (?, ?)"
    db.execute(sql, [item_id, image])

def get_image(image_id):
    sql = "SELECT image FROM images WHERE id = ?"
    result = db.query(sql, [image_id])
    return result[0][0] if result else None

def remove_image(item_id, image_id):
    sql = "DELETE FROM images WHERE id = ? AND item_id = ?"
    db.execute(sql, [image_id, item_id])

def get_classes(item_id):
    sql = "SELECT title, value FROM item_classes WHERE item_id = ?"
    return db.query(sql, [item_id])

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

def update_item(item_id, title, size, color, description, classes):
    sql = """UPDATE items SET title = ?,
                                size = ?,
                                color = ?,
                                description = ?
                            WHERE id = ?"""
    db.execute(sql, [title, size, color, description, item_id])

    sql = "DELETE FROM item_classes WHERE item_id = ?"
    db.execute(sql, [item_id])

    sql = "INSERT INTO item_classes (item_id, title, value) VALUES (?, ?, ?)"
    for title, value in classes:
        db.execute(sql, [item_id, title, value])

def remove_item(item_id):
    sql = "DELETE FROM comments WHERE item_id = ?"
    db.execute(sql, [item_id])
    sql = "DELETE FROM images WHERE item_id = ?"
    db.execute(sql, [item_id])
    sql = "DELETE FROM item_classes WHERE item_id = ?"
    db.execute(sql, [item_id])
    sql = "DELETE FROM items WHERE id = ?"
    db.execute(sql, [item_id])

def find_items(query):
    sql = """
        SELECT items.id, items.title
        FROM items
        LEFT JOIN item_classes ON items.id = item_classes.item_id
        LEFT JOIN classes ON item_classes.title = classes.title AND item_classes.value = classes.value
        WHERE items.title LIKE ?
            OR items.description LIKE ?
            OR items.size LIKE ?
            OR items.color LIKE ?
            OR classes.title LIKE ?
            OR classes.value LIKE ?
        ORDER BY items.id DESC
    """
    like = "%" + query + "%"
    return db.query(sql, [like, like, like, like, like, like])

def add_comment(item_id, user_id, comment):
    sql = """INSERT INTO comments (item_id, user_id, comment)
             VALUES (?, ?, ?)"""
    db.execute(sql, [item_id, user_id, comment])

def get_comments(item_id):
    sql = """SELECT comments.comment,
                    users.id user_id,
                    users.username
             FROM comments, users
             WHERE comments.user_id = users.id AND
                    comments.item_id = ?"""
    result = db.query(sql, [item_id])
    return result if result else []
