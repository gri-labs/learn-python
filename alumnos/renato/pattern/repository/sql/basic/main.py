from connector_database import ConnectorDatabase
from repository import Repository
from print_data import PrintData

if __name__ == '__main__':
    # TODO: Instancia el repositorio con el conector y tu classe para printar datos
    conn = ConnectorDatabase(
        host='localhost',
        user='root',
        password='root',
        database='students',
        port='3307'

    )
    repoStudents = Repository(conn)
    printData = PrintData()

    repoStudents.insert_student("Renato", "renato@gmail.com", "Acc", 32)
    printData.print_data(repoStudents.get_student_by_id(1))

    printData.print_data(repoStudents.get_students())

    repoStudents.update_student(1, "Merlin")
    printData.print_data(repoStudents.get_student_by_id(1))

    repoStudents.delete_student(1)
    printData.print_data(repoStudents.get_students())
