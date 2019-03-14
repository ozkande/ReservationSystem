from django.db import models
from contactus.models import CustomerServiceHours
from datetime import datetime
import pytz


class Table(models.Model):
    table_number = models.IntegerField()
    table_type = models.IntegerField()
    table_reservation_list = []

    def __str__(self):
        return "Table number " + str(self.table_number)


class Reservation(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.CharField(max_length= 100, null=True)
    reservation_start = models.DateTimeField()
    reservation_end = models.DateTimeField()
    reservation_confirmed = models.BooleanField(default = False)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, null=True)
    reservation_list = []


    def reservation_date_past_or_future(self, reservation_start):
        # This function validates whether the user defined date is in the future.

        if reservation_start > datetime.now(tz=pytz.timezone('Europe/Helsinki')):
            print('The time is in the future')
            return True
        else:
            print('Time is in the past')
            return False


    def check_whether_restaurant_is_open(self, reservation_start):
        # This function validates whether the restaurant is open during the user defined hours

        reservation_day = reservation_start.strftime('%w')
        reservation_hour = reservation_start.strftime("%H")
        service_hours = CustomerServiceHours.objects.get(id=reservation_day)
        opens = service_hours.company_open_hours_start
        closes = service_hours.company_open_hours_end

        if (reservation_hour > opens) and (reservation_hour < closes):
            print('restaurant is open')
            return True

        else:
            print('restaurant is closed')
            return False


    def check_available_tables(self, reservation_start):
        table_list = []

        for t in Table.objects.all():
            table_list.append(t)
        for r in Reservation.objects.all():
            if reservation_start == r.reservation_start:
                reservation_start1 = (str(reservation_start) + '+00:00')
                if str(r.reservation_start) <= reservation_start1 <= str(r.reservation_end):
                    if r.reservation_confirmed == True:
                        table_list.remove(r.table)

        for t in table_list:
            print(t)



    def different_way_check_available_tables(self, reservation_start, table):
        reservation_start1 = (str(reservation_start) + '+00:00')
        for r in Reservation.objects.filter(table=table):
            if str(r.reservation_start) <= str(reservation_start) <= str(r.reservation_end):
                print('reservation start' , r.reservation_start)
                print('you wanna reserve', reservation_start)
                print('reservation end' , r.reservation_end)
                if r.reservation_confirmed:
                    print('we are booked for that table')
                    return False
            else:
                print('Reservation succeeded for ' + str(reservation_start) + ' ' + str(table))
                return True









































