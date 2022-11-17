from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

admin.site.register(FormBlockAdminModel)
admin.site.register(ManagersModel)


class EmployeeInstanceInline(admin.StackedInline):
    """Employees inline"""
    model = EmployeeAdminModel
    extra = 0
    fields = (('employee_name', 'employee_position'), 'employee_photo', 'get_image')
    readonly_fields = ('get_image', )


class GalleryImageInstanceInline(admin.TabularInline):
    """Gallery images inline"""
    model = GalleryImageModel
    extra = 0
    readonly_fields = ('get_image', )


class ProductInstanceInline(admin.StackedInline):
    """Product inline"""
    model = ProductModel
    extra = 0
    fields = (('product_name', 'product_property'), 'product_description', ('product_photo', 'get_image'), )
    readonly_fields = ('get_image', )


@admin.register(LandingModel)
class LandingModelAdmin(admin.ModelAdmin):
    """Landing settings admin panel"""
    fieldsets = (
        ('Верхний блок лендинга', {
            'fields': ('top_utp',
                       'top_descriptor',
                       'top_fb_url',
                       'top_tw_url',
                       'top_insta_url',
                       'top_picture')
        }),
        ('Блок "О нас"', {
            'fields': ('about_us_header',
                       'about_us_text1',
                       'about_us_text2',
                       'about_us_picture1',
                       'about_us_picture2',
                       'about_us_value',
                       'about_us_capacity',
                       'about_us_employee')
        }),
        ('Блок "Продукты"', {
            'fields': ('products_header',
                       'products_description',
                       'products_first_card_utp',
                       'products_first_card_desc',
                       'products_second_card_utp',
                       'products_second_card_desc',
                       'products_third_card_utp',
                       'products_third_card_desc',
                       )
        }),
        ('Блок "Преимущества"', {
            'fields': ('benefits_header',
                       'benefits_first',
                       'benefits_second',
                       'benefits_third',
                       'benefits_fourth',
                       'benefits_fifth',
                       'benefits_sixth',
                       'benefits_seventh')
        }),
        ('Блок "Галерея"', {
            'fields': ('gallery_header',),
        }),
        ('Блок "Наша команда"', {
            'fields': ('team_header',)
        }),
        ('Блок "Футер"', {
            'fields': ('footer_address', 'footer_email', 'fax_footer', 'form_personal_data')
        })
    )
    inlines = [EmployeeInstanceInline, GalleryImageInstanceInline, ProductInstanceInline]

    def has_add_permission(self, request, obj=None):
        if self.get_queryset(request):
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        return False


