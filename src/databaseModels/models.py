import uuid

from django.contrib.contenttypes.models import ContentType
from django.db import models

# Possibilities Dicts
from polymorphic.models import PolymorphicModel

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


EXTRACTIONS = [
    ("MIN", "Mining"),
    ("CHO", "Chopping"),
    ("CHE", "Chemical Creation"),
]

STORAGE = [
    ("WRH", "Warehouse"),
    ("RWH", "Refrigerated Warehouse"),
    ("HWH", "Heated Warehouse"),
]


# Models
class BaseModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    class Meta:
        abstract = True


class CompanyModel(PolymorphicModel):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    impact_score = models.IntegerField(blank=True, null=True)

    date_in = models.DateTimeField()
    date_out = models.DateTimeField()
    

class ObjectItem(BaseModel):

    material = models.CharField(choices=OBJECT_MATERIAL, max_length=3)
    state = models.CharField(choices=OBJECT_STATE, max_length=3)
    category = models.CharField(max_length=3, null=True, blank=True)

    address = models.CharField(max_length=50, null=True, blank=True)
    supplier = models.CharField(null=True, blank=True, max_length=50)
    website = models.CharField(null=True, blank=True, max_length=50)
    brand = models.CharField(null=True, blank=True, max_length=50)

    def __str__(self):
        return str(self.supplier) + " " + str(self.brand) + " " + str(self.id)[:5]


class Transport(CompanyModel):

    objectItem = models.ForeignKey(to=ObjectItem, on_delete=models.CASCADE, related_name="item")

    transportType = models.CharField(choices=TRANSPORT_TYPES, max_length=5)

    quantity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return "Transport of " + str(self.objectItem) + ", " + str(self.date_in) + " - " + str(self.date_out)


class Transform(CompanyModel):

    objectItem_input = models.ForeignKey(to=ObjectItem, on_delete=models.CASCADE, related_name="input")
    objectItem_output = models.ForeignKey(to=ObjectItem, on_delete=models.CASCADE, related_name="output")

    process = models.CharField(choices=PROCESSES, max_length=3)


    def __str__(self):
        return str(self.process) + ' of ' + str(self.objectItem_input) + " into " + str(self.objectItem_output) \
               + " , " + str(self.date_in) + " - " + str(self.date_out)


class Storage(CompanyModel):

    objectItem = models.ForeignKey(to=ObjectItem, on_delete=models.CASCADE, related_name="objectItem")

    storageType = models.CharField(choices=STORAGE, max_length=3, null=True, blank=True)

    def __str__(self):
        return "Storage of " + str(self.objectItem) + ", " + str(self.date_in) + " - " + str(self.date_out)


class Extracts(CompanyModel):

    objectItem_output = models.ForeignKey(to=ObjectItem, on_delete=models.CASCADE, related_name="extr_output")

    extract_type = models.CharField(choices=EXTRACTIONS, max_length=3)

    def __str__(self):
        return "Extraction of" + str(self.objectItem_output) + ", " + str(self.date_out)


class ProductChain(BaseModel):
    object = models.ForeignKey(to=ObjectItem, on_delete=models.CASCADE, related_name="object")
    lastStep = models.ForeignKey(to=CompanyModel, on_delete=models.CASCADE, related_name="lastStep", null=True, blank=True)
    currStep = models.ForeignKey(to=CompanyModel, on_delete=models.CASCADE, related_name="currStep")
    nextStep = models.ForeignKey(to=CompanyModel, on_delete=models.CASCADE, related_name="nextStep", null=True, blank=True)

    def __str__(self):
        return str(self.currStep)
