# encoding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse
from manozodynas.testutils import StatefulTesting
from .models import Terminai

class IndexTestCase(StatefulTesting):
    def test_index_page(self):
        self.open(reverse('index'))
        self.assertStatusCode(200)


class TerminaiTestCase(TestCase):
    def setUp(self):
        Terminai.objects.create(en_term="pc", lt_term="kompiuteris")
        Terminai.objects.create(en_term="fan", lt_term="ventiliatorius")

    def test_termino_ivedima_objektas(self):
        pc = Terminai.objects.get(en_term="pc")
        fan = Terminai.objects.get(en_term="fan")
        self.assertEqual(pc.get_translation(), "kompiuteris")
        self.assertEqual(fan.get_translation(), "ventiliatorius")
        
        # groteles rodo kad id is html ima
        
        
class TerminaiStatefulTesting(StatefulTesting):
    
    def test_termino_ivedima_pilnas(self):
        self.open(reverse('naujo_termino_ivedimas'))
        self.selectForm('#terminui-form')
        self.submitForm({
                         'input': 'Hard_disk,kietasis_diskas',
                         })
        self.assertStatusCode(200)