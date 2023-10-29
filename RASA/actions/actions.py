

from tkinter import ARC
from typing import Any, Text, Dict, List
from urllib import response
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from swiplserver import PrologMQI
import random
import graphviz
import csv
import os
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree



model=DecisionTreeClassifier(max_depth=5)#arbol de decision
#mappings para arboles
switch_categoria = {
   'accion': 1,
   'aventura': 2,
   'vehiculos': 3,
   'deportes': 4,
   'mmo': 5,
   'rpg': 6,
   'sandbox': 7,
   'indie': 8,
  'shooter': 9,
                    
}
switch_productora = {
  'cd project red': 1,
  'mojang': 2,
  'rockstar games': 3,
  'blizzard': 4,
  'nintendo': 5,
  'riot': 6,
  'krafton': 7,
  'hoyoverse': 8,
  'wargaming': 9,
  'hi rez': 10,
  'bethesda': 11,
  'ubisoft': 12,
  'overkill': 13,
  'hello games': 14,
  'valve': 15,
  'psyonix': 16,
  'hoyoverse': 17,
  'new world interactive': 18,
  'void interactive': 19,
  'bohemia interactive': 20,
  'ea': 21,
  'tripwire interactive': 22,
  'netherrealm': 23,
  'indie stone': 24,
  'yager': 25,
  'playdead': 26,
  'gaijin': 27,
  'studio mdhr': 28,
  'team cherry': 29,
  'smartly dressed': 30,
  'rebellion': 31,
  'namco bandai': 32,
  'sector d2': 33,
  'techland': 34,
  'dice': 35,
  'kojima': 36,
                    
}




class ActionDarJuegosMejoresCat(Action):
    def name(self) -> Text:
        return "action_dar_mejores_juegos_cat"
    
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        genero = tracker.get_slot('generoUsar')
        with PrologMQI(port=8000) as mqi:
            with mqi.create_thread() as prolog_thread:
                prolog_thread.query("consult('C:/Users/usuario/Desktop/Universidad/Segundo semestre Tercer anio/Cosas exploratoria/JuegosProlog.pl')")
                response = prolog_thread.query(f"videojuegos_por_rating_mayor_categoria(7,{genero},Videojuegos)")
        
        dispatcher.utter_message(text=f"Los siguientes son los mejores juegos del genero de {genero}:")
        juegos = response[0]['Videojuegos']
        for juego in juegos:
            juego_formateado = juego.replace("_", " ").title()
            dispatcher.utter_message(text=f"- {juego_formateado}")
        return []
class ActionDarJuegosPeoresCat(Action):
    def name(self) -> Text:
        return "action_dar_peores_juegos_cat"
    
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        genero = tracker.get_slot('generoUsar')
        with PrologMQI(port=8000) as mqi:
            with mqi.create_thread() as prolog_thread:
                prolog_thread.query("consult('C:/Users/usuario/Desktop/Universidad/Segundo semestre Tercer anio/Cosas exploratoria/JuegosProlog.pl')")
                response = prolog_thread.query(f"videojuegos_por_rating_menor_categoria(5,{genero},Videojuegos)")
        
        dispatcher.utter_message(text=f"Los siguientes son los peores juegos del genero de {genero}:")
        juegos = response[0]['Videojuegos']
        for juego in juegos:
            juego_formateado = juego.replace("_", " ").title()
            dispatcher.utter_message(text=f"- {juego_formateado}")
        return []
class ActionDarJuegosCat(Action):
    def name(self) -> Text:
        return "action_dar_juegos_cat"
    
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        genero = tracker.get_slot('generoUsar')
        with PrologMQI(port=8000) as mqi:
            with mqi.create_thread() as prolog_thread:
                prolog_thread.query("consult('C:/Users/usuario/Desktop/Universidad/Segundo semestre Tercer anio/Cosas exploratoria/JuegosProlog.pl')")
                response = prolog_thread.query(f"videojuegos_por_categoria({genero}, Videojuegos)")
        
        dispatcher.utter_message(text=f"Los siguientes son algunos juegos del genero de {genero}:")
        juegos = response[0]['Videojuegos']
        for juego in juegos:
            juego_formateado = juego.replace("_", " ").title()
            dispatcher.utter_message(text=f"- {juego_formateado}")
        return []
    
class ActionDarJuegosPrecio(Action):
    def name(self) -> Text:
        return "action_dar_juegos_a_precio"
    
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
     
        precio_entities = tracker.latest_message['entities']
        precio_value = None

        for entity in precio_entities:
            if entity['entity'] == 'precio':
                precio_value = entity['value']

        if precio_value is not None:
            precio_str = str(precio_value)
        with PrologMQI(port=8000) as mqi:
            with mqi.create_thread() as prolog_thread:
                prolog_thread.query("consult('C:/Users/usuario/Desktop/Universidad/Segundo semestre Tercer anio/Cosas exploratoria/JuegosProlog.pl')")
                response = prolog_thread.query(f"videojuegos_por_precio({precio_str},Videojuegos)")
        
        dispatcher.utter_message(text=f"Estos son algunos juegos con valor de {precio_str} dolares:")
        juegos = response[0]['Videojuegos']
        for juego in juegos:
            juego_formateado = juego.replace("_", " ").title()
            dispatcher.utter_message(text=f"- {juego_formateado}")
        return []    

class ActionDarJuegosGratis(Action):
    def name(self) -> Text:
        return "action_dar_juegos_gratis"
    
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
        with PrologMQI(port=8000) as mqi:
            with mqi.create_thread() as prolog_thread:
                prolog_thread.query("consult('C:/Users/usuario/Desktop/Universidad/Segundo semestre Tercer anio/Cosas exploratoria/JuegosProlog.pl')")
                response = prolog_thread.query(f"videojuegos_por_precio(0, Videojuegos)")
        
        dispatcher.utter_message(text=f"Los siguientes son algunos juegos gratis del momento:")
        juegos = response[0]['Videojuegos']
        for juego in juegos:
            juego_formateado = juego.replace("_", " ").title()
            dispatcher.utter_message(text=f"- {juego_formateado}")
        return []
class ActionDarJuegosPrecioMayor(Action):
    def name(self) -> Text:
        return "action_dar_juegos_mayor_a_precio"
    
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        precio_entities = tracker.latest_message['entities']
        precio_value = None
        for entity in precio_entities:
            if entity['entity'] == 'precio':
                precio_value = entity['value']

        if precio_value is not None:
            precio_str = str(precio_value)
        with PrologMQI(port=8000) as mqi:
            with mqi.create_thread() as prolog_thread:
                prolog_thread.query("consult('C:/Users/usuario/Desktop/Universidad/Segundo semestre Tercer anio/Cosas exploratoria/JuegosProlog.pl')")
                response = prolog_thread.query(f"videojuegos_por_precio_mayor({precio_str},Videojuegos)")
        
        dispatcher.utter_message(text=f"Estos son algunos juegos con valor mayor a {precio_str} dolares:")
        juegos = response[0]['Videojuegos']
        for juego in juegos:
            juego_formateado = juego.replace("_", " ").title()
            dispatcher.utter_message(text=f"- {juego_formateado}")
        return []
class ActionDarJuegosPrecioMenor(Action):
    def name(self) -> Text:
        return "action_dar_juegos_menor_a_precio"
    
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        precio_entities = tracker.latest_message['entities']
        precio_value = None

        for entity in precio_entities:
            if entity['entity'] == 'precio':
                precio_value = entity['value']

        if precio_value is not None:
            precio_str = str(precio_value)
        with PrologMQI(port=8000) as mqi:
            with mqi.create_thread() as prolog_thread:
                prolog_thread.query("consult('C:/Users/usuario/Desktop/Universidad/Segundo semestre Tercer anio/Cosas exploratoria/JuegosProlog.pl')")
                response = prolog_thread.query(f"videojuegos_por_precio_menor({precio_str},Videojuegos)")
        
        dispatcher.utter_message(text=f"Estos son algunos juegos con valor menor a {precio_str} dolares:")
        juegos = response[0]['Videojuegos']
        for juego in juegos:
            juego_formateado = juego.replace("_", " ").title()
            dispatcher.utter_message(text=f"- {juego_formateado}")
        return []
class ActionDarJuegosRatingMayor(Action):
    def name(self) -> Text:
        return "action_dar_juegos_mayor_rating"
    
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        rating_entities = tracker.latest_message['entities']
        rating_value = None
        rating_str = ""  # Asigna un valor predeterminado

        for entity in rating_entities:
            if entity['entity'] == 'rating':
                rating_value = entity['value']

        if rating_value is not None:
            rating_str = str(rating_value)
        with PrologMQI(port=8000) as mqi:
            with mqi.create_thread() as prolog_thread:
                prolog_thread.query("consult('C:/Users/usuario/Desktop/Universidad/Segundo semestre Tercer anio/Cosas exploratoria/JuegosProlog.pl')")
                response = prolog_thread.query(f"videojuegos_por_rating_mayor({rating_str},Videojuegos)")
        
        dispatcher.utter_message(text=f"Estos son algunos juegos con rating mayor a {rating_str}:")
        juegos = response[0]['Videojuegos']
        for juego in juegos:
            juego_formateado = juego.replace("_", " ").title()
            dispatcher.utter_message(text=f"- {juego_formateado}")
        return []
class ActionDarJuegosRatingMenor(Action):
    def name(self) -> Text:
        return "action_dar_juegos_menor_rating"
    
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        rating_entities = tracker.latest_message['entities']
        rating_value = None
        rating_str = "" 
        for entity in rating_entities:
            if entity['entity'] == 'rating':
                rating_value = entity['value']

        if rating_value is not None:
            rating_str = str(rating_value)
        with PrologMQI(port=8000) as mqi:
            with mqi.create_thread() as prolog_thread:
                prolog_thread.query("consult('C:/Users/usuario/Desktop/Universidad/Segundo semestre Tercer anio/Cosas exploratoria/JuegosProlog.pl')")
                response = prolog_thread.query(f"videojuegos_por_rating_menor({rating_str},Videojuegos)")
        
        dispatcher.utter_message(text=f"Estos son algunos juegos con rating menor a {rating_str}:")
        juegos = response[0]['Videojuegos']
        for juego in juegos:
            juego_formateado = juego.replace("_", " ").title()
            dispatcher.utter_message(text=f"- {juego_formateado}")
        return []
class ActionDarJuegosRating(Action):
    def name(self) -> Text:
        return "action_dar_juegos_rating"
    
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        rating_entities = tracker.latest_message['entities']
        rating_value = None
        rating_str = "" 
        for entity in rating_entities:
            if entity['entity'] == 'rating':
                rating_value = entity['value']

        if rating_value is not None:
            rating_float=float(rating_value)
            rating_str = str(rating_float)
        with PrologMQI(port=8000) as mqi:
            with mqi.create_thread() as prolog_thread:
                prolog_thread.query("consult('C:/Users/usuario/Desktop/Universidad/Segundo semestre Tercer anio/Cosas exploratoria/JuegosProlog.pl')")
                response = prolog_thread.query(f"videojuegos_por_rating({rating_str},Videojuegos)")
        
        dispatcher.utter_message(text=f"Estos son algunos juegos con rating de {rating_str}:")
        juegos = response[0]['Videojuegos']
        for juego in juegos:
            juego_formateado = juego.replace("_", " ").title()
            dispatcher.utter_message(text=f"- {juego_formateado}")
        return []
class ActionDarInfoJuego(Action):
    def name(self) -> Text:
        return "action_dar_info_juego"
    
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        juego = tracker.get_slot('juegoSolicitado')
        juegoMod = juego.lower().replace(" ", "_")
        with PrologMQI(port=8000) as mqi:
            with mqi.create_thread() as prolog_thread:
                prolog_thread.query("consult('C:/Users/usuario/Desktop/Universidad/Segundo semestre Tercer anio/Cosas exploratoria/JuegosProlog.pl')")
                response = prolog_thread.query(f"datos_juego({juegoMod}, Precio, Categoria, Rating)")
        
        
        
        if response:
            juego_data = response[0]
            message = f"Estos son los datos del juego {juego}:"
            
            for key, value in juego_data.items():
                message += f"\n- {key.capitalize()}: {value}"
            
            dispatcher.utter_message(text=message)
        else:
            dispatcher.utter_message(text=f"No se encontraron datos para el juego {juego}.")
        return []
class ActionDarPaginaJuego(Action):
    def name(self) -> Text:
        return "action_dar_link_juego"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        juego = tracker.get_slot('juegoSolicitado')
        if juego is not None:
            juegoMod = juego.lower().replace(" ", "_")
        else:
            juegoMod = "1"
        with PrologMQI(port=8000) as mqi:
            with mqi.create_thread() as prolog_thread:
                prolog_thread.query("consult('C:/Users/usuario/Desktop/Universidad/Segundo semestre Tercer anio/Cosas exploratoria/JuegosProlog.pl')")
                response = prolog_thread.query(f"pagina({juegoMod},Pagina)")
        
        if response:
            dispatcher.utter_message(text=f"Aqui te paso el link de la pagina oficial del juego {juego}.")
            enlace = response[0]['Pagina']
            dispatcher.utter_message(text=f"- Pagina: {enlace}")
        else:
            dispatcher.utter_message(text=f"No se encontraron datos para el juego {juego}.")
        
       
        return []
class ActionDarDespedida(Action):
    def name(self) -> Text:
        return "action_bot_say_goodbye"
 
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        frases=["Adios","Hasta luego","Nos vemos mas tarde","Hasta la proxima","Chau","Cuidate","Hasta pronto"]
        frase_random=random.choice(frases)
        nombre = tracker.get_slot('nombreGuardado')
        if nombre is not None:
            dispatcher.utter_message(text=f"{frase_random} {nombre}!.")
        else:
            dispatcher.utter_message(text=f"{frase_random}!.")
        return []
class ActionDarBienvenida(Action):
    def name(self) -> Text:
        return "action_bot_say_hello"
    
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        frases= ["Hola", "Bienvenido", "Saludos", "Hola de nuevo", "Encantado de verte", "Bienvenido de nuevo", "Buenas, estoy aqui para ayudarte"]
        frase_random=random.choice(frases)
        nombre = tracker.get_slot('nombreGuardado')
        if nombre is not None:
            dispatcher.utter_message(text=f"{frase_random} {nombre}!.")
            
        else:
            dispatcher.utter_message(text=f"{frase_random}!.")
          
        return [] 
class ActionDarGracias(Action):
    def name(self) -> Text:
        return "action_bot_say_your_welcome"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        frases= ["Con gusto", "Fue un placer", "Un placer", "Encantado de que te haya sido util", "No, de nada", "Estoy aqui para ayudarte"]
        frase_random=random.choice(frases)
        nombre = tracker.get_slot('nombreGuardado')
        if nombre is not None:
            dispatcher.utter_message(text=f"{frase_random} {nombre}!.")
            
        else:
            dispatcher.utter_message(text=f"{frase_random}!.")
          
        return []
    
class ActionGuardarJuegoGustado(Action):
    def name(self) -> Text:
        return "action_save_game_liked"
    
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        frases= ["Me parece fenomenal", "Me parece espectacular", "Me alegro"]
        frase_random=random.choice(frases)
        nombre = tracker.get_slot('nombreGuardado')
        if nombre is None:
            dispatcher.utter_message(text=f"{frase_random}!.")
        else:
            juego = tracker.get_slot('juegoSolicitado')
            juegoMod = juego.lower().replace(" ", "_")
            nombre = tracker.get_slot('nombreGuardado')
            if juego is not None:
                if nombre is not None:
                    archivo_csv ='C:\\Users\\usuario\\Desktop\\Universidad\\Segundo semestre Tercer anio\\CSVS\\' + nombre
                    dispatcher.utter_message(text=f"{frase_random} {nombre}!.")
                
                    with PrologMQI(port=8000) as mqi:
                        with mqi.create_thread() as prolog_thread:
                            prolog_thread.query("consult('C:/Users/usuario/Desktop/Universidad/Segundo semestre Tercer anio/Cosas exploratoria/JuegosProlog.pl')")
                            response = prolog_thread.query(f"caracteristicas_videojuego({juegoMod},Categoria,Precio,Rating,Conexion,Productora)")
     
                    if response:
                    
                        categoria=response[0]['Categoria']
                        precio=response[0]['Precio']
                        rating=response[0]['Rating']
                        conexion=response[0]['Conexion']
                        productora=response[0]['Productora']
                    

                        if not os.path.exists(archivo_csv):
                            with open(archivo_csv, 'w', newline='') as archivo_csv:
                                writer = csv.writer(archivo_csv)
                                writer.writerow(["categoria","precio","rating","conexion","productora","gusto"])
                                writer.writerow([categoria, precio, rating, conexion, productora,1])
                        else:
                            with open(archivo_csv, 'a', newline='') as archivo_csv:
                                writer = csv.writer(archivo_csv)
                                writer.writerow([categoria, precio, rating, conexion, productora,1])
                    
          
        return [] 
class ActionGuardarJuegoNoGustado(Action):
    def name(self) -> Text:
        return "action_save_game_disliked"
    
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        frases= ["Ok", "Me parece bien", "Interesante"]
        frase_random=random.choice(frases)
        nombre = tracker.get_slot('nombreGuardado')
        if nombre is None:
            dispatcher.utter_message(text=f"{frase_random}!.")
        else:
            juego = tracker.get_slot('juegoSolicitado')
            juegoMod = juego.lower().replace(" ", "_")
            nombre = tracker.get_slot('nombreGuardado')
            if juego is not None:
            
                if nombre is not None:
                    archivo_csv ='C:\\Users\\usuario\\Desktop\\Universidad\\Segundo semestre Tercer anio\\CSVS\\' + nombre
                    dispatcher.utter_message(text=f"{frase_random} {nombre}!.")
                
                    with PrologMQI(port=8000) as mqi:
                        with mqi.create_thread() as prolog_thread:
                            prolog_thread.query("consult('C:/Users/usuario/Desktop/Universidad/Segundo semestre Tercer anio/Cosas exploratoria/JuegosProlog.pl')")
                            response = prolog_thread.query(f"caracteristicas_videojuego({juegoMod},Categoria,Precio,Rating,Conexion,Productora)")
     
                    if response:
                    
                        categoria=response[0]['Categoria']
                        precio=response[0]['Precio']
                        rating=response[0]['Rating']
                        conexion=response[0]['Conexion']
                        productora=response[0]['Productora']
                    

                        if not os.path.exists(archivo_csv):
                            with open(archivo_csv, 'w', newline='') as archivo_csv:
                                writer = csv.writer(archivo_csv)
                                writer.writerow(["categoria","precio","rating","conexion","productora","gusto"])
                                writer.writerow([categoria, precio, rating, conexion, productora,0])
                        else:
                            with open(archivo_csv, 'a', newline='') as archivo_csv:
                                writer = csv.writer(archivo_csv)
                                writer.writerow([categoria, precio, rating, conexion, productora,0])  
        return []
class ActionRecomendarJuego(Action):
    def name(self) -> Text:
        return "action_recommend_game"
    
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        frases= ["Este juego te va a encantar", "El siguiente juego sera de tu agrado", "Te recomendaria el siguiente juego"]
        frase_random=random.choice(frases)
        nombre = tracker.get_slot('nombreGuardado')
        if nombre is not None:
             archivo_csv ='C:\\Users\\usuario\\Desktop\\Universidad\\Segundo semestre Tercer anio\\CSVS\\' + nombre
             dispatcher.utter_message(text=f"{frase_random} {nombre}!.")
             df=pd.read_csv(archivo_csv)
             df['categoria'] = df['categoria'].map(switch_categoria)
             df['productora'] = df['productora'].map(switch_productora)
             
             x= df.drop(columns=['gusto'])
             print("X")
             print(x)
             y=df['gusto']
            
             print(y)
            
             #model=DecisionTreeClassifier(max_depth=5)
             print(model)
             model.fit(x,y)
             dot_data = tree.export_graphviz(
                model, 
                out_file=None,
                feature_names=x.columns.tolist(),
                class_names=df['gusto'].astype(str).unique().tolist(),
                filled=True, rounded=True,
                special_characters=True)

             graph = graphviz.Source(dot_data)
             nombre_arbol='arbolPreview_' + nombre
             graph.render(nombre_arbol)


             print(model.score(x,y))
             with PrologMQI(port=8000) as mqi:
                    with mqi.create_thread() as prolog_thread:
                        prolog_thread.query("consult('C:/Users/usuario/Desktop/Universidad/Segundo semestre Tercer anio/Cosas exploratoria/JuegosProlog.pl')")
                        response1 = prolog_thread.query(f"todos_los_juegos(Juegos)")
              
             juego_random=random.choice(response1[0]['Juegos'])
             print(juego_random)
             with PrologMQI(port=8000) as mqi:
                    with mqi.create_thread() as prolog_thread:
                        prolog_thread.query("consult('C:/Users/usuario/Desktop/Universidad/Segundo semestre Tercer anio/Cosas exploratoria/JuegosProlog.pl')")
                        response = prolog_thread.query(f"caracteristicas_videojuego({juego_random},Categoria,Precio,Rating,Conexion,Productora)")
     
             if response:
                     
                    categoria=response[0]['Categoria']
                    precio=response[0]['Precio']
                    rating=response[0]['Rating']
                    conexion=response[0]['Conexion']
                    productora=response[0]['Productora']        
                    
                    dato_prueba = [[switch_categoria.get(categoria,None),precio,rating,conexion,switch_productora.get(productora,None)]]
                    columnas = x.columns.tolist()  
                    dato_prueba_df = pd.DataFrame(dato_prueba, columns=columnas)  
                    ypred = model.predict(dato_prueba_df)
                    
                    
                 
                    
                    contador=1
                    print(ypred)
                    print(x)
                    while(ypred[0]==0):
                         print("contador:")
                         contador=contador+1 
                         print(contador)
                         juego_random=random.choice(response1[0]['Juegos'])
                         print(juego_random)
                         with PrologMQI(port=8000) as mqi:
                            with mqi.create_thread() as prolog_thread:
                                prolog_thread.query("consult('C:/Users/usuario/Desktop/Universidad/Segundo semestre Tercer anio/Cosas exploratoria/JuegosProlog.pl')")
                                response2 = prolog_thread.query(f"caracteristicas_videojuego({juego_random},Categoria,Precio,Rating,Conexion,Productora)")
                         print(response2)
                         if response2:
                            categoria=response2[0]['Categoria']
                            precio=response2[0]['Precio']
                            rating=response2[0]['Rating']
                            conexion=response2[0]['Conexion']
                            productora=response2[0]['Productora']
                            df['categoria'] = df['categoria'].map(switch_categoria)
                            df['productora'] = df['productora'].map(switch_productora)
                            
                                    
                            dato_prueba = [[switch_categoria.get(categoria,None),precio,rating,conexion,switch_productora.get(productora,None)]]
                            columnas = x.columns.tolist()  
                            dato_prueba_df = pd.DataFrame(dato_prueba, columns=columnas)  
                            ypred = model.predict(dato_prueba_df)
                                  
                            print(ypred)
                    if(ypred[0]==1):
                        juego_tipeado=juego_random.replace("_", " ").title()
                        dispatcher.utter_message(text=f"{juego_tipeado}")
                        print(juego_tipeado)
        
        else:
            dispatcher.utter_message("Por favor inicie sesion para asi te puedo recomendar juegos!")
        return []

class ActionDarLinkUnJuegoGustado(Action):
    def name(self) -> Text:
        return "action_give_link_liked"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        frases= ["Me alegro!", "Que bien!"]
        frase_random=random.choice(frases)
        nombre = tracker.get_slot('nombreGuardado')
        if nombre is None:
            dispatcher.utter_message(text=f"{frase_random}!.")
        else:
            archivo_csv ='C:\\Users\\usuario\\Desktop\\Universidad\\Segundo semestre Tercer anio\\CSVS\\' + nombre
            df = pd.read_csv(archivo_csv)
            filas_gusto_1 = df[df['gusto'] == 1]
            if not filas_gusto_1.empty:
                
                fila_elegida = filas_gusto_1.sample()#Elijo fila al azar con gusto=1

                categoria = fila_elegida['categoria'].values[0]
                precio = fila_elegida['precio'].values[0]
                rating = fila_elegida['rating'].values[0]
                conexion = fila_elegida['conexion'].values[0]
                productora = fila_elegida['productora'].values[0]
                print('categoria')
                print(categoria)
                print('precio')
                print(precio)
                print('rating')
                print(rating)
                print('conexion')
                print(conexion)
                print('productora')
                print(productora)
                with PrologMQI(port=8000) as mqi:
                            with mqi.create_thread() as prolog_thread:
                                prolog_thread.query("consult('C:/Users/usuario/Desktop/Universidad/Segundo semestre Tercer anio/Cosas exploratoria/JuegosProlog.pl')")
                                response = prolog_thread.query(f"buscar_juego({categoria}, {precio},{rating},{conexion}, {productora}, Juego)")
                if response:
                    with PrologMQI(port=8000) as mqi:    
                        with mqi.create_thread() as prolog_thread:
                                prolog_thread.query("consult('C:/Users/usuario/Desktop/Universidad/Segundo semestre Tercer anio/Cosas exploratoria/JuegosProlog.pl')")
                                response2 = prolog_thread.query(f"pagina({response[0]['Juego']},Pagina)")
                    
                    if response2:
                        print('entre response 2')
                        dispatcher.utter_message(text=f"{frase_random}!")
                        dispatcher.utter_message(text=f"Esta informacion te va a gustar!")
                        enlace = response2[0]['Pagina']
                        dispatcher.utter_message(text=f"-{enlace}")
            else:
                dispatcher.utter_message(text=f"{frase_random}!.")
            
        return []
    
class ActionRecomendarJuegoSinTrain(Action):
    def name(self) -> Text:
        return "action_recommend_game_nc"
    
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        frases= ["Que pena", "No te preocupes estoy aqui para ayudarte", "Arriba el animo"]
        frase_random=random.choice(frases)
        
        nombre = tracker.get_slot('nombreGuardado')
        archivo_csv ='C:\\Users\\usuario\\Desktop\\Universidad\\Segundo semestre Tercer anio\\RASA\\arbolPreview_' + nombre
        if nombre is not None and os.path.isfile(archivo_csv):
               print('entre:')   
               print("El modelo del arbol esta entrenado.")
               with PrologMQI(port=8000) as mqi:
                    with mqi.create_thread() as prolog_thread:
                        prolog_thread.query("consult('C:/Users/usuario/Desktop/Universidad/Segundo semestre Tercer anio/Cosas exploratoria/JuegosProlog.pl')")
                        response1 = prolog_thread.query(f"todos_los_juegos(Juegos)")
              
               juego_random=random.choice(response1[0]['Juegos'])
               print(juego_random)
               with PrologMQI(port=8000) as mqi:
                        with mqi.create_thread() as prolog_thread:
                            prolog_thread.query("consult('C:/Users/usuario/Desktop/Universidad/Segundo semestre Tercer anio/Cosas exploratoria/JuegosProlog.pl')")
                            response = prolog_thread.query(f"caracteristicas_videojuego({juego_random},Categoria,Precio,Rating,Conexion,Productora)")
     
               if response:
                       archivo_csv ='C:\\Users\\usuario\\Desktop\\Universidad\\Segundo semestre Tercer anio\\CSVS\\' + nombre
                       dispatcher.utter_message(text=f"{frase_random} {nombre}!.")
                       df=pd.read_csv(archivo_csv)
                       df['categoria'] = df['categoria'].map(switch_categoria)
                       df['productora'] = df['productora'].map(switch_productora)    
                       x= df.drop(columns=['gusto'])
                       print("X")
                       print(x)
                       y=df['gusto']
                       categoria=response[0]['Categoria']
                       precio=response[0]['Precio']
                       rating=response[0]['Rating']
                       conexion=response[0]['Conexion']
                       productora=response[0]['Productora']        
                    
                       dato_prueba = [[switch_categoria.get(categoria,None),precio,rating,conexion,switch_productora.get(productora,None)]]
                       columnas = x.columns.tolist()  
                       dato_prueba_df = pd.DataFrame(dato_prueba, columns=columnas)  
                       ypred = model.predict(dato_prueba_df)
                    
                    
                 
                    
                       contador=1
                       print(ypred)
                       print(x)
                       contador=0
                       while(ypred[0]==0):
                               
                             print("contador:")
                             contador=contador+1 
                             print(contador)
                             juego_random=random.choice(response1[0]['Juegos'])
                             print(juego_random)
                             with PrologMQI(port=8000) as mqi:
                                with mqi.create_thread() as prolog_thread:
                                    prolog_thread.query("consult('C:/Users/usuario/Desktop/Universidad/Segundo semestre Tercer anio/Cosas exploratoria/JuegosProlog.pl')")
                                    response2 = prolog_thread.query(f"caracteristicas_videojuego({juego_random},Categoria,Precio,Rating,Conexion,Productora)")
                             print(response2)
                             if response2:
                                categoria=response2[0]['Categoria']
                                precio=response2[0]['Precio']
                                rating=response2[0]['Rating']
                                conexion=response2[0]['Conexion']
                                productora=response2[0]['Productora']
                                df['categoria'] = df['categoria'].map(switch_categoria)
                                df['productora'] = df['productora'].map(switch_productora)
                            
                                    
                                dato_prueba = [[switch_categoria.get(categoria,None),precio,rating,conexion,switch_productora.get(productora,None)]]
                                columnas = x.columns.tolist()  
                                dato_prueba_df = pd.DataFrame(dato_prueba, columns=columnas)  
                                ypred = model.predict(dato_prueba_df)
                                  
                                print(ypred)
                             
                             contador=contador+1
                       if(ypred[0]==1):
                                juego_tipeado=juego_random.replace("_", " ").title()
                                dispatcher.utter_message(text=f"Tengo algo para animarte! Proba este juego:")
                                dispatcher.utter_message(text=f"{juego_tipeado}")
                                print(juego_tipeado)
        else:
            dispatcher.utter_message(text=f"{frase_random}!.")
        return []
            