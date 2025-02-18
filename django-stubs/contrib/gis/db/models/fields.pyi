from collections.abc import Iterable
from typing import Any, NamedTuple, TypeVar

from django.contrib.gis import forms
from django.contrib.gis.geos import (
    GeometryCollection,
    GEOSGeometry,
    LineString,
    MultiLineString,
    MultiPoint,
    MultiPolygon,
    Point,
    Polygon,
)
from django.core.validators import _ValidatorCallable
from django.db.models.expressions import Combinable, Expression
from django.db.models.fields import NOT_PROVIDED, Field, _ErrorMessagesMapping
from django.utils.choices import _Choices
from django.utils.functional import _StrOrPromise

# __set__ value type
_ST_contra = TypeVar("_ST_contra", contravariant=True)
# __get__ return type
_GT_co = TypeVar("_GT_co", covariant=True)

class SRIDCacheEntry(NamedTuple):
    units: Any
    units_name: str
    spheroid: str
    geodetic: bool

def get_srid_info(srid: int, connection: Any) -> SRIDCacheEntry: ...

class BaseSpatialField(Field[_ST_contra, _GT_co]):
    form_class: type[forms.GeometryField]
    geom_type: str
    geom_class: type[GEOSGeometry] | None
    geography: bool
    spatial_index: bool
    srid: int
    def __init__(
        self,
        verbose_name: _StrOrPromise | None = ...,
        srid: int = ...,
        spatial_index: bool = ...,
        *,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: bool = ...,
        db_index: bool = ...,
        default: Any = ...,
        db_default: type[NOT_PROVIDED] | Expression | _ST_contra = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: _Choices | None = ...,
        help_text: _StrOrPromise = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesMapping | None = ...,
    ) -> None: ...
    def db_type(self, connection: Any) -> Any: ...
    def spheroid(self, connection: Any) -> Any: ...
    def units(self, connection: Any) -> Any: ...
    def units_name(self, connection: Any) -> Any: ...
    def geodetic(self, connection: Any) -> Any: ...
    def get_placeholder(self, value: Any, compiler: Any, connection: Any) -> Any: ...
    def get_srid(self, obj: Any) -> Any: ...
    def get_db_prep_value(self, value: Any, connection: Any, *args: Any, **kwargs: Any) -> Any: ...
    def get_raster_prep_value(self, value: Any, is_candidate: Any) -> Any: ...
    def get_prep_value(self, value: Any) -> Any: ...

class GeometryField(BaseSpatialField[_ST_contra, _GT_co]):
    dim: int
    def __init__(
        self,
        verbose_name: _StrOrPromise | None = ...,
        dim: int = ...,
        geography: bool = ...,
        *,
        extent: tuple[float, float, float, float] = ...,
        tolerance: float = ...,
        srid: int = ...,
        spatial_index: bool = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: bool = ...,
        db_index: bool = ...,
        default: Any = ...,
        db_default: type[NOT_PROVIDED] | Expression | _ST_contra = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: _Choices | None = ...,
        help_text: _StrOrPromise = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesMapping | None = ...,
    ) -> None: ...
    def formfield(  # type: ignore[override]
        self,
        *,
        form_class: type[forms.GeometryField] | None = ...,
        geom_type: str = ...,
        srid: Any = ...,
        **kwargs: Any,
    ) -> forms.GeometryField: ...
    def select_format(self, compiler: Any, sql: Any, params: Any) -> Any: ...

# __set__ value type
_POINTFIELDST_contra = TypeVar("_POINTFIELDST_contra", contravariant=True, default=Point | Combinable)
# __get__ return type
_POINTFIELDGT_co = TypeVar("_POINTFIELDGT_co", covariant=True, default=Point)

class PointField(GeometryField[_POINTFIELDST_contra, _POINTFIELDGT_co]):
    _pyi_private_set_type: Point | Combinable
    _pyi_private_get_type: Point
    _pyi_lookup_exact_type: Point

    geom_class: type[Point]
    form_class: type[forms.PointField]

# __set__ value type
_LINESTRINGFIELDST_contra = TypeVar("_LINESTRINGFIELDST_contra", contravariant=True, default=LineString | Combinable)
# __get__ return type
_LINESTRINGFIELDGT_co = TypeVar("_LINESTRINGFIELDGT_co", covariant=True, default=LineString)

class LineStringField(GeometryField[_LINESTRINGFIELDST_contra, _LINESTRINGFIELDGT_co]):
    _pyi_private_set_type: LineString | Combinable
    _pyi_private_get_type: LineString
    _pyi_lookup_exact_type: LineString

    geom_class: type[LineString]
    form_class: type[forms.LineStringField]

# __set__ value type
_POLYGONFIELDST_contra = TypeVar("_POLYGONFIELDST_contra", contravariant=True, default=Polygon | Combinable)
# __get__ return type
_POLYGONFIELDGT_co = TypeVar("_POLYGONFIELDGT_co", covariant=True, default=Polygon)

class PolygonField(GeometryField[_POLYGONFIELDST_contra, _POLYGONFIELDGT_co]):
    _pyi_private_set_type: Polygon | Combinable
    _pyi_private_get_type: Polygon
    _pyi_lookup_exact_type: Polygon

    geom_class: type[Polygon]
    form_class: type[forms.PolygonField]

# __set__ value type
_MULTIPOINTFIELDST_contra = TypeVar("_MULTIPOINTFIELDST_contra", contravariant=True, default=Polygon | Combinable)
# __get__ return type
_MULTIPOINTFIELDGT_co = TypeVar("_MULTIPOINTFIELDGT_co", covariant=True, default=Polygon)

class MultiPointField(GeometryField[_MULTIPOINTFIELDST_contra, _MULTIPOINTFIELDGT_co]):
    _pyi_private_set_type: MultiPoint | Combinable
    _pyi_private_get_type: MultiPoint
    _pyi_lookup_exact_type: MultiPoint

    geom_class: type[MultiPoint]
    form_class: type[forms.MultiPointField]

# __set__ value type
_MULTILINESTRINGFIELDST_contra = TypeVar(
    "_MULTILINESTRINGFIELDST_contra", contravariant=True, default=Polygon | Combinable
)
# __get__ return type
_MULTILINESTRINGFIELDGT_co = TypeVar("_MULTILINESTRINGFIELDGT_co", covariant=True, default=Polygon)

class MultiLineStringField(GeometryField[_MULTILINESTRINGFIELDST_contra, _MULTILINESTRINGFIELDGT_co]):
    _pyi_private_set_type: MultiLineString | Combinable
    _pyi_private_get_type: MultiLineString
    _pyi_lookup_exact_type: MultiLineString

    geom_class: type[MultiLineString]
    form_class: type[forms.MultiLineStringField]

# __set__ value type
_MULTIPOLYGONFIELDST_contra = TypeVar("_MULTIPOLYGONFIELDST_contra", contravariant=True, default=Polygon | Combinable)
# __get__ return type
_MULTIPOLYGONFIELDGT_co = TypeVar("_MULTIPOLYGONFIELDGT_co", covariant=True, default=Polygon)

class MultiPolygonField(GeometryField[_MULTIPOLYGONFIELDST_contra, _MULTIPOLYGONFIELDGT_co]):
    _pyi_private_set_type: MultiPolygon | Combinable
    _pyi_private_get_type: MultiPolygon
    _pyi_lookup_exact_type: MultiPolygon

    geom_class: type[MultiPolygon]
    form_class: type[forms.MultiPolygonField]

# __set__ value type
_GEOMETRYCOLLECTIONFIELDST_contra = TypeVar(
    "_GEOMETRYCOLLECTIONFIELDST_contra", contravariant=True, default=Polygon | Combinable
)
# __get__ return type
_GEOMETRYCOLLECTIONFIELDGT_co = TypeVar("_GEOMETRYCOLLECTIONFIELDGT_co", covariant=True, default=Polygon)

class GeometryCollectionField(GeometryField[_GEOMETRYCOLLECTIONFIELDST_contra, _GEOMETRYCOLLECTIONFIELDGT_co]):
    _pyi_private_set_type: GeometryCollection | Combinable
    _pyi_private_get_type: GeometryCollection
    _pyi_lookup_exact_type: GeometryCollection

    geom_class: type[GeometryCollection]
    form_class: type[forms.GeometryCollectionField]

class ExtentField(Field):
    def get_internal_type(self) -> Any: ...
    def select_format(self, compiler: Any, sql: Any, params: Any) -> Any: ...

class RasterField(BaseSpatialField):
    def db_type(self, connection: Any) -> Any: ...
    def from_db_value(self, value: Any, expression: Any, connection: Any) -> Any: ...
    def get_transform(self, name: Any) -> Any: ...
