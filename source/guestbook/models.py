from django.db import models

BOOK_ACTIVE_CHOICE = 'active'
BOOK_ACTIVE_CHOICE_2 = 'blocked'
BOOK_STATUS = (
    (BOOK_ACTIVE_CHOICE, 'Active'),
    (BOOK_ACTIVE_CHOICE_2, 'Blocked')
)


class GuestBook(models.Model):
    status = models.CharField(max_length=20, verbose_name='Status',
                              choices=BOOK_STATUS,
                              default=BOOK_ACTIVE_CHOICE
                              )
    name = models.CharField(max_length=25, verbose_name='Name')
    email = models.EmailField(max_length=70, verbose_name='Email', null=False, blank=False)
    text = models.TextField(max_length=1000, verbose_name='Text')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'GuestBook'
        verbose_name_plural = 'GuestBooks'
