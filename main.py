import sys

f_a = []
f_b = []
f_c = []
vector_inicial = []
dic_funcs = {
    "1" : f_a,
    "2" : f_b,
    "3" : f_c
}
N = 3

print("Ingrese el numero de interaciones que quiere realizar ")
N = int(input("n : ").strip())



print("Ingrese los valores x, y, z para el vector inicial. los valores deben estar separados por un espacio")
vars_ = input("").strip()
vector_inicial = [float(x) for x in vars_.split(" ") if x != ""][:3]
print("Vector inicial : ({}, {}, {})".format(*vector_inicial))
print("")

print("ingrese los datos para x, y, z y la constante separados por espacios:  ")
print("Ejemplo : 12 -32 4 329")
for i in range(1,4):
    print(f"Ingresando la ecuacion {i} format [x,y,z]")
    vars_ = input("").strip()
    vars_ = [float(x) for x in vars_.split(" ") if x != ""][:4]
    #print(vars_)
    dic_funcs[str(i)] = vars_


# validando linea dominante
validate_domain = lambda list_vars: bool(list_vars[0] > list_vars[1] and list_vars[0] > list_vars[2]) 
def organize_vars(key, vars):
    if key == 1:
        x,y,z,c = vars
        return [x,y,z]
    elif key == 2:
        x,y,z,c = vars
        return [y,x,z]
    elif key == 3:
        x,y,z,c = vars
        return [z,y,x]

def validate():
    for key in dic_funcs:
        x,y,z,c = dic_funcs[key]
        dominante_flag = validate_domain(organize_vars(int(key), dic_funcs[key]))
        if not dominante_flag:
            print(f"{x}x {y}y {z}z = {c} ::: ERROR , rompe la condicion de diagonal dominante")    
            sys.exit(1)
#############################

validate()

print("Funciones")
for key in dic_funcs:
    x,y,z,c = dic_funcs[key]
    print(f"{x}x {y}y {z}z = {c}")


def funcion_transf(key, values_init, values_aux):
    x,y,z,c = values_init
    x_aux, y_aux,z_aux = values_aux
    if key == 1:
        #print("para x_aux ")
        #print(f"({c} + ({y}*{y_aux}*-1) + ({z}*{z_aux}*-1))/{x}")
        #print("resultado: {}".format((c + (y*y_aux*-1) + (z*z_aux*-1))/x))
        return (c + (y*y_aux*-1) + (z*z_aux*-1))/x
    if key == 2:
        #print("para y_aux ")
        #print(f"({c} + ({x}*{x_aux}*-1) + ({z}*{z_aux}*-1))/{y}")
        #print("resultado: {}".format((c + (x*x_aux*-1) + (z*z_aux*-1))/y))
        return (c + (x*x_aux*-1) + (z*z_aux*-1))/y
    if key == 3:
        #print("para z_aux ")
        #print(f"{c} + ({y}*{y_aux}*-1) + ({x}*{x_aux}*-1))/{z}")
        #print("resultado: {}".format((c + (y*y_aux*-1) + (x*x_aux*-1))/z))
        return (c + (y*y_aux*-1) + (x*x_aux*-1))/z
    
    
######## 
# Iteraciones
def process():
    values = []
    values.append(vector_inicial)
    x_aux,y_aux, z_aux = vector_inicial
    for i in range(N):
        x_aux = float("{:.6}".format(funcion_transf(1, dic_funcs["1"], [x_aux, y_aux, z_aux])))
        y_aux = float("{:.6}".format(funcion_transf(2, dic_funcs["2"], [x_aux, y_aux, z_aux])))
        z_aux = float("{:.6}".format(funcion_transf(3, dic_funcs["3"], [x_aux, y_aux, z_aux])))
        #print([x_aux, y_aux,z_aux])
        values.append([x_aux, y_aux,z_aux])
    print("Valores finales:")
    print("x    y   z")
    for v in values:
        print("{}   {}  {}".format(*v))
        
process()