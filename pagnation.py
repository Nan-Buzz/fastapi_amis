from __future__ import annotations

import math
from contextvars import ContextVar
from typing import Callable, Generic, Optional, Sequence, Type, TypeVar

from fastapi import Query
from fastapi_pagination.api import resolve_params
from fastapi_pagination.bases import BasePage, AbstractParams, RawParams, AbstractPage
from pydantic import BaseModel

T = TypeVar("T")

class Params(BaseModel, AbstractParams):
    page: int = Query(1, ge=1, description="Page number")
    perPage: int = Query(20, ge=1, le=100, description="Page size")

    def to_raw_params(self) -> RawParams:
        return RawParams(
            limit=self.perPage,
            offset=self.perPage * (self.page - 1),
        )

class Page(BasePage[T], Generic[T]):
    # page: int
    # size: int

    __params_type__ = Params  # Set params related to Page

    @classmethod
    def create(
        cls,
        items: Sequence[T],
        total: int,
        params: AbstractParams
    ) -> Page[T]:
        if not isinstance(params, Params):
            raise ValueError("Page should be used with Params")
        # total_pages = math.ceil(total / params.perPage)

        return cls(
            total=total,
            items=items,
            page=params.page,
            size=params.perPage
        )

page_type: ContextVar[Type[AbstractPage]] = ContextVar("page_type", default=Page)

def create_page(items: Sequence[T], total: int, params: AbstractParams) -> AbstractPage[T]:
    return page_type.get().create(items, total, params)

def paginate(
    sequence: Sequence[T],
    params: Optional[AbstractParams] = None,
    length_function: Callable[[Sequence[T]], int] = len,
) -> AbstractPage[T]:
    params = resolve_params(params)
    raw_params = params.to_raw_params()

    return create_page(
        items=sequence[raw_params.offset : raw_params.offset + raw_params.limit],
        total=length_function(sequence),
        params=params,
    )

