import sys
import shelve


if __name__ == '__main__':
    try:
        db = shelve.open("test.db")

        command = sys.argv[1]
        if command in ('get', 'set'):
            key = sys.argv[2]
            if command == 'set':
                db[key] = sys.argv[3]
            print("{0} = {1}".format(key, db[key]))
        else:
            raise ValueError
    except (IndexError, ValueError):
        print("Usage:\n  db get <key>\n  db\n", end="")
    except KeyError:
        print("Key not found.")
    finally:
        db.close
