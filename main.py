# Создайте реализацию паттерна Command. Протестируйте работу созданного класса


from collections import deque


class Command:
    def execute(self):
        raise NotImplementedError("Необходимо реализовать метод execute")


class PrintCommand(Command):
    def __init__(self, message):
        self.message = message

    def execute(self):
        print(f"Выполнение команды PrintCommand: {self.message}")


class CommandQueue:
    def __init__(self):
        self._commands = deque()

    def add_command(self, command: Command):
        self._commands.append(command)
        print(f"Добавлена команда: {command.__class__.__name__}")


    def execute_next(self):
        if self._commands:
            command = self._commands.popleft()
            print(f"Проведение {command.__class__.__name__} из очереди")
            command.execute()
        else:
            print("Нет команд для выполнения")

    def has_commands(self):
        return len(self._commands) > 0


if __name__ == "__main__":

    queue = CommandQueue()

    # Добавляем несколько команд
    queue.add_command(PrintCommand("привет, мир!"))
    queue.add_command(PrintCommand("Выполнение следующей команды..."))
    queue.add_command(PrintCommand("Заключительная команда в queue"))


    while queue.has_commands():
        queue.execute_next()



# _________________2 версия_______________________

#
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.prev = None
#         self.next = None
#
#
# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def append(self, value):
#         new_node = Node(value)
#         if not self.head:
#             self.head = self.tail = new_node
#         else:
#             self.tail.next = new_node
#             new_node.prev = self.tail
#             self.tail = new_node
#
#     def remove(self, node):
#         if node.prev:
#             node.prev.next = node.next
#         if node.next:
#             node.next.prev = node.prev
#         if node == self.head:
#             self.head = node.next
#         if node == self.tail:
#             self.tail = node.prev
#
#     def find(self, value):
#         current = self.head
#         while current:
#             if current.value == value:
#                 return current
#             current = current.next
#         return None
#
#     def display(self):
#         current = self.head
#         while current:
#             print(current.value, end=" <-> ")
#             current = current.next
#         print("None")
#
#
# class Command:
#     def execute(self):
#         raise NotImplementedError("Этот метод необходимо переопределить")
#
#     def undo(self):
#         raise NotImplementedError("Этот метод необходимо переопределить")
#
#
# class AddCommand(Command):
#     def __init__(self, dll, value):
#         self.dll = dll
#         self.value = value
#         self.node = None
#
#     def execute(self):
#         print(f"Выполнение команды добавления: {self.value}")
#         self.dll.append(self.value)
#         self.node = self.dll.tail
#
#     def undo(self):
#         print(f"Отмена команды добавления: {self.value}")
#         if self.node:
#             self.dll.remove(self.node)
#
#
# class RemoveCommand(Command):
#     def __init__(self, dll, value):
#         self.dll = dll
#         self.value = value
#         self.node = None
#
#     def execute(self):
#         print(f"Выполнение команды удаления: {self.value}")
#         self.node = self.dll.find(self.value)
#         if self.node:
#             self.dll.remove(self.node)
#         else:
#             print("Значение не найдено")
#
#     def undo(self):
#         print(f"Отмена команды удаления: {self.value}")
#         if self.node:
#             if self.node.prev:
#                 self.dll.append(self.value)
#                 self.node = self.dll.tail
#                 self.node.prev = self.node.prev
#                 self.dll.tail = self.node
#             else:
#                 self.dll.append(self.value)
#                 self.node = self.dll.tail
#         else:
#             print("Невозможно отменить удаление.")
#
#
# class CommandManager:
#     def __init__(self):
#         self.history = []
#         self.redo_stack = []
#
#     def execute_command(self, command):
#         command.execute()
#         self.history.append(command)
#         self.redo_stack.clear()
#
#     def undo(self):
#         if self.history:
#             command = self.history.pop()
#             command.undo()
#             self.redo_stack.append(command)
#         else:
#             print("Нет команд для отмены.")
#
#     def redo(self):
#         if self.redo_stack:
#             command = self.redo_stack.pop()
#             command.execute()
#             self.history.append(command)
#         else:
#             print("Нет команд для повтора.")
#
#
# # Пример использования
# if __name__ == "__main__":
#     dll = DoublyLinkedList()
#     manager = CommandManager()
#
#     # Добавляем числа в список
#     manager.execute_command(AddCommand(dll, 10))
#     manager.execute_command(AddCommand(dll, 20))
#     manager.execute_command(AddCommand(dll, 30))
#
#     dll.display()
#
#     # Отменяем последнюю команду
#     manager.undo()
#     dll.display()
#
#     # Повторяем последнюю отменённую команду
#     manager.redo()
#     dll.display()
#
#     # Удаляем число из списка
#     manager.execute_command(RemoveCommand(dll, 20))
#     dll.display()
#
#     # Отменяем удаление
#     manager.undo()
#     dll.display()
#


# 2 Есть класс, предоставляющий доступ к набору чисел.
# Источником этого набора чисел является некоторый
# файл. Приложение должно получать доступ к этим данным и
# выполнять набор операций над ними (сумма, максимум,
# минимум и т.д.). При каждой попытке доступа к этому
# набору необходимо вносить запись в лог-файл. При реализации используйте паттерн Proxy (для логгирования)
# и другие необходимые паттерны.

#
# import os
# from abc import ABC, abstractmethod
#
#
# class Logger:
#     def __init__(self, log_file='access.log'):
#         self.log_file = log_file
#
#     def log(self, message):
#         with open(self.log_file, 'a') as file:
#             file.write(message +'n')
#
#
# class NumberData(ABC):
#     @abstractmethod
#     def get_numbers(self):
#         pass
#
#     @abstractmethod
#     def sum_numbers(self):
#         pass
#
#     @abstractmethod
#     def max_number(self):
#         pass
#
#     @abstractmethod
#     def min_number(self):
#         pass
#
#
# class FileNumberData(NumberData):
#     def __init__(self, file_path):
#         self.file_path = file_path
#
#     def get_numbers(self):
#         with open(self.file_path, 'r') as file:
#             numbers = [int(line.strip()) for line in file]
#         return numbers
#
#     def sum_numbers(self):
#         numbers = self.get_numbers()
#         return sum(numbers)
#
#     def max_number(self):
#         numbers = self.get_numbers()
#         return max(numbers)
#
#     def min_number(self):
#         numbers = self.get_numbers()
#         return min(numbers)
#
#
# class LoggingProxy(NumberData):
#     def __init__(self, file_number_data, logger):
#         self._file_number_data = file_number_data
#         self._logger = logger
#
#     def get_numbers(self):
#         self._logger.log("Accessed get_numbers")
#         return self._file_number_data.get_numbers()
#
#     def sum_numbers(self):
#         self._logger.log("Accessed sum_numbers")
#         return self._file_number_data.sum_numbers()
#
#     def max_number(self):
#         self._logger.log("Accessed max_number")
#         return self._file_number_data.max_number()
#
#     def min_number(self):
#         self._logger.log("Accessed min_number")
#         return self._file_number_data.min_number()
#
#
# if __name__ == "__main__":
#
#     file_path = 'numbers.txt'
#     if not os.path.exists(file_path):
#         with open(file_path, 'w') as file:
#             file.write('10\n5\n20\n3\n8')
#
#
#     file_number_data = FileNumberData(file_path)
#     logger = Logger('access.log')
#
#     logging_proxy = LoggingProxy(file_number_data, logger)
#
#
#     print("Числа:", logging_proxy.get_numbers())
#     print("Сумма:", logging_proxy.sum_numbers())
#     print("Максимум:", logging_proxy.max_number())
#     print("Минимум:", logging_proxy.min_number())
#
