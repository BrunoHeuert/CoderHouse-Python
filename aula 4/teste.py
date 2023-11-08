from plyer import notification
#IMPORTANDO A BILBIOTECA NOTIFICATION
import datetime
#IMPROTANDO A BIBLIOTECA DE DATAS
def alerta(nivel = 0, base = 'CLIENTES', etapa = 'EXTRACAO'):
    if nivel == 1:
        nivel = 'Alerta Baixo'
    elif nivel == 2:
        nivel = 'Alerta Médio'
    elif nivel == 3:
        nivel = 'Alerta Alto'
    else:
        nivel = 'NÃO REGISTRADO'
    #O IF ACIMA VAI APONTAR QUAL TIPO DE ALERTA SERÁ DISPARADO
    notification.notify(
        title= nivel,#TITULO DA NOTIFICAÇÃO
        message=f'Falha no carregamento da base {base} na etapa {etapa}.\n{datetime.datetime.today()}',#MENSAGEM A SER DISPARADA
        app_name='Nome do aplicativo',
        timeout=10 )
alerta(4, 'CLIENTES', 'EXTRACAO')
#O ALERTA ACIMA VAI GERAR A NOTIFICAÇÃO, O PRIMEIRO VALOR É REFERENTE AO NIVEL, O SEGUNDO A BASE E O TERCEIRO A ETAPA
