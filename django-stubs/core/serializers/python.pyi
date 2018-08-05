from collections import OrderedDict
from typing import Any, Iterator, List, Optional

from django.core.serializers import base
from django.core.serializers.base import DeserializedObject
from django.db.models.base import Model
from django.db.models.fields import Field
from django.db.models.fields.related import ForeignKey, ManyToManyField


class Serializer(base.Serializer):
    options: Dict[Any, Any]
    selected_fields: None
    stream: _io.StringIO
    use_natural_foreign_keys: bool
    use_natural_primary_keys: bool
    internal_use_only: bool = ...
    objects: List[Any] = ...
    def start_serialization(self) -> None: ...
    def end_serialization(self) -> None: ...
    def start_object(self, obj: Model) -> None: ...
    def end_object(self, obj: Model) -> None: ...
    def get_dump_object(self, obj: Model) -> OrderedDict: ...
    def handle_field(self, obj: Model, field: Field) -> None: ...
    def handle_fk_field(self, obj: Model, field: ForeignKey) -> None: ...
    def handle_m2m_field(self, obj: Model, field: ManyToManyField) -> None: ...
    def getvalue(self): ...

def Deserializer(
    object_list: List,
    *,
    using: Any = ...,
    ignorenonexistent: bool = ...,
    **options: Any
) -> Iterator[DeserializedObject]: ...