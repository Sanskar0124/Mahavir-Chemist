from django.db import models
from django.db.models.fields import AutoField, DateTimeField, TimeField
from django.utils.html import format_html
from datetime import date
from .choices import DRIVING_TIME, DRIVER_STATUS, DRIVER_EXPERIENCE, OWNER_SHIP, VEHICLE_TYPE, FUEL_TYPE, PERMIT_TYPE, VEHICLE_STATUS, TRAVEL_STATUS, MARRATIAL
from .validations import license, adharCard, name, panCard, phoneNumber, zipCode, name, fullName, ownerName, phoneNumber, policyNumber, pucNumber, rcNumber, vehicleNumber
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
    marritial_status = models.CharField(max_length=20, choices=MARRATIAL, default='Single')
    driver_image = models.ImageField(upload_to="drivers/images", default="")


    def license_exp_remaining(self):
        datRem = self.license_exp_date - current_date
        strDate = str(datRem).split()
        intDate = int(strDate[0])
        if(intDate < 0):
            return format_html(
                '<span style="color: {};">{}</span>',
                "red",
                "Need to renew",
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
        else:
            return format_html(
                '<span style="color: {};">{}</span>',
                "green",
                "No need to worry",
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
    branch = models.CharField(max_length=15, default="", validators=[fullName])
    base_location = models.CharField(max_length=15, default="", validators=[fullName])
    zip_code = models.IntegerField(default=0, validators=[zipCode])
    address = models.CharField(max_length=200)
    driving_time = models.CharField(max_length=20, choices=DRIVING_TIME, default='day')
    status = models.CharField(max_length=10, choices=DRIVER_STATUS, default='Active')
    experience = models.CharField(max_length=20, choices=DRIVER_EXPERIENCE, default='2 - 4')
    date_of_birth = models.DateField(default=datetime.date.today)
    salary = models.IntegerField(default=0)
    license_no = models.ForeignKey(DriverDoc, on_delete=models.CASCADE)
    note = models.ForeignKey(DriverNote, on_delete=models.CASCADE)

    def Driver_status(self):
        # print(self.status)
        if(self.status == "Active"):
            return format_html(
                '<span style="color: {};">{}</span>',
                "green",
                "Active",
                )
        elif(self.status == "Engage"):
            return format_html(
                '<span style="color: {};">{}</span>',
                "yellow",
                "Engage",
                )
        else:
            return format_html(
                '<span style="color: {};">{}</span>',
                "red",
                "InActive",
                )    

    def __str__(self):
        return self.first_name +" "+ self.last_name



class VehicleDoc(Base):
    id = models.AutoField
    owner_name = models.CharField(max_length=25, default="", validators=[fullName])
    owner_phone = models.IntegerField(default=0, validators=[phoneNumber])
    rc_book = models.ImageField(upload_to="vehiclesDocs/images", default="")
    rc_number = models.CharField(max_length=15, default="", validators=[rcNumber])
    papers_img = models.ImageField(upload_to="vehiclesDocs/images", default="") 
    permit = models.ImageField(upload_to="vehiclesDocs/images", default="")

    def __str__(self):
        return self.rc_number


class VehicleMaintainance(Base):
    id = models.AutoField
    vehicle_number = models.CharField(max_length=30, default="", validators=[vehicleNumber])
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
        if(intDate < 15):
            return format_html(
                '<span style="color: {};">{}</span>',
                "red",
                str(intDate) + " Days remaining",
                )
        if(intDate < 30):
            return format_html(
                '<span style="color: {};">{}</span>',
                "orange",
                str(intDate) + " Days remaining",
                )
        if(intDate < 45):
            return format_html(
                '<span style="color: {};">{}</span>',
                "green",
                str(intDate) + " Days remaining",
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
        if(intDate < 15):
            return format_html(
                '<span style="color: {};">{}</span>',
                "red",
                str(intDate) + " Days remaining",
                )
        if(intDate < 30):
            return format_html(
                '<span style="color: {};">{}</span>',
                "orange",
                str(intDate) + " Days remaining",
                )
        if(intDate > 45):
            return format_html(
                '<span style="color: {};">{}</span>',
                "green",
                str(intDate) + " Days remaining",
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

    
    def __str__(self):
        return str(self.vehicle_number)



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
    Rc_number = models.ForeignKey(VehicleDoc, on_delete=models.CASCADE)
    number_plate = models.ForeignKey(VehicleMaintainance, on_delete=models.CASCADE)
    vehicle_image = models.ImageField(upload_to="vehicles/images", default="")
    def save(self, *args, **kwargs):
        message = "Your vehicle is ready to departure"
        status = "Unseen"
        driverMessage = DriverNote(message=message, status=status)
        driverMessage.save() 
        super(Vehicle, self).save(*args, **kwargs)

    def Vehicle_status(self):
        # print(self.status)
        if(self.status == "Active"):
            return format_html(
                '<span style="color: {};">{}</span>',
                "green",
                "Active",
                )
        else:
            return format_html(
                '<span style="color: {};">{}</span>',
                "red",
                "InActive",
                )  

    @property            
    def Vehicles_Image(self):
        return mark_safe('<img src="{}" width="180" height="130" />'.format(self.vehicle_image.url))

    def __str__(self):
        return self.model



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
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    destination = models.CharField(max_length=15)
    estimated_time = models.CharField(max_length=15)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=30, choices=TRAVEL_STATUS, default='Ready to deliver')

    def Travel_status(self):
        # print(self.status)
        if(self.status == "Active"):
            return format_html(
                '<span style="color: {};">{}</span>',
                "green",
                "Active",
                )
        else:
            return format_html(
                '<span style="color: {};">{}</span>',
                "red",
                "InActive",
                )  

    def __str__(self):
        return str(self.order_id)