class Service:
    def __init__(self, repository):
        self.repository = repository

    def get_student_by_id(self, id):
        # TODO: Validamos la entrada y salida de datos

        return ""

    def add_student(self, student_entity):
        return self.repository.add_student(student_entity)

    def delete_student_by_id(self, id):
        return self.repository.delete_student_by_id(id)

    def update_student(self, student_entity):
        return self.repository.update_user(student_entity)
