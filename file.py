def file_init():
    global branch, documentos, SCP, personal
    SCP = ["SCP-028", "SCP-096", "SCP-049", "SCP-173", "SCP-035"] 
    documentos = ["A-002", "A-828", "A-627"]
    personal = ["P-819", "P-802"]
    branch = "main"
    return branch, SCP, documentos, personal

def interpeter(sign):
    global branch
    if sign == "back":
        if "/" in branch:
            while True:
                branch = branch[:-1]
                if branch[-1] == "/":
                    branch = branch[:-1]
                    break
            open_files(branch)
    elif sign == "exit":
        exit()
    elif sign == "1":
        if branch == "main":
            branch = "main/SCP"
            open_files("main/SCP")
        else:
            print("[Error]: Commando no reconocido")
            open_files(branch)
    elif sign == "2":
        if branch == "main":
            branch = "main/documentos"
            open_files("main/documentos")
        else:
            print("[Error]: Commando no reconocido")
            open_files(branch)
    elif sign == "3":
        if branch == "main":
            branch = "main/personal"
            open_files("main/personal")
        else:
            print("[Error]: Commando no reconocido")
            open_files(branch)
    elif sign == "SCP-096":
        if branch == "main/SCP":
            branch = "main/SCP/SCP-096"
            open_files("main/SCP/SCP-096")
        else:
            print("[Error]: Commando no reconocido")
            open_files(branch)
    elif sign == "SCP-028":
        if branch == "main/SCP":
            branch = "main/SCP/SCP-028"
            open_files("main/SCP/SCP-028")
        else:
            print("[Error]: Commando no reconocido")
            open_files(branch)
    elif sign == "SCP-049":
        if branch == "main/SCP":
            branch = "main/SCP/SCP-049"
            open_files("main/SCP/SCP-049")
        else:
            print("[Error]: Commando no reconocido")
            open_files(branch)
    elif sign == "SCP-173":
        if branch == "main/SCP":
            branch = "main/SCP/SCP-173"
            open_files("main/SCP/SCP-173")
        else:
            print("[Error]: Commando no reconocido")
            open_files(branch)
    elif sign == "SCP-035":
        if branch == "main/SCP":
            branch = "main/SCP/SCP-035"
            open_files("main/SCP/SCP-035")
        else:
            print("[Error]: Commando no reconocido")
            open_files(branch)
    elif sign == "A-002":
        if branch == "main/documentos":
            branch = "main/documentos/A-002"
            open_files("main/documentos/A-002")
        else:
            print("[Error]: Commando no reconocido")
            open_files(branch)
    elif sign == "A-828":
        if branch == "main/documentos":
            branch = "main/documentos/A-828"
            open_files("main/documentos/A-828")
        else:
            print("[Error]: Commando no reconocido")
            open_files(branch)
    elif sign == "A-627":
        if branch == "main/documentos":
            branch = "main/documentos/A-627"
            open_files("main/documentos/A-627")
        else:
            print("[Error]: Commando no reconocido")
            open_files(branch)
    elif sign == "P-819":
        if branch == "main/personal":
            branch = "main/personal/P-819"
            open_files("main/personal/P-819")
        else:
            print("[Error]: Commando no reconocido")
            open_files(branch)
    elif sign == "P-802":
        if branch == "main/personal":
            branch = "main/personal/P-802"
            open_files("main/personal/P-802")
        else:
            print("[Error]: Commando no reconocido")
            open_files(branch)
    else:
            print("[Error]: Commando no reconocido")
            open_files(branch)

def open_files(user):
    global branch, SCP, documentos, personal
    print(" ")
    if user == "main":
        print("1.- SCP y entidades anomalas")
        print("2.- Documentos clasificados")
        print("3.- Personal de la Fundacion")
        res = input(user + "> ")
        interpeter(res)
    elif user == "main/SCP":
        for x in SCP:
            print(x)
        branch = user
        res = input(user + "> ")
        interpeter(res)
    elif user == "main/documentos":
        for x in documentos:
            print(x)
        branch = user
        res = input(user + "> ")
        interpeter(res)
    elif user == "main/personal":
        for x in personal:
            print(x)
        branch = user
        res = input(user + "> ")
        interpeter(res)
    elif user == "main/SCP/SCP-096":
        print("[SCP-096]: El chico timido")
        print("Clase: Keter. Peligro: Fisico extremo")
        print("Ataca al ver su rostro, ya sea en fotos o en prescencial,")
        print("Destruye todo a su paso, nada lo detiene...")
        print("Escriba <back> para volver")
        res = input(user + "> ")
        interpeter(res)
    elif user == "main/SCP/SCP-049":
        print("[SCP-049]: El medico de la plaga")
        print("Clase: Euclid. Peligro: Fisico y Biologico")
        print("Esta fascinado por la pestiliencia, y cree que el es la cura a eso...")
        print("Todo al que cure, lo vuelve un zombi")
        print("Escriba <back> para volver")
        res = input(user + "> ")
        interpeter(res)
    elif user == "main/SCP/SCP-028":
        print("[SCP-028]: Sala de conocimiento instantaneo")
        print("Clase: Euclid. Peligro: Cognitivo")
        print("Apenas entres en el area de SCP-028, obtendras una informacion al azar")
        print("La informacion puede ser util, inutil o perturbadora.")
        print("Escriba <back> para volver")
        res = input(user + "> ")
        interpeter(res)
    elif user == "main/SCP/SCP-173":
        print("[SCP-173]: La escultura")
        print("Clase: Eucid. Peligro: Fisico")
        print("Escultura de arcilla y barro que se mueve a gran velocidad a")
        print("La perdida de contacto visual... este puede [REDACTADO] y romper")
        print("El cuello de sus victimas de manera instantanea")
        print("Escriba <back> para volver")
        res = input(user + "> ")
        interpeter(res)
    elif user == "main/SCP/SCP-035":
        print("[SCP-035]: La mascara possesiva")
        print("Clase: Eucid. Peligro: Cognitivo, Psicologico y Corruptor")
        print("Mascara de procelana que cambia de cara constantemente...")
        print("Hipnotiza a las personas para colocarse la mascara")
        print("Y luego las posee y las convierte en su marioneta...")
        print("Escriba <back> para volver")
        res = input(user + "> ")
        interpeter(res)
    elif user == "main/documentos/A-002":
        print("[A-002]: Informe de anomalía dimensional")
        print("Ubicación: Sitio-19, sector de pruebas")
        print("Descripción: Brecha temporal detectada durante experimento con SCP-███")
        print("Resultado: 3 sujetos perdidos en línea temporal desconocida")
        print("Estado: Investigación suspendida por riesgo de colapso espacio-tiempo")
        res = input(user + "> ")
        interpeter(res)
    elif user == "main/documentos/A-627":
        print("[A-627]: Evaluación psicológica del Dr. █████")
        print("Motivo: Comportamiento errático tras exposición prolongada a SCP-035")
        print("Hallazgos: Tendencias suicidas, pérdida de identidad, lenguaje arcaico")
        print("Recomendación: Separación inmediata del proyecto y contención médica")
        print("Estado: Personal reubicado, caso bajo revisión ética")
        res = input(user + "> ")
        interpeter(res)
    elif user == "main/documentos/A-828":
        print("[A-828]: Registro de comunicación interceptada")
        print("Origen: Transmisión no autorizada desde coordenadas fuera del planeta")
        print("Contenido: Mensaje cifrado con patrones no humanos")
        print("Acción: SCP-079 activado para decodificación parcial")
        print("Estado: Clasificado nivel 4, acceso restringido")
        res = input(user + "> ")
        interpeter(res)
    elif user == "main/personal/P-819":
        print("[P-819]: Samuel █████████")
        print("Origen: ███ ██ █ █████ ██████ ██ ████ █")
        print("Trabajo: Miembro del equipo de videovigilancia conocido como Sep-29")
        print("Rango: Acceso de nivel 2, interno █████")
        print("Estado: Trabajando en Sep-29 junto a ███████ ██ ███")
        res = input(user + "> ")
        interpeter(res)
    elif user == "main/personal/P-802":
        print("[P-802]: ████ Rose")
        print("Origen: anteriormente Clase D , luego del ███ ██████ ███ ██ paso a ser un interno")
        print("Trabajo: Guardia de Seguridad del sitio-84")
        print("Rango: Acceso nivel 2, interno menor")
        print("Estado: Lesionado por █████ ███ ██ █ █████ █")
        res = input(user + "> ")
        interpeter(res)
    else:
        print("[Error]: Archivo no encontrado")
        res = input(user + "> ")
        interpeter(res)