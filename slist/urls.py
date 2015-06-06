from django.conf.urls import url
#from lists import views

urlpatterns = [
    # Examples:
    url(r'^$', 'lists.views.home_page', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
]
