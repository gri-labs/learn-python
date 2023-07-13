import mysql.connector


class SQLRepository:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        cursor = self.db.cursor()
        query = "SELECT * FROM movies"
        cursor.execute(query)
        row = cursor.fetchall()
        return row

    def get_by_id(self, id):
        # TODO implementar
        pass


if __name__ == '__main__':
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='gri',
        port=int(3307)
    )

    repository = SQLRepository(db)

    movies_data = repository.get_all()

    for movie in movies_data:
        print(movie)
