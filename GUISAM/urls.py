
from django.conf.urls import url
from GUISAM import views

app_name = 'GUISAM'
urlpatterns = [

    url(regex=r'^$', view=views.index, name='index'),
    url(regex=r'^assignment3/$', view=views.assignment3, name='assignment3'),
    url(regex=r'^assignment4/$', view=views.assignment4, name='assignment4'),
    url(regex=r'^assignment5/$', view=views.assignment5, name='assignment5'),
    url(regex=r'^assignment6/$', view=views.assignment6, name='assignment6'),
    url(regex=r'^assignment7/$', view=views.assignment7, name='assignment7'),
   # url(regex=r'^grub/$', view=views.grub, name='grub'),
    url(regex=r'^shutdown/$', view=views.shutdown, name='shutdown'),
    url(regex=r'^cancel-shutdown/$', view=views.cancel_shutdown, name='cancel-shutdown'),
    url(regex=r'^logout/$', view=views.logout, name='logout'),
    url(regex=r'^restart/$', view=views.restart, name='restart'),
    url(regex=r'^force-restart/$', view=views.force_restart, name='force-restart'),
    url(regex=r'^change-screen/$', view=views.change_screen, name='change-screen'),
    url(regex=r'^change-grub-order/$', view=views.grub_order, name='grub-order'),
    url(regex=r'^change-grub-timeout/$', view=views.grub_timeout, name='grub-timeout'),
    url(regex=r'^Add-user/$', view=views.Add_user, name='Add-user'),
    url(regex=r'^delete-user/$', view=views.delete_user, name='delete-user'),
    url(regex=r'^Add-group/$', view=views.Add_group, name='Add-group'),
    url(regex=r'^delete-group/$', view=views.delete_group, name='delete-group'),
    url(regex=r'^add-users-list/$', view=views.add_users_list, name='add-users-list'),
    #url(regex=r'^Add-batch/$', view=views.Add_batch, name='Add-batch'),
    url(regex=r'^memory-usage/$', view=views.memory_usage, name='memory-usage'),
    url(regex=r'^CPU-usage/$', view=views.CPU_usage, name='CPU-usage'),
    url(regex=r'^renice/$', view=views.renice, name='renice'),
    url(regex=r'^add-update-perm/$', view=views.set_perm, name='add-perm'),
    url(regex=r'^umask-cal/$', view=views.umask_cal, name='umask-cal'),
    url(regex=r'^add-update-user-perm-acl/$', view=views.acl_user_perm, name='user-acl'),
    url(regex=r'^add-update-group-perm-acl/$', view=views.acl_group_perm, name='group-acl'),
    url(regex=r'^rsyslog/$', view=views.rsyslog, name='rsyslog'),
    url(regex=r'^rsyslog-form/$', view=views.rsyslog_form, name='rsyslog-form'),
    url(regex=r'^log-rotate/$', view=views.log_rotate, name='log-rotate'),
    url(regex=r'^log-rotate-form/$', view=views.log_rotate_form, name='log-rotate-form'),
]