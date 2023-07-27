class Service:
    def __init__(self, repository):
        self.repository = repository

    def get_student_by_id(self, id):
        if id is None:
            raise ValueError("id is required")

        student_entity = self.repository.get_student_by_id(id)

        if student_entity is None:
            raise ValueError("student not found")

        return student_entity

    def get_student_by_name(self, name):
        if name is None:
            raise ValueError("name is required")

        student_entity = self.repository.get_student_by_filter(filter_by={'nombre': name})

        if student_entity is None:
            raise ValueError("student not found")

        return student_entity

    def add_student(self, student_entity):
        return self.repository.add_student(student_entity)

    def delete_student_by_id(self, id):
        return self.repository.delete_student_by_id(id)

    def update_student(self, student_entity):
        return self.repository.update_user(student_entity)
