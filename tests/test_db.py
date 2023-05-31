import pytest
import sqlite3

@pytest.fixture
def db():
    with sqlite3.connect("my_test.db") as db:
        yield db

@pytest.fixture
def transaction(db):
    cursor = db.cursor()
    try:
        yield cursor
        db.commit()
    except:
        db.rollback()

def test_a(db):
    print(db)

def test_b(transaction):
    transaction.execute("INSERT INTO tb1(name) VALUES ('John')")
    # raise RuntimeError("Error text")
    transaction.execute("INSERT INTO tb1(name) VALUES ('Mary')")

"""def test_c(db):
    cursor = db.cursor()
    sqlite_select_query = "select sqlite_version();"
    cursor.execute(sqlite_select_query)
    record = cursor.fetchall()
    print("Версия базы данных SQLite: ", record)
    cursor.close()"""