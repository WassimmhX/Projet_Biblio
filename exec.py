from defs import *
from mainwindow import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.ui.actionHome.triggered.connect(self.home)
        self.ui.actionAjouter.triggered.connect(self.ajouterEtd)
        self.ui.actionsupprimer.triggered.connect(self.supprimerEtd)
        self.ui.actionModifier_4.triggered.connect(self.modifierEtd)
        self.ui.actionAfficher_2.triggered.connect(self.afficherEtd)
        self.ui.actionRech_par_ID.triggered.connect(self.recherche_id)
        self.ui.actionRech_par_Section.triggered.connect(self.recherche_sec)
        self.ui.actionRech_par_Niveau.triggered.connect(self.recherche_niv)
        self.ui.actionRech_par_Niv_Sec_2.triggered.connect(self.recherche_cl)
        self.ui.actionAjouter_2.triggered.connect(self.ajouterLv)
        self.ui.actionsupprimer_2.triggered.connect(self.supprimerLv)
        self.ui.actionModifier_2.triggered.connect(self.modifierLv)
        self.ui.actionAfficher_3.triggered.connect(self.afficherLv)
        self.ui.actionRech_par_Ref.triggered.connect(self.recherche_ref)
        self.ui.actionRech_par_titre.triggered.connect(self.recherche_tit)
        self.ui.actionRech_par_auteur.triggered.connect(self.recherche_aut)
        self.ui.actionRech_par_annee.triggered.connect(self.recherche_ann)
        self.ui.actionAjouter_3.triggered.connect(self.ajouterEmp)
        self.ui.actionSupprimer_3.triggered.connect(self.supprimerEmp)
        self.ui.actionModifier_date_Emprunt.triggered.connect(self.modifierDateEmp)
        self.ui.actionModifier_date_Retour.triggered.connect(self.modifierDateRet)
        self.ui.actionAfficher.triggered.connect(self.afficherEmp)
        self.ui.actionRech_par_Etudiant.triggered.connect(self.recherche_etd)
        self.ui.actionRech_par_Livre.triggered.connect(self.recherche_liv)
        self.ui.actionRech_par_date_emprunt.triggered.connect(self.recherche_demp)
        self.ui.actionRech_par_date_Retour.triggered.connect(self.recherche_dret)
        self.ui.actionrech_entre_deux_dates_Emp.triggered.connect(self.recherche_entredemp)
        self.ui.actionRech_entre_deux_date_Ret.triggered.connect(self.recherche_entredret)
        self.ui.actionRetour_d_un_emprunt.triggered.connect((self.retour_emp))
        self.window.show()

    def home(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)

    def ajouterEtd(self):
        self.ajouter=ajouterEtudiant()
        self.ui.stackedWidget.addWidget(self.ajouter.window)
        self.ui.stackedWidget.setCurrentWidget(self.ajouter.window)

    def supprimerEtd(self):
        self.supprimer=supprimerEtudiant()
        self.ui.stackedWidget.addWidget(self.supprimer.window)
        self.ui.stackedWidget.setCurrentWidget(self.supprimer.window)

    def modifierEtd(self):
        self.modifier=modifierEtudiant()
        self.ui.stackedWidget.addWidget(self.modifier.window)
        self.ui.stackedWidget.setCurrentWidget(self.modifier.window)

    def afficherEtd(self):
        self.afficher = afficherEtudiant()
        self.ui.stackedWidget.addWidget(self.afficher.window)
        self.ui.stackedWidget.setCurrentWidget(self.afficher.window)

    def recherche_id(self):
        self.recherche = recherche_par_id()
        self.ui.stackedWidget.addWidget(self.recherche.window)
        self.ui.stackedWidget.setCurrentWidget(self.recherche.window)

    def recherche_sec(self):
        self.recherche = recherche_par_sec()
        self.ui.stackedWidget.addWidget(self.recherche.window)
        self.ui.stackedWidget.setCurrentWidget(self.recherche.window)

    def recherche_cl(self):
        self.recherche = recherche_par_cl()
        self.ui.stackedWidget.addWidget(self.recherche.window)
        self.ui.stackedWidget.setCurrentWidget(self.recherche.window)

    def recherche_niv(self):
        self.recherche = recherche_par_niv()
        self.ui.stackedWidget.addWidget(self.recherche.window)
        self.ui.stackedWidget.setCurrentWidget(self.recherche.window)

    def ajouterLv(self):
        self.ajouter=ajouterLivre()
        self.ui.stackedWidget.addWidget(self.ajouter.window)
        self.ui.stackedWidget.setCurrentWidget(self.ajouter.window)

    def supprimerLv(self):
        self.supprimer=supprimerLivre()
        self.ui.stackedWidget.addWidget(self.supprimer.window)
        self.ui.stackedWidget.setCurrentWidget(self.supprimer.window)

    def modifierLv(self):
        self.modifier=modifierLivre()
        self.ui.stackedWidget.addWidget(self.modifier.window)
        self.ui.stackedWidget.setCurrentWidget(self.modifier.window)

    def afficherLv(self):
        self.afficher = afficherLivre()
        self.ui.stackedWidget.addWidget(self.afficher.window)
        self.ui.stackedWidget.setCurrentWidget(self.afficher.window)

    def recherche_ref(self):
        self.recherche = recherche_par_ref()
        self.ui.stackedWidget.addWidget(self.recherche.window)
        self.ui.stackedWidget.setCurrentWidget(self.recherche.window)

    def recherche_tit(self):
        self.recherche = recherche_par_tit()
        self.ui.stackedWidget.addWidget(self.recherche.window)
        self.ui.stackedWidget.setCurrentWidget(self.recherche.window)

    def recherche_aut(self):
        self.recherche = recherche_par_aut()
        self.ui.stackedWidget.addWidget(self.recherche.window)
        self.ui.stackedWidget.setCurrentWidget(self.recherche.window)

    def recherche_ann(self):
        self.recherche = recherche_par_ann()
        self.ui.stackedWidget.addWidget(self.recherche.window)
        self.ui.stackedWidget.setCurrentWidget(self.recherche.window)

    def ajouterEmp(self):
        self.ajouter=ajouterEmprunt()
        self.ui.stackedWidget.addWidget(self.ajouter.window)
        self.ui.stackedWidget.setCurrentWidget(self.ajouter.window)

    def supprimerEmp(self):
        self.supprimer=supprimerEmprunt()
        self.ui.stackedWidget.addWidget(self.supprimer.window)
        self.ui.stackedWidget.setCurrentWidget(self.supprimer.window)

    def modifierDateEmp(self):
        self.modifier=modifierDateEmp()
        self.ui.stackedWidget.addWidget(self.modifier.window)
        self.ui.stackedWidget.setCurrentWidget(self.modifier.window)

    def modifierDateRet(self):
        self.modifier=modifierDateRet()
        self.ui.stackedWidget.addWidget(self.modifier.window)
        self.ui.stackedWidget.setCurrentWidget(self.modifier.window)

    def afficherEmp(self):
        self.afficher = afficherEmprunt()
        self.ui.stackedWidget.addWidget(self.afficher.window)
        self.ui.stackedWidget.setCurrentWidget(self.afficher.window)

    def recherche_etd(self):
        self.recherche = recherche_par_etd()
        self.ui.stackedWidget.addWidget(self.recherche.window)
        self.ui.stackedWidget.setCurrentWidget(self.recherche.window)

    def recherche_liv(self):
        self.recherche = recherche_par_liv()
        self.ui.stackedWidget.addWidget(self.recherche.window)
        self.ui.stackedWidget.setCurrentWidget(self.recherche.window)

    def recherche_demp(self):
        self.recherche = recherche_par_demp()
        self.ui.stackedWidget.addWidget(self.recherche.window)
        self.ui.stackedWidget.setCurrentWidget(self.recherche.window)

    def recherche_dret(self):
        self.recherche = recherche_par_dret()
        self.ui.stackedWidget.addWidget(self.recherche.window)
        self.ui.stackedWidget.setCurrentWidget(self.recherche.window)

    def recherche_entredemp(self):
        self.recherche = recherche_entre_demp()
        self.ui.stackedWidget.addWidget(self.recherche.window)
        self.ui.stackedWidget.setCurrentWidget(self.recherche.window)

    def recherche_entredret(self):
        self.recherche = recherche_entre_dret()
        self.ui.stackedWidget.addWidget(self.recherche.window)
        self.ui.stackedWidget.setCurrentWidget(self.recherche.window)

    def retour_emp(self):
        self.retour = retourEmp()
        self.ui.stackedWidget.addWidget(self.retour.window)
        self.ui.stackedWidget.setCurrentWidget(self.retour.window)