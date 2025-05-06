from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# ID
# nome, sobrenome, telefone, email, data criada,
# categoria(barbeiro, gerenciador), show, owner, foto, chavePix, 

class Categoria(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.name}'

class Barbeiro(models.Model):
    nome = models.CharField(max_length=70)
    sobrenome = models.CharField(max_length=120, blank=True)
    apelido = models.CharField(max_length=70, blank=True)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(max_length=254, blank=True)
    chave_pix = models.CharField(max_length=500)
    picture = models.ImageField(blank=True, upload_to='picture/%Y/%m', verbose_name='Foto')
    data_criada = models.DateTimeField(default=timezone.now)
    show = models.BooleanField(default=True, verbose_name='mostrar')
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        blank=True, null=True,
    )

    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )

    def __str__(self) -> str:
        if not self.apelido:
            return f'{self.nome} {self.sobrenome}'
        return f'{self.apelido} - {self.nome} {self.sobrenome}'
        