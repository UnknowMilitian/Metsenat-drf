from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, Group, Permission


# Create your models here.
class Payment(models.Model):
    money = models.IntegerField(_("Maney"), default=1000000)

    def __str__(self):
        return self.money


class User(AbstractUser):
    class Type_user(models.TextChoices):
        sponsor = "Sponsor", "sponsor"
        student = "Student", "student"

    type_user = models.CharField(
        max_length=8, choices=Type_user, default=Type_user.student
    )
    fullname = models.CharField(_("Fullname"), max_length=255)
    telephone = models.CharField(_("Telephone"), max_length=255, unique=True)
    payment = models.ForeignKey(
        Payment,
        verbose_name=_("Payment"),
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="user_payment",
    )
    company = models.CharField(_("Company"), max_length=255, null=True, blank=True)

    # Adding related_name to avoid clashes with the default auth models
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",
        blank=True,
        help_text=_(
            "The groups this user belongs to. A user will get all permissions "
            "granted to each of their groups."
        ),
        verbose_name=_("groups"),
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",
        blank=True,
        help_text=_("Specific permissions for this user."),
        verbose_name=_("user permissions"),
    )

    def __str__(self):
        return self.fullname
