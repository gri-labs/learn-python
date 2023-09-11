from pattern.student.domain.model import StudentDTORepositoryService


class StudentService:
    def __init__(self, repository):
        self.repository = repository

    def get_student_by_id(self, student_id):
        if id is None:
            raise ValueError("id is required")

        student_model = StudentDTORepositoryService()

        student_model.id = id

        result = self.repository.get_student_by_id(student_model, student_id)

        if result is None:
            raise ValueError("User not found")

        return result

    def add_student(self, student):
        if student is None:
            raise ValueError("student is required")

        student_model = StudentDTORepositoryService()

        student_model.name = student.name
        student_model.last_name = student.last_name
        student_model.age = student.age
        student_model.dni = student.dni

        return self.repository.add_student(student)
