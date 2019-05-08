#!/usr/bin/env python
# -*- coding: utf-8 -*-

from colorama import init
from termcolor import colored

init()
filesFolder = 'Solucion_Habitacional/Solucion_Habitacional'
filesPath = [
    # Program
    filesFolder + '/Program.cs',
    filesFolder + '/App.config',


    # Dominio
    # InterfacesRepositorio
    filesFolder + ".Dominio/InterfacesRepositorio/IRepositorioBarrio.cs",
    filesFolder + ".Dominio/InterfacesRepositorio/IRepositorioParametro.cs",
    filesFolder + ".Dominio/InterfacesRepositorio/IRepositorioPasante.cs",
    filesFolder + ".Dominio/InterfacesRepositorio/IRepositorioVivienda.cs",

    # Repositorios
    # ADO
    filesFolder + ".Dominio/Repositorios/ADO/RepositorioBarrio.cs",
    filesFolder + ".Dominio/Repositorios/ADO/RepositorioParametro.cs",
    filesFolder + ".Dominio/Repositorios/ADO/RepositorioPasante.cs",
    filesFolder + ".Dominio/Repositorios/ADO/RepositorioVivienda.cs",

    # Utilidades
    filesFolder + ".Dominio/Utilidades/UtilidadesDB.cs",

    filesFolder + ".Dominio/Barrio.cs",
    filesFolder + ".Dominio/IActiveRecord.cs",
    filesFolder + ".Dominio/Parametro.cs",
    filesFolder + ".Dominio/Pasante.cs",
    filesFolder + ".Dominio/Vivienda.cs",
    filesFolder + ".Dominio/VNueva.cs",
    filesFolder + ".Dominio/VUsada.cs",

    # Servicio
    # Utilities
    filesFolder + ".Servicio/Utilities/ObjectConversor.cs",

    filesFolder + ".Servicio/IServicioBarrio.cs",
    filesFolder + ".Servicio/IServicioParametro.cs",
    filesFolder + ".Servicio/IServicioPasante.cs",
    filesFolder + ".Servicio/IServicioVivienda.cs",
    filesFolder + ".Servicio/ServicioBarrio.svc.cs",
    filesFolder + ".Servicio/ServicioParametro.svc.cs",
    filesFolder + ".Servicio/ServicioPasante.svc.cs",
    filesFolder + ".Servicio/ServicioVivienda.svc.cs",
    filesFolder + ".Servicio/Web.config"
]

exported = open('exported.txt', "w")

numFiles = 0
errors = 0
for f in filesPath:
    try:
        fp = open(f, "r")
        print(colored(f, "green"))

        numFiles = numFiles + 1

        if numFiles != 1:
            exported.write("\n\n\n")
        else:
            from datetime import date
            exported.write(
                "Autogenerated file - {}\n\n\n".format(date.today().strftime("%B %d, %Y")))

        exported.write(r"// {}".format(f.split('/', )
                                       [len(f.split('/', ))-1].split('.', )[0]) + "\n")

        for cnt, line in enumerate(fp):
            if cnt != 0:
                exported.write(r"{}".format(line))
            else:
                # Slice 3 first character caus are not printables
                exported.write(r"{}".format(line)[3:])

        fp.close()

    except (OSError, IOError) as e:
        errors = errors + 1
        print(colored("Error! - {}".format(e), "white", "on_red"))

exported.close()
print("\n\nFinished!")
print(colored("\tFiles written: {}".format(numFiles), "green"))
print(colored("\tErrors: {}".format(errors), "red"))
