import os
import sqlite3
import pytest


from nojazz.sqlite import connect_to_db


def test_context_manager(tmp_path):
    conn = sqlite3.connect(str(tmp_path) + "test.db")
    cursor = conn.cursor()
    cursor.execute("create table new_table (id integer)")
    cursor.execute("insert into new_table (id) values (1)")
    conn.commit()
    conn.close()

    with connect_to_db("test.db", db_dir=tmp_path) as cursor:
        cursor.execute("select * from new_table")
        result = cursor.fetchone()

    assert result == (1,)
