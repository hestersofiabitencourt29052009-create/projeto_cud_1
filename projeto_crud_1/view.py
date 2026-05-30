# template  -  interface -  front-end

import streamlit as st
import controller

nova_entrada  =  st.text_input('Escreva algo ...')

if st.button('Salvar'):
    if controller.adicionar_nota(nova_entrada):
       st.success('Salva com sucesso')
    else:
       st.error('Digite algo antes de salvar')

st.subheader('histórico')
for nota in controller.listar_notas():
    st.write(nota)       





