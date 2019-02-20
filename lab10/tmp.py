import datetime

def get_weekday_name(date, lang):
    named_wd = {
        'bg':["понеделник", "вторник", "сряда", "четвъртък", "петък", "събота", "неделя"],
        'en':["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    }
    


    wd_name = named_wd[lang][date.weekday()]
    return wd_name

now = datetime.datetime.now()

print('Today is', get_weekday_name(now, "bg"))