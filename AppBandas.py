import tkinter as tk
from tkinter import messagebox


class Participante:
    def __init__(self, nombre, insitucion):
        self.nombre = nombre
        self.insitucion = insitucion

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, insitucion: {self.insitucion}")


class BandaEscolar(Participante):
    def __init__(self, nombre, insitucion, categoria):
        super().__init__(nombre, insitucion)
        self.categoria = categoria
        self.puntaje = {}

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, nuevacategoria):
        categorias = ["primaria", "basico", "diversificado", "básico"]
        if nuevacategoria.lower() in categorias:
            self._categoria = nuevacategoria
        else:
            messagebox.showerror("Error", "Categoria incorrecta")

    @property
    def puntaje(self):
        return self.puntaje

    @puntaje.setter
    def puntaje(self, nuevapuntaje):
        for clave, valor in nuevapuntaje.items():
            if valor == "":
                print("Puntaje no se puede dejar en blanco")
            elif valor < 0:
                print("El puntaje no puede ser negativo")
            else:
                self.puntaje = valor


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
                messagebox.showinfo("Banda encontrada", f"Banda inscrita, se les asignará la evaluacion a la banda {banda.nombre}")
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
        ventana_evaluacion.geometry("700x300")

        titulo = tk.Label(ventana_evaluacion, text="Registrar Evaluación", font=("Arial", 16, "bold"))
        buscar = tk.Label(ventana_evaluacion, text="Ingrese el nombre de la banda a evaluar: ", font=("Arial", 12))
        entrada_buscar = tk.Entry(ventana_evaluacion, font=("Arial", 12))
        boton_buscar = tk.Button(ventana_evaluacion, text="BUSCAR", font=("Arial", 12), command= lambda: self.buscar(entrada_buscar.get()))

        titulo.grid(row=0, column=3 ,pady=5)
        buscar.grid(row=1, column=2, pady=5)
        entrada_buscar.grid(row=1, column=3, pady=5)
        boton_buscar.grid(row=1, column=4, pady=5)


    def listar_bandas(self):
        print("Se abrió la ventana: Listado de Bandas")
        tk.Toplevel(self.ventana).title("Listado de Bandas")

    def ver_ranking(self):
        print("Se abrió la ventana: Ranking Final")
        tk.Toplevel(self.ventana).title("Ranking Final")

    def inscribir_banda(self, nombre, insti, categoria):
        print("Inscribiendo Banda")
        x=tk.Tk()
        x.title("Inscribiendo Banda")
        nuevaBanda= BandaEscolar(nombre,insti,categoria)
        self.Bandas.append(nuevaBanda)
        for banda in self.Bandas:
            print(banda.nombre)
        messagebox.showinfo("Inscripción", "Banda Inscrita")
        x.destroy()
if __name__ == "__main__":
    ConcursoBandasApp()
