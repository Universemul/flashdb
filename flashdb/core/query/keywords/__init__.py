from flashdb.core.query.keywords.aggregateby_keyword import AggregateByKeyword
from flashdb.core.query.keywords.limit_keyword import LimitKeyword
from flashdb.core.query.keywords.select import SelectKeyword
from flashdb.core.query.keywords.sort_keyword import SortKeyword
from flashdb.core.query.keywords.index_keyword import IndexKeyword

SELECT = "select"
INDEX = "index"
WHERE = "where"
AGGREGATE_BY = "aggregate_by"
SORT = "sort"
LIMIT = "limit"
UPDATE = "update"
CREATE = "create"
DELETE = "delete"

KEYWORDS = {
    SELECT: SelectKeyword,
    INDEX: IndexKeyword,
    WHERE: object,
    AGGREGATE_BY: AggregateByKeyword,
    SORT: SortKeyword,
    LIMIT: LimitKeyword,
    UPDATE: object,
    CREATE: object,
    DELETE: object
}
