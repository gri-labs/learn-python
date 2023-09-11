from pattern.student.domain.model import StudentDTORepositoryService
class StudentService:
    def __init__(self, repository):
        self.repository = repository

    def get_student_by_id(self, id):
        if id is None:
            raise ValueError("id is required")

        student_model = StudentDTORepositoryService()

        student_model.id = id

        student = self.repository.get_student_by_id(student_model, id)

        if student is None:
            print("student not found")
            raise ValueError("student not found")

        return student
