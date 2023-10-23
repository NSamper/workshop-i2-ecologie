import uuid
from django.db import models

# Possibilities Dicts

TRANSPORT_TYPES = [
    ("STTRU", "Standard Truck"),
    ("RFTRU", "Refrigirated Truck"),
    ("STTRA", "Standard Train"),
    ("STBOA", "Standard Boat"),
    ("STPLA", "Standard Plane"),
]

OBJECT_MATERIAL = [
    ('MET', "Metal"),
    ('WOO', "Wood"),
    ("PLA", "Plastic"),
    ('CHM', "Chemical Compound")
]

OBJECT_STATE = [
    ("RAW", "Raw material"),
    ("RFM", "Refined Material"),
    ("IPR", "In processing"),
    ("PRP", "Processed piece"),
    ("FIN", "Final State")
]

PROCESSES = [
    ("CUT", "Cut"),
    ("SME", "Smelt"),
    ("TRE", "Chemical Treatment"),
    ("SHP", "Reshape"),
    ("ASB", "Assemble")
]


# Models
class BaseModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    class Meta:
        abstract = True


class CompanyModel(BaseModel):
    impact_score = models.IntegerField(blank=True, null=True)

    class Meta:
        abstract = True


class ObjectItem(BaseModel):

    material = models.CharField(choices=OBJECT_MATERIAL, max_length=3)
    state = models.CharField(choices=OBJECT_STATE, max_length=3)

    def __str__(self):
        return str(self.state) + " " + str(self.material) + " " + str(self.id)[:5]


class Transport(CompanyModel):

    objectItem = models.ForeignKey(to=ObjectItem, on_delete=models.CASCADE, related_name="item")

    departure = models.DateTimeField()
    arrival = models.DateTimeField()

    transportType = models.CharField(choices=TRANSPORT_TYPES, max_length=5)

    def __str__(self):
        return "Transport of " + str(self.objectItem) + ", " + str(self.departure) + " - " + str(self.arrival)


class Transform(CompanyModel):

    objectItem_input = models.ForeignKey(to=ObjectItem, on_delete=models.CASCADE, related_name="input")
    objectItem_output = models.ForeignKey(to=ObjectItem, on_delete=models.CASCADE, related_name="output")

    departure = models.DateTimeField()
    arrival = models.DateTimeField()

    process = models.CharField(choices=PROCESSES, max_length=3)


    def __str__(self):
        return str(self.process) + ' of ' + str(self.objectItem_input) + " into " + str(self.objectItem_output) \
               + " , " + str(self.departure) + " - " + str(self.arrival)


class Storage(CompanyModel):

    objectItem = models.ForeignKey(to=ObjectItem, on_delete=models.CASCADE, related_name="objectItem")

    departure = models.DateTimeField()
    arrival = models.DateTimeField()

    def __str__(self):
        return "Storage of" + str(self.objectItem) + ", " + str(self.departure) + " - " + str(self.arrival)



class ProductChain(BaseModel):
    object = models.ForeignKey(to=ObjectItem, on_delete=models.CASCADE, related_name="object")
    lastStep = models.UUIDField()
    currStep = models.UUIDField()
    nextStep = models.UUIDField()

