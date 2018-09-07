import datetime
dd = datetime.datetime.strptime(date,'%y%m%d')
if dd.year > 2005:
   dd = dd.replace(year=dd.year-100)
