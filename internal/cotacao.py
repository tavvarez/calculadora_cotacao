#Função para receber as entradas do usuário

def get_user_input(prompt):
    while True:
        try:
            user_input = float(input(prompt))
            return user_input
        except ValueError:
            print("Por favor, digite um valor válido!")

valor_mercadoria = get_user_input("Digite o valor da mercadoria: ")
valor_icms = get_user_input("Digite o ICMS: ")
valor_comissao = get_user_input("Digite a comissão: ")
valor_pedagio = get_user_input("Digite o valor do pedágio: ")
valor_motorista = get_user_input("Digite o valor do motorista: ")
pis_cofins = 3.650


#Funções para realizar os cálculos fixos da cotaçao
def calculo_rctrc():
    rctrc = 0.050
    seguro_rctrc = valor_mercadoria * (rctrc / 100)
    seguro_rctrc_icms = seguro_rctrc / ((100 - valor_icms) / 100)
    seguro_final_rctrc = (seguro_rctrc * (pis_cofins / 100)) + seguro_rctrc_icms
    return seguro_final_rctrc

def calculo_rcfdc():
    rcfdc = 0.050
    seguro_rcfdc = valor_mercadoria * (rcfdc / 100)
    seguro_rcfdc_icms = seguro_rcfdc / ((100 - valor_icms) / 100)
    seguro_final_rcfdc = (seguro_rcfdc * (pis_cofins / 100)) + seguro_rcfdc_icms
    return seguro_final_rcfdc

def calculo_gris():
    gris = 0.050
    seguro_gris = valor_mercadoria * (gris / 100)
    seguro_gris_icms = seguro_gris / ((100 - valor_icms) / 100)
    seguro_final_gris = (seguro_gris * (pis_cofins / 100)) + seguro_gris_icms
    return seguro_final_gris

def calculo_indice():
    financeiro = 1.500
    pamcard = 0.800
    soma = pis_cofins + pamcard + financeiro + valor_icms + valor_comissao
    resultado = 100 - soma    
    return resultado

resultado = calculo_indice()
seguro_rctrc = calculo_rctrc()
seguro_rcfdc = calculo_rcfdc()
seguro_gris = calculo_gris()

# print("Resultado:", resultado)
# print("Seguro RCTRC:", seguro_rctrc)
# print("Seguro RC/FDC:", seguro_rcfdc)
# print("Seguro GRIS:", seguro_gris)


def calculo_pedagio():
    pedágio_icms = valor_pedagio / ((100 - valor_icms) / 100)
    pedagio_total = (valor_pedagio * (pis_cofins / 100)) + pedágio_icms
    return pedagio_total

pedagio = calculo_pedagio()


def calculo_frete_total():
    seguro = seguro_rctrc + seguro_rcfdc
    vlr_pedagio = pedagio
    vlr_gris = seguro_gris
    frete_peso = (valor_motorista / resultado*100)
    total_cte = seguro + frete_peso + vlr_pedagio + vlr_gris
    return total_cte

# total = calculo_frete_total()
