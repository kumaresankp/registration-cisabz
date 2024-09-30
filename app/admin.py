from django.contrib import admin
from .models import Registration, Event

class TechnicalEventFilter(admin.SimpleListFilter):
    title = 'Technical Events'
    parameter_name = 'technical_events'

    def lookups(self, request, model_admin):
        events = Event.objects.filter(event_type='technical')
        return [(event.id, event.name) for event in events]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(technical_events__id=self.value())
        return queryset

class NonTechnicalEventFilter(admin.SimpleListFilter):
    title = 'Non-Technical Events'
    parameter_name = 'non_technical_events'

    def lookups(self, request, model_admin):
        events = Event.objects.filter(event_type='non_technical')
        return [(event.id, event.name) for event in events]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(non_technical_events__id=self.value())
        return queryset

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    # Customize the list display in the admin panel
    list_display = ('name', 'college', 'get_technical_events', 'get_non_technical_events', 'phone', 'email')
    
    # Add search capability to the admin panel
    search_fields = ('name', 'college', 'phone', 'email')

    # Add custom filters for technical and non-technical events
    list_filter = (TechnicalEventFilter, NonTechnicalEventFilter, 'college')

    # Optional: Add ordering
    ordering = ('name',)

    # Optional: Customize the admin form layout
    fieldsets = (
        (None, {
            'fields': ('name', 'college', 'technical_events', 'non_technical_events', 'phone', 'email')
        }),
    )

    # Custom methods to display events in list_display
    def get_technical_events(self, obj):
        return ", ".join([event.name for event in obj.technical_events.all()])
    get_technical_events.short_description = 'Technical Events'

    def get_non_technical_events(self, obj):
        return ", ".join([event.name for event in obj.non_technical_events.all()])
    get_non_technical_events.short_description = 'Non-Technical Events'
