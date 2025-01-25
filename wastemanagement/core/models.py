from django.db import models
from django.utils import timezone

class WasteImage(models.Model):
    WASTE_TYPES = [
        ('organic', 'Organic'),
        ('recyclable', 'Recyclable'),
        ('hazardous', 'Hazardous'),
        ('other', 'Other'),
        ('unclassified', 'Unclassified')
    ]

    image = models.ImageField(upload_to='waste_images/')
    uploaded_at = models.DateTimeField(default=timezone.now)
    classification_result = models.CharField(
        max_length=20,
        choices=WASTE_TYPES,
        default='unclassified'
    )
    confidence_score = models.FloatField(null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Waste Image {self.id} - {self.classification_result}"

    class Meta:
        ordering = ['-uploaded_at']