#usr/bin/pyhthon3

import database.database as database

class Requisition:

    def __init__(self, access, id, value, invoice, provider):
        self.id = id
        self.access = access
        self.value = value
        self.invoice = invoice
        self.provider = provider

    def save(self, access, id, value, invoice, provider):
        try:
            conn = database.createconnection()

            cursor = conn.cursor()
            cursor.execute("INSERT INTO controle(id, access, value, invoice, provider) VALUES(",
            id,",",
            access,",",
            value,",",
            invoice,",",
            provider,
            ");"
            )
            conn.commit()
        except:
            print('It was not possible to persist data into the database')     

        return
        
