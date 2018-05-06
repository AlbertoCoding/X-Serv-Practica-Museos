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
#                 elif atributo.get('nombre') in datos:
#                     tmp = atributo.text
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
                elif atributo.get('nombre') == "CONTENT-URL":
                    url2 = atributo.text
                    museo.url = url2
                elif atributo.get('nombre') == "LOCALIZACION":
                    for subAtributo in atributo.findall('atributo'):
                        if subAtributo.get('nombre') == "NOMBRE-VIA":
                            nombre_via2 = subAtributo.text
                            museo.nombre_via = nombre_via2
                        if subAtributo.get('nombre') == "CLASE-VIAL":
                            clase_vial2 = subAtributo.text
                            museo.clase_vial = clase_vial2
                        if subAtributo.get('nombre') == "TIPO-NUM":
                            tipo_num2 = subAtributo.text
                            museo.tipo_num = tipo_num2
                        if subAtributo.get('nombre') == "NUM":
                            num2 = subAtributo.text
                            museo.num = num2
                        if subAtributo.get('nombre') == "LOCALIDAD":
                            localidad2 = subAtributo.text
                            museo.localidad = localidad2
                        if subAtributo.get('nombre') == "PROVINCIA":
                            provincia2 = subAtributo.text
                            museo.provincia = provincia2
                        if subAtributo.get('nombre') == "CODIGO-POSTAL":
                            codigo_postal2 = subAtributo.text
                            museo.codigo_postal = codigo_postal2
                        if subAtributo.get('nombre') == "BARRIO":
                            barrio2 = subAtributo.text
                            museo.barrio = barrio2
                        if subAtributo.get('nombre') == "DISTRITO":
                            distrito2= subAtributo.text
                            museo.distrito = distrito2
                        if subAtributo.get('nombre') == "COORDENADA-X":
                            coordenada_x2 = subAtributo.text
                            museo.coordenada_x = coordenada_x2
                        if subAtributo.get('nombre') == "COORDENADA-Y":
                            coordenada_y2 = subAtributo.text
                            museo.coordenada_y = coordenada_y2
                        if subAtributo.get('nombre') == "LATITUD":
                            latitud2 = subAtributo.text
                            museo.latitud = latitud2
                        if subAtributo.get('nombre') == "LONGITUD":
                            longitud2 = subAtributo.text
                            museo.longitud = longitud2
                if atributo.get('nombre') == "DATOSCONTACTOS":
                    email2 = "No proporcionado"
                    telefono2 = "No proporcionado"
                    fax2 = "No proporcionado"
                    for subAtributo in atributo.findall('atributo'):
                        if subAtributo.get('nombre') == "TELEFONO":
                            telefono2 = subAtributo.text
                            museo.telefono = telefono2
                        if subAtributo.get('nombre') == "FAX":
                            fax2 = subAtributo.text
                            museo.fax = fax2
                        if subAtributo.get('nombre') == "EMAIL":
                            email2 = subAtributo.text
                            museo.email = email2
                    continue
            museo.save()


