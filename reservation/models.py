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


    def check_available_tables(self, reservation_start, reservation_end):
        table_list = []

        for t in Table.objects.all():
            table_list.append(t)

        for r in Reservation.objects.all():
            if Reservation.objects.all().count():
                reservation_start1 = (str(reservation_start) + '+00:00')
                if str(r.reservation_start) <= reservation_start1 <= str(r.reservation_end) and (str(r.reservation_start) <= str(reservation_end) <= str(r.reservation_end)):
                    if r.reservation_confirmed == True:
                        table_list.remove(r.table)

        for t in table_list:
            print(t)



    def different_way_check_available_tables(self, reservation_start, reservation_end, table):
        reservation_start1 = (str(reservation_start) + '+00:00')
        print(reservation_start)
        for r in Reservation.objects.filter(table=table):
            count = Reservation.objects.filter(table=table).count()
            print(count)
            if count > 1:
                if (str(r.reservation_start) <= str(reservation_start) <= str(r.reservation_end)) and (str(r.reservation_start) <= str(reservation_end) <= str(r.reservation_end)):
                    print(r.reservation_start)
                    if r.reservation_confirmed:
                        print('Reservation failed for ' + str(reservation_start) + ' ' + str(table))
                        return False
                    else:
                        print('Reservation succeeded')
                    return True
            else:
                print('reservation should be ok.')
                return True



           # if reservation_start == r.reservation_start:


'''
     table_list = []

            for t in Table.objects.all():
                table_list.append(t)
            for r in Reservation.objects.all():
                if reservation_start == r.reservation_start:
                    if r.reservation_confirmed == True:
                        table_list.remove(r.table)

            for t in table_list:
                print(t)

'''

  #  def __str__(self):
   #     return self.customer_name +  " " + str(self.reservation_start)


class ReservationDatabase(models.Model):
    reservation_datetime = models.DateTimeField()
    table = models.ForeignKey(Table, on_delete=models.CASCADE, null= True)
    customer = models.ForeignKey(Reservation, on_delete= models.CASCADE, null= True)

    def check_the_reservations(self, reservation_start):
        r = ReservationDatabase.objects.all()
       # print(r)













'''
        def create_reservation_json(self,name,email, reservation_start, reservation_end):

            return {
            'name' : name,
            'email': email,
            'reservation_start': reservation_start,
            'reservation_end' : reservation_end
        }


    #reservation list should be an json field in the end, organize accordingly.

    def check_available_tables(self, reservation_start):
        for t in Table.objects.all():
            if reservation_start in t.table_reservation_list:
                print('Reservation is not posible for table:', t)
            else:
                print('Reservation is possible for table: ', t)

#check the party size


'''

'''


    def reservation_analyse(self, form):
        customer_name = form.data['customer_name']
        reservation_start = form.data['reservation_start']
        reservation_format = datetime.datetime.strptime(reservation_start, "%Y-%m-%d %H:%M:%S")
        reservation_hour = reservation_format.strftime("%H")
        reservation_day = reservation_format.strftime('%w')
        print(reservation_day)
        print(reservation_hour)


                for t in Table.objects.all():
                    if reservation_start in t.table_reservation_list:
                        print('Reservation is not posible')
                        print(t.table_reservation_list)

                    else:
                        print("Reservation succeeded.")
                        t.table_reservation_list.append(reservation_start)
                        break
                        
'''

   # def new_reservation(self, reservation_start, customer_name):
    #    return reservation_start





















