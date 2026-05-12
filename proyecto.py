# ══════════════════════════════════════════════════════════════
# proyecto.py · Ficha 3236582 · SENA CTM Itagüí
# Completá con los datos reales de tu proyecto
# ══════════════════════════════════════════════════════════════

nombre_proyecto = "VIKAM"           # nombre de tu proyecto
descripcion     = "App multiplataforma sobre habitos saludables"           # qué problema resuelve
tecnologias     = ["Html","Python","PostgresSQL"]           # ["HTML", "Python", "MySQL"]
integrantes     = ["Miguel Reyes","Miguel Arenas","Samuel Lopez"]           # ["Nombre 1", "Nombre 2"]
funcionalidades = ["Login","Login","CRUD","Gamificacion"]           # ["Login", "Registro", "Reportes"]


def mostrar_info():
    print(f"Proyecto:      {nombre_proyecto}")
    print(f"Descripción:   {descripcion}")
    print(f"Equipo:        {', '.join(integrantes)}")
    print(f"Tecnologías:   {', '.join(tecnologias)}")
    print(f"Funcionalidades:")
    for f in funcionalidades:
        print(f"  - {f}")


mostrar_info()