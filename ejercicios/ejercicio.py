Diccionario={
    "Mijail":58,
    "Alice":99,
    "Juan":2,
    "Brian":72,
    "Ramon":42,
    "Kevin":79
}

def impar(a):
    if(a%2!=0):
        return a

def cursos(c):
    return c.upper()

num = {1,2,3,4,5,6,7,8,9,0}
numimp = list(map(impar,num))

lista = {'Mijail','Alice','Kevin'}
ListaGrade = list(map(cursos,lista))

print(numimp)
print(ListaGrade)