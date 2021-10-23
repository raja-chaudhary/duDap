from django.shortcuts import render
from sex.models import Sex
from discussions.models import Discussion
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta, datetime


# Create your views here.

@login_required
def stats_view(request):
    charts = [
        all_sex_vs_arguments(request),
        sex_ytd_monthly_weekly(request),
        arguments_ytd_monthly_weekly(request)
    ]
    print(charts)
    return render(request, "stats/stats.html", context={"charts": charts})


def all_sex_vs_arguments(request):
    all_sex = Sex.objects.filter(sex_user=request.user).count()
    all_arguments = Discussion.objects.filter(user=request.user).count()
    context = {
        'all_sex': all_sex,
        'all_arguments': all_arguments
    }
    return context


def sex_ytd_monthly_weekly(request):
    starting_day_of_current_year = datetime.now().date().replace(month=1, day=1)
    startdate = date.today() + timedelta(days=1)
    weekly_startdate = startdate - timedelta(days=6)
    monthly_startdate = startdate - timedelta(days=30)
    # ytd_enddate = datetime(2021, 1, 1)
    sex_past_week = Sex.objects.filter(sex_user=request.user,
                                       created__range=[weekly_startdate, startdate]).count()
    sex_past_month = Sex.objects.filter(sex_user=request.user,
                                        created__range=[monthly_startdate, startdate]).count()
    sex_this_year = Sex.objects.filter(sex_user=request.user,
                                       created__range=[starting_day_of_current_year, startdate]).count()
    print(sex_past_week)

    context = {
        'sex_past_week': sex_past_week,
        'sex_past_month': sex_past_month,
        'sex_this_year': sex_this_year
    }
    return context


def arguments_ytd_monthly_weekly(request):
    starting_day_of_current_year = datetime.now().date().replace(month=1, day=1)
    startdate = date.today() + timedelta(days=1)
    weekly_startdate = startdate - timedelta(days=6)
    monthly_startdate = startdate - timedelta(days=30)
    # ytd_enddate = datetime(2021, 1, 1)
    print(starting_day_of_current_year)
    arguments_past_week = Discussion.objects.filter(user=request.user,
                                                    created__range=[weekly_startdate, startdate]).count()
    arguments_past_month = Discussion.objects.filter(user=request.user,
                                                     created__range=[monthly_startdate, startdate]).count()
    arguments_this_year = Discussion.objects.filter(user=request.user,
                                                    created__range=[starting_day_of_current_year, startdate]).count()

    context = {
        'arguments_past_week': arguments_past_week,
        'arguments_past_month': arguments_past_month,
        'arguments_this_year': arguments_this_year
    }
    return context
