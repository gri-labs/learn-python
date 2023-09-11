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
