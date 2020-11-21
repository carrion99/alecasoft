from django.db import models

# Create your models here.

class Usuario(models.Model):
    idUsuario = models.PositiveIntegerField(primary_key=True)
    nombreUsuario = models.CharField(max_length=30, unique=True)
    claveUsuario = models.CharField(max_length=100)

    def __str__(self):
        return "{0}".format(self.nombreUsuario)


class Estado_Civil(models.Model):
    idEstadoCivil = models.PositiveIntegerField(primary_key=True)
    estadoCivil = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=1000)

    def __str__(self):
        return "{0}".format(self.estadoCivil)


class Ciudad(models.Model):
    idCiudad = models.PositiveIntegerField(primary_key=True)
    ciudad = models.CharField(max_length=1000, unique=True)
    descripcion = models.CharField(max_length=1000)

    def __str__(self):
        return "{0}".format(self.ciudad)


class Direccion(models.Model):
    idDireccion = models.PositiveIntegerField(primary_key=True)
    callePrincipal = models.CharField(max_length=1000)
    calleSecundaria = models.CharField(max_length=1000)
    referencia = models.CharField(max_length=1000)
    descripcion = models.CharField(max_length=1000)

    def direccionCompleta(self):
        txt = "{0} {1} {2}"
        return txt.format(self.callePrincipal, ' y ' ,self.calleSecundaria)

    def __str__(self):
        return self.direccionCompleta()


class Tipo(models.Model):
    idTipo = models.PositiveIntegerField(primary_key=True)
    tipo = models.CharField(max_length=1000, unique=True)
    descripcion = models.CharField(max_length=1000)

    def __str__(self):
        return "{0}".format(self.tipo)


class Email(models.Model):
    idEmail = models.PositiveIntegerField(primary_key=True)
    email = models.CharField(max_length=1000,unique=True )
    descripcion = models.CharField(max_length=1000)

    def __str__(self):
        return "{0}".format(self.email)


class Sexo(models.Model):
    idSexo = models.PositiveIntegerField(primary_key=True)
    sexo = models.CharField(max_length=500, unique=True )
    descripcion = models.CharField(max_length=1000)

    def __str__(self):
        return "{0}".format(self.sexo)


class Persona(models.Model):
    dni = models.CharField(primary_key=True, max_length=10)
    Tipo = models.ForeignKey(Tipo, null=False, blank=False, on_delete=models.CASCADE)
    apellidoPaterno = models.CharField(max_length=1000)
    apellidoMaterno = models.CharField(max_length=1000)
    nombres = models.CharField(max_length=1000)
    fechaNacimiento = models.DateField()
    Sexo = models.ForeignKey(Sexo, null=False, blank=False, on_delete=models.CASCADE)
    Estado_Civil = models.ForeignKey(Estado_Civil, null=False, blank=False, on_delete=models.CASCADE)
    Ciudad = models.ForeignKey(Ciudad, null=False, blank=False, on_delete=models.CASCADE)
    Direccion = models.ForeignKey(Direccion, null=False, blank=False, on_delete=models.CASCADE)
    Email = models.ForeignKey(Email, null=False, blank=False, on_delete=models.CASCADE)
    Usuario = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)

    def nombreCompleto(self):
        txt = "{0} {1} {2}"
        return txt.format(self.apellidoPaterno, self.apellidoMaterno)

    def __str__(self):
        return self.nombreCompleto()


class Telefono(models.Model):
    idTelefono = models.PositiveIntegerField(primary_key=True)
    numero = models.PositiveIntegerField(unique=True)
    descripcion = models.CharField(max_length=1000)

    def __str__(self):
        return "{0}".format(self.numero)


class PersonaTelefono(models.Model):
    idPersonaCelular = models.PositiveIntegerField(primary_key=True)
    Telefono = models.ForeignKey(Telefono, null=False, blank=False, on_delete=models.CASCADE)
    Persona = models.ForeignKey(Persona, null=False, blank=False, on_delete=models.CASCADE)
