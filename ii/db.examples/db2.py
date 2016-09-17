import sys
import sqlite3


if __name__ == '__main__':
    try:
        connection = sqlite3.connect("test.sqldb")
        cursor = connection.cursor()

        command = sys.argv[1]
        if command == 'create':
            cursor.execute("CREATE TABLE data (key TEXT, value TEXT)")
        elif command in ('get', 'set'):
            key = sys.argv[2]
            if command == 'set':
                value = sys.argv[3]
                cursor.execute("INSERT OR REPLACE INTO data (key, value) VALUES (?, ?)", (key, value))
                connection.commit()
            cursor.execute("SELECT key, value FROM data WHERE key = ?", key)
            print("{0} = {1}".format(*next(cursor)))
        else:
            raise ValueError
    except (IndexError, ValueError):
        print("Usage:\n  db get <key>\n  db\n", end="")
    except KeyError:
        print("Key not found.")
    finally:
        connection.close
