from typing import Final

from django.db import models
from django.utils.translation.trans_null import gettext_lazy as _

_COMPANY_NAME_MAX_LENGTH: Final = 150


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/company_<name>/<filename>
    return f'company_{instance.name.replace(" ", "_")}/{filename.replace(" ", "_")}'


class Company(models.Model):

    name = models.CharField(_('name'), max_length=_COMPANY_NAME_MAX_LENGTH)
    description = models.TextField(_('description'))
    file = models.FileField(upload_to=user_directory_path)
    picture = models.ImageField(upload_to=user_directory_path)

    def __str__(self):
        """Returns company name."""
        return self.name
