from django.contrib import admin



from things.models import DeadPeople
from things.models import LivePeople
from things.models import Thing
from things.models import LiveThings
from things.models import DeadThings
from things.models import Holder

admin.site.register(DeadPeople)
admin.site.register(LivePeople)
admin.site.register(LiveThings)
admin.site.register(DeadThings)
admin.site.register(Thing)
admin.site.register(Holder)