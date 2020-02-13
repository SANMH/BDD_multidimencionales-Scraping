# Proyecto de bases de datos multidimensional.
https://raw.githubusercontent.com/SANMH/BDD_multidimencionales-Scraping/master/img/logoepn.jpg

el objetivo de este proyecto es centralizar la información de diversas fuentes de información como los son bases de datos de naturaleza SQL y noSQL ademas de información raspada desde la web de algun sitio como: **Tweeter, facebook e Instagran**.

**Integrantes
>Fernando Sanmartin	

>Bryan Farinango

>Bryan Perez

>Dennis Nunez

# Software usado

-ElasticSearch
-Logstash
-Kibana
![imagen 1 funcionamiento de dataLake Tenemos todas nuestras fuentes de datos, que envían información a Logstash, que al tener muchos plugins de entrada y salida, podemos introducir gran cantidad de datos. Esos datos son procesados antes de almacenarlos en la base de datos de Elasticsearch, y con Kibana se montan las visualizaciones que accedan a esa información, para poder así monitorizarlas.](https://dc722jrlp2zu8.cloudfront.net/media/cache/ac/fb/acfb8540e183c26ce471e0370d80d470.webp)
-Python
![enter image description here](https://gameartschool.eu/wp-content/uploads/2018/09/python-logo-master-v3-TM.png)
-CouchDB (noSQL)
-MongoDB (noSQL)
-MySql (SQL)
![enter image description here](https://image.slidesharecdn.com/20100123dodugi-alt-100124141539-phpapp02/95/couchdb-vs-mongodb-2-728.jpg?cb=1285493025)

## Carpetas y archivos

en la carpeta cosecha se encontrara los scripts para el raspado de información de Tweeter e Instagran ademas de la transformación de datos por parte de Logstach y una pagina que muestra los resultados del análisis realizado. 

## Codigo base de Scraping

   import couchdb #Libreria de CouchDB (requiere ser instalada primero)
 from tweepy import Stream #tweepy es la librería que trae tweets desde la API de Twitter (requiere ser instalada primero)
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json #Librería para manejar archivos JSON

#En esta sección se debe ingresar los tokens generados como usuarios develop de Tweeter.
ckey = ""
csecret = ""
atoken = ""
asecret = ""

class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            dictTweet["_id"] = str(dictTweet['id'])
           
            doc = db.save(dictTweet) #Aqui se guarda el tweet en la base de couchDB
            print ("Guardado " + "=> " + dictTweet["_id"])
        except:
            print ("Documento ya existe")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

#Setear la URL del servidor de couchDB
server = couchdb.Server('http://localhost:5984/')
try:
    #Si no existe la Base de datos la crea
    db = server.create('transito')
except:
    #Caso contrario solo conectarse a la base existente
    db = server['transito']
    
#Aquí se define el bounding box con los limites geográficos donde recolectar los tweets
twitterStream.filter(track=["AMTQuito","ATMGuayaquil","ECU911Loja","emov_ep","ECU911Ambato"])


## Recolectando Información en CouchDB




