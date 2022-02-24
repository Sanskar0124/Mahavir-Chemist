from django.contrib import admin
from .models import Driver, DriverNote, DriverDoc, VehicleDoc,Vehicle, VehicleMaintainance, Travel, Routes


# Drivers Models
class DriverAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "phone1","status","driving_time", "salary", "documents")

class DriverDocAdmin(admin.ModelAdmin):
    list_display = ( "license_no", "license_exp_date", "license_exp_remaining", "license_status","drivers_image")
    readonly_fields = ('drivers_image',)

admin.site.register(Driver, DriverAdmin)
admin.site.register(DriverNote)
admin.site.register(DriverDoc, DriverDocAdmin)



# Vehicles Models
class VehicleAdmin(admin.ModelAdmin):
    list_display = ("model", "ownerShip","carrying_space","carrying_capacity","volume", "vehicle_type", "fuel_type", "permit_type", "status", "Vehicles_Image")

class VehicleMaintainanceAdmin(admin.ModelAdmin):
    list_display = ("last_service", "servicing_days_remaining", "insurance_exp_remaining","insurance_status","puc_exp","puc_exp_remaining", "puc_status", "updated_at")

class VehicleDocAdmin(admin.ModelAdmin):
    list_display = ("owner_name", "owner_phone", "rc_number")

admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(VehicleDoc, VehicleDocAdmin)
admin.site.register(VehicleMaintainance, VehicleMaintainanceAdmin)



# Travels Models
class TravelAdmin(admin.ModelAdmin):
    list_display = ("order", "vehicle", "driver", "updated_at" ,"departure_loc", "destination", "status")

admin.site.register(Travel, TravelAdmin)
admin.site.register(Routes)
