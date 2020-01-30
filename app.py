from flask import Flask,render_template
from flask import request
from sklearn.externals import joblib
import pandas as pd

import os

Path = os.getcwd()
loaded_model_rotativo_logistico = joblib.load(Path + "/rotativo/modelo_credito_rotativo_logistico.sav")
loaded_model_rotativo_random_forest = joblib.load(Path + "/rotativo/modelo_credito_rotativo_rf_ajustado.sav")
loaded_model_subsidio_logistico = joblib.load(Path + "/subsidio/modelo_credito_subsidio_logistico.sav")
loaded_model_subsidio_random_forest = joblib.load(Path + "/subsidio/modelo_credito_subsidio_rf_ajustado.sav")
print('models loaded!')

"""
Created on Sun Jan 19 22:14:25 2020

@author: Robert Romero
"""

#Path = "C:/Users/robert.romero/Documents/Robert/herme/comfand/Predict"

def Score_Clientes(Base, tCred, model):
    # Base: data
    # tCred: rotativo o subsidio
    # model: logistico, random_forest

    if tCred == "rotativo" and model == "logistico":
        loaded_model = loaded_model_rotativo_logistico
    elif tCred == "rotativo" and model == "random_forest":
        loaded_model = loaded_model_rotativo_random_forest
    elif tCred == "subsidio" and model == "logistico":
        loaded_model = loaded_model_subsidio_logistico
    else: #tCred == "subsidio" and model == "random_forest":
        loaded_model = loaded_model_subsidio_random_forest

    nPath = Path + "/"+tCred+"/"
    result = pd.DataFrame(loaded_model.predict_proba(Base))
    print(result)
    return str(result.iat[0,1])

#http://127.0.0.1:5000/scoring?tCred=rotativo&model=logistico&cant_per_car=2&hijos_afiliados=1&mayor65_afiliados=2&salario=8281.16&edad=59&meses_Afili=52&prom_cantidad=0&prom_compras=563900&ultima_compra=300000&categoria_A=1&categoria_B=0&categoria_C=0&categoria_D=0&estado_civil_1=0&estado_civil_2=1&estado_civil_3=0&estado_civil_4=0&estado_civil_5=0&genero_M=1&identificadorTipoVivienda_A=0&identificadorTipoVivienda_F=0&identificadorTipoVivienda_H=0&identificadorTipoVivienda_O=0&identificadorTipoVivienda_P=1&tipoContrato_CO=0&tipoContrato_OC=0&tipoContrato_PR=0&tipoContrato_PS=0&tipoContrato_PT=0&tipoContrato_TF=0&tipoContrato_TI=1

#http://127.0.0.1:5000/scoring?tCred=rotativo&model=random_forest&cant_per_car=2&hijos_afiliados=1&mayor65_afiliados=2&salario=8281.16&edad=59&meses_Afili=52&prom_cantidad=2&prom_compras=563900&ultima_compra=300000&categoria_A=1&categoria_B=0&categoria_C=0&categoria_D=0&estado_civil_1=0&estado_civil_2=1&estado_civil_3=0&estado_civil_4=0&estado_civil_5=0&genero_M=1&identificadorTipoVivienda_A=0&identificadorTipoVivienda_F=0&identificadorTipoVivienda_H=0&identificadorTipoVivienda_O=0&identificadorTipoVivienda_P=1&tipoContrato_CO=0&tipoContrato_OC=0&tipoContrato_PR=0&tipoContrato_PS=0&tipoContrato_PT=0&tipoContrato_TF=0&tipoContrato_TI=1

#http://127.0.0.1:5000/scoring?tCred=subsidio&model=logistico&cant_per_car=2&hijos_afiliados=2&mayor65_afiliados=2&salario=7812.42&edad=31&meses_Afili=42&prom_cantidad=0.0&prom_compras=0.0&ultima_compra=773112.0&categoria_A=0&categoria_B=0&categoria_C=0&categoria_D=1&estado_civil_1=0&estado_civil_2=0&estado_civil_3=0&estado_civil_4=0&estado_civil_5=1&genero_M=1&identificadorTipoVivienda_A=0&identificadorTipoVivienda_F=0&identificadorTipoVivienda_H=0&identificadorTipoVivienda_O=1&identificadorTipoVivienda_P=0&tipoContrato_CO=0&tipoContrato_OC=0&tipoContrato_PR=0&tipoContrato_PS=0&tipoContrato_PT=0&tipoContrato_TF=0&tipoContrato_TI=1

#http://127.0.0.1:5000/scoring?tCred=subsidio&model=random_forest&cant_per_car=2&hijos_afiliados=2&mayor65_afiliados=2&salario=7812.42&edad=31&meses_Afili=42&prom_cantidad=0.0&prom_compras=0.0&ultima_compra=773112.0&categoria_A=0&categoria_B=0&categoria_C=0&categoria_D=1&estado_civil_1=0&estado_civil_2=0&estado_civil_3=0&estado_civil_4=0&estado_civil_5=1&genero_M=1&identificadorTipoVivienda_A=0&identificadorTipoVivienda_F=0&identificadorTipoVivienda_H=0&identificadorTipoVivienda_O=1&identificadorTipoVivienda_P=0&tipoContrato_CO=0&tipoContrato_OC=0&tipoContrato_PR=0&tipoContrato_PS=0&tipoContrato_PT=0&tipoContrato_TF=0&tipoContrato_TI=1

app = Flask(__name__,
            static_url_path='',
            static_folder='web/static',
            template_folder='web/templates')
@app.route('/scoring', methods=['GET'])
def score():
    cant_per_car = request.args.get('cant_per_car')
    hijos_afiliados = request.args.get('hijos_afiliados')
    mayor65_afiliados = request.args.get('mayor65_afiliados')
    salario = request.args.get('salario')
    edad = request.args.get('edad')
    meses_Afili = request.args.get('meses_Afili')
    prom_cantidad = request.args.get('prom_cantidad')
    prom_compras = request.args.get('prom_compras')
    ultima_compra = request.args.get('ultima_compra')
    categoria_A = request.args.get('categoria_A')
    categoria_B = request.args.get('categoria_B')
    categoria_C = request.args.get('categoria_C')
    categoria_D = request.args.get('categoria_D')
    estado_civil_1 = request.args.get('estado_civil_1')
    estado_civil_2 = request.args.get('estado_civil_2')
    estado_civil_3 = request.args.get('estado_civil_3')
    estado_civil_4 = request.args.get('estado_civil_4')
    estado_civil_5 = request.args.get('estado_civil_5')
    #genero_F = request.args.get('genero_F')
    genero_M = request.args.get('genero_M')
    identificadorTipoVivienda_A = request.args.get('identificadorTipoVivienda_A')
    identificadorTipoVivienda_F = request.args.get('identificadorTipoVivienda_F')
    identificadorTipoVivienda_H = request.args.get('identificadorTipoVivienda_H')
    identificadorTipoVivienda_O = request.args.get('identificadorTipoVivienda_O')
    identificadorTipoVivienda_P = request.args.get('identificadorTipoVivienda_P')
    tipoContrato_CO = request.args.get('tipoContrato_CO')
    tipoContrato_OC = request.args.get('tipoContrato_OC')
    tipoContrato_PR = request.args.get('tipoContrato_PR')
    tipoContrato_PS = request.args.get('tipoContrato_PS')
    tipoContrato_PT = request.args.get('tipoContrato_PT')
    tipoContrato_TF = request.args.get('tipoContrato_TF')
    tipoContrato_TI = request.args.get('tipoContrato_TI')

    model = request.args.get('model')
    tCred = request.args.get('tCred')

    print(tCred+" "+model+" "+cant_per_car+" "+ hijos_afiliados+" "+ mayor65_afiliados+" "+ salario+" "+ edad+" "+ meses_Afili+" "+ prom_cantidad+" "+ prom_compras+" "+ ultima_compra+" "+ categoria_A+" "+ categoria_B+" "+ categoria_C+" "+ categoria_D+" "+ estado_civil_1+" "+ estado_civil_2+" "+ estado_civil_3+" "+ estado_civil_4+" "+ estado_civil_5+" "+ genero_M+" "+ identificadorTipoVivienda_A+" "+ identificadorTipoVivienda_F+" "+ identificadorTipoVivienda_H+" "+ identificadorTipoVivienda_O+" "+ identificadorTipoVivienda_P+" "+ tipoContrato_CO+" "+ tipoContrato_OC+" "+ tipoContrato_PR+" "+ tipoContrato_PS+" "+ tipoContrato_PT+" "+tipoContrato_TF+" "+tipoContrato_TI)

    data = [[cant_per_car, hijos_afiliados, mayor65_afiliados, salario, edad, meses_Afili, prom_cantidad, prom_compras, ultima_compra, categoria_A, categoria_B, categoria_C, categoria_D, estado_civil_1, estado_civil_2, estado_civil_3, estado_civil_4, estado_civil_5, genero_M, identificadorTipoVivienda_A, identificadorTipoVivienda_F, identificadorTipoVivienda_H, identificadorTipoVivienda_O, identificadorTipoVivienda_P, tipoContrato_CO, tipoContrato_OC, tipoContrato_PR, tipoContrato_PS, tipoContrato_PT,tipoContrato_TF,tipoContrato_TI]]

    df = pd.DataFrame(data, columns = ['cant_per_car','hijos_afiliados','mayor65_afiliados','salario','edad','meses_Afili','prom_cantidad','prom_compras','ultima_compra','categoria_A','categoria_B','categoria_C','categoria_D','estado_civil_1','estado_civil_2','estado_civil_3','estado_civil_4','estado_civil_5','genero_M','identificadorTipoVivienda_A','identificadorTipoVivienda_F','identificadorTipoVivienda_H','identificadorTipoVivienda_O','identificadorTipoVivienda_P','tipoContrato_CO','tipoContrato_OC','tipoContrato_PR','tipoContrato_PS','tipoContrato_PT','tipoContrato_TF','tipoContrato_TI'])

    return Score_Clientes(df, tCred, model)

@app.route("/")
def index():
    return render_template("index.html");
