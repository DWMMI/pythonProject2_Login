import os

import PySide6
from PySide6.QtWidgets import *
from PySide6.QtGui import *


# Clase de la ventana principal
class VentanaPrincipal(QMainWindow):

    def __init__(self):
        # Llama al constructor de la clase base
        super().__init__()

        # Establece el icono de la ventana
        ruta_icono = os.path.join(os.path.dirname(__file__), "iniciar-sesion.png")
        self.setWindowIcon(QIcon(ruta_icono))

        # Establece el título de la ventana
        self.setWindowTitle("Login")

        # Tamaño y posición de la ventana principal
        self.setFixedSize(250, 150)

        # barra de menú
        barra_menu = self.menuBar()
        # añadirla la menú principal
        menu = barra_menu.addMenu("&Ayuda")
        # crear acción
        accion = QAction("Imprimir por consola", self)
        # Atajo de teclado
        accion.setShortcut(QKeySequence("ctrl+i"))
        # descripción
        accion.setToolTip("Imprime un mensaje en la consola")
        # conectar acción con ranura
        accion.triggered.connect(self.imprimir_consola)
        # añadir acción al menú
        menu.addAction(accion)

        # Crea un icono para la ventana principal
        icon = PySide6.QtGui.QIcon("iniciar-sesion.png.png")
        # Asigna el icono a la ventana principal
        self.setWindowIcon(icon)

        # Usaremos el QGridLayout para construir nuestra ventana de login
        # creamso un objeto layout
        layout_cuadricula = QGridLayout()
        componente_principal = QWidget()
        componente_principal.setLayout(layout_cuadricula)
        self.setCentralWidget(componente_principal)

        # Añadimos los formularios de usuario y contraseña

        label00 = QLabel("Usuario: ")
        label01 = QLineEdit()
        label01.setPlaceholderText("Usuario")
        label10 = QLabel("Contraseña: ")
        label11 = QLineEdit()
        label11.setPlaceholderText("Contraseña")
        self.label2 = QPushButton("Login", self)

        # El evento clic del button
        self.label2.clicked.connect(self.clic_de_boton)

        layout_cuadricula.addWidget(label00, 0, 0)
        layout_cuadricula.addWidget(label01, 0, 1)
        layout_cuadricula.addWidget(label10, 1, 0)
        layout_cuadricula.addWidget(label11, 1, 1)
        layout_cuadricula.addWidget(self.label2, 2, 0, 1, 2)

    def imprimir_consola(self):
        print("Acción lanzada a traves del menu")

    def clic_de_boton(self):
        print("Señal de clic recibida -> Ejecución de la ranura")


# Punto de entrada del programa
if __name__ == "__main__":
    # Crea una aplicación Qt
    app = QApplication([])
    # Crea una ventana principal
    ventana1 = VentanaPrincipal()
    # Muestra la ventana
    ventana1.show()
    # Ejecuta la aplicación
    app.exec()
