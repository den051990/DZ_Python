from sqlalchemy import create_engine
from sqlalchemy.sql import text


db_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"
db = create_engine(db_connection_string)


def test_db_connection():
	names = db.table_names()
	assert names[1] == 'app_users'

def test_select():
    db = create_engine(db_connection_string)
    rows = db.execute("SELECT * FROM company").fetchall()
    print(rows)
    row1 = rows[-1]

    assert row1["id"] == 1445
    assert row1["name"] == 'Company to be deactivated'

def test_select_1_row():
    db = create_engine(db_connection_string)
    sql_statement = text("select * from company where id = :com_id")

    rows = db.execute(sql_statement, com_id = 1445).fetchall()

    assert len(rows) == 1
    assert rows[0]["name"] == 'Company to be deactivated'

def test_select_1_row_with_two_filtres():
    db = create_engine(db_connection_string)
    sql_statement = text("select * from company where \"is_active\" = :is_active and id > :id")

    my_params ={
         'id': 1610,
         'is_active': True
    }

    rows = db.execute(sql_statement, my_params ).fetchall()

    assert len(rows) == 2
    assert rows[0]["name"] == 'SQL School 2020'

def test_insert():
    db = create_engine(db_connection_string)
    sql = text("insert into company(\"name\") values (:new_name)")
    rows = db.execute(sql, new_name = 'SQL School 2021')

def test_update():
    db = create_engine(db_connection_string)
    sql = text("update company set description = :descr where id = :id")

    db.execute(sql, descr = 'new_descr', id = 790)

def test_delete():
    db = create_engine(db_connection_string)
    sql = text("delete from company where id =:id")
    db.execute(sql, id = 677 )