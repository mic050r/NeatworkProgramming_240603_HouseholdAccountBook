# 가계부(Household Account Book)
1. startproject householdAccountBook
   1. python -m pip install django~=4.2
   2. django-admin startproject householdAccountBook . 
   3. File > Settings ... > Language & Frameworks > Django > [v] Enable Django Support
   4. Run > Edit Configurations... > + Django Server > Name : runserver
   5. VCS > Enable Version Control Integration... > git > ok 
2. 차트용 실습 : startapp chart_test
   1. python manage.py startapp chart_test
   2. settings > INSTALLED_APPS > 'chart_test', 
3. chart_test/
   1. views
      1. show_chart()
   2. templates
      1. chart_view.html
   3. urls
      1. chart_test:show_chart
4. 프로젝트명/
   1. urls
      1. include('chart_test.urls')
   2. data/data.json
      1. 임시데이터
5. startapp accountbook
   1. python manage.py startapp accountbook
   2. settings.py > INSTALLED_APPS > 'accountbook'
6. accountbook/
   1. modles
      1. Category
         1. name, bgcolor
      2. AccountBook
         1. type(0: 지출, 1: 소비), price, category, time, contents, created)at, updated_at
         2. ~~photho~~
      3. python manage.py makemigrations accountbook
      4. python manage.py migrate
   2. admin
      1. Category
      2. AccountBook
      3. python manage.py createsuperuser
   3. views
      1. CategoryListView
      2. AccountbookListView
      3. AccountbookCreateView
      4. AccountbookUpdateView
      5. AccountbookDeleteView
      6. dashboard_accountBook()
      7. get_daily_accountbook_list()
      8. get_weekly_chart_data()
      9. get_all_chart_data()
      10. accountbook_createform()
   4. templates/accountbook/
      1. category_list.html
      2. accountbook_list.html
      3. accountbook_create.html
      4. accountbook_update.html
      5. account_confirm_delete.html
      6. accountbook_dashboard.html
         1. humanize
         2. reset.css, nav.css, dashboard.css
         3. calendar.js, calendar.css
         4. daily.css
         5. weekly.js
      7. daily_accountbook_list.html
      8. accountbook_createform.html
         1. createform.css
   5. urls 
      1. accountbook:category_list
      2. accountbook:accountbook_list
      3. accountbook:accountbook_create
      4. accountbook:accountbook_update
      5. accountbook:accountbook_delete
      6. accountbook:account_dashboard
      7. accountbook:daily_accountbook_list
      8. accountbook:weekly_chart_data
      9. accountbook:all_chart_data
      10. accountbook:accountbook_createform
   6. forms
      1. AccountBookForm
