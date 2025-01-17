/*
 * This is sample code generated by rpcgen.
 * These are only templates and you can use them
 * as a guideline for developing your own functions.
 */

#include "calculadora.h"
#include <math.h>

double* producto_escalar(t_vector vector1, t_vector vector2){
	static double resultado = 0;
	for (int i=0; i<vector1.t_vector_len; i++){
		resultado += vector1.t_vector_val[i] * vector2.t_vector_val[i];
	}

	return &resultado;
}
void suma_vectores(t_vector vector1, t_vector vector2, t_vector solucion){

	for (int i=0; i< vector2.t_vector_len; i++){
		solucion.t_vector_val[i] = vector1.t_vector_val[i] + vector2.t_vector_val[i];

	}
	
}

double *
calculadora_1_svc(datos arg1,  struct svc_req *rqstp)
{
	static double  result;
	switch(arg1.menu){
		case 1:
				result = arg1.valor_1 + arg1.valor_2;
				break;
		case 2: 
				result = arg1.valor_1 - arg1.valor_2;
				break;
	 	case 3: 
		 		result = arg1.valor_1 * arg1.valor_2;
				break;
		case 4: 
				result = arg1.valor_1 / arg1.valor_2;
				break;
		case 5:
				result = (int)arg1.valor_1 % (int)arg1.valor_2;
				break;
		case 6: 
				result = pow((double)arg1.valor_1,(double)arg1.valor_2);
				break;
		case 7:
				result = log((double)arg1.valor_1)/log((double)arg1.valor_2);
				break;
		case 8: 
				result = *producto_escalar(arg1.vector_1,arg1.vector_2);
				break;
		// LA SUMA DE VECTORES NO FUNCIONA 
		case 9: 
				result = 1;
				suma_vectores(arg1.vector_1,arg1.vector_2,arg1.solucion);
				break;
		default:
				printf("ERROR al seleccionar la operacio");
				break;
	}


	return &result;
}
