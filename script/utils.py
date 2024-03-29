import pandas as pd
from datetime import date, timedelta
from collections import namedtuple

##################################################
### GLOBAL VARIABLES                           ###
##################################################

DATES = {
    "TODAY" : date.today() - timedelta(days=1),
    "SEMESTER_START" : "09/01/2022"
}

PATHS = {
    "ADVANCEMENT" : "img/avancement.pdf",
    "CURVE" : "img/Courbe_S.pdf",
    "DVP" : "../DVP-Feuille-Temps.xlsm",
    "HOURS" : "img/heures_travaillees.pdf",
    "ISSUES" : "tableauDeProblemes.tex",
    "OBJECTIVES" : "img/progression_objectifs.png",
    "STYLE" : "./script/dashboard.mplstyle",
    "TASKS" : "tableauDeTaches.tex"
}

SHEETS = {
    "CBTP" : "Prevision_Courbe_S",
    "CRTE" : "Travail_Courbe_S",
    "CBTE" : "Avancement_Courbe_S"
}

DATA_DVP = pd.read_excel(
    io         = PATHS["DVP"], 
    sheet_name = 'DVP',
    header     = 1,
    usecols    = 'B:M',
    engine     = 'openpyxl'
)
DATA_CBTP = pd.read_excel(
    io         = PATHS["DVP"],
    sheet_name = 'Prevision_Courbe_S',
    header     = 2,
    usecols    = 'B:U',
    engine     = 'openpyxl'
)
DATA_CRTE = pd.read_excel(
    io         = PATHS["DVP"],
    sheet_name = 'Travail_Effectue',
    usecols    = 'A:L',
    engine     = 'openpyxl'
)
DATA_CBTE = pd.read_excel(
    io         = PATHS["DVP"],
    sheet_name = 'Avancement_Courbe_S',
    header     = 2,
    usecols    = 'B:U',
    engine     = 'openpyxl'
)
DATA_FORMULA = pd.read_excel(
    io         = PATHS["DVP"],
    sheet_name = 'Formule',
    usecols    = 'v',
    engine     = 'openpyxl'
)

Sheets = namedtuple('Sheets', ['DVP', 'CBTP', 'CRTE', 'CBTE', 'FORMULA'])
DATA   = Sheets(DVP=DATA_DVP, CBTP=DATA_CBTP, CRTE=DATA_CRTE, CBTE=DATA_CBTE, FORMULA=DATA_FORMULA) 


class Systeme():
    """[Classe pour les différents systèmes du projet contenant le nom, le numéro et le nombre d'heures total estimé des sytèmes]

    Returns:
        [dict]: [description]
    """
    SIMULATEUR      = {'name':'Simulateur', 'number':'SIM1', 'hours':2500}
    INSTRUMENTATION = {'name':'Instrumentation', 'number':'INS1', 'hours':1000}
    CONTROLE        = {'name':'Contrôle moteur et onduleur', 'number':'MOT2', 'hours':1000}
    GESTION         = {'name':'Gestion de projet', 'number':'GES1', 'hours':1000}
    ERGONOMIE       = {'name':'Ergonomie', 'number':'ERG1', 'hours':500}
    COQUE           = {'name':'Coque', 'number':'COQ1', 'hours':1500}
    CHASSIS         = {'name':'Chassis', 'number':'CHA1', 'hours':1500}
    DIRECTION       = {'name':'Direction', 'number':'DIR1', 'hours':500}
    FREIN           = {'name':'Frein', 'number':'FRE1', 'hours':500}
    THERMIQUE       = {'name':'Transferts thermiques', 'number':'TTH1', 'hours':500}
    SUSPENSION      = {'name':'Suspension', 'number':'SUS1', 'hours':500}
    MOTEUR          = {'name':'Moteur/transmission', 'number':'MOT1', 'hours':500}
    BATTERIE        = {'name':'Batterie/BMS', 'number':'BAT1', 'hours':500}
    
    ALL = [SIMULATEUR, INSTRUMENTATION, CONTROLE, GESTION, ERGONOMIE, COQUE, CHASSIS, DIRECTION, FREIN, THERMIQUE, SUSPENSION, MOTEUR, BATTERIE]

    @staticmethod
    def mapSysteme(number):
        """[Switch case pour aller chercher un objet Systeme avec le numéro de système]

        Args:
            number ([string]): [numéro de système]

        Returns:
            [Systeme]: [retourne l'objet de la classe Système associé au numéro de système]
        """
        return {
            'SIM1': Systeme.SIMULATEUR,
            'INS1': Systeme.INSTRUMENTATION,
            'MOT2': Systeme.CONTROLE,
            'GES1': Systeme.GESTION,
            'ERG1': Systeme.ERGONOMIE,
            'COQ1': Systeme.COQUE,
            'CHA1': Systeme.CHASSIS,
            'CHA_': Systeme.CHASSIS,
            'DIR1': Systeme.DIRECTION,
            'FRE1': Systeme.FREIN,
            'TTH1': Systeme.THERMIQUE,
            'SUS1': Systeme.SUSPENSION,
            'MOT1': Systeme.MOTEUR,
            'BAT1': Systeme.BATTERIE
        }[number]


class Speciality():
    """[Classe pour les différentes équipes du projet contenant les systèmes de chaque équipes ainsi que les membres]
    """
    INFO = {'systemes': [Systeme.SIMULATEUR, Systeme.INSTRUMENTATION, Systeme.CONTROLE, Systeme.ERGONOMIE, Systeme.GESTION],
            'membres': {'Louis Tardif':{'initials': 'L. T.'}, 'Alexandre Bergeron':{'initials': 'A. B.'}, 'Claude Garrison-Pelletier':{'initials': 'C. G.-P.'}, 'Malik Claveau':{'initials': 'M. C.'}, 'Marian Lambert-Rivest':{'initials': 'M. L.-R.'}, 'Gabriel Quirion':{'initials': 'G. Q.'}, 'Mathieu Parent':{'initials': 'M. P.'}, 'William Rousseau':{'initials': 'W. R.'}, 'Charles-Etienne Granger':{'initials': 'C.-E. G.'}}}
    MECA = {'systemes': [Systeme.SIMULATEUR, Systeme.COQUE, Systeme.CHASSIS, Systeme.DIRECTION, Systeme.FREIN, Systeme.THERMIQUE, Systeme.SUSPENSION, Systeme.ERGONOMIE, Systeme.GESTION],
            'membres': {'Joé Morin':{'initials': 'J. M.'}, 'Gabriel Ouellet':{'initials': 'G. O.'}, 'Donald Brouillard':{'initials': 'D. B.'}, 'Alexandre Dumont':{'initials': 'A. D.'}, "Jean-Simon D'Amours-Cyr":{'initials': 'J.-S. D.-C.'}, 'Jérémi Hamelin':{'initials': 'J. H.'}, 'Anthony Martin':{'initials': 'A. M.'}, 'Charles Ouzilleau':{'initials': 'C. O.'}, 'Marco Roger':{'initials': 'M. R.'}}}
    ELEC = {'systemes': [Systeme.SIMULATEUR, Systeme.INSTRUMENTATION, Systeme.CONTROLE, Systeme.MOTEUR, Systeme.BATTERIE, Systeme.GESTION, Systeme.THERMIQUE],
            'membres': {'Vincent Bonneau':{'initials': 'V. B.'}, 'Marc-Antoine Dubreuil':{'initials': 'M.-A. D.'}, 'Jérôme Gelé':{'initials': 'J. G.'}, 'François Paquette':{'initials': 'F. P.'}, 'Loïc Poirier':{'initials': 'L. P.'}, 'Joël Grégoire-Lagueux':{'initials': 'J.G.-L.'}, 'Gabriel Cabana':{'initials': 'G. C.'}, 'Thomas Chagnon':{'initials': 'T. C.'}, 'Xavier Morin':{'initials': 'X. M.'}}}
