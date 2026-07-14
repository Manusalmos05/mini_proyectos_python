from database.connection import DatabaseConnection


def main():
    database = DatabaseConnection()

    database.close_connection()


if __name__ == "__main__":
    main()