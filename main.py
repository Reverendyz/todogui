import tkinter as tk
from tkinter import StringVar, ttk



def createconection():
    import database.database as database
    database.createconnection()
    return

def add_requisition(access, req, value, invoice, provider):
    
    return

def abrirjanela():
    import teste
    return

def finish_task():
    return

def show_accomplished_tasks():
    return

def show_tasks():
    return

def delete_task():
    return

def main():
    root = tk.Tk()

    #Display config
    root.geometry('680x420')
    root.title('Purchase requisition ')
    root.resizable(False, False)
    
    lf = ttk.LabelFrame(root, text='Contas')
    lf.pack(ipady=5)
    
    addrequisitionframe = ttk.Frame(lf)
    addrequisitionframe.pack(pady=50)

    ttk.Label(addrequisitionframe, text='Conta: ').grid(column=0, row=0, padx=20, pady=1)
    ttk.Label(addrequisitionframe, text='Requisicao: ').grid(column=0, row=1, padx=20, pady=1)
    ttk.Label(addrequisitionframe, text='Valor: ').grid(column=0, row=2, padx=20, pady=1)
    ttk.Label(addrequisitionframe, text='NF: ').grid(column=0, row=3, padx=20, pady=1)
    ttk.Label(addrequisitionframe, text='Fornecedor: ').grid(column=0, row=4, padx=20, pady=1)

    access = StringVar()
    access_entry = ttk.Entry(addrequisitionframe, textvariable=access).grid(column=1, row=0, padx=20, pady=1)
    
    requisition = StringVar()
    requisition_entry = ttk.Entry(addrequisitionframe, textvariable=requisition).grid(column=1, row=1, padx=20, pady=1)

    value = StringVar()
    value_entry = ttk.Entry(addrequisitionframe, textvariable=value).grid(column=1, row=2, padx=20, pady=1)

    invoice_number = StringVar()
    invoice_number_entry = ttk.Entry(addrequisitionframe, textvariable=invoice_number).grid(column=1, row=3, padx=20, pady=1)
    
    provider = StringVar()
    provider_entry = ttk.Entry(addrequisitionframe, textvariable=provider).grid(column=1, row=4, padx=20, pady=1)


    #Buttons

    tk.Button(
        addrequisitionframe,
        text='Cadastrar',
        command=lambda:
            add_requisition(
                access.get().strip(),
                requisition.get().strip(),
                value.get().strip(),
                invoice_number.get().strip(),
                provider.get().strip()), width=25, height=10).grid(column=2, row=0, rowspan=5)

    tk.Button(root, text='Criar conexao', command=createconection).pack()

    tk.Button(root, text='Abrir nova janela', command=abrirjanela).pack()
    
    tk.Button(root, text='Sair', command=root.quit).pack(pady=10)

    root.mainloop()
    print('Sistema encerrado corretamente :D')

if __name__ == '__main__':
    main()