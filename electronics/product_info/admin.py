from django.contrib import admin


from product_info.models import Sales, Products, Contacts


class SalesAdmin(admin.ModelAdmin):
    list_display = ('chain_link', 'title', 'provider_link', 'arrears', 'creation_time')
    list_fields = ('country',)
    list_editable = ('arrears',)
    fieldsets = [
        (None, {'fields': ['chain_link', 'title', 'providers', 'arrears', 'creation_time']}),
        ('contacts', {'fields': ['email', 'country', 'city', 'street', 'home_number']}),
        ('products', {'fields': ['product_title', 'model', 'date_release']}),
    ]

    def provider_link(self, obj):
        """ссылка на поставщика"""
        if obj.provider:
            return "<a href='%s'>Link</a>" % obj.provider
        else:
            return ''


admin.site.register(Sales, SalesAdmin)
admin.site.register(Products)
admin.site.register(Contacts)


@admin.action(description='Обнуление задолженности перед поставщиком')
def clean_arrears(self, request, queryset):
    queryset.update(arrears=0)
