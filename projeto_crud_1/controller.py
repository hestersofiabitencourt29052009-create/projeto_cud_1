# controlar e conectar 

import model

def adicionar_nota(texto):
    if texto.strip():
        model.salvar_no_banco(texto)
        return True
    return False

def listar_notas():
    return model.ler_do_banco()        
