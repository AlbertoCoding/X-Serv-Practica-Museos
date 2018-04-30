from .models import Museo
import xml.etree.ElementTree as ET

def parser_xml(xml):
    tree = ET.parse(xml)
    contenidos = tree.getroot()
    for contenido in contenidos.findall('contenido'):
        for atributos in contenido.findall('atributos'):

            museo = Museo(museo_id=000000, nombre='No hay nombre disponible', descripcion='No hay descripcion disponible', accesibilidad=0)
            for atributo in atributos.findall('atributo'):
                if atributo.get('nombre') == "ID-ENTIDAD":
                    museo_id2 = atributo.text
                    museo.museo_id = museo_id2
                elif atributo.get('nombre') == "NOMBRE":
                    nombre2 = atributo.text
                    museo.nombre = nombre2
                elif atributo.get('nombre') == "DESCRIPCION-ENTIDAD":
                    descripcion2 = atributo.text
                    museo.descripcion = descripcion2
                elif atributo.get('nombre') == "HORARIO":
                    horario2 = atributo.text
                    museo.horario = horario2
                elif atributo.get('nombre') == "EQUIPAMIENTO":
                    equipamiento2 = atributo.text
                    museo.equipamiento = equipamiento2
                elif atributo.get('nombre') == "TRANSPORTE":
                    transporte2 = atributo.text
                    museo.transporte = transporte2
                elif atributo.get('nombre') == "ACCESIBILIDAD":
                    accesibilidad2 = atributo.text
                    museo.accesibilidad = accesibilidad2
     



            museo.save()


