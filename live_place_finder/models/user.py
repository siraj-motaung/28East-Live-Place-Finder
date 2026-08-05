from live_place_finder.database import get_connection

def get_users(id: int):

    conn = get_connection("users")

    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE id=%s", (id,))
        user = cursor.fetchone()

    conn.close()

    return user

