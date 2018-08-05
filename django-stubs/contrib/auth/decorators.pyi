from typing import Any, Callable, List, Optional, Set, Union


def user_passes_test(
    test_func: Callable,
    login_url: Optional[str] = ...,
    redirect_field_name: str = ...,
) -> Callable: ...
def login_required(
    function: Optional[Callable] = ...,
    redirect_field_name: str = ...,
    login_url: Optional[str] = ...,
) -> Callable: ...
def permission_required(
    perm: Union[str, List[str], Set[str]],
    login_url: None = ...,
    raise_exception: bool = ...,
) -> Callable: ...