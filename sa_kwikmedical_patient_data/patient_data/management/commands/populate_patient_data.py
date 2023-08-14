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
        "Running", "Jumping", "Swimming", "Cooking", "Driving", "Singing", "Dancing", "Painting",
        "Reading", "Writing", "Thinking", "Walking", "Sleeping", "Dreaming", "Flying", "Climbing",
        "Jogging", "Playing", "Eating", "Working", "Studying", "Teaching", "Learning", "Creating",
        "Building", "Baking", "Hiking", "Exploring", "Rowing", "Sailing", "Traveling", "Cycling",
        "Knitting", "Designing", "Sculpting", "Rowing", "Sailing", "Cycling", "Traveling", "Hiking",
        "Drawing", "Crafting", "Cooking", "Running", "Writing", "Singing", "Painting", "Swimming",
        "Thinking", "Dancing", "Teaching", "Learning", "Jumping", "Climbing", "Jogging", "Sleeping",
        "Dreaming", "Flying", "Driving", "Playing", "Baking", "Rowing", "Sailing", "Traveling",
        ]

        # Start date for random birthdates
        start_date = date(1960, 1, 1)

        # Loop to create patients
        for condition in CONDITION_CHOICES:
            injury_index = CONDITION_CHOICES.index(condition)
            for i in range(8):
                first_name = random.choice(given_names)
                last_name = random.choice(surnames)
                dob = start_date + timedelta(days=random.randint(0, 15000))  # Approximately 41 years

                # Assign the next injury choice sequentially
                injury_choice = INJURY_CHOICES[injury_index]

                # Create the patient record
                Patient.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    dob=dob,
                    condition_type=condition,
                    injury_type=injury_choice
                )

                # Move to the next injury type
                injury_index = (injury_index + 1) % len(INJURY_CHOICES)
                
        self.stdout.write(self.style.SUCCESS('Successfully populated the patient database with sample data'))