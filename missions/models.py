from django.db import models

class Misison(models.Model):
    STATUS_CHOICES = [
        ('Ativa', 'Ativa'),
        ('Concluída', 'Concluída'),
        ('Abortada', 'Abortada'),
        ('Planejada', 'Planejada'),
        ('Em Trânsito', 'Em Trânsito'),
    ]

    name = models.CharField("Nome da Missão", max_length=200)
    lauch_date = models.DateField("Dara de Lançamento")
    destination = models.CharField("Destino", max_length=200)
    state  = models.CharField('Estado da Missão', max_length=50, choices=STATUS_CHOICES, default='Planejada')
    crew = models.TextField("Tripulação", helo_text="Um nome por linha")

    payload = models.TextField("Carga ÚTIL")

    duration = models.CharField("Duração da Missão", max_length=100,
                                help_text="Ex: 6 meses, 180 dias")
    
    cost = models.DecimalField("Custo da Missão", max_digits=20, decimal_places=2)

    sattus_info = models.TextField("Satus Detalhado", blank=True)

    class Meta:
        ordering = ['-laucnh_date']
        verbose_name = "Missão"
        verbose_name_plural = "Missões"

    def __str__(self):
        return self.name

    def crew_list(self):
        return [m.strip() for m in self.crew.splitlines() if m.strip()]
        