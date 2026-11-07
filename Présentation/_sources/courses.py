"""Métadonnées du cours IIN et répartition des 30 séances de 2 heures (60 heures)."""

COURS = r"C:\Users\Thierry MINKA\OneDrive\Documents\COURS"

IIN = {
    "sigle": "IIN",
    "code": "SEC4031",
    "titre": "Introduction à l'Investigation Numérique",
    "sous_titre": "Fondements, méthodes et cadre juridique de la forensique numérique",
    "master": "Département de Génie Informatique · HN4",
    "bandeau": "Université de Yaoundé I",
    "logo_g": "uy1",
    "logo_d": "enspy",
    "n_jours": 30,
    "annee": "2026-2027",
    "dossier": COURS + r"\ENSPY\SEC4031\Présentation",
    "fil_rouge": "MBONGO (prologue), ONAMBELE, TANGUE, MVOM (TRANSBOIS SA), WOURI",
    "parties": [
        ("Prologue", "La scène de crime numérique", "P00"),
        ("Partie I", "Fondements épistémologiques et historiques", "C01–C05"),
        ("Partie II", "Processus et méthodologies d'investigation", "C06–C09"),
        ("Partie III", "Cadre normatif, judiciaire et déontologique", "C10–C13"),
    ],
    # jour : (thème court, contenu détaillé, ateliers, labs)
    "jours": {
        1: ("Ouverture · La scène de crime numérique", "Présentation du cours + P00 §0.1-0.2", [], []),
        2: ("Le Trilemme CRO · Les dix premières minutes · MBONGO", "P00 §0.3-0.5", ["P00"], []),
        3: ("L'investigation comme pratique discursive · La trace", "C01 §1.1-1.3", [], []),
        4: ("Mathématiques, authenticité invisible, CRO, éthique", "C01 §1.4-1.7", ["C01"], []),
        5: ("Histoire (1) : des prémices à la standardisation", "C02 §2.1-2.3", [], []),
        6: ("Histoire (2) : big data, IA, Afrique, accélération", "C02 §2.4-2.7", ["C02"], []),
        7: ("Grandes affaires (1) : BTK, Stuxnet, WannaCry, Enron", "C03 §3.1-3.4", [], []),
        8: ("Grandes affaires (2) : ONAMBELE, TANGUE, MVOM, WOURI", "C03 §3.5-3.9", ["C03"], []),
        9: ("Locard numérique · Shannon · Graphes · Dolev-Yao", "C04 §4.1-4.4", [], []),
        10: ("Complexité, modèles de processus, théorie de la preuve", "C04 §4.5-4.8", ["C04"], []),
        11: ("État de l'art (1) : IA, deepfakes, cloud, IoT, mobile", "C05 §5.1-5.3", [], []),
        12: ("État de l'art (2) : OSINT, DICES, carrière", "C05 §5.4-5.7", ["C05"], []),
        13: ("Le PIU (1) : architecture, cadrage, Quality Gate 1", "C06 §6.1-6.2", [], []),
        14: ("Le PIU (2) : acquisition et analyse, QG2 et QG3", "C06 §6.3-6.4", [], []),
        15: ("Le PIU (3) : transmission, suivi, cas ROUSSEAU", "C06 §6.5-6.8", ["C06"], []),
        16: ("Standards (1) : DFRWS, ISO/IEC 2703x, NIST, RFC 3227", "C07 §7.1-7.5", [], []),
        17: ("Standards (2) : ACPO, FOR508, DICES, émergents", "C07 §7.6-7.9", ["C07"], []),
        18: ("Chaîne de custody (1) : fondements, loi, formulaire, protocoles", "C08 §8.1-8.4", [], []),
        19: ("Chaîne de custody (2) : erreurs fatales, MBONGO, admissibilité", "C08 §8.5-8.7", ["C08"], []),
        20: ("Acquisition (1) : write blocker, formats, FTK Imager, dd", "C09 §9.1-9.3", [], []),
        21: ("Acquisition (2) : mobile, Volatility 3", "C09 §9.4-9.5", [], []),
        22: ("Acquisition (3) : Wireshark, carving, choix des outils", "C09 §9.6-9.8", ["C09"], []),
        23: ("Cadre normatif (1) : Budapest, Malabo, protocoles", "C10 §10.1-10.3", [], []),
        24: ("Cadre normatif (2) : INTERPOL, AFRIPOL, MLAT, BAOBAB", "C10 §10.4-10.7", ["C10"], []),
        25: ("Législation mondiale (1) : droit américain et européen", "C11 §11.1-11.2", [], []),
        26: ("Législation mondiale (2) : Afrique régionale, stratégie", "C11 §11.3-11.4", ["C11"], []),
        27: ("Droit camerounais (1) : loi 2010/012, loi 2024/017", "C12 §12.1-12.3", [], []),
        28: ("Droit camerounais (2) : sanctions, qualification, procédure", "C12 §12.4-12.8", ["C12"], []),
        29: ("Déontologie (1) : cadres éthiques, tensions, PEACE, biais", "C13 §13.1-13.4", [], []),
        30: ("Déontologie (2) · ONAMBELE · Synthèse et clôture", "C13 §13.5-13.7 + synthèse", ["C13"], []),
    },
}

ALL = {"IIN": IIN}
