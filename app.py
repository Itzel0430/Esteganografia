import subprocess  #1
import os          #2

def detect_steganography(image_path, contra): #3
    cmdStegInfo = ['steghide', 'info', '-p', contra, image_path] #4
    result = subprocess.run(cmdStegInfo, capture_output=True, text=True) #5

    if result.returncode == 0: #6
        return result.stdout   #7
    else:  #8
        return f'Error: {result.stderr}' #8

def remove_steganography(image_path):  #9 
    result = subprocess.run(['convert', image_path, image_path], capture_output=True, text=True)  #10
    if result.returncode == 0:  #11
        print(f"Datos ocultos eliminados de {image_path}") #12
    else: #13
        print(f"Error al eliminar datos ocultos de {image_path}: {result.stderr}") #13

def check_if_clean(image_path, contra): #14
    result = detect_steganography(image_path, contra) #15
    if 'could not find any file with matching' in result.lower(): #16
        print("La imagen está limpia. No tiene contenido oculto.") #17
    else: #18
        print("La imagen tiene contenido oculto.") #18

def main(): #19
    while True: #20
        print("\nMenú de Esteganografía") #21
        print("1. Detectar Esteganografía") #22
        print("2. Eliminar Esteganografía") #23
        print("3. Corroborar que está limpia") #24 
        print("4. Salir") #25
        
        choice = input("Seleccione una opción: ") #26
        
        if choice == '1': #27
            image_path = input("Ingrese la ruta de la imagen: ") #28
            contra = input("Ingrese la contraseña: ") #29
            resultado = detect_steganography(image_path, contra) #30
            print(resultado) #31
        
        elif choice == '2': #32
            image_path = input("Ingrese la ruta de la imagen: ") #33
            if os.path.isfile(image_path): #34
                contra = input("Ingrese la contraseña: ") #35
                if 'could not find any file with matching' not in detect_steganography(image_path, contra).lower(): #36
                    remove_steganography(image_path) #37
                else: #38
                    print("No se ha detectado esteganografía en la imagen.") #38
            else:  #39
                print("La ruta de la imagen proporcionada no es válida.") #39
        
        elif choice == '3': #40
            image_path = input("Ingrese la ruta de la imagen: ") #41
            if os.path.isfile(image_path): #42
                contra = input("Ingrese la contraseña: ") #43
                check_if_clean(image_path, contra) #44
            else: #45
                print("La ruta de la imagen proporcionada no es válida.") #45
        
        elif choice == '4':  #46
            print("Saliendo...") #47
            break #48
         
        else: #49
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.") #49
 
if __name__ == "__main__": #50
    main() #51