from unittest.mock import MagicMock

from django.core.files import File
from django.test import TestCase
import os
from datetime import date


from .models import Maid


class TestMaid(TestCase):
    def test_model_should_have_fields(self):
        maid = Maid.objects.create(
            name='BB',
            birthday=date(1998, 4, 29),
            description='Maid of the year',
            certificate='Best maid 2017',
            salary=3000,
        )   

        maid = Maid.objects.last()

        self.assertEqual(maid.name, 'BB')
        self.assertEqual(maid.birthday, date(1998, 4, 29))
        self.assertEqual(maid.description, 'Maid of the year')
        self.assertEqual(maid.certificate, 'Best maid 2017')
        self.assertEqual(maid.salary, 3000)

    def test_model_should_have_image_profile(self):
        image = MagicMock(spec=File)
        image.name = 'profile.png'

        maid = Maid.objects.create(
            name='BB',
            profile_image=image,
            birthday=date(1998, 4, 29),
            description='Maid of the year',
            certificate='Best maid 2017',
            salary=3000,
        )  

        self.assertEqual(maid.profile_image, image)

        os.remove('profile.png')
