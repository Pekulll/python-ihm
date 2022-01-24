import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)

window = QWidget()
window.setGeometry(0, 0, 200, 200)  # permet de postionner la fenetre et forcer la taille et le placement

"""
bouton = QPushButton(window)
bouton.setText("Bouton")
bouton.move(100, 100)
"""

# Pour avoir une appli adaptable, on évite les positions absolue
# solution : utiliser des layouts

"""Etape 2
bouton1 = QPushButton("Premier")
bouton2 = QPushButton("Deuxième")

verticalBoxLayout = QVBoxLayout()

verticalBoxLayout.addWidget(bouton1)
verticalBoxLayout.addWidget(bouton2)

window.setLayout(verticalBoxLayout)"""

"""Etape 3
bouton3 = QPushButton("Troisième")
bouton4 = QPushButton("Quatrième")

horizontalBoxLayout = QHBoxLayout()

horizontalBoxLayout.addWidget(bouton3)
horizontalBoxLayout.addStretch()  # on rajoute une boite vie
horizontalBoxLayout.addWidget(bouton4)

window.setLayout(horizontalBoxLayout)"""

"""Etape 4 : QGridLayout"""
bouton1 = QPushButton("Premier")
bouton2 = QPushButton("Deuxième")
bouton3 = QPushButton("Troisième")
bouton4 = QPushButton("Quatrième")

grille = QGridLayout()

grille.addWidget(bouton1, 1, 1)
grille.addWidget(bouton2, 1, 2)
grille.addWidget(bouton3, 2, 1)
grille.addWidget(bouton4, 2, 2)

window.setLayout(grille)
window.setGeometry(300, 200, 100, 100)  # setGeometry est compatible avec les layout


window.show()
sys.exit(app.exec())
