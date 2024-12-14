def calculate_bmi(height: float, weight: float) -> float:
    """
    Calcule l'Indice de Masse Corporelle (BMI).
    :param height: Taille en mètres.
    :param weight: Poids en kilogrammes.
    :return: BMI arrondi à 2 décimales.
    """
    if height <= 0 or weight <= 0:
        raise ValueError("La taille et le poids doivent être supérieurs à 0.")
    return round(weight / (height ** 2), 2)

def calculate_bmr(height: float, weight: float, age: int, gender: str) -> float:
    """
    Calcule le Taux Métabolique de Base (BMR).
    :param height: Taille en centimètres.
    :param weight: Poids en kilogrammes.
    :param age: Âge en années.
    :param gender: Sexe ('male' ou 'female').
    :return: BMR arrondi à 2 décimales.
    """
    if height <= 0 or weight <= 0 or age <= 0:
        raise ValueError("La taille, le poids et l'âge doivent être supérieurs à 0.")
    
    gender = gender.lower()
    if gender == 'male':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender == 'female':
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        raise ValueError("Le genre doit être 'male' ou 'female'.")
    
    return round(bmr, 2)
