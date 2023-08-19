from django.core.management.base import BaseCommand
import random
from datetime import timedelta, date
from patient_data.models import Patient

class Command(BaseCommand):
    help = 'Populate the patient database with sample data'

    def handle(self, *args, **options):        # Delete existing data (optional)
        Patient.objects.all().delete()
        
        
        CONDITION_CHOICES = ["critical", "serious", "stable", "minor"]
        INJURY_CHOICES = ["head", "fracture", "burn", "internal", "superficial"]
        given_names = [
        "Goku", "Vegeta", "Piccolo", "Gohan", "Trunks", "Bulma", "Chi-Chi", "Krillin",
        "Frieza", "Cell", "Majin", "Aragorn", "Frodo", "Gandalf", "Legolas", "Gimli",
        "Samwise", "Bilbo", "Boromir", "Gollum", "Sauron", "Saruman", "Eowyn", "Galadriel", "Elrond", "Faramir",
        "Kirk", "Spock", "Picard", "Riker", "Data", "Worf", "Leia", "Luke", "Han", "Chewbacca",
        "Vader", "Yoda", "Obi-Wan", "Rey", "Finn", "Sephiroth", "Cloud", "Aerith", "Tifa", "Squall",
        "Rinoa", "Zidane", "Garnet", "Vivi", "Tidus", "Yuna", "Auron", "Vaan", "Ashe", "Lightning",
        "Geralt", "Yennefer", "Ciri", "Triss", "Jaskier", "Eskel", "Lambert", "Vesemir",
        "Kaulder", "Leiot Steinberg", "Kyouhei", "Ranmaru", "Yoshimasa", "Takeru", "Miyabi", "Himeji",
        "Hajime", "Sakamoto", "Kanji", "Ryu", "Ken", "Chun-Li", "Guile", "Blanka", "Dhalsim",
        "Thor", "Odin", "Zeus", "Horus", "Ra", "Anubis", "Isis", "Athena", "Hera", "Poseidon",    
        ]

        surnames = [
            "Enveloping", "Transmogrifying", "Galvanizing", "Peregrinating", "Exhilarating",
            "Percolating", "Resplendent", "Emanating", "Serendipitous", "Zephyrizing",
            "Quixotically", "Mellifluously", "Incandescent", "Effervescent", "Euphoric",
            "Synchronizing", "Ardently", "Cacophonous", "Nebulizing", "Vivaciously",
            "Bucolic", "Ebullient", "Halcyon", "Eclipsing", "Bewildering",
            "Panoramic", "Effulgent", "Cerulean", "Luminescent", "Elysian"
        ]

        num_loops = 50  # Number of loops to create patients

        start_date = date(1960, 1, 1)
        nhs_number_counter = 100000

        for i in range(num_loops):
            first_name = random.choice(given_names)
            last_name = random.choice(surnames)
            dob = start_date + timedelta(days=random.randint(0, 15000))
            nhs_number = f"NHS{nhs_number_counter}"
            nhs_number_counter += 1

            Patient.objects.create(
                first_name=first_name,
                last_name=last_name,
                dob=dob,
                nhs_number=nhs_number
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated the patient database with sample data'))