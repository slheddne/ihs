import sys

from PyQt5.QtWidgets import QApplication

from components.FenetrePrincipale import FenetrePrincipale

if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre_principale = FenetrePrincipale()
    sys.exit(app.exec_())
