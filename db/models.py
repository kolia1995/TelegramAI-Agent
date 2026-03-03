
class Users:
    def __init__(self, telegram_id):
        self.telegram_id = telegram_id

    def exists(self, cur):
        cur.execute(
            "SELECT * FROM users WHERE telegram_id = %s;",
            (self.telegram_id,)
        )
        return cur.fetchone() is not None

    def get(self, cur):
        cur.execute(
            "SELECT id FROM users WHERE telegram_id=%s",
            (self.telegram_id, )
        )

        rows = cur.fetchall()
        if rows:
            return rows[0]
        return None

    def delete(self, cur):
        cur.execute(
            "DELETE FROM users WHERE telegram_id = %s;",
            (self.telegram_id,)
        )

    def save(self, cur):
        cur.execute(
            "INSERT INTO users (telegram_id) VALUES (%s) RETURNING id",
            (self.telegram_id,)
        )

class Message:
    def __init__(self, telegram_id, content, role):
        self.telegram_id = telegram_id
        self.content = content
        self.role = role

    def exists(self, cur):
        cur.execute(
            "SELECT user_id FROM message WHERE user_id = %s",
            (self.telegram_id, )
        )

        return cur.fetchone() is not None

    def get_all(self, cur):
        cur.execute(
            "SELECT role, content FROM message WHERE user_id = (SELECT id FROM users WHERE telegram_id = %s) "
            "ORDER BY id DESC LIMIT 50",
            (self.telegram_id, )
        )

        rows  = cur.fetchall()
        rows.reverse()

        return [
            {"role": role, "content": content}
            for role, content in rows
        ]

    def save(self, cur):
        cur.execute(
            "INSERT INTO message (user_id, content, role) "
            "VALUES ((SELECT id FROM users WHERE telegram_id = %s), %s, %s) RETURNING id",
            (self.telegram_id, self.content, self.role)
        )

    def delete(self, cur):
        cur.execute(
            "DELETE FROM message WHERE user_id=%s",
            (self.telegram_id, )
        )

class Memory:
    def __init__(self, telegram_id, key, value):
        self.telegram_id = telegram_id
        self.key = key
        self.value = value

    def exists(self, cur):
        cur.execute(
            "SELECT user_id, value, key FROM memory WHERE user_id=%s AND value=%s AND key=%s",
            (self.telegram_id, self.value, self.key)
        )

        return cur.fetchone()

    def get_all(self, cur):
        cur.execute(
            "SELECT key, value FROM memory WHERE user_id = (SELECT id FROM users WHERE telegram_id = %s)",
            (self.telegram_id, )
        ) 
        
        rows = cur.fetchall()

        mas = {}        
        for key, value in rows:
            if key not in mas:
                mas[key] = []
            mas[key].append(value)

        return mas

    def get_by_key(self, cur):
        cur.execute(
            "SELECT value FROM memory WHERE user_id=%s AND key=%s",
            (self.telegram_id, self.key)
        )

        rows = cur.fetchall()
        mas = {}

        for key, value in rows:
            mas.setdefault(key, []).append(value)

        return mas

    def save(self, cur):
        cur.execute(
            """
                INSERT INTO memory (user_id, key, value)
                VALUES ((SELECT id FROM users WHERE telegram_id = %s), %s, %s)
                ON CONFLICT (user_id, key, value) DO NOTHING
            """,
        (self.telegram_id, self.key, self.value)
    )