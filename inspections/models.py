from django.db import models
from django.urls import reverse
import datetime
from datetime import date

# Create your models here.
class Inspector(models.Model):
    fname = models.CharField(max_length = 50, help_text = "Enter first name", verbose_name="First name")
    lname = models.CharField(max_length = 50, help_text = "Enter last name", verbose_name= "Last name")
    INSPECTOR_STATUS = ( 
        ('a', 'Active'),
        ('r', 'Retired'),
    )
    status = models.CharField(max_length=1, choices=INSPECTOR_STATUS, default='a', help_text='Inspector status')
    
    def __str__(self):
        return '%s %s' % (self.fname, self.lname)
        
    def get_absolute_url(self):
        return reverse('inspector-detail', args=[str(self.id)])
    
class OperationType(models.Model):
    type_of_operation = models.CharField(max_length = 100, help_text = "Enter operation")
    
    def __str__(self):
        return self.type_of_operation
        
    def get_absolute_url(self):
        return reverse('operationtype-detail', args=[str(self.id)])
        
class CityTown(models.Model):
    name = models.CharField(max_length = 100, help_text = "City / Town of")
    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('citytown-detail', args=[str(self.id)])
    
class inspectionsEstablishment(models.Model):
    name = models.CharField(max_length = 100, help_text = "Enter name")
    address = models.CharField(max_length = 200, help_text = "Enter address")
    phone_number = models.CharField(max_length = 16, help_text = "Enter phone number")
    # from phonenumber_field.modelfields import PhoneNumberField
    # phone_number = PhoneNumberField()
    
    type_of_operation = models.ManyToManyField(OperationType)
    person_in_charge = models.CharField(max_length = 100, help_text = "Enter name of person in charge")
    permit_no = models.CharField(max_length = 50, help_text = "Enter permit number")
    city_town = models.ForeignKey('CityTown', on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('inspectionsestablishment-detail', args=[str(self.id)])
    
class inspectionsEstablishmentInspectionReport(models.Model):
    inspector = models.ForeignKey( 
        'Inspector', 
        on_delete=models.SET_NULL, 
        null=True, 
        limit_choices_to={'status':'a'} 
    )
    inspections_establishment = models.ForeignKey('inspectionsEstablishment', on_delete=models.SET_NULL, null=True)
    date = models.DateField('Inspection Date', default=date.today )
    
    # This field is for testing purposes only.
    inspection_data = models.CharField(max_length = 100, help_text = "Test data only", null=True)
    
    def __str__(self):
        return '%s, Inspected on %s by %s.' % (self.inspections_establishment, self.date, self.inspector)

    def get_absolute_url(self):
        return reverse('inspectionreport-detail', args=[str(self.id)])