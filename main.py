from internal.cotacao import calculo_rctrc, calculo_rcfdc, calculo_gris, calculo_indice, calculo_pedagio, calculo_frete_total

# módulo main para iniciar as funções
resultado = calculo_indice()
seguro_rctrc = calculo_rctrc()
seguro_rcfdc = calculo_rcfdc()
seguro_gris = calculo_gris()
pedagio = calculo_pedagio()
total = calculo_frete_total()

resultado_formatado = "{:,.2f}".format(resultado).replace(",", ";").replace(".", ",").replace(";", ".")
seguro_rctrc_formatado = "{:,.2f}".format(seguro_rctrc).replace(",", ";").replace(".", ",").replace(";", ".")
seguro_rcfdc_formatado = "{:,.2f}".format(seguro_rcfdc).replace(",", ";").replace(".", ",").replace(";", ".")
seguro_gris_formatado = "{:,.2f}".format(seguro_gris).replace(",", ";").replace(".", ",").replace(";", ".")
calculo_pedagio_formatado = "{:,.2f}".format(pedagio).replace(",", ";").replace(".", ",").replace(";", ".")
calculo_total_formatado = "{:,.2f}".format(total).replace(",", ";").replace(".", ",").replace(";", ".")

print("Resultado:", resultado_formatado)
print("Seguro RCTRC:", seguro_rctrc_formatado)
print("Seguro RC/FDC:", seguro_rcfdc_formatado)
print("Seguro GRIS:", seguro_gris_formatado)
print("O valor do pedágio é:", calculo_pedagio_formatado)
print("O valor total do frete é:", calculo_total_formatado)


input("Pressione Enter para sair...")