from django.contrib.auth.models import Permission

# Получить все объекты разрешений
permissions = Permission.objects.all()

# Вывести список разрешений
for permission in permissions:
    print(permission)
