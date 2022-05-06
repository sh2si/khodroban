from django.db import models


class Car(models.Model):
    """
    Defining Car specs
    """

    class Meta:
        verbose_name = "خودرو"
        verbose_name_plural = "خودروها"

    COMMON_COLORS = (
        (1, "سفید"),
        (2, "مشکی"),
        (3, "خاکستری (طوسی)"),
        (4, "قرمز"),
        (5, "نارنجی (مسی | آجری)"),
        (6, "آبی"),
        (7, "سرمه ای (آبی تیره | آبی نفتی)"),
        (8, "سبز"),
        (9, "فسفری"),
        (10, "طلایی"),
        (11, "نقره ای"),
        (12, "یشمی (سبز تیره)"),
        (13, "بژ (کرم | خاکی | شیری)"),
        (14, "زرد"),
        (15, "متفرقه"),
    )
    car_brand = models.CharField("نوع خودرو", max_length=30)
    car_model = models.CharField("مدل", max_length=40)
    generation_year = models.PositiveSmallIntegerField(
        "سال ساخت", null=True, blank=True
    )
    reg_kilometer_indicator = models.BigIntegerField(
        "کیلومتر طی شده", null=True, blank=True
    )
    paint_color = models.PositiveSmallIntegerField("رنگ", choices=COMMON_COLORS)

    def year_model(self):
        ym = str(self.generation_year)
        if ym[2] == "0":
            return ym
        else:
            return ym[2:]

    def __str__(self):
        return f"{self.car_brand} {self.car_model} \({self.year_model()}"
