from src.load import ScheduleSDSFactory

try:
    sched = ScheduleSDSFactory("..\TestData\MSIMFILE")
    print("Read {0} lines".format(sched.getSchedule()))

except FileNotFoundError as ex:
    print("Unable to open MSIMFILE: {0}".format(ex))

