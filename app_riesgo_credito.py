from pycaret.regression import load_model, predict_model
import streamlit as st
import pandas as pd

model = load_model("C:/Users/USER/Desktop/Proyecto Riesgo de Mora DS EAFIT/boosted_lr_01102021")

def predict(model, input_df):
    predictions_df = predict_model(estimator=model, data=input_df)
    label = predictions_df['Label'][0]
    prob = predictions_df['Score'][0]*100
    return label,prob

def run():
    add_selectbox = st.sidebar.selectbox("Tipo de predicción", ('Online', 'csv'))
    st.sidebar.info("App para predecir si existe riesgo de no pago en clientes potenciales para créditos. Un resultado de 0 indica que no hay riesgo; un resultado de 1 indica riesgo.")
    st.title('Predicción de Riesgo Crediticio')

    if add_selectbox == 'Online':
        Indicador_Mora = st.number_input('Riesgo de no pago', min_value=0, max_value=1)
        score_central_riesgo = st.number_input('Score central de riesgo', min_value = 0)
        antig_entidad = st.number_input('Antiguedad en la entidad (años)', min_value = 0)
        estado_civil = st.selectbox('Estado Civil', ['C','U','E','V','S'])
        nivel_estudio = st.selectbox('Nivel de Estudios', ['U','E','T','B','P','N'])
        tipo_contrato = st.selectbox('Tipo de Contrato Laboral', [0,'F','I','O','V','P','L','R','N'])
        oficina= st.selectbox('Oficina',[342,805,825,66,424,705,131,145,404,433,5,720,600,648,501,643,172,83
,401,226,184,462,183,163,831,446,815,513,303,512,510,818,329,933,812,677
,821,311,351,146,129,861,451,460,128,212,951,940,13,711,181,860,185,158
,154,139,125,227,101,106,121,235,668,901,213,120,896,925,39,17,465,85
,853,79,30,347,811,837,72,656,313,327,330,497,312,116,251,803,530,205
,902,33,991,239,161,143,174,164,252,688,119,157,234,109,223,638,840,277
,833,866,32,118,253,99,40,644,210,0,952,54,904,138,34,27,31,428
,344,696,80,41,675,341,102,539,514,522,505,310,701,423,70,666,9,77
,687,569,19,457,76,681,713,449,725,941,684,930,75,324,78,141,108,343
,511,550,801,809,52,442,622,710,841,57,452,422,21,63,4,509,603,601
,602,216,911,314,814,443,403,202,350,22,503,970,571,14,634,502,726,702
,750,694,46,640,931,8,10,695,2,639,81,712,18,220,447,630,15,636
,25,11,615,47,37,670,698,35,572,92,328,508,604,613,715,26,71,73
,28,410,16,280,64,649,357,339,865,804,439,352,721,279,836,69,610,61
,224,201,302,348,301,942,903,912,924,405,450,230,326,177,819,923,928,820
,127,323])
        dest_credito = st.selectbox('Destino del crédito', [1,11,10,2,9,0,4,6])
        antig_actividad = st.number_input('Antiguedad en actividad laboral (años)', min_value=0)
        total_ingresos = st.number_input('Ingresos en COP', min_value=0)
        ingresos_smmlv = st.number_input('Ingresos en SMMLV (Dividir ingresos entre $908.526)', min_value=0,format="%i")

        output = ""

        input_dict= {'Indicador_Mora': Indicador_Mora,
                      'Socre Central': score_central_riesgo,
                      'ANTIG_Entidad': antig_entidad,
                      'ESTADO_CIVIL': estado_civil,
                      'NIVEL_ESTUDIOS': nivel_estudio,
                      'TIPO_CONTRATO': tipo_contrato,
                      'OFICINA': oficina,
                      'DEST_CREDITO': dest_credito,
                      'ANTIG_ACTIV_ANOS': antig_actividad,
                      'TOTAL_INGRESOS': total_ingresos,
                      'INGRESO_SMMLV': ingresos_smmlv
                     }
        input_df = pd.DataFrame([input_dict])

        if st.button('Preddición'):
            label, prob = predict(model = model, input_df = input_df)
            st.success('La predicción es: {ou1}, con una certeza del {ou2}%'.format(ou1=str(label),ou2=str(prob)))

    if add_selectbox == 'csv':
        file_upload = st.file_uploader('Subir Archivo Csv', type=['csv'])

        if file_upload is not None:
            data = pd.read_csv(file_upload)
            predictions = predict_model(estimator=model, data=data)
            st.wrtie(predictions)
if __name__ == '__main__':
    run()
