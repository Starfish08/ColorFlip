from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PIL import Image, ImageOps
import sys
import os
Color = "RGB"

class ApplicationColorFlip:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.fenetre = QMainWindow()
        self.fenetre.setGeometry(400, 400, 450, 200)
        self.fenetre.setWindowTitle("Color Flip!")

        self.questionAcces = QtWidgets.QLabel(self.fenetre)
        self.questionSave = QtWidgets.QLabel(self.fenetre)
        self.reponseAcces = QtWidgets.QLineEdit(self.fenetre)
        self.reponseSave = QtWidgets.QLineEdit(self.fenetre)

        self.questionAcces.setText("Quelle image souhaitez-vous convertir en négatif noir & blanc ?")
        self.questionAcces.adjustSize()

        self.reponseAcces.setFixedWidth(300)
        self.reponseAcces.move(0, 35)
        self.reponseAcces.setPlaceholderText("/Chemin/Vers/MonImage.png")

        self.questionSave.setText("Où souhaitez-vous enregistrer l'image inversée ?")
        self.questionSave.adjustSize()
        self.questionSave.move(0, 75)

        self.reponseSave.setFixedWidth(300)
        self.reponseSave.adjustSize()
        self.reponseSave.move(0, 102)
        self.reponseSave.setPlaceholderText("/Chemin/Vers/MonImageInverse.png")

        self.flipCheckBox = QCheckBox("Convertir en monochrome", self.fenetre)
        self.flipCheckBox.adjustSize()
        self.flipCheckBox.move(0, 130)
        self.flipCheckBox.setChecked(False)  # Par défaut, la case à cocher est désactivée
        if self.flipCheckBox.isChecked():
            Color = "L"
        else:
            Color = "RGB"

        self.bouton = QtWidgets.QPushButton(self.fenetre)
        self.bouton.setText("Flip!")
        self.bouton.clicked.connect(self.renverser_couleurs)
        self.bouton.move(100, 170)

        # Connexion pour remplir automatiquement le champ de sauvegarde
        self.reponseAcces.textChanged.connect(self.remplir_champ_enregistrement)

        self.fenetre.show()
        sys.exit(self.app.exec_())

    def renverser_couleurs(self):
        cheminAcces = self.reponseAcces.text()
        cheminEnregistrement = self.reponseSave.text()
        im = Image.open(cheminAcces).convert(Color)
        im_inverse = ImageOps.invert(im)
        im_inverse.save(cheminEnregistrement, quality=95)

    def remplir_champ_enregistrement(self):
        cheminAcces = self.reponseAcces.text()
        nom_fichier = os.path.basename(cheminAcces)
        nom_fichier_sans_extension, extension = os.path.splitext(nom_fichier)
        chemin_enregistrement = os.path.dirname(cheminAcces)
        chemin_enregistrement = os.path.join(chemin_enregistrement, nom_fichier_sans_extension + "_Flip" + extension)
        self.reponseSave.setText(chemin_enregistrement)

if __name__ == "__main__":
    app = ApplicationColorFlip()
