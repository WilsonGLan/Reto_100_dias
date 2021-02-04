import menu_01 as opc

def encontrar_mcm(m,n):
    m_max=m
    n_max=n
    mcm = 0
    while m_max != n_max:
        if n_max < m_max:
            n_max += n
        elif m_max < n_max:
            m_max += m
    if m_max == n_max:
        mcm = m_max
    return mcm

def encontrar_mcd(m,n):
    mcm = encontrar_mcm(m,n)
    mcd = m/(mcm/n)
    return mcd

print(opc.menu)

opcion = int(input("Que opción del menú de operaciones selecciona:\t"))
if opcion in [1,2]:
    numero_uno = int(input("Ingrese el primer número\t"))    
    numero_dos = int(input("Ingrese el segundo número\t"))
    
    if opcion == 1:     
        m_c_m = encontrar_mcm(numero_uno,numero_dos)
        print(f"El m.c.m. de {numero_uno} y {numero_dos} es {m_c_m}")
    elif opcion == 2:
        m_c_d = encontrar_mcd(numero_uno,numero_dos)        
        print(f"El m.c.d. de {numero_uno} y {numero_dos} es {int(m_c_d)}")
else:
    print("error")

