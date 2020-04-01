from calculadora import Calculadora 

from thrift import Thrift 
from thrift.transport import TSocket
from thrift.transport import TTransport 
from thrift.protocol import TBinaryProtocol

transport = TSocket.TSocket('localhost', 9090)
transport = TTransport.TBufferedTransport(transport)
protocol = TBinaryProtocol.TBinaryProtocol(transport)

client = Calculadora.Client(protocol)

transport.open()

print("Hacemos ping al server")
client.ping()

resultado = client.suma(1,1)
print("1+1="+str(resultado))
resultado = client.resta(1,1)
print("1-1="+str(resultado))
resultado = client.multiplicacion(2,1)
print("2*1="+str(resultado))
resultado = client.division(4,2)
print("4/2="+str(resultado))
resultado = client.modulo(5,2)
print("5%2="+str(resultado))
resultado = client.potencia(4,2)
print("4^2="+str(resultado))
resultado = client.logaritmo(16,2)
print("log(2)16="+str(resultado))
resultado = client.suma_de_vectores([2,3,5,1],[1,2,3,4])
print("Suma de [2,3,5,1]+[1,2,3,4]="+str(resultado))
resultado = client.resta_de_vectores([2,3,5,1],[1,2,3,4])
print("Resta de [2,3,5,1]-[1,2,3,4]="+str(resultado))
resultado = client.producto_escalar(7,[1,2,3,4])
print("Producto escalar de 7 * [1,2,3,4]="+str(resultado))
resultado = client.producto_vectorial([2,3,5,1],[1,2,3,4])
print("Producto vectorial [2,3,5,1]*[1,2,3,4]="+str(resultado))
resultado = client.suma_de_matrices([[7,7,7],[7,7,7],[7,7,7]],[[7,7,7],[7,7,7],[7,7,7]])
print("Suma de [7,7,7],[7,7,7],[7,7,7]+[7,7,7],[7,7,7],[7,7,7]="+str(resultado))
resultado = client.resta_de_matrices([[17,17,17],[17,17,17],[17,17,17]],[[7,7,7],[7,7,7],[7,7,7]])
print("Resta de [17,17,17],[17,17,17],[17,17,17]-[7,7,7],[7,7,7],[7,7,7]="+str(resultado))
resultado = client.multiplicacion_de_matrices([[7,7,7],[7,7,7],[7,7,7]],[[7,7,7],[7,7,7],[7,7,7]])
print("Multiplicacion de [7,7,7],[7,7,7],[7,7,7]+[7,7,7],[7,7,7],[7,7,7]="+str(resultado))


transport.close()