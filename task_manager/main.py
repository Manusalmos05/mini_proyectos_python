
from database.connection import DatabaseConnection
from repository.task_repository import TaskRepository
from services.task_service import TaskService
from ui.menu import Menu


def main():

    database=DatabaseConnection()

    connection=database.get_connection()


    repository=TaskRepository(connection)

    task_service = TaskService(repository)
    menu = Menu(task_service)

    menu.main_menu()
  





if __name__ == "__main__":
    main()
