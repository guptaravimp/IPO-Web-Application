from django.contrib import admin
from home.models import IPOUpcoming
from home.models import FaqModel
# Register your models here.
class upcommmingadmin(admin.ModelAdmin):
    list_display=('icons','company_name','company_link','price_band',
    'open_date','close_date','issue_size','issue_type','listing_date')

admin.site.register(IPOUpcoming,upcommmingadmin)

class faqAdmin(admin.ModelAdmin):
    list_display=('question','ans1','ans2','ans3','ans4','ans5')
admin.site.register(FaqModel,faqAdmin)