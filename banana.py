"""A banana preferences survey written in Python with Tkinter"""

import tkinter as tk

# Cria a root window
root = tk.Tk()

# Confiura o título
root.title('Banana interest survey')

# confiura dimensões da root window
root.geometry('640x480+300+300')
root.resizable(False, False)

###########
# Widgets #
###########

title = tk.Label(
  root,
  text='Please take the survey',
  font=('Arial 16 bold'),
  bg='brown',
  fg='#FF0'
)

# Uso de Stringvar 
name_var = tk.StringVar(root)
name_label = tk.Label(root, text='Qual seu nome?')
name_inp = tk.Entry(root, textvariable=name_var)

# uso de BooleanVar para True/False
eater_var = tk.BooleanVar()
eater_inp = tk.Checkbutton(
  root, variable=eater_var, text='Confirme esse botão se você tem o habito de comer bananas.'
)

# Uso de IntVar 
# Pode-se configurar um valor padrão
num_var = tk.IntVar(value=3)
num_label = tk.Label(text='Quantas bananas você come por dia?')
# Mesmo se  tratando de uma IntVar, o argumento continua sendo "textvariable".
num_inp = tk.Spinbox(
  root,
  textvariable=num_var,
  from_=0,
  to=1000,
  increment=1
)

# Listboxes não funcionam bem com variaveis de controle
# OptionMenu funcionam bem!
# Aqui também foi configurado um valor padrão.
color_var = tk.StringVar(value='Any')
color_label = tk.Label(
  root,
  text='Qual a melhor cor para uma banana?'
)
color_choices = (
  'Qualquer Uma', 'Verde', 'Verde/Amarelo', 'Amarelo', 'Marrom', 'Preta'
)
color_inp = tk.OptionMenu(
  root, color_var, *color_choices
)

plantain_label = tk.Label(root, text='Você come hortaliças?')
# Criação de um frame para contenção de widgets
plantain_frame = tk.Frame(root)

# Podemos utilizar qualquer tipo de variável de controleem radiobuttom
plantain_var = tk.BooleanVar()
plantain_yes_inp = tk.Radiobutton(
  plantain_frame,
  text='Sim',
  value=True,
  variable=plantain_var
)
plantain_no_inp = tk.Radiobutton(
  plantain_frame,
  text='Não',
  value=False,
  variable=plantain_var
)

# Text widget não suporta variáveis de controle
banana_haiku_label = tk.Label(root, text='Considerações')
banana_haiku_inp = tk.Text(root, height=3)


# Cria botão gatilho de ações
submit_btn = tk.Button(root, text='Submeter respostas')

# Labels suportam StringVar 
output_var = tk.StringVar(value='')
output_line = tk.Label(
  root,
  textvariable=output_var,
  anchor='w',
  justify='left'
)


#######################
# Geometry Management #
#######################
# Uso de Grid ao invés de pack para deposito dos widgets
title.grid(columnspan=2)
name_label.grid(row=1, column=0)
name_inp.grid(row=1, column=1)
eater_inp.grid(row=2, columnspan=2, sticky='we')
num_label.grid(row=3, sticky=tk.W)
num_inp.grid(row=3, column=1, sticky=(tk.W + tk.E))
color_label.grid(row=4, columnspan=2, sticky=tk.W, pady=10)
color_inp.grid(row=5, columnspan=2, sticky=tk.W + tk.E, padx=25)
plantain_yes_inp.pack(side='left', fill='x', ipadx=10, ipady=5)
plantain_no_inp.pack(side='left', fill='x', ipadx=10, ipady=5)
plantain_label.grid(row=6, columnspan=2, sticky=tk.W)
plantain_frame.grid(row=7, columnspan=2, stick=tk.W)
banana_haiku_label.grid(row=8, sticky=tk.W)
banana_haiku_inp.grid(row=9, columnspan=2, sticky='NSEW')

submit_btn.grid(row=99)
output_line.grid(row=100, columnspan=2, sticky='NSEW')

root.columnconfigure(1, weight=1)

root.rowconfigure(99, weight=2)
root.rowconfigure(100, weight=1)

#####################
# Add some behavior #
#####################

def on_submit():
  """Para ser executado quando o usuario submeter as respostas"""
  name = name_var.get()
  try:
    number = num_var.get()
  except tk.TclError:
    number = 10000

  # o uso de variaveis torna o OptionMenu mais simples
  color = color_var.get()

  # Checkbutton tbm se beneficia do uso de variáveis
  banana_eater = eater_var.get()
  plantain_eater = plantain_var.get()

  haiku = banana_haiku_inp.get('1.0', tk.END)
  message = f'Thanks for taking the survey, {name}.\n'

  if not banana_eater:
    message += "Ok, nem todo mundo gosta de bananas!\n"

  else:
    message += f'Ok, aqui estão sua(s) {number} {color} bananas!\n'

  if plantain_eater:
    message += 'Que bom, hortaliças são benéficas para a saúde!'
  else:
    message += 'Ok, nem todo mundo gosta de hortaliças!'

  if haiku.strip():
    message += f'\n\nConsiderações:\n{haiku}'

  # Atualize o valor da variável usando .set()
  # NÃO USE:  output_var = 'my string'
  output_var.set(message)


# configuração do botão de submição das respotas
submit_btn.configure(command=on_submit)

###############
# Execute App #
###############

root.mainloop()