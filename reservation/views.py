from django.shortcuts import render, redirect, HttpResponse
from .forms import ReservationForm, DateSelected
from . models import Table, CustomerServiceHours, Reservation



def datetimecheckpage(request):
    if request.method == 'POST':
        form = DateSelected(request.POST)
        if form.is_valid():
            print('Hello')
            reservation_start = form.data['selected_date']

            table_list = []

            for t in Table.objects.all():
                table_list.append(str(t))
            print('initial list', table_list)
            for r in Reservation.objects.all():
                reservation_start1 = (str(reservation_start) + '+00:00')
                if str(r.reservation_start) <= reservation_start1 <= str(r.reservation_end):
                    if r.reservation_confirmed == True:
                        table_list.remove(str(r.table))

            context = {

            'table_list': table_list

            }
            print('here is the table list', table_list)

        return render(request, 'reservation/availabletables.html', context)




    else:
        form = DateSelected()
        return render(request, 'reservation/dateselected.html', {'form': form})





def home(request):
    if request.method == 'POST':
        result = False
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            reservation_request = Reservation.objects.get(customer_name=form.data['customer_name'], reservation_start=form.data['reservation_start'] )
            date_is_valid =reservation_request.reservation_date_past_or_future(reservation_request.reservation_start)
            if date_is_valid == True:
                hours_valid = reservation_request.check_whether_restaurant_is_open(reservation_request.reservation_start)
                if hours_valid == True:
                    reservation_request.check_available_tables(reservation_request.reservation_start)
                    result = reservation_request.different_way_check_available_tables(reservation_request.reservation_start, reservation_request.table)
                    if result == True:
                        reservation_request.reservation_confirmed = True
                        reservation_request.save()

                        print(reservation_request.customer_name)

        content = {
            'result': result
            }
        return render(request, 'reservation/result.html', content)

    if request.method == 'GET':
        form = ReservationForm()
        return render(request, 'reservation/reservation.html', {'form': form})
























