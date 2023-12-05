from ex1 import validator
import ex2.Operations.calculate as calc
from ex3.merge import merge
import ex4.generator.password_generator as gen


def ex1():
    print("--EX 1--")
    file_path = "stores.csv"
    file_path2 = "stores_fara.csv"
    data_types1 = {
        "Magazin": str,
        "Produs": str,
        "Cantitate": int,
    }
    data_types2 = {
        "Magazin": int,
        "Produs": str,
        "Cantitate": int,
    }
    errors1 = validator.run_validation(file_path, data_types1)
    errors2 = validator.run_validation(file_path2, data_types2)
    print("Errors:")
    print(errors1)
    print("Errors2:")
    print(errors2)


def ex2():
    print("--EX 2--")
    print("Add: ", calc.add(1, 2))
    print("Substract: ", calc.substract(4.5, 6.7))
    print("Multiply: ", calc.multiply(1.7, 0.2))
    print("Divide: ", calc.divide(6776, 25.75))


def ex3():
    print("--EX 3--")
    files = ["a.txt", "b.txt", "stores.csv"]
    output_file = "output.csv"
    separators = ['!!!!!!!!!!!!!!!!!!!!!!', '??????????????????????']
    merge.merge_files(files, output_file, separators)


def ex4():
    print("--EX 4--")
    pass1 = gen.password_generator(10, True, True, True)
    pass2 = gen.password_generator(15, False, True, False)
    pass3 = gen.password_generator(20, False, False, False)
    pass4 = gen.password_generator(4, True, True, True)
    print("Password 1: ", pass1)
    print("Password 2: ", pass2)
    print("Password 3: ", pass3)
    print("Password 4: ", pass4)


if __name__ == "__main__":
    ex1()
    ex2()
    ex3()
    ex4()
