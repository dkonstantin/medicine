from datetime import timedelta, datetime, time
from django.utils import timezone
from django import forms
from django.conf import settings
from django.db.models import Q
from django.forms import ModelForm, SplitDateTimeWidget
from medicine.models import Visit

class VisitForm(ModelForm):
    class Meta:
        model = Visit
        exclude = ['created_at']
        widgets = {
            'datetime': SplitDateTimeWidget
        }

    def clean_datetime(self):
        data = self.cleaned_data['datetime']

        if data < timezone.now():
            raise forms.ValidationError("Sorry, we do not work in the past.")
        if data.weekday() > 4:
            raise forms.ValidationError("You cannot sign up for holiday.")

        hour = int(data.strftime('%H'))
        minute = int(data.strftime('%M'))
        if (not hour in settings.JOB_TIME_RANGE) or (hour == settings.END_JOB_TIME-1 and minute > 0):
            raise forms.ValidationError("Working time is over.")

        if 'doctor' in self.cleaned_data:
            doctor = self.cleaned_data['doctor']
            end_date = data + timedelta(hours=1)
            visits = Visit.objects.filter(Q(doctor=doctor) &
                                          Q(datetime__gte=data) &
                                          Q(datetime__lte=end_date))
            if visits.count() > 0:
                raise forms.ValidationError("Busy time, select another hour")
        return data