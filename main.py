import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)
        for name, info in data.items():

            race_data = info["race"]
            race, created = Race.objects.get_or_create(
                name=race_data["name"],
                defaults={"description": race_data["description"]}
            )

            for skill_data in race_data["skills"]:
                skill, created = Skill.objects.get_or_create(
                    name=skill_data["name"],
                    race=race,
                    defaults={"bonus": skill_data["bonus"]}
                )

            guild_data = info.get("guild")
            if guild_data:
                guild, created = Guild.objects.get_or_create(
                    name=guild_data["name"],
                    defaults={"description": guild_data["description"]}
                )
            else:
                guild = None

            Player.objects.create(
                nickname=name,
                email=info["email"],
                bio=info["bio"],
                race=race,
                guild=guild,
            )


if __name__ == "__main__":
    main()
