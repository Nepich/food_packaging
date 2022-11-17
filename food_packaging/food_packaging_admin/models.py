from django.db import models
from django.utils.safestring import mark_safe


class LandingModel(models.Model):
    """Model for landing exclude 'Form' block"""
    top_utp = models.TextField(verbose_name='UTP')
    top_descriptor = models.TextField(verbose_name='Описание utp')
    top_fb_url = models.URLField(verbose_name='Facebook url')
    top_tw_url = models.URLField(verbose_name='Twitter url')
    top_insta_url = models.URLField(verbose_name='Instagram url')
    top_picture = models.ImageField(upload_to='top/', verbose_name='Изображение для блока')
    about_us_header = models.CharField(max_length=100, verbose_name='Название блока', default='О нас')
    about_us_text1 = models.TextField(verbose_name='Первая часть текста')
    about_us_text2 = models.TextField(verbose_name='Вторая часть текста')
    about_us_picture1 = models.ImageField(upload_to='about_us/', verbose_name='Изображение для блока о нас 1')
    about_us_picture2 = models.ImageField(upload_to='about_us/', verbose_name='Изображение для блока о нас 2')
    about_us_value = models.TextField(verbose_name='Значение производительности (добавьте единицы измерения)')
    about_us_capacity = models.TextField(verbose_name='Значение объема выполненных работ (добавьте единицы измерения)')
    about_us_employee = models.IntegerField(verbose_name='Значение числа сотрудников')
    products_header = models.CharField(max_length=100, verbose_name='Название блока', default='Продукция')
    products_description = models.TextField(verbose_name='Описание для блока продукции')
    products_first_card_utp = models.TextField(verbose_name='Первая карточка продукции название')
    products_first_card_desc = models.TextField(verbose_name='Первая карточка продукции описание')
    products_second_card_utp = models.TextField(verbose_name='Вторая карточка продукции название')
    products_second_card_desc = models.TextField(verbose_name='Вторая карточка продукции описание')
    products_third_card_utp = models.TextField(verbose_name='Третья карточка продукции название')
    products_third_card_desc = models.TextField(verbose_name='Третья карточка продукции описание')
    benefits_header = models.CharField(max_length=100, verbose_name='Название блока', default='Почему именно мы?')
    benefits_first = models.TextField(verbose_name='Первое преимущество')
    benefits_second = models.TextField(verbose_name='Второе преимущество')
    benefits_third = models.TextField(verbose_name='Третье преимущество')
    benefits_fourth = models.TextField(verbose_name='Четвертое преимущество')
    benefits_fifth = models.TextField(verbose_name='Пятое преимущество')
    benefits_sixth = models.TextField(verbose_name='Шестое преимущество')
    benefits_seventh = models.TextField(verbose_name='Седьмое преимущество')
    gallery_header = models.CharField(max_length=100, verbose_name='Название блока', default='Галерея')
    team_header = models.CharField(max_length=100, verbose_name='Название блока', default='Наша команда')
    form_personal_data = models.FileField(upload_to='uploads/', verbose_name='Соглашение о персональных данных')
    footer_address = models.TextField(verbose_name='Адрес компании')
    footer_email = models.CharField(max_length=100, verbose_name='Email компании')
    fax_footer = models.CharField(max_length=100, verbose_name='Факс компании')

    class Meta:
        verbose_name = 'Настройка лендинга'
        verbose_name_plural = 'Настройки лендинга'

    def __str__(self):
        return f'Настройка полей лендинга'


class EmployeeAdminModel(models.Model):
    """Model for employee in 'Employee' landing block"""
    employee_name = models.CharField(max_length=200, verbose_name='Имя и фамилия сотрудника')
    employee_position = models.CharField(max_length=100, verbose_name='Должность сотрудника')
    employee_photo = models.ImageField(upload_to='employee/', verbose_name='Фото сотрудника')
    employee_block = models.ForeignKey(to=LandingModel, on_delete=models.CASCADE, related_name='employees')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f'{self.employee_name}'

    def get_image(self):
        if self.employee_photo:
            return mark_safe(f'<img src={self.employee_photo.url} width="50" height="60"')
        else:
            return '(No image)'

    get_image.short_description = 'Изображение'


class GalleryImageModel(models.Model):
    """Model for images in 'Gallery' landing block"""
    photo = models.ImageField(upload_to='gallery/', verbose_name='Фото для галереи')
    gallery_block = models.ForeignKey(to=LandingModel, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = 'Фото для галереи'
        verbose_name_plural = 'Фото для галереи'

    def __str__(self):
        return f'Фото галереи {self.photo}'

    def get_image(self):
        if self.photo:
            return mark_safe(f'<img src={self.photo.url} width="50" height="60"')
        else:
            return '(No image)'

    get_image.short_description = 'Изображение'


class ProductModel(models.Model):
    """Model for products to 'Products' landing block"""
    product_name = models.CharField(max_length=200, verbose_name='Название продукта')
    product_description = models.TextField(verbose_name='Описание продукта')
    product_property = models.CharField(max_length=100, verbose_name='Свойства продукта (добавьте единицы измерения)')
    product_photo = models.ImageField(upload_to='products/', verbose_name='Фото продукта')
    products_block = models.ForeignKey(to=LandingModel, on_delete=models.CASCADE, related_name='products')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.product_name}'

    def get_image(self):
        if self.product_photo:
            return mark_safe(f'<img src={self.product_photo.url} width="50" height="60"')
        else:
            return '(No image)'

    get_image.short_description = 'Изображение'


class FormBlockAdminModel(models.Model):
    """Model for 'Form' landing block"""
    form_customer_name = models.CharField(max_length=200, verbose_name='Имя')
    form_customer_phone = models.CharField(max_length=20, verbose_name='Телефон')
    form_customer_message = models.TextField(verbose_name='Сообщение')

    class Meta:
        verbose_name = 'Блок "Заявки"'
        verbose_name_plural = 'Блок "Заявки"'

    def __str__(self):
        return f'Заявка от {self.form_customer_name}'


class ManagersModel(models.Model):
    """Model for email notification"""
    managers_name = models.CharField(max_length=100, verbose_name='Имя менеджера')
    managers_email = models.CharField(max_length=100, verbose_name='Емэйл для отправки почты')

    class Meta:
        verbose_name = 'Менеджер'
        verbose_name_plural = 'Менеджеры'

    def __str__(self):
        return f'Менеджер {self.managers_name}'
