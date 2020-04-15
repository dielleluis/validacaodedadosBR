from datetime import datetime, timedelta

class DatasBr:
    
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_data()

    def mes_cadastro(self):
        meses = [
            'Janeiro', 'Fevereiro', 'Março',
            'Abril', 'Maio', 'Junho',
            'Julho', 'Agosto', 'Setembro',
            'Outubro', 'Novembro', 'Dezembro'
        ]
        mes_catro = self.momento_cadastro.month - 1

        return meses[mes_catro]

    def dia_semana(self):
        dia = [
            'Segunda-feira', 'Terça-feira', 'Quarta-feira',
            'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo'
        ]
        dia_semana = self.momento_cadastro.weekday()
        
        return dia[dia_semana]

    def format_data(self):
        data_formatada = self.momento_cadastro.strftime('%d/%m/%Y %H:%M')
        return data_formatada

    def tempo_cadastro(self):
        tempo_cad = (datetime.today() + timedelta(days=30)) - self.momento_cadastro
        return tempo_cad