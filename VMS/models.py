from django.db import models
from django.db.models.fields import AutoField, DateTimeField, TimeField
from django.utils.html import format_html
from datetime import date
from .choices import DRIVING_TIME, DRIVER_STATUS, DRIVER_EXPERIENCE, OWNER_SHIP, VEHICLE_TYPE, FUEL_TYPE, PERMIT_TYPE, VEHICLE_STATUS, TRAVEL_STATUS
from .validations import license, adharCard, name, panCard, phoneNumber, zipCode, name, ownerName, phoneNumber, policyNumber, pucNumber, rcNumber, vehicleNumber
from django.utils.html import mark_safe
from shop.models import Orders
import datetime 

current_date = date.today()

# Create your models here.

# Base Class
class Base(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


# Models for Drivers.
class DriverNote(Base):
    id = models.AutoField
    message = models.CharField(max_length=200)
    status = models.CharField(max_length=20)
    def __str__(self):
        return self.status+" - " +self.message

class DriverDoc(Base):
    id = models.AutoField
    license_img = models.ImageField(upload_to="driversDocs/images", default="")
    license_no = models.CharField(max_length=15, validators=[license])
    license_exp_date = models.DateField()
    adharCard_img = models.ImageField(upload_to="driversDocs/images", default="")
    adharCard_no = models.CharField(max_length=15, validators=[adharCard])
    panCard_img = models.ImageField(upload_to="driversDocs/images", default="")
    panCard_no = models.CharField(max_length=15, validators=[panCard])
    marritial_status = models.CharField(max_length=20)
    driver_image = models.ImageField(upload_to="drivers/images", default="")


    def license_exp_remaining(self):
        datRem = self.license_exp_date - current_date
        strDate = str(datRem).split()
        intDate = int(strDate[0])
        if(intDate < 0):
            return format_html(
                '<span style="color: {};">{}</span>',
                "red",
                "Need to reneve",
                )
        if(intDate < 30):
            return format_html(
                '<span style="color: {};">{}</span>',
                "red",
                str(intDate) + " Days remaining",
                )
        if(intDate < 60):
            return format_html(
                '<span style="color: {};">{}</span>',
                "orange",
                str(intDate) + " Days remaining",
                )
    
    def license_status(self):
        datRem = self.license_exp_date - current_date
        strDate = str(datRem).split()
        intDate = int(strDate[0])
        if(intDate < 0):
            return format_html(
                '<span style="color: {};">{}</span>',
                "red",
                "InActive",
                )
        else:
            return format_html(
                '<span style="color: {};">{}</span>',
                "green",
                "Active",
                )

    @property            
    def drivers_image(self):
        return mark_safe('<img src="{}" width="160" height="130" />'.format(self.driver_image.url))

    # @property
    # def driver_name(self):
    #     name = Driver.first_name
    #     return name

    def __str__(self):
        return self.license_no


class Driver(Base):
    id = models.AutoField
    first_name = models.CharField(max_length=15, validators=[name])
    last_name = models.CharField(max_length=15, validators=[name])
    phone1 = models.IntegerField(default=0, validators=[phoneNumber])
    phone2 = models.IntegerField(default=0, validators=[phoneNumber])
    email = models.EmailField(max_length=150, default="")
    branch = models.CharField(max_length=15, default="", validators=[name])
    base_location = models.CharField(max_length=15, default="", validators=[name])
    zip_code = models.IntegerField(default=0, validators=[zipCode])
    address = models.CharField(max_length=200)
    driving_time = models.CharField(max_length=20, choices=DRIVING_TIME, default='day')
    status = models.CharField(max_length=10, choices=DRIVER_STATUS, default='Active')
    experience = models.CharField(max_length=20, choices=DRIVER_EXPERIENCE, default='2 - 4')
    date_of_birth = models.DateField(default=datetime.date.today)
    salary = models.IntegerField(default=0)
    documents = models.ForeignKey(DriverDoc, on_delete=models.CASCADE)
    note = models.ForeignKey(DriverNote, on_delete=models.CASCADE)
    def __str__(self):
        return self.first_name +" "+ self.last_name + " - "+ self.status



class VehicleDoc(Base):
    id = models.AutoField
    owner_name = models.CharField(max_length=15, default="", validators=[ownerName])
    owner_phone = models.IntegerField(default=0, validators=[phoneNumber])
    rc_book = models.ImageField(upload_to="vehiclesDocs/images", default="")
    rc_number = models.CharField(max_length=15, default="", validators=[rcNumber])
    papers_img = models.ImageField(upload_to="vehiclesDocs/images", default="") 
    permit = models.ImageField(upload_to="vehiclesDocs/images", default="")

    def __str__(self):
        return self.owner_name

class VehicleMaintainance(Base):
    id = models.AutoField
    last_service = models.DateField()
    insurance_policy_no = models.CharField(max_length=12,default="", validators=[policyNumber])
    insurance_exp = models.DateField()
    puc_no = models.CharField(max_length=12,default="", validators=[pucNumber])
    puc_exp = models.DateField()

    def insurance_exp_remaining(self):
        datRem = self.insurance_exp - current_date
        strDate = str(datRem).split()
        intDate = int(strDate[0])
        if(intDate < 0):
            return format_html(
                '<span style="color: {};">{}</span>',
                "red",
                "Need to reneve",
                )
        if(intDate < 30):
            return format_html(
                '<span style="color: {};">{}</span>',
                "red",
                str(intDate) + " Days remaining",
                )
        if(intDate < 60):
            return format_html(
                '<span style="color: {};">{}</span>',
                "orange",
                str(intDate) + " Days remaining",
                )
        if(intDate > 60):
            return format_html(
                '<span style="color: {};">{}</span>',
                "green",
                str(intDate) + " Days remaining",
                )

    def insurance_status(self):
        datRem = self.insurance_exp - current_date
        strDate = str(datRem).split()
        intDate = int(strDate[0])
        if(intDate < 0):
            return format_html(
                '<span style="color: {};">{}</span>',
                "red",
                "InActive",
                )
        else:
            return format_html(
                '<span style="color: {};">{}</span>',
                "green",
                "Active",
                )

    def puc_exp_remaining(self):
        datRem = self.puc_exp - current_date
        strDate = str(datRem).split()
        intDate = int(strDate[0])
        if(intDate < 0):
            return format_html(
                '<span style="color: {};">{}</span>',
                "red",
                "Need to reneve",
                )
        if(intDate < 30):
            return format_html(
                '<span style="color: {};">{}</span>',
                "red",
                str(intDate) + " Days remaining",
                )
        if(intDate < 60):
            return format_html(
                '<span style="color: {};">{}</span>',
                "orange",
                str(intDate) + " Days remaining",
                )
        if(intDate > 60):
            return format_html(
                '<span style="color: {};">{}</span>',
                "green",
                str(intDate) + " Days remaining",
                )

    def puc_status(self):
        datRem = self.puc_exp - current_date
        strDate = str(datRem).split()
        intDate = int(strDate[0])
        if(intDate < 0):
            return format_html(
                '<span style="color: {};">{}</span>',
                "red",
                "InActive",
                )
        else:
            return format_html(
                '<span style="color: {};">{}</span>',
                "green",
                "Active",
                )

    def servicing_days_remaining(self):
        servicingTime = 90
        datRem = current_date - self.last_service
        strDate = str(datRem).split()
        intDate = int(strDate[0])
        remains = servicingTime-intDate  
        if(intDate < 70):
            return format_html(
                '<span style="color: {};">{}</span>',
                "green",
                str(remains) + " Days remaining",
                )
        if(intDate > 90):
            return format_html(
                '<span style="color: {};">{}</span>',
                "red",
                "Need Servicing",
                )
        if(intDate > 75):
            return format_html(
                '<span style="color: {};">{}</span>',
                "red",
                str(remains) + " Days remaining",
                )
        if(intDate > 55):
            return format_html(
                '<span style="color: {};">{}</span>',
                "orange",
                str(remains) + " Days remaining",
                )



# Models For Vehicles
class Vehicle(Base):
    id = models.AutoField
    model = models.CharField(max_length=30)
    ownerShip = models.CharField(max_length=30, choices=OWNER_SHIP, default='Company')
    vehicle_type = models.CharField(max_length=15, choices=VEHICLE_TYPE)
    fuel_type = models.CharField(max_length=15, choices=FUEL_TYPE, default='Diesel')
    permit_type = models.CharField(max_length=15, choices=PERMIT_TYPE, default='State')
    branch = models.CharField(max_length=15, default="")
    current_branch = models.CharField(max_length=12, default="")
    status = models.CharField(max_length=15, choices=VEHICLE_STATUS, default='Active')
    carrying_capacity = models.CharField(max_length=15, default="")
    carrying_space = models.CharField(max_length=15, default="")
    length = models.FloatField(default=0)
    breadth = models.FloatField(default=0)
    height = models.FloatField(default=0)
    volume = models.FloatField(default=0)
    documents = models.ForeignKey(VehicleDoc, on_delete=models.CASCADE)
    maintainence = models.ForeignKey(VehicleMaintainance, on_delete=models.CASCADE)
    number_plate = models.CharField(max_length=30, default="", validators=[vehicleNumber])
    vehicle_image = models.ImageField(upload_to="vehicles/images", default="")
    def save(self, *args, **kwargs):
        message = "Your vehicle is ready to departure"
        status = "Unseen"
        driverMessage = DriverNote(message=message, status=status)
        driverMessage.save() 
        super(Vehicle, self).save(*args, **kwargs)

    @property            
    def Vehicles_Image(self):
        return mark_safe('<img src="{}" width="180" height="130" />'.format(self.vehicle_image.url))

    def __str__(self):
        return self.number_plate + self.status



# Models For Travels
class Routes(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=15)
    destination_1 = models.CharField(max_length=15)
    destination_2 = models.CharField(max_length=15)
    destination_3 = models.CharField(max_length=15)
    destination_4 = models.CharField(max_length=15)
    destination_5 = models.CharField(max_length=15)
    destination_6 = models.CharField(max_length=15)
    destination_7 = models.CharField(max_length=15)
    destination_8 = models.CharField(max_length=15)
    destination_9 = models.CharField(max_length=15)
    destination_10 = models.CharField(max_length=15)
    def __str__(self):
        return self.name

class Travel(models.Model):
    id = models.AutoField
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    routes = models.ForeignKey(Routes, on_delete=models.CASCADE)
    location = models.CharField(max_length=15)
    departure_time = models.CharField(max_length=15)
    departure_loc = models.CharField(max_length=15)
    destination = models.CharField(max_length=15)
    estimated_time = models.CharField(max_length=15)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=30, choices=TRAVEL_STATUS, default='Ready to deliver')
    def __str__(self):
        return self.departure_loc+" to " +self.destination