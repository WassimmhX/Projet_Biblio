

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(790, 564)
        MainWindow.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("238-2386202_icon-of-a-stack-of-colorful-books-with.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setTabletTracking(False)
        self.stackedWidget.setAcceptDrops(False)
        self.stackedWidget.setStyleSheet("border-image: url(f867c4a1391713dbbda30e2a472f9dde.jpg);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setStyleSheet("border-image: url(b.png);")
        self.page.setObjectName("page")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout.setContentsMargins(9, 150, -1, 20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"text-decoration:italic;\n"
"font: 48pt \"Poor Richard\";\n"
"color: rgb(124, 0, 186);\n"
"color: rgb(255, 255, 255);\n"
"padding:15;\n"
"margin-top:50")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.label = QtWidgets.QLabel(self.page)
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.82, y1:0.93, x2:0.865, y2:0.449, stop:0 rgba(202, 157, 218, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 87 12pt \"Arial Black\";\n"
"color: rgb(67, 142, 255);\n"
"text-decoration: underline;")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.verticalLayout.setStretch(1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 790, 22))
        self.menubar.setObjectName("menubar")
        self.menuHome = QtWidgets.QMenu(self.menubar)
        self.menuHome.setToolTip("")
        self.menuHome.setAutoFillBackground(False)
        self.menuHome.setTearOffEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Home-icon.svg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuHome.setIcon(icon1)
        self.menuHome.setSeparatorsCollapsible(False)
        self.menuHome.setToolTipsVisible(False)
        self.menuHome.setObjectName("menuHome")
        self.menuEtudiant = QtWidgets.QMenu(self.menubar)
        self.menuEtudiant.setObjectName("menuEtudiant")
        self.menuRecherche = QtWidgets.QMenu(self.menuEtudiant)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuRecherche.setIcon(icon2)
        self.menuRecherche.setObjectName("menuRecherche")
        self.menuLivres = QtWidgets.QMenu(self.menubar)
        self.menuLivres.setObjectName("menuLivres")
        self.menuRechrche = QtWidgets.QMenu(self.menuLivres)
        self.menuRechrche.setIcon(icon2)
        self.menuRechrche.setObjectName("menuRechrche")
        self.menuEmprunt = QtWidgets.QMenu(self.menubar)
        self.menuEmprunt.setObjectName("menuEmprunt")
        self.menuModifier = QtWidgets.QMenu(self.menuEmprunt)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("m.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuModifier.setIcon(icon3)
        self.menuModifier.setObjectName("menuModifier")
        self.menuRecherche_2 = QtWidgets.QMenu(self.menuEmprunt)
        self.menuRecherche_2.setIcon(icon2)
        self.menuRecherche_2.setObjectName("menuRecherche_2")
        MainWindow.setMenuBar(self.menubar)
        self.actionAjouter = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("plus-sign-icon-png-16.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAjouter.setIcon(icon4)
        self.actionAjouter.setObjectName("actionAjouter")
        self.actionModifier_4 = QtWidgets.QAction(MainWindow)
        self.actionModifier_4.setIcon(icon3)
        self.actionModifier_4.setObjectName("actionModifier_4")
        self.actionSupprimer_un_etudiant = QtWidgets.QAction(MainWindow)
        self.actionSupprimer_un_etudiant.setObjectName("actionSupprimer_un_etudiant")
        self.actionSupprimer_un_niveau = QtWidgets.QAction(MainWindow)
        self.actionSupprimer_un_niveau.setObjectName("actionSupprimer_un_niveau")
        self.actionSupprimer_une_section = QtWidgets.QAction(MainWindow)
        self.actionSupprimer_une_section.setObjectName("actionSupprimer_une_section")
        self.actionSupprimer_un_classe = QtWidgets.QAction(MainWindow)
        self.actionSupprimer_un_classe.setObjectName("actionSupprimer_un_classe")
        self.actionAjouter_2 = QtWidgets.QAction(MainWindow)
        self.actionAjouter_2.setIcon(icon4)
        self.actionAjouter_2.setObjectName("actionAjouter_2")
        self.actionModifier_2 = QtWidgets.QAction(MainWindow)
        self.actionModifier_2.setIcon(icon3)
        self.actionModifier_2.setObjectName("actionModifier_2")
        self.actionSupprimer_un_livre = QtWidgets.QAction(MainWindow)
        self.actionSupprimer_un_livre.setObjectName("actionSupprimer_un_livre")
        self.actionSupprimer_des_livres_d_un_auteur = QtWidgets.QAction(MainWindow)
        self.actionSupprimer_des_livres_d_un_auteur.setObjectName("actionSupprimer_des_livres_d_un_auteur")
        self.actionSupprimer_des_livres_d_une_ann_e = QtWidgets.QAction(MainWindow)
        self.actionSupprimer_des_livres_d_une_ann_e.setObjectName("actionSupprimer_des_livres_d_une_ann_e")
        self.actionAjouter_3 = QtWidgets.QAction(MainWindow)
        self.actionAjouter_3.setIcon(icon4)
        self.actionAjouter_3.setObjectName("actionAjouter_3")
        self.actionSupprimer_3 = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images (3).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSupprimer_3.setIcon(icon5)
        self.actionSupprimer_3.setObjectName("actionSupprimer_3")
        self.actionRetour_d_un_emprunt = QtWidgets.QAction(MainWindow)
        self.actionRetour_d_un_emprunt.setObjectName("actionRetour_d_un_emprunt")
        self.actionAfficher = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("d.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAfficher.setIcon(icon6)
        self.actionAfficher.setObjectName("actionAfficher")
        self.actionAfficher_2 = QtWidgets.QAction(MainWindow)
        self.actionAfficher_2.setIcon(icon6)
        self.actionAfficher_2.setObjectName("actionAfficher_2")
        self.actionAfficher_3 = QtWidgets.QAction(MainWindow)
        self.actionAfficher_3.setIcon(icon6)
        self.actionAfficher_3.setObjectName("actionAfficher_3")
        self.actionsupprimer = QtWidgets.QAction(MainWindow)
        self.actionsupprimer.setIcon(icon5)
        self.actionsupprimer.setObjectName("actionsupprimer")
        self.actionsupprimer_2 = QtWidgets.QAction(MainWindow)
        self.actionsupprimer_2.setIcon(icon5)
        self.actionsupprimer_2.setObjectName("actionsupprimer_2")
        self.actionRecherche_Etudiant = QtWidgets.QAction(MainWindow)
        self.actionRecherche_Etudiant.setObjectName("actionRecherche_Etudiant")
        self.actionRechrche_livre = QtWidgets.QAction(MainWindow)
        self.actionRechrche_livre.setObjectName("actionRechrche_livre")
        self.actionRechrche_emprunt = QtWidgets.QAction(MainWindow)
        self.actionRechrche_emprunt.setObjectName("actionRechrche_emprunt")
        self.actionModifier_date_Emprunt = QtWidgets.QAction(MainWindow)
        self.actionModifier_date_Emprunt.setObjectName("actionModifier_date_Emprunt")
        self.actionModifier_date_Retour = QtWidgets.QAction(MainWindow)
        self.actionModifier_date_Retour.setObjectName("actionModifier_date_Retour")
        self.actionRech_par_Ref = QtWidgets.QAction(MainWindow)
        self.actionRech_par_Ref.setObjectName("actionRech_par_Ref")
        self.actionRech_par_titre = QtWidgets.QAction(MainWindow)
        self.actionRech_par_titre.setObjectName("actionRech_par_titre")
        self.actionRech_par_annee = QtWidgets.QAction(MainWindow)
        self.actionRech_par_annee.setObjectName("actionRech_par_annee")
        self.actionRech_par_auteur = QtWidgets.QAction(MainWindow)
        self.actionRech_par_auteur.setObjectName("actionRech_par_auteur")
        self.actionRech_par_ID = QtWidgets.QAction(MainWindow)
        self.actionRech_par_ID.setObjectName("actionRech_par_ID")
        self.actionRech_par_Section = QtWidgets.QAction(MainWindow)
        self.actionRech_par_Section.setObjectName("actionRech_par_Section")
        self.actionRech_par_Niveau = QtWidgets.QAction(MainWindow)
        self.actionRech_par_Niveau.setObjectName("actionRech_par_Niveau")
        self.actionRech_par_Niv_Sec_2 = QtWidgets.QAction(MainWindow)
        self.actionRech_par_Niv_Sec_2.setObjectName("actionRech_par_Niv_Sec_2")
        self.actionRech_par_Livre = QtWidgets.QAction(MainWindow)
        self.actionRech_par_Livre.setObjectName("actionRech_par_Livre")
        self.actionRech_par_Etudiant = QtWidgets.QAction(MainWindow)
        self.actionRech_par_Etudiant.setObjectName("actionRech_par_Etudiant")
        self.actionRech_par_date_emprunt = QtWidgets.QAction(MainWindow)
        self.actionRech_par_date_emprunt.setObjectName("actionRech_par_date_emprunt")
        self.actionRech_par_date_Retour = QtWidgets.QAction(MainWindow)
        self.actionRech_par_date_Retour.setObjectName("actionRech_par_date_Retour")
        self.actionrech_entre_deux_dates_Emp = QtWidgets.QAction(MainWindow)
        self.actionrech_entre_deux_dates_Emp.setObjectName("actionrech_entre_deux_dates_Emp")
        self.actionRech_entre_deux_date_Ret = QtWidgets.QAction(MainWindow)
        self.actionRech_entre_deux_date_Ret.setObjectName("actionRech_entre_deux_date_Ret")
        self.actionHome = QtWidgets.QAction(MainWindow)
        self.actionHome.setIcon(icon1)
        self.actionHome.setObjectName("actionHome")
        self.menuHome.addAction(self.actionHome)
        self.menuRecherche.addAction(self.actionRech_par_ID)
        self.menuRecherche.addSeparator()
        self.menuRecherche.addAction(self.actionRech_par_Section)
        self.menuRecherche.addSeparator()
        self.menuRecherche.addAction(self.actionRech_par_Niveau)
        self.menuRecherche.addSeparator()
        self.menuRecherche.addAction(self.actionRech_par_Niv_Sec_2)
        self.menuEtudiant.addSeparator()
        self.menuEtudiant.addAction(self.actionAfficher_2)
        self.menuEtudiant.addSeparator()
        self.menuEtudiant.addAction(self.actionAjouter)
        self.menuEtudiant.addSeparator()
        self.menuEtudiant.addAction(self.actionsupprimer)
        self.menuEtudiant.addSeparator()
        self.menuEtudiant.addAction(self.actionModifier_4)
        self.menuEtudiant.addSeparator()
        self.menuEtudiant.addAction(self.menuRecherche.menuAction())
        self.menuRechrche.addAction(self.actionRech_par_Ref)
        self.menuRechrche.addSeparator()
        self.menuRechrche.addAction(self.actionRech_par_titre)
        self.menuRechrche.addSeparator()
        self.menuRechrche.addAction(self.actionRech_par_annee)
        self.menuRechrche.addSeparator()
        self.menuRechrche.addAction(self.actionRech_par_auteur)
        self.menuLivres.addAction(self.actionAfficher_3)
        self.menuLivres.addSeparator()
        self.menuLivres.addAction(self.actionAjouter_2)
        self.menuLivres.addSeparator()
        self.menuLivres.addAction(self.actionsupprimer_2)
        self.menuLivres.addSeparator()
        self.menuLivres.addAction(self.actionModifier_2)
        self.menuLivres.addSeparator()
        self.menuLivres.addAction(self.menuRechrche.menuAction())
        self.menuModifier.addAction(self.actionModifier_date_Emprunt)
        self.menuModifier.addSeparator()
        self.menuModifier.addAction(self.actionModifier_date_Retour)
        self.menuRecherche_2.addAction(self.actionRech_par_Livre)
        self.menuRecherche_2.addSeparator()
        self.menuRecherche_2.addAction(self.actionRech_par_Etudiant)
        self.menuRecherche_2.addSeparator()
        self.menuRecherche_2.addAction(self.actionRech_par_date_emprunt)
        self.menuRecherche_2.addSeparator()
        self.menuRecherche_2.addAction(self.actionRech_par_date_Retour)
        self.menuRecherche_2.addSeparator()
        self.menuRecherche_2.addAction(self.actionrech_entre_deux_dates_Emp)
        self.menuRecherche_2.addSeparator()
        self.menuRecherche_2.addAction(self.actionRech_entre_deux_date_Ret)
        self.menuEmprunt.addAction(self.actionAfficher)
        self.menuEmprunt.addSeparator()
        self.menuEmprunt.addAction(self.actionAjouter_3)
        self.menuEmprunt.addSeparator()
        self.menuEmprunt.addAction(self.actionSupprimer_3)
        self.menuEmprunt.addSeparator()
        self.menuEmprunt.addAction(self.menuModifier.menuAction())
        self.menuEmprunt.addSeparator()
        self.menuEmprunt.addAction(self.actionRetour_d_un_emprunt)
        self.menuEmprunt.addSeparator()
        self.menuEmprunt.addAction(self.menuRecherche_2.menuAction())
        self.menubar.addAction(self.menuHome.menuAction())
        self.menubar.addAction(self.menuEtudiant.menuAction())
        self.menubar.addAction(self.menuLivres.menuAction())
        self.menubar.addAction(self.menuEmprunt.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "bibliothèque"))
        self.label_2.setText(_translate("MainWindow", "Bibliothèque"))
        self.label.setText(_translate("MainWindow", "Made by Wassim Maharsia"))
        self.menuHome.setTitle(_translate("MainWindow", "Home"))
        self.menuEtudiant.setTitle(_translate("MainWindow", "Etudiants"))
        self.menuRecherche.setTitle(_translate("MainWindow", "Recherche"))
        self.menuLivres.setTitle(_translate("MainWindow", "Livres"))
        self.menuRechrche.setTitle(_translate("MainWindow", "Rechrche"))
        self.menuEmprunt.setTitle(_translate("MainWindow", "Emprunt"))
        self.menuModifier.setTitle(_translate("MainWindow", "Modifier"))
        self.menuRecherche_2.setTitle(_translate("MainWindow", "Recherche"))
        self.actionAjouter.setText(_translate("MainWindow", "Ajouter"))
        self.actionModifier_4.setText(_translate("MainWindow", "Modifier"))
        self.actionSupprimer_un_etudiant.setText(_translate("MainWindow", "Supprimer un etudiant"))
        self.actionSupprimer_un_niveau.setText(_translate("MainWindow", "Supprimer un niveau"))
        self.actionSupprimer_une_section.setText(_translate("MainWindow", "Supprimer une section"))
        self.actionSupprimer_un_classe.setText(_translate("MainWindow", "Supprimer un classe"))
        self.actionAjouter_2.setText(_translate("MainWindow", "Ajouter"))
        self.actionModifier_2.setText(_translate("MainWindow", "Modifier"))
        self.actionSupprimer_un_livre.setText(_translate("MainWindow", "Supprimer un livre"))
        self.actionSupprimer_des_livres_d_un_auteur.setText(_translate("MainWindow", "Supprimer des livres d\'un auteur"))
        self.actionSupprimer_des_livres_d_une_ann_e.setText(_translate("MainWindow", "Supprimer des livres d\'une année"))
        self.actionAjouter_3.setText(_translate("MainWindow", "Ajouter"))
        self.actionSupprimer_3.setText(_translate("MainWindow", "Supprimer"))
        self.actionRetour_d_un_emprunt.setText(_translate("MainWindow", "Retour d\'un emprunt"))
        self.actionAfficher.setText(_translate("MainWindow", "Afficher"))
        self.actionAfficher_2.setText(_translate("MainWindow", "Afficher"))
        self.actionAfficher_3.setText(_translate("MainWindow", "Afficher"))
        self.actionsupprimer.setText(_translate("MainWindow", "supprimer"))
        self.actionsupprimer_2.setText(_translate("MainWindow", "supprimer"))
        self.actionRecherche_Etudiant.setText(_translate("MainWindow", "Recherche Etudiant"))
        self.actionRechrche_livre.setText(_translate("MainWindow", "Rechrche livre"))
        self.actionRechrche_emprunt.setText(_translate("MainWindow", "Rechrche emprunt"))
        self.actionModifier_date_Emprunt.setText(_translate("MainWindow", "Modifier date Emprunt"))
        self.actionModifier_date_Retour.setText(_translate("MainWindow", "Modifier date Retour"))
        self.actionRech_par_Ref.setText(_translate("MainWindow", "Rech. par Réf"))
        self.actionRech_par_titre.setText(_translate("MainWindow", "Rech. par titre"))
        self.actionRech_par_annee.setText(_translate("MainWindow", "Rech. par année edt"))
        self.actionRech_par_auteur.setText(_translate("MainWindow", "Rech. par Auteur"))
        self.actionRech_par_ID.setText(_translate("MainWindow", "Rech. par ID"))
        self.actionRech_par_Section.setText(_translate("MainWindow", "Rech. par Section"))
        self.actionRech_par_Niveau.setText(_translate("MainWindow", "Rech. par Niveau"))
        self.actionRech_par_Niv_Sec_2.setText(_translate("MainWindow", "Rech. par Niv+Sec"))
        self.actionRech_par_Livre.setText(_translate("MainWindow", "Rech. par Livre"))
        self.actionRech_par_Etudiant.setText(_translate("MainWindow", "Rech. par Etudiant"))
        self.actionRech_par_date_emprunt.setText(_translate("MainWindow", "Rech. par date Emprunt"))
        self.actionRech_par_date_Retour.setText(_translate("MainWindow", "Rech. par date Retour"))
        self.actionrech_entre_deux_dates_Emp.setText(_translate("MainWindow", "rech. entre deux dates Emp"))
        self.actionRech_entre_deux_date_Ret.setText(_translate("MainWindow", "Rech. entre deux date Ret"))
        self.actionHome.setText(_translate("MainWindow", "Home"))
