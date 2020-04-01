service Calculadora{
    void ping(),
    double suma(1:double num1, 2:double num2),
    double resta(1:double num1, 2:double num2),
    double multiplicacion(1:double num1, 2:double num2),
    double division(1:double num1, 2:double num2),
    i32 modulo(1:i32 num1, 2:i32 num2),
    double potencia(1:double num1, 2:i32 num2),
    i32 logaritmo(1:i32 num1, 2:i32 num2),
    list<i32> suma_de_vectores(1:list<i32> num1, 2:list<i32> num2),
    list<i32> resta_de_vectores(1:list<i32> num1, 2:list<i32> num2),
    list<i32> producto_escalar(1:i32 num1, 2:list<i32> num2),
    list<i32> producto_vectorial(1:list<i32> num1, 2:list<i32> num2),
    list<list<i32>> suma_de_matrices(1:list<list<i32>> num1, 2:list<list<i32>> num2),
    list<list<i32>> resta_de_matrices(1:list<list<i32>> num1, 2:list<list<i32>> num2),
    list<list<i32>> multiplicacion_de_matrices (1: list<list<i32>> num1, 2:list<list<i32>> num2),

}