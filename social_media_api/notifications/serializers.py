from rest_framework import serializers
from .models import Notification
from django.contrib.contenttypes.models import ContentType

class NotificationSerializer(serializers.ModelSerializer):
    actor_username = serializers.CharField(source='actor.username', read_only=True)
    target = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = ['id', 'actor', 'actor_username', 'verb', 'target', 'unread', 'timestamp']

    def get_target(self, obj):
        # Provide minimal representation: content_type and id (can be expanded)
        if obj.target_content_type and obj.target_object_id:
            return {
                "app_label": obj.target_content_type.app_label,
                "model": obj.target_content_type.model,
                "object_id": obj.target_object_id
            }
        return None
