def func_one(execute_func):
    execute_func()


def func_execute():
    print("Ejecutando función")


func_one(func_execute)
