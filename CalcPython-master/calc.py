from Parser import (
    Parser,
    ParserError,
    ProgrammerError
)

def main():
    print("Please, enter the mathematical expression containing floating point numbers, operations +, -, *, /, %% or ():")
    expr = input("> ")

    parser = Parser(expr)

    try:
        expr = parser.parse()
        print(expr.calculate())
    except ParserError as pe:
        print(f"Parser error: {pe}")
    except ZeroDivisionError as zde:
        print(f"Calculation error: {zde}")
    except ProgrammerError as pre:
        print(f"Programmer error: {pre}")
    except: # pylint: disable=bare-except
        print("Unknown error")

    input("Press <Enter> key to exit...")

if __name__ == "__main__":
    main()
