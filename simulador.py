#!/usr/bin/env python
# coding: utf-8

# In[3]:


import tkinter as tk
import locale

# formato brasileiro
locale.setlocale(locale.LC_ALL, 'pt_BR.utf-8')

def formatar_valor(valor):
    return locale.currency(valor, grouping=True, symbol=None)

def validar_entrada(valor, entrada_anterior, motivo):
    if valor == "":
        return True

    try:
        float(valor.replace(",", "."))
        return True
    except ValueError:
        return False

def calcular_preco_importacao():
    try:
        # Entradas dos dados
        valor_mercadoria = float(valor_mercadoria_entry.get().replace(",", "."))
        despesas_portuarias = float(despesas_portuarias_entry.get().replace(",", "."))
        frete_internacional = float(frete_internacional_entry.get().replace(",", "."))
        valor_despesa_aduaneira = float(valor_despesa_aduaneira_entry.get().replace(",", "."))
        valor_frete_interno = float(valor_frete_interno_entry.get().replace(",", "."))
        cotacao_dolar = float(cotacao_dolar_entry.get().replace(",", "."))
        imposto_importacao = float(imposto_importacao_entry.get().replace(",", "."))
        ipi = float(ipi_entry.get().replace(",", "."))
        pis = float(pis_entry.get().replace(",", "."))
        cofins = float(cofins_entry.get().replace(",", "."))
        icms = float(icms_entry.get().replace(",", "."))

        # Realização dos cálculos
        valor_aduaneiro = valor_mercadoria + despesas_portuarias + frete_internacional
        imposto_importacao_valor = valor_aduaneiro * (imposto_importacao / 100)
        ipi_valor = (valor_aduaneiro + imposto_importacao_valor) * (ipi / 100)
        valor_atualizado_importacao = (
            valor_aduaneiro + imposto_importacao_valor + ipi_valor
        )
        pis_valor = valor_aduaneiro * (pis / 100)
        cofins_valor = valor_aduaneiro * (cofins / 100)
        valor_atualizado_importacao = (
            valor_atualizado_importacao + pis_valor + cofins_valor
        )
        base_calculo_icms = (
            (valor_atualizado_importacao + valor_despesa_aduaneira) / (1 - icms / 100)
        )
        icms_valor = base_calculo_icms * (icms / 100)
        valor_total_importacao = (
            valor_aduaneiro
            + imposto_importacao_valor
            + ipi_valor
            + pis_valor
            + cofins_valor
            + valor_despesa_aduaneira
            + icms_valor
            + valor_frete_interno
        )
        valor_total_importacao_reais = valor_total_importacao * cotacao_dolar

        # Resultados
        resultado = {
            "Valor Aduaneiro": valor_aduaneiro,
            "Imposto de Importação": imposto_importacao_valor,
            "IPI": ipi_valor,
            "Valor Atualizado com II e IPI": valor_atualizado_importacao,
            "PIS": pis_valor,
            "COFINS": cofins_valor,
            "Valor Atualizado com II, IPI, PIS e COFINS": valor_atualizado_importacao,
            "ICMS": icms_valor,
            "Valor Total da Mercadoria Importada": valor_total_importacao_reais,
        }

        # Exibição do resultado na interfâce do tkinter
        resultados_texto = "\n".join([f"{chave}: {formatar_valor(valor)} BRL" for chave, valor in resultado.items()])
        resultado_label.config(text=resultados_texto)

    except ValueError:
        resultado_label.config(text="Certifique-se de inserir valores válidos.")

# Janela tkinter
root = tk.Tk()
root.title("Simulador de preços")

# Campos de entrada no tkinter
valor_mercadoria_entry = tk.Entry(root)
valor_mercadoria_entry.grid(row=0, column=1)
tk.Label(root, text="Valor da Mercadoria em dólares:").grid(row=0, column=0)

despesas_portuarias_entry = tk.Entry(root)
despesas_portuarias_entry.grid(row=1, column=1)
tk.Label(root, text="Despesas Portuárias em dólares:").grid(row=1, column=0)

frete_internacional_entry = tk.Entry(root)
frete_internacional_entry.grid(row=2, column=1)
tk.Label(root, text="Frete Internacional em dólares:").grid(row=2, column=0)

valor_despesa_aduaneira_entry = tk.Entry(root)
valor_despesa_aduaneira_entry.grid(row=3, column=1)
tk.Label(root, text="Valor da Despesa Aduaneira em dólares:").grid(row=3, column=0)

valor_frete_interno_entry = tk.Entry(root)
valor_frete_interno_entry.grid(row=4, column=1)
tk.Label(root, text="Valor do frete interno em dólares:").grid(row=4, column=0)

cotacao_dolar_entry = tk.Entry(root)
cotacao_dolar_entry.grid(row=5, column=1)
tk.Label(root, text="Cotação do dolar:").grid(row=5, column=0)

imposto_importacao_entry = tk.Entry(root)
imposto_importacao_entry.grid(row=6, column=1)
tk.Label(root, text="Imposto de Importação em %:").grid(row=6, column=0)

ipi_entry = tk.Entry(root)
ipi_entry.grid(row=7, column=1)
tk.Label(root, text="IPI em %:").grid(row=7, column=0)

pis_entry = tk.Entry(root)
pis_entry.grid(row=8, column=1)
tk.Label(root, text="PIS em %:").grid(row=8, column=0)

cofins_entry = tk.Entry(root)
cofins_entry.grid(row=9, column=1)
tk.Label(root, text="COFINS em %:").grid(row=9, column=0)

icms_entry = tk.Entry(root)
icms_entry.grid(row=10, column=1)
tk.Label(root, text="ICMS em %:").grid(row=10, column=0)

# Vírgula como separador decimal ao invés de pontos
entrada_valida = root.register(validar_entrada)

valor_mercadoria_entry.config(validate="key", validatecommand=(entrada_valida, "%P", "%S", "%d"))
despesas_portuarias_entry.config(validate="key", validatecommand=(entrada_valida, "%P", "%S", "%d"))
frete_internacional_entry.config(validate="key", validatecommand=(entrada_valida, "%P", "%S", "%d"))
valor_despesa_aduaneira_entry.config(validate="key", validatecommand=(entrada_valida, "%P", "%S", "%d"))
valor_frete_interno_entry.config(validate="key", validatecommand=(entrada_valida, "%P", "%S", "%d"))
cotacao_dolar_entry.config(validate="key", validatecommand=(entrada_valida, "%P", "%S", "%d"))
imposto_importacao_entry.config(validate="key", validatecommand=(entrada_valida, "%P", "%S", "%d"))
ipi_entry.config(validate="key", validatecommand=(entrada_valida, "%P", "%S", "%d"))
pis_entry.config(validate="key", validatecommand=(entrada_valida, "%P", "%S", "%d"))
cofins_entry.config(validate="key", validatecommand=(entrada_valida, "%P", "%S", "%d"))
icms_entry.config(validate="key", validatecommand=(entrada_valida, "%P", "%S", "%d"))

# Rótulos para exibição dos resultados
resultado_label = tk.Label(root, text="Aguardando resultados...", wraplength=300)
resultado_label.grid(row=13, columnspan=2, pady=10)

# Botão para calcular
calcular_button = tk.Button(root, text="Calcular Resultados", command=calcular_preco_importacao)
calcular_button.grid(row=14, columnspan=2)

# Botão para fechar a janela
fechar_botao = tk.Button(root, text="Fechar", command=root.destroy)
fechar_botao.grid(row=15, columnspan=2)

# Iniciar o loop principal da interface
root.mainloop()


# In[ ]:




