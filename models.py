#CRUD
#CREAR
def crear_persona(mysql,Tipodoc,Documento, Nombres, Apellidos, Nacimiento, Genero, Email, 
                Telefono, Direccion, es_alumno,es_acudiente,es_colaborador):
     #Cursor para la ejecución
     cur= mysql.connection.cursor()   
     #QUERY de Insert
     sQuery='''INSERT INTO persona (TipoId, Identificacion, Nombres, Apellidos, FechaNacimiento, Genero,
      Correo, Telefono, Direccion, Es_Alumno, Es_Acudiente, Es_Colaborador) 
      VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
     #print(sQuery)
     
     #Ejecucion de la Sentencia
     cur.execute(sQuery,(Tipodoc,Documento, Nombres, Apellidos, Nacimiento, Genero, Email, 
                Telefono, Direccion, es_alumno,es_acudiente,es_colaborador))
     mysql.connection.commit()
     
     #Cerramos el cursor
     cur.close()

def crear_usuario(mysql,Documento, Nom_usuario, Email, Telefono, Contraseña):
     #Cursor para la ejecución
     cur= mysql.connection.cursor()   
     #QUERY de Insert
     sQuery='''INSERT INTO usuario (Usuario, Nom_usuario, Email, Telefono, Privilegio, Contraseña) 
      VALUES(%s, %s, %s, %s, %s, %s)'''
     #print(sQuery)
     
     #Ejecucion de la Sentencia
     cur.execute(sQuery,(Documento, Nom_usuario, Email, Telefono,'', Contraseña))
     mysql.connection.commit()
     
     #Cerramos el cursor
     cur.close()

#READ
def validar_persona(mysql,Documento):
     #Cursor para la ejecución
     cur= mysql.connection.cursor()            
     sQuery="SELECT Identificacion FROM persona WHERE Identificacion='{}'".format(Documento)
     cur.execute(sQuery)
     row=cur.fetchone()
     #Cerramos el cursor
     cur.close()
     
     return row

def validar_usuario(mysql,Documento):
     #Cursor para la ejecución
     cur= mysql.connection.cursor()            
     sQuery="SELECT Usuario,Contraseña,Privilegio FROM bd_escuela.usuario WHERE Usuario='{}'".format(Documento)
     print(sQuery)
     cur.execute(sQuery)
     row=cur.fetchone()
     #Cerramos el cursor
     cur.close()
     
     return row

#uUPDATE
def actualizar(mysql,email,name):
     #Cursor para la ejecución
     cur= mysql.connection.cursor()   
     #QUERY de UPDATE           
     #Ejecucion de la Sentencia
     cur.execute('''UPDATE usuarios SET name=%s WHERE email=%s ''',(name,email))
     mysql.connection.commit()
     
     #Cerramos el cursor
     cur.close()

#DELETE
def Eliminar(mysql,email):
     #Cursor para la ejecución
     cur= mysql.connection.cursor()            
     sQuery="DELETE FROM usuarios WHERE email='{}'".format(email)
     print(sQuery)
     cur.execute(sQuery)
     row=cur.fetchone()
     #Cerramos el cursor
     cur.close()
     
     return row






