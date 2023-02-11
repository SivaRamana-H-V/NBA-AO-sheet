from openpyxl import load_workbook
import openpyxl
import Readxl #add mark file
import ReadxlIA2 #add mark file
import ReadxlModel #add mark file
import Place  #add pasteing place
import streamlit as st
import pandas as pd
import numpy as np
import io
import base64
from streamlit.components.v1 import html
from tempfile import NamedTemporaryFile


st.title('NBA')
'''Name = st.text_area('Enter the Student Names List :')
REG = st.text_area('Enter the Student Names REG.NO :')
Rank=st.text_area('Enter the Student University Rank :')
DN=st.text_input('Enter the Department Name :')
Dn='DEPARTMENT OF '
CN=st.text_input('Enter the Course Name :')
FN=st.text_input('Enter the Faculty Name :')'''
TSN=st.text_input("Total_Students :")

@st.cache(suppress_st_warning=True)
def download_excel(o,fn):
    b64 = base64.b64encode(output.getvalue()).decode()
    return f'<a href="data:application/octet-stream;base64,{b64}" download="{fn}">Download Excel File</a>'

def Convert(string):
    li = list(string.split("\n"))
    return li
N=Convert(Name)
R=Convert(REG)
U=Convert(Rank)
# st.write(Convert(Name))
# st.write(Convert(REG))

uploaded_file = st.file_uploader("Upload Excel Files Template",type=['xlsx','csv'])
if uploaded_file is not None:
    workbook = load_workbook(uploaded_file)
    sheet = workbook.active

    sheet['AT8']=CN
    sheet['AT9']=FN
    sheet['AQ4']=Dn+DN
    try:
        '''n=Place.XLPlace('C',TSN)
        for i in range(len(n)):
            sheet[n[i]] = N[i]

        r=Place.XLPlace('B',TSN)
        for i in range(len(r)):
            sheet[r[i]] = int(R[i])'''
        
        u=Place.XLPlace('AI',TSN)
        st.write(u)
        for i in range(len(u)):
            sheet[u[i]] = U[i]
        
    except IndexError:
        st.write('Enter The Detiles *')

    IA1=Readxl.ReadValue()
    if IA1 is not None:
        #st.write('IA1:',IA1)
        B=Place.XLPlace('D',TSN)
        #st.write(B)
        st.write(len(B))
        for i in range(len(B)):
            sheet[B[i]] = IA1[0][i]
        
        B1=Place.XLPlace('J',TSN)
        for i in range(len(B)):
            sheet[B1[i]] = IA1[1][i]
        #workbook.save('output.xlsx')

        IA2=ReadxlIA2.ReadValue()
        if IA2 is not None:
            #st.write('IA2:',IA2)
            C=Place.XLPlace('P',TSN)
            for i in range(len(C)):
                sheet[C[i]] = IA2[0][i]
            C1=Place.XLPlace('V',TSN)
            for i in range(len(C)):
                sheet[C1[i]] = IA2[1][i]

            Model=ReadxlModel.ReadValue()
            if Model is not None:
                #st.write('Model:',Model)
                D=Place.XLPlace('E',TSN)
                for i in range(len(D)):
                    sheet[D[i]] = Model[0][i]
                D1=Place.XLPlace('K',TSN)
                for i in range(len(D1)):
                    sheet[D1[i]] = Model[1][i]
                D2=Place.XLPlace('Q',TSN)
                for i in range(len(D2)):
                    sheet[D2[i]] = Model[2][i]
                D3=Place.XLPlace('W',TSN)
                for i in range(len(D3)):
                    sheet[D3[i]] = Model[3][i]
                D4=Place.XLPlace('AC',TSN)
                for i in range(len(D4)):
                    sheet[D4[i]] = Model[4][i]
                output = io.BytesIO()
                workbook.save(output)
                output.seek(0)
                O=output


try:
    
    if O is not None:
        fn=st.text_input('Enter the Output File Name :')
        fn= fn+'.xlsx'
        st.markdown(download_excel(O,fn), unsafe_allow_html=True)

except NameError:
    st.write('Complete the Process')
