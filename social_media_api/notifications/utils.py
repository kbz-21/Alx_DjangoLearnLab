from .models import Notification
from django.contrib.contenttypes.models import ContentType

def create_notification(recipient, actor, verb, target=None):
    """
    Create a notification. Target can be any model instance.
    """
    target_ct = None
    target_id = None
    if target is not None:
        target_ct = ContentType.objects.get_for_model(target)
        target_id = str(getattr(target, 'pk', None))
    # You might want to avoid duplicate notifications — check existing ones (optional)
    Notification.objects.create(
        recipient=recipient,
        actor=actor,
        verb=verb,
        target_content_type=target_ct,
        target_object_id=target_id
    )
