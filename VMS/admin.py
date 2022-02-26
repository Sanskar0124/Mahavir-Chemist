from django.contrib import admin
from .models import Driver, DriverNote, DriverDoc, VehicleDoc,Vehicle, VehicleMaintainance, Travel


# Drivers Models
class DriverAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name","license_no",  "phone1", "email", "Driver_status", "branch", "salary","driving_time")

class DriverDocAdmin(admin.ModelAdmin):
    list_display = ("license_no", "adharCard_no", "license_exp_date", "license_exp_remaining", "license_status","drivers_image")
    readonly_fields = ('drivers_image',)

admin.site.register(Driver, DriverAdmin)
admin.site.register(DriverNote)
admin.site.register(DriverDoc, DriverDocAdmin)



# Vehicles Models
class VehicleAdmin(admin.ModelAdmin):
    list_display = ( "model", "Rc_number","number_plate","vehicle_type", "fuel_type", "permit_type", "Vehicle_status", "Vehicles_Image")

class VehicleMaintainanceAdmin(admin.ModelAdmin):
    list_display = ("vehicle_number", "last_service", "servicing_days_remaining", "insurance_exp_remaining","puc_exp_remaining", "updated_at")

class VehicleDocAdmin(admin.ModelAdmin):
    list_display = ("rc_number", "owner_name", "owner_phone")

admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(VehicleDoc, VehicleDocAdmin)
admin.site.register(VehicleMaintainance, VehicleMaintainanceAdmin)



# Travels Models
class TravelAdmin(admin.ModelAdmin):
    list_display = ("order_id", "vehicle", "driver", "updated_at", "Travel_status")

admin.site.register(Travel, TravelAdmin)