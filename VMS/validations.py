from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


# Validations For Drivers
def license(value):
    if len(value) == 0 or len(value) > 15 or len(value) < 15:
        raise ValidationError(
            _('%(value)s is not a valid DL NO, Please eneter a valid DL no.'),
            params={'value': value},
            )


def adharCard(value):
    if len(value) == 0 or len(value) > 12 or len(value) < 12:
        raise ValidationError(
            _('%(value)s is not a valid Adhar Card NO, Please eneter a Adhar Card no.'),
            params={'value': value},
        )

def panCard(value):
    if len(value) == 0 or len(value) > 10 or len(value) < 10:
        raise ValidationError(
            _('%(value)s is not a valid DL NO, Please eneter a valid DL no.'),
            params={'value': value},
        )

def name(value):
    if value=="" or len(value) > 10:
        raise ValidationError(
            _('%(value)s is not a valid name, Please eneter your valid name.'),
            params={'value': value},
        )

def fullName(value):
    if value=="" or len(value) > 30:
        raise ValidationError(
            _('%(value)s is not a valid name, Please eneter your valid name.'),
            params={'value': value},
        )

def phoneNumber(value):
    number = str(value)
    if len(number) == 0 or len(number) > 12 or len(number) < 10:
        raise ValidationError(
            _('%(value)s is not a valid number, Please eneter your valid contact number.'),
            params={'value': number},
        )

def zipCode(value):
    number = str(value)
    if len(number) == 0 or len(number) > 6 or len(number) < 6:
        raise ValidationError(
            _('%(value)s is not a valid ZipCode, Please eneter a valid ZipCode.'),
            params={'value': number},
        )



# Validations For Vehicles
def name(value):
    if value=="" or len(value) > 10:
        raise ValidationError(
            _('%(value)s is not a valid name, Please eneter your valid name.'),
            params={'value': value},
        )

def ownerName(value):
    if value=="" or len(value) > 25:
        raise ValidationError(
            _('%(value)s is not a valid name, Please eneter your valid name.'),
            params={'value': value},
        )
    
def phoneNumber(value):
    number = str(value)
    if len(number) == 0 or len(number) > 12 or len(number) < 10:
        raise ValidationError(
            _('%(value)s is not a valid number, Please eneter your valid contact number.'),
            params={'value': number},
        )
        
def rcNumber(value):
    if len(value) == 0 or len(value) > 12 or len(value) < 12:
        raise ValidationError(
            _('%(value)s is not a valid number, Please eneter your valid contact number.'),
            params={'value': value},
        )

def policyNumber(value):
    if len(value) == 0 or len(value) > 12 or len(value) < 12:
        raise ValidationError(
            _('%(value)s is not a valid number, Please eneter your valid contact number.'),
            params={'value': value},
        )

def pucNumber(value):
    if len(value) == 0 or len(value) > 7 or len(value) < 7:
        raise ValidationError(
            _('%(value)s is not a valid number, Please eneter your valid contact number.'),
            params={'value': value},
        )

def vehicleNumber(value):
    if len(value) == 0 or len(value) > 10:
        raise ValidationError(
            _('%(value)s is not a valid number, Please eneter your valid contact number.'),
            params={'value': value},
        )