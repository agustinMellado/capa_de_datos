class Usuario:
    def __init__(self,username,password):
        self._username=username
        self._password=password
    
   
    #observadores
    @property
    def username(self):
        return self._username
    @property
    def password(self):
        return self._password
    #modificadores
    @username.setter
    def username(self,username):
        self._username= username
    @password.setter
    def password(self,password):
        self._password=password
     
     
    def __str__(self):
        return f'''
            nombre: {self._username},
            contraseña: {self._password} 
        '''