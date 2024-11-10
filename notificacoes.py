import schedule
import time
from plyer import notification

# Funções de cada tarefa
def lembrar_beber_agua():
    notification.notify(
        title="Hidratação", message="Hora de beber um copo com água!", timeout=1
    )
    print("Lembrete de hidratação enviado!")

def lembrar_exercicio():
    notification.notify(
        title="Exercício", message="Levante-se e faça alguns alongamentos!", timeout=1
    )
    print("Lembrete de exercício enviado!")

def tarefa_diaria():
    notification.notify(
        title="Tarefas de hoje", message="Lembre-se de organizar seu espaço e cumprir as tarefas!", timeout=1
    )
    print("Lembrete de tarefas diárias enviado!")

# Agendamento das tarefas
schedule.every(1).minutes.do(lembrar_beber_agua)
schedule.every(2).minutes.do(lembrar_exercicio)
schedule.every(3).minutes.do(tarefa_diaria)

# Loop para manter o bot ativo
while True:
    schedule.run_pending()
    time.sleep(10)
