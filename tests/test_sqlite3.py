import sqlite3

class BottlePlugin:
    def __init__(self):
        self.conn = sqlite3.connect('bottles.db')
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS bottles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                message TEXT NOT NULL,
                sender TEXT NOT NULL,
                receiver TEXT NOT NULL,
                status INTEGER DEFAULT 0
            );
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS comments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                bottle_id INTEGER NOT NULL,
                comment TEXT NOT NULL
            );
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS likes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                bottle_id INTEGER NOT NULL,
                user TEXT NOT NULL
            );
        ''')
        self.conn.commit()

    def throw_bottle(self, message, sender):
        self.cursor.execute("INSERT INTO bottles (message, sender, receiver) VALUES (?, ?, '')", (message, sender))
        self.conn.commit()

    def pick_bottle(self, receiver):
        self.cursor.execute("SELECT id, message, sender FROM bottles WHERE receiver='' OR receiver=? ORDER BY RANDOM() LIMIT 1", (receiver,))
        row = self.cursor.fetchone()
        if row is None:
            return None
        bottle_id, message, sender = row
        self.cursor.execute("UPDATE bottles SET receiver=? WHERE id=?", (receiver, bottle_id))
        self.conn.commit()
        return {'id': bottle_id, 'message': message, 'sender': sender}

    def add_comment(self, bottle_id, comment):
        self.cursor.execute("INSERT INTO comments (bottle_id, comment) VALUES (?, ?)", (bottle_id, comment))
        self.conn.commit()

    def get_comments(self, bottle_id):
        self.cursor.execute("SELECT comment FROM comments WHERE bottle_id=?", (bottle_id,))
        rows = self.cursor.fetchall()
        return [row[0] for row in rows]

    def like_bottle(self, bottle_id, user):
        self.cursor.execute("INSERT INTO likes (bottle_id, user) VALUES (?, ?)", (bottle_id, user))
        self.conn.commit()

    def get_likes(self, bottle_id):
        self.cursor.execute("SELECT user FROM likes WHERE bottle_id=?", (bottle_id,))
        rows = self.cursor.fetchall()
        return [row[0] for row in rows]

    def clear_bottles(self):
        self.cursor.execute("DELETE FROM bottles")
        self.cursor.execute("DELETE FROM comments")
        self.cursor.execute("DELETE FROM likes")
        self.conn.commit()




plugin = BottlePlugin()

# 扔一个漂流瓶
plugin.throw_bottle('Hello, world!', 'Alice')

# 捡一个漂流瓶
bottle = plugin.pick_bottle('Bob')
if bottle is not None:
    print(bottle)

# 添加评论
plugin.add_comment(1, 'Nice message!')
comments = plugin.get_comments(1)
print(comments)

# 点赞
plugin.like_bottle(1, 'Charlie')
likes = plugin.get_likes(1)
print(likes)

# 清空漂流瓶
# plugin.clear_bottles()