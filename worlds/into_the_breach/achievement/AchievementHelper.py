from .Achievements import achievements_by_squad


def can_get_all_achievements(squad) -> bool:
    squad_achievements = achievements_by_squad[squad.name]
    for achievement_name in squad_achievements:
        achievement = squad_achievements[achievement_name]
        if not achievement.is_doable_by_squad(squad):
            return False
    return True
