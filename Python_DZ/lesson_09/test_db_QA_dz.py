from sqlalchemy.sql import text
from Python_DZ.lesson_09.db_QA_dz import DatabaseQA


db = DatabaseQA("postgresql://postgres:password@localhost:5432/QA_DZ")


def test_add_subject():
    body = db.get_subjects()
    len_before = len(body)

    subject_id = 222
    subject_title = "testing"
    result = db.create(subject_id, subject_title)

    body = db.get_subjects()
    len_after = len(body)

    db.delete(subject_id)

    assert len_after - len_before == 1

    found = False
    for company in body:
        if company["subject_id"] == subject_id:
            found = True
            assert company["subject_title"] == "testing"
            break
    
    assert found

def test_update_subject():
    subject_id = 222
    subject_title = "testing"
    db.create(subject_id, subject_title)

    new_title = "QAtesting"
    db.update(new_title, subject_id)
    edited = db.get_subjects_by_id(subject_id)
    db.delete(subject_id)

    assert edited["subject_title"] == new_title

def test_delete():
    subject_id = 222
    subject_title = "testing"
    db.create(subject_id, subject_title)

    body = db.get_subjects()
    len_before = len(body)

    deleted = db.delete(subject_id)

    body = db.get_subjects()
    len_after = len(body)
    assert len_before - len_after == 1
