typedef float t_vector<>;
struct datos{
    int menu;
    double valor_1;
    double valor_2;
    t_vector vector_1;
    t_vector vector_2;
    t_vector solucion;
    
};

program Caculadora{
    version V1{
        double calculadora (datos) = 1;
    } = 1;
} = 0x20000001;