import pytest
import os
import tempfile
from database.database import Database, EmployeeTable, DepartmentTable

@pytest.fixture
def temp_employee_file():
    """ Создаем временный файл для таблицы рабочих """
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
    yield temp_file.name
    os.remove(temp_file.name)

@pytest.fixture
def temp_department_file():
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
    yield temp_file.name
    os.remove(temp_file.name)

#Пример, как используются фикстуры
@pytest.fixture
def database(temp_employee_file, temp_department_file):
    """ Данная фикстура задает БД и определяет таблицы. """
    db = Database()

    # Используем временные файлы для тестирования файлового ввода-вывода в EmployeeTable и DepartmentTable
    employee_table = EmployeeTable()
    employee_table.FILE_PATH = temp_employee_file
    department_table = DepartmentTable()
    department_table.FILE_PATH = temp_department_file

    db.register_table("employees", employee_table)
    db.register_table("departments", department_table)

    return db

def test_insert_employee(database):
    database.insert("employees", "1 Alice 30 70000")
    database.insert("employees", "2 Bob 28 60000")

    # Проверяем вставку, подгружая с CSV
    employee_data = database.select("employees", 1, 2)
    print(employee_data)
    assert len(employee_data) == 2
    assert employee_data[0] == {'id': '1', 'name': 'Alice', 'age': '30', 'salary': '70000'}
    assert employee_data[1] == {'id': '2', 'name': 'Bob', 'age': '28', 'salary': '60000'}

def test_insert_department(database):
    pass

def test_join_employees_departments(database):
    pass


def test_employee_unique_constraints(database):
    database.insert("employees", "1 Alice 30 70000 101")
    
    with pytest.raises(ValueError):
        database.insert("employees", "1 Bob 25 50000 102")  
    
    with pytest.raises(ValueError):
        database.insert("employees", "1 Charlie 35 80000 101") 

def test_department_select_by_name(database):
    database.insert("departments", "101 Engineering")
    database.insert("departments", "102 Marketing")
    database.insert("departments", "103 Engineering")

    result = database.select("departments", "Engineering")
    assert len(result) == 2
    assert {'id': '101', 'department_name': 'Engineering'} in result
    assert {'id': '103', 'department_name': 'Engineering'} in result


def test_join_operation(database):
    database.insert("employees", "1 Alice 30 70000 101")
    database.insert("employees", "2 Bob 28 60000 102")
    database.insert("departments", "101 Engineering")
    database.insert("departments", "102 Marketing")

    result = database.join("employees", "departments", "department_id", "id")
    assert len(result) == 2
    assert {'id': '1', 'name': 'Alice', 'age': '30', 'salary': '70000',
            'department_id': '101', 'department_name': 'Engineering'} in result
    assert {'id': '2', 'name': 'Bob', 'age': '28', 'salary': '60000',
            'department_id': '102', 'department_name': 'Marketing'} in result


def test_no_csv_files_after_tests(database):
    assert not os.path.exists(EmployeeTable.FILE_PATH)
    assert not os.path.exists(DepartmentTable.FILE_PATH)
