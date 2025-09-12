from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    """Добавляет существующего пользователя в группу moders"""

    def add_arguments(self, parser):
        parser.add_argument(
            "user_id", type=int, help="ID пользователя для добавления в группу moders"
        )

    def handle(self, *args, **kwargs):
        user_id = kwargs["user_id"]
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            self.stdout.write(
                self.style.ERROR(f"Пользователь с ID {user_id} не найден.")
            )
            return

        try:
            group = Group.objects.get(name="moders")
        except Group.DoesNotExist:
            self.stdout.write(self.style.ERROR('Группа "moders" не найдена.'))
            return

        user.groups.add(group)
        self.stdout.write(
            self.style.SUCCESS(
                f"Пользователь {user.username} добавлен в группу moders."
            )
        )
