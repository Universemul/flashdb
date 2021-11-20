from flashdb.core.query.functions.aggregate_functions import Avg, Count, Max, Min, Sum
from flashdb.core.query.functions.string_functions import Length, Lower, Trim, Upper
from flashdb.core.query.functions.time_functions import Now
from flashdb.core.query.functions.misc_functions import Distinct


VALID_FUNCTIONS = {
    "avg": Avg,
    "count": Count,
    "distinct": Distinct,
    "length": Length,
    "lower": Lower,
    "max": Max,
    "min": Min,
    "now": Now,
    "sum": Sum,
    "trim": Trim,
    "upper": Upper
}
