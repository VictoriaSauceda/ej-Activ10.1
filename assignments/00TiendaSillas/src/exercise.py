def precio_antes_descuento(tipo_silla, cantidad) :
    # Agrega aquí el código de la funcion
    if tipo_silla == 'B':
        precio=700*cantidad
        return precio
    elif tipo_silla == 'E':
        precio=900*cantidad
        return precio
    else:
        precio=1500*cantidad
        return precio

def calcula_descuento(precio, tipo_cl):
    # Agrega aquí el código de la funcion
    if tipo_cl == 'F':
        desc=precio *.20
        return desc
    else:
        if 10000<=precio<20000:
            desc = precio *.10
            return desc
        elif precio >= 20000:
            desc = precio *.15
            return desc
        else:
            desc= 0
            return desc

def main() :
    # pido el tipo de silla (B E L)
    tipo_silla = input("Tipo silla: ")
    # pido el tipo de cliente (N F)
    tipo_cl = input("Tipo cliente: ")
    cantidad = int(input("Cantidad de sillas: "))

    totalsd = precio_antes_descuento(tipo_silla, cantidad)
    descuento = calcula_descuento(totalsd, tipo_cl)

    subtotal = float(totalsd)
    desc = float(descuento)
    total = float(totalsd-descuento)

    print(f"Total sin dcto.  ${subtotal:>7}")
    print(f"Descuento        ${desc:>7}")
    print(f"Total a pagar    ${total:>7}")


if __name__=='__main__':
    main()
