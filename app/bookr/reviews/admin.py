from django.contrib import admin
# # # from django.contrib.admin import AdminSite
# # from admin import main_admin_site

from reviews.models import Publisher, Contributor, Book, \
    BookContributor, Review


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'isbn')

@admin.register(Publisher, Contributor, \
    BookContributor, Review)
class ReviewsAdminSite(admin.ModelAdmin):
    title_header = 'Reviews Admin'
    site_header = 'Reviews administration'
    index_title = 'Reviews site admin'


# reviews_admin_site = ReviewsAdminSite
# Register your models here.
# admin.site.register(Publisher, BookrAdminSite)
# admin.site.register(Contributor, BookrAdminSite)
# admin.site.register(Book, BookrAdminSite)
# admin.site.register(BookContributor, BookrAdminSite)
# admin.site.register(Review, BookrAdminSite)
