from flashdb.core.query.functions.base import Function


class Avg(Function):
    name = "avg"


class Count(Function):
    name = "count"


class Max(Function):
    name = "max"


class Min(Function):
    name = "min"


class Sum(Function):
    name = "sum"
