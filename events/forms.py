# -*- encoding:utf-8 -*-
#
# Copyright (C) 2009 Novopia Solutions Inc.
#
# Author: Pierre-Luc Beaudoin <pierre-luc.beaudoin@novopia.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from django import forms
from events.models import Event, City, Region
from events.widgets import SplitSelectDateTimeWidget
from django.forms.util import ErrorList
from datetime import datetime

class EventForm(forms.ModelForm):
    start_time = forms.DateTimeField(widget=SplitSelectDateTimeWidget(hour_step=1, \
        minute_step=15, second_step=30, twelve_hr=False, years=[2009,2010,2011]))

    end_time = forms.DateTimeField(widget=SplitSelectDateTimeWidget(hour_step=1, \
        minute_step=15, second_step=30, twelve_hr=False, years=[2009,2010,2011]))

    city = forms.ModelChoiceField(City.objects.all(), empty_label=None, label="Ville")

    class Meta:
      model = Event
      exclude = ('submission_time', 'updated_time', 'decision_time',
                 'moderator', 'moderated', 'latitude', 'longitude')

    def clean(self):
      cleaned_data = self.cleaned_data
      start_time = cleaned_data.get("start_time")
      end_time = cleaned_data.get("end_time")

      if start_time >= end_time:
        msg = u"L'évènement ne peut se terminer avant son début"
        self._errors["start_time"] = ErrorList([msg])
        self._errors["end_time"] = ErrorList([msg])

        del cleaned_data["start_time"]
        del cleaned_data["end_time"]

      elif start_time < datetime.today():
        msg = u"Seul les évènements à venir sont acceptés"
        self._errors["start_time"] = ErrorList([msg])

        del cleaned_data["start_time"]

      return cleaned_data

class RegionFilterForm (forms.Form):
    region = forms.ModelChoiceField(Region.objects.all(), empty_label="Toutes les régions", required=False, label="Région",
        widget=forms.Select(attrs={'onchange':'document.getElementById("filter").submit();'}))

