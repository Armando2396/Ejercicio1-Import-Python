import operaciones as o

def main():
    resSuma = o.suma(2, 2)
    resResta = o.resta(5, 3)
    resMulti = o.multiplicacion(5, 5)
    resDivi = o.division(5, 6)

    print("La suma es: ", resSuma)
    print("La resta es: ", resResta)
    print("La Multiplicacion es: ", resMulti)
    print("La Division es: ", resDivi)


if __name__ == '__main__':
    main()