from sqlalchemy import create_engine
from sqlalchemy.sql import text


class DatabaseQA:
    __scripts = {
            "select": text("SELECT * FROM subject"),
            "delete by id": text(
                 "DELETE FROM subject WHERE subject_id =:id_to_delete"),
            "insert new": text(
                "INSERT INTO subject"
                "(\"subject_id\", \"subject_title\") "
                "values (:new_id, :new_title)"),
            "select by id": text(
                "SELECT * FROM subject WHERE subject_id = :select_id"),
            "update by title": text(
                "update subject set subject_title = :descr"
                " where subject_id = :id"),
            "select by subject title": text(
                "SELECT * FROM subject WHERE subject_title = :descr")
    }
 
    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get_subjects(self):
        return self.__db.execute(self.__scripts["select"]).fetchall()

    def create(self, subject_id, subject_title):
        self.__db.execute(
            self.__scripts["insert new"], new_id= subject_id,
            new_title= subject_title)

    def update(self, new_title, subject_id):
        self.__db.execute(
            self.__scripts["update by title"], 
            {"id": subject_id, "descr": new_title})

    def delete(self, subject_id):
            self.__db.execute(self.__scripts["delete by id"],
                            id_to_delete= subject_id )

    def get_subjects_by_id(self, subject_id):
        return self.__db.execute(
             self.__scripts["select by id"], select_id= subject_id).fetchone()

    def get_subjects_by_subject_title(self, subject_title):
        return self.__db.execute(
             self.__scripts["select by subject title"], 
            descr = subject_title).fetchone()