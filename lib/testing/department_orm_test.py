import pytest
from lib.department import Department

def test_department_orm():
    Department.drop_table()
    Department.create_table()

    department = Department("Test", "Location")
    department.save()

    assert department.id is not None

    department.location = "New Location"
    department.update()

    updated_department = Department.create("Updated Test", "New Location")
    assert updated_department.id is not None

    updated_department.delete()
    assert updated_department.id is None
