import tkinter as tk
from tkinter import messagebox


class Participante:
    def __init__(self, nombre, institucion):
        self.nombre = nombre
        self.institucion = institucion

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, insitucion: {self.institucion}")


class BandaEscolar(Participante):
    def __init__(self, nombre, institucion, categoria):
        super().__init__(nombre, institucion)
        self.categoria = categoria
        self.puntaje = {}




class ConcursoBandasApp:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Concurso de Bandas - Quetzaltenango")
        self.ventana.geometry("500x300")
        self.Bandas =[]
        self.menu()

        tk.Label(
            self.ventana,
            text="Sistema de Inscripción y Evaluación de Bandas Escolares\nConcurso 14 de Septiembre - Quetzaltenango",
            font=("Arial", 12, "bold"),
            justify="center"
        ).pack(pady=50)

        self.ventana.mainloop()

    def menu(self):
        barra = tk.Menu(self.ventana)
        opciones = tk.Menu(barra, tearoff=0)
        opciones.add_command(label="Inscribir Banda", command=self.ventana_inscribir_banda)
        opciones.add_command(label="Registrar Evaluación", command=self.registrar_evaluacion)
        opciones.add_command(label="Listar Bandas", command=self.listar_bandas)
        opciones.add_command(label="Ver Ranking", command=self.ver_ranking)
        opciones.add_separator()
        opciones.add_command(label="Salir", command=self.ventana.quit)
        barra.add_cascade(label="Opciones", menu=opciones)
        self.ventana.config(menu=barra)
    def buscar(self, nombre):
        for banda in self.Bandas:
            if banda.nombre.lower() == nombre.lower():
                messagebox.showinfo("Banda encontrada", f"Banda inscrita, se les asignará la evaluacion a la banda:"
                                                        f"\n Nombre: {banda.nombre}, Institución: {banda.insitucion}, Categoria: {banda.categoria}")
            else:
                messagebox.showerror("Error", "No existe una banda con ese nombre")
    def ventana_inscribir_banda(self):
        print("Se abrió la ventana: Inscribir Banda")
        ventana_inscribir = tk.Tk()
        ventana_inscribir.title("Inscribir Banda")


        ventana_inscribir.geometry("700x300")
        titulo = tk.Label(ventana_inscribir, text="Inscribir Banda", font=("Arial", 16, "bold"))
        etiqueta_nombre = tk.Label(ventana_inscribir, text="Ingresa el nombre de la Banda: ", font=("Arial", 12))
        nombre = tk.Entry(ventana_inscribir, font=("Arial", 12))
        etiqueta_insti=tk.Label(ventana_inscribir,text="Ingresa la Institucion de la Banda:", font=("Arial", 12))
        insti= tk.Entry(ventana_inscribir, font=("Arial", 12))
        etiqueta_categoria=tk.Label(ventana_inscribir,text="Ingresa la categoria de la Banda: ", font=("Arial", 12))
        categoria= tk.Entry(ventana_inscribir, font=("Arial", 12))
        inscribir = tk.Button(ventana_inscribir, text="Inscribir Banda", command=lambda: self.inscribir_banda(nombre.get(),insti.get(),categoria.get()))


        titulo.grid(row=0, column=3 ,pady=10)
        etiqueta_nombre.grid(row=1, column=2,pady=10)
        nombre.grid(row=1, column=3, pady=10)
        etiqueta_insti.grid(row=2, column=2, pady=10)
        insti.grid(row=2, column=3, pady=10)
        etiqueta_categoria.grid(row=3, column=2, pady=10)
        categoria.grid(row=3, column=3, pady=10)
        inscribir.grid(row=4, column=3, pady=10)

    def registrar_evaluacion(self):
        print("Se abrió la ventana: Registrar Evaluación")
        ventana_evaluacion = tk.Tk()
        ventana_evaluacion.title("Registrar Evaluación")
        ventana_evaluacion.geometry("800x400")

        titulo = tk.Label(ventana_evaluacion, text="Registrar Evaluación", font=("Arial", 16, "bold"))
        buscar = tk.Label(ventana_evaluacion, text="Ingrese el nombre de la banda a evaluar: ", font=("Arial", 12))
        entrada_buscar = tk.Entry(ventana_evaluacion, font=("Arial", 12))
        boton_buscar = tk.Button(ventana_evaluacion, text="BUSCAR", font=("Arial", 12), command= lambda: self.buscar(entrada_buscar.get()))
        titulo_evaluacion = tk.Label(ventana_evaluacion, text=f"Ingrese la evaluacion de la banda: {entrada_buscar.get()}", font=("Arial", 16, "bold"))
        ritmo = tk.Label(ventana_evaluacion, text="Ritmo: ", font=("Arial", 12))
        ritmo_entrada = tk.Entry(ventana_evaluacion, font=("Arial", 12))
        uniformidad = tk.Label(ventana_evaluacion, text="Uniformidad: ", font=("Arial", 12))
        uniformidad_entrada = tk.Entry(ventana_evaluacion, font=("Arial", 12))
        coreografia = tk.Label(ventana_evaluacion, text="Coreografia: ", font=("Arial", 12))
        coreografia_entrada = tk.Entry(ventana_evaluacion, font=("Arial", 12))
        alineacion = tk.Label(ventana_evaluacion, text="Alineacion: ", font=("Arial", 12))
        alineacion_entrada = tk.Entry(ventana_evaluacion, font=("Arial", 12))
        puntualidad = tk.Label(ventana_evaluacion, text="Puntualidad: ", font=("Arial", 12))
        puntualidad_entrada = tk.Entry(ventana_evaluacion, font=("Arial", 12))
        puntuacion = tk.Button(ventana_evaluacion, text="ENVIAR EVALUACION", command=lambda: self.evaluacion(entrada_buscar.get(),ritmo_entrada.get(),uniformidad_entrada.get(), coreografia_entrada.get(),alineacion_entrada.get(), puntualidad_entrada.get()))

        titulo.grid(row=0, column=3 ,pady=5)
        buscar.grid(row=1, column=2, pady=5)
        entrada_buscar.grid(row=1, column=3, pady=5)
        boton_buscar.grid(row=1, column=4, pady=5)
        titulo_evaluacion.grid(row=2, column=3, pady=5)
        ritmo.grid(row=3, column=2, pady=5)
        ritmo_entrada.grid(row=3, column=3, pady=5)
        uniformidad.grid(row=4, column=2, pady=5)
        uniformidad_entrada.grid(row=4, column=3, pady=5)
        coreografia.grid(row=5, column=2, pady=5)
        coreografia_entrada.grid(row=5, column=3, pady=5)
        alineacion.grid(row=6, column=2, pady=5)
        alineacion_entrada.grid(row=6, column=3, pady=5)
        puntualidad.grid(row=7, column=2, pady=5)
        puntualidad_entrada.grid(row=7, column=3, pady=5)
        puntuacion.grid(row=8, column=3, pady=10)

    def listar_bandas(self):
        print("Se abrió la ventana: Listado de Bandas")
        ventana_lista=tk.Tk()
        ventana_lista.title("Listado de Bandas")
        ventana_lista.geometry("400x300")

        titulo = tk.Label(ventana_lista, text="Bandas inscritas en el concurso", font=("Arial", 16, "bold"))
        titulo.grid(row=0, column=3, pady=5)
        for x in range(len(self.Bandas)):
            banda = tk.Label(ventana_lista, text=f"{x+1}. Nombre: {self.Bandas[x].nombre} - Categoria: {self.Bandas[x].categoria} - Institucion: {self.Bandas[x].institucion}", font=("Arial", 12))
            banda.grid(row=x+1, column=2, pady=3)

    def ver_ranking(self):
        print("Se abrió la ventana: Ranking Final")
        tk.Toplevel(self.ventana).title("Ranking Final")

    def inscribir_banda(self, nombre, insti, categoria):
        print("Inscribiendo Banda")
        x=tk.Tk()
        x.title("Inscribiendo Banda")
        categorias = ["primaria", "basico", "diversificado", "básico"]
        if len(self.Bandas)>0:
            for banda in self.Bandas:
                if banda.nombre.lower() == nombre.lower():
                    messagebox.showerror("Error", "Banda ya existe. No pueden haber 2 bandas con el mismo nombre")
                    print("a")
                else:
                    if categoria.lower() in categorias:
                        nueva_banda= BandaEscolar(nombre,insti,categoria)
                        self.Bandas.append(nueva_banda)
                        messagebox.showinfo("Inscribiendo Banda", "Banda inscrita")
                    else:
                        messagebox.showerror("Error", "Error en la categoria")
        else:
            if categoria.lower() in categorias:
                nueva_banda = BandaEscolar(nombre, insti, categoria)
                self.Bandas.append(nueva_banda)
                messagebox.showinfo("Inscribiendo Banda", "Banda inscrita")
            else:
                messagebox.showerror("Error", "Error en la categoria")
        x.destroy()

    def evaluacion(self,nombre, ritmo, uniformidad, coreografia, alineacion, puntuacion):
        x=tk.Tk()
        x.title("Evaluacion")
        ritmo = float(ritmo)
        uniformidad = float(uniformidad)
        coreografia = float(coreografia)
        alineacion = float(alineacion)
        puntuacion = float(puntuacion)
        if 0 < ritmo < 10:
            if 0<uniformidad < 10:
                if 0<coreografia < 10:
                    if 0<alineacion < 10:
                        if 0<puntuacion < 10:
                            total = ritmo+uniformidad+coreografia+alineacion+puntuacion
                            promedio = total/5
                            if len(self.Bandas)>0:
                                for banda in self.Bandas:
                                    if banda.nombre.lower() == nombre.lower():
                                        banda.puntaje={
                                            "ritmo": ritmo,
                                            "uniformidad": uniformidad,
                                            "coreografia": coreografia,
                                            "alineacion": alineacion,
                                            "puntuacion": puntuacion,
                                            "total": total,
                                            "promedio": promedio
                                        }
                                    messagebox.showinfo("Evaluacion",
                                                f"Se ha registrado la evaluación correctamente para\nla banda: {banda.nombre}")
                        else:
                            messagebox.showerror("Error", "La calificacion en *Puntualidad* no puede ser negativa, ni mayor a 10")
                    else:
                        messagebox.showerror("Error", "La calificacion en *Alineacion* no puede ser negativa, ni mayor a 10")
                else:
                    messagebox.showerror("Error", "La calificacion en *Coreografia* no puede ser negativa, ni mayor a 10")
            else:
                messagebox.showerror("Error", "La calificacion en *Uniformidad* no puede ser negativa, ni mayor a 10")
        else:
            messagebox.showerror("Error", "La calificacion en *Ritmo* no puede ser negativa, ni mayor a 10")
        x.destroy()
    def ordenar_bandas(self, lista):
        if len(lista) <=1:
            return lista
        else:
            pivote = lista[0]
            menores = [x for x in lista[1:] if x.puntajes["promedio"]<pivote.puntajes["promedio"] ]
            iguales = [x for x in lista if x.puntajes["promedio"] == pivote.puntajes["promedio"]]
            mayores = [x for x in lista[1:] if x.puntajes["promedio"]>pivote.puntajes["promedio"]]
            return self.ordenar_bandas(mayores) + iguales+ self.ordenar_bandas(menores)
#class Concurso:
#    def __init__(self,nombre):
 #       self.nombre = nombre
  #      self.bandas_ordenadas=[]
   # def ordenar_bandas(self, lista):
    #    if len(lista) <=1:
     #       return lista
      #  else:
       #     pivote = lista[0]
        #    menores = [x for x in lista[1:] if x.puntajes["promedio"]<pivote.puntajes["promedio"] ]
         #   iguales = [x for x in lista if x.puntajes["promedio"] == pivote.puntajes["promedio"]]
          #  mayores = [x for x in lista[1:] if x.puntajes["promedio"]>pivote.puntajes["promedio"]]
           # return self.ordenar_bandas(mayores) + iguales+ self.ordenar_bandas(menores)

if __name__ == "__main__":
    ConcursoBandasApp()
