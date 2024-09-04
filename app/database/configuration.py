# datos para la conexion a BD
#variables de 
dataBaseName = "gestordb"
userName = "root"
userPassword = ""
connectionPort = 3306
server = "localhost"

#creando la conexion
databaseConection = f"mysql+mysqlconnector://{userName}:{userPassword}@{server}:{connectionPort}/{dataBaseName}"
print(databaseConection)


   
