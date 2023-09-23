from register.register import Register
import register.constants as const



run = Register()
run.get_url()
run.booking_test()
run.search_box(country=const.COUNTRY, city=const.EXAM_CITY)
run.type_of_format()
run.choose_all_days()
run.search_button()
run.date_of_test(test_day=const.EXAM_DAY, test_month=const.EXAM_MONTH, test_year=const.EXAM_YEAR)
run.check_account(email=const.EMAIL)

