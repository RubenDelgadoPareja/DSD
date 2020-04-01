import glob 
import sys 
import math


from calculadora import Calculadora 

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer



import logging
logging.basicConfig(level=logging.DEBUG)

class CalculadoraHandler:
    def __init__(self):
        self.log = {}

    def ping(self):
        print('Me han hecho ping()')

    def suma(self, n1, n2):
        print('sumando '+str(n1)+ " con "+str(n2))
        return n1 + n2

    def resta(self, n1, n2):
        print('restando '+str(n1)+ " con "+str(n2))
        return n1 - n2

    def multiplicacion(self, n1, n2):
        print('multiplicando '+str(n1)+ " por "+str(n2))
        return n1 * n2
    
    def division(self, n1, n2):
        print('dividiendo '+str(n1)+ " entre "+str(n2))
        return n1 / n2

    def modulo(self, n1, n2):
        print('haciendo ' +str(n1)+ " modulo "+ str(n2))
        return n1%n2

    def potencia(self, n1, n2):
        print('elevando '+str(n1)+ " a "+str(n2))
        return n1**n2

    def logaritmo(self, n1, n2):
        print('haciendo el logaritmo de ' +str(n1)+ " en base "+ str(n2))
        return math.log(n1)/math.log(n2)

    def suma_de_vectores(self, n1, n2):
        resultado = []
        print('sumando el vector ' +str(n1)+ " a " +str(n2))
        for i in range(0,len(n1)):
            resultado.append(n1[i] + n2[i])
        return resultado

    def resta_de_vectores(self, n1, n2):
        resultado = []
        print('restando el vector ' +str(n1)+ " a " +str(n2))
        for i in range(0,len(n1)):
            resultado.append(n1[i] - n2[i])
        return resultado

    def producto_escalar(self, n1, n2):
        resultado = []
        print('haciendo el producto escalar del escalar '+str(n1)+" por el vector "+str(n2))
        for i in range(0,len(n2)):
            resultado.append(n1 * n2[i])
        return resultado

    def producto_vectorial(self, n1, n2):
        resultado = []
        print('haciendo el producto vectorial del vector '+str(n1)+" y el vector "+str(n2))
        for i in range(0,len(n1)):
            resultado.append(n1[i] * n2[i])
        return resultado

    def suma_de_matrices(self, n1, n2):
        resultado = [[0,0,0],[0,0,0],[0,0,0]]
        print('sumando la matriz'+str(n1)+" y la matriz "+str(n2))
        for i in range(len(n1)):
            for j in range(len(n1[0])):
                resultado[i][j] = n1[i][j] + n2[i][j]

        return resultado


    def resta_de_matrices(self, n1, n2):
        resultado = [[0,0,0],[0,0,0],[0,0,0]]
        print('restando la matriz'+str(n1)+" y la matriz "+str(n2))
        for i in range(len(n1)):
            for j in range(len(n1[0])):
                resultado[i][j] = n1[i][j] - n2[i][j]

        return resultado
    
    def multiplicacion_de_matrices(self, n1, n2):
            resultado = [[0,0,0],[0,0,0],[0,0,0]]
            print('multiplicando la matriz'+str(n1)+" y la matriz "+str(n2))
            for i in range(len(n1)):
                for j in range(len(n2[0])):
                    for k in range(len(n2)):
                        resultado[i][j] += n1[i][k] * n2[k][j]

            return resultado



    



if __name__ == '__main__':
    handler = CalculadoraHandler()
    processor = Calculadora.Processor(handler)
    transport = TSocket.TServerSocket(host='127.0.0.1', port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    print('Iniciando servidor...')
    server.serve()
    print('done.')


