import json
from logging import exception
from flask import Flask,jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin


app = Flask(__name__)


#conexion de la base de datos
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "ptecnica"

#cors
CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})

conexion = MySQL(app)

@app.route('/encuesta', methods=['GET'])
def leerEncuestas():

    
        cursor = conexion.connection.cursor()
        #solicitando el numero de encuestas ralizadas
        sql="SELECT MAX(id),SUM(fb)/MAX(id),SUM(ws)/MAX(id),SUM(tw)/MAX(id),SUM(ig)/MAX(id),SUM(tt)/MAX(id) FROM encuesta" 
        cursor.execute(sql)
        datos=cursor.fetchall()
        encHechas=datos[0][0]

        totalfb=datos[0][1]
        totalws=datos[0][2]
        totaltw=datos[0][3]
        totalig=datos[0][4]
        totaltt=datos[0][5]

        #calculando red social favorita y menos favorita
        sql="SELECT fav, COUNT(*) FROM encuesta GROUP BY fav"
        cursor.execute(sql)
        datos=cursor.fetchall()
        favorita = datos[0][0]
        noFavorita=datos[len(datos)-1][0]

        #Calculando la red social mas usada por rango de edad
        def redMasUsadaEdades(A,B):
            try:
                sql= "SELECT SUM(fb)/MAX(id),SUM(ws)/MAX(id),SUM(tw)/MAX(id),SUM(ig)/MAX(id),SUM(tt)/MAX(id) FROM encuesta WHERE edad BETWEEN "+ str(A) +" AND "+ str(B) 
                cursor.execute(sql)
                datos=cursor.fetchall()
                numbers= {'Facebook':datos[0][0],'WhatsApp':datos[0][1],'Twitter':datos[0][2],'Instagram':datos[0][3],'TikTok':datos[0][4]}
                favorita= max(numbers, key = numbers.get)
                resp=[favorita,numbers.get(favorita)]
                return resp
            except Exception as ex:
                return 'Sin Datos'



        infoquest={'Encuestas-realizadas':encHechas,'Favorita':favorita,'NoFavorita':noFavorita,
                'totalFace':totalfb,'totalWhats':totalws,'totalTwi':totaltw,'totalIg':totalig,
                'totalTik':totaltt,'social18-25':redMasUsadaEdades(18,25),'social26-33':redMasUsadaEdades(26,33),
                'social34-40':redMasUsadaEdades(34,40),'social40+':redMasUsadaEdades(40,100)}
    
        return jsonify({'encuesta':infoquest})


    

def notfound(error):
    return "<h1>La pagina no existe</h1>"

@app.route('/encuesta', methods=['POST'])
def registrarEncuesta():
    try: #Recibiendo datos y añadiendolo a las db
        cursor = conexion.connection.cursor()
        sql = """INSERT INTO encuesta ( email, edad, sexo, fav, fb, ws, tw, ig, tt) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}')""".format(
                    request.json['email'],request.json['edad'],request.json['sexo'],
                    request.json['fav'] ,request.json['fb']   ,request.json['ws'],
                    request.json['tw']  ,request.json['ig']   ,request.json['tt'])
        cursor.execute(sql)
        conexion.connection.commit()
        return jsonify({'mensaje': 'Informacion almacenada'})  
    except Exception as ex:
        return jsonify({'mensaje': "Error"})   


if __name__ == '__main__':
    app.run()
