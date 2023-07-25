import bcrypt


class Service:
    def __init__(self, repository):
        self.repository = repository

    def get_temporally_password(self, id):
        student = self.repository.get_student_by_id(id)

        if student is None:
            return None

        student.password = generate_password_hash("123456")

        return student

    def get_random_sub_name(self, id):
        student = self.repository.get_student_by_id(id)

        if student is None:
            return None

        student.nombre = student.nombre[0:3]

        return student

    def get_student_by_id(self, id):
        return self.repository.get_student_by_id(id)

    def add_student(self, student_entity):
        return self.repository.add_student(student_entity)

    def delete_student_by_id(self, id):
        return self.repository.delete_student_by_id(id)

    def update_student(self, student_entity):
        return self.repository.update_user(student_entity)


def generate_password_hash(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
