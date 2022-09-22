def main():
    def prueba():
        f=open('nuevofichero.txt','w')
        f.write('Hola, esto es una prueba de creación y escritura en un fichero desde Python.\n')
        f.close()

    def actualizar():
        f=open('nuevofichero.txt', 'a')
        f.write('Aqui hemos actualizado el fichero')
        f.close()

    prueba()
    actualizar()

if __name__=="__main__":
    main()