from flashdb.core.query.keywords.limit import Limit
from flashdb.core.query.keywords.select import SelectKeyword
from flashdb.core.query.keywords.sort import Sort

SELECT = "SELECT"
FROM = "FROM"
WHERE = "WHERE"
AGGREGATE_BY = "AGGREGATE_BY"
SORT = "SORT"
LIMIT = "LIMIT"
UPDATE = "UPDATE"
CREATE = "CREATE"
DELETE = "DELETE"

KEYWORDS = {
    SELECT: SelectKeyword,
    FROM: object,
    WHERE: object,
    AGGREGATE_BY: object,
    SORT: Sort,
    LIMIT: Limit,
    UPDATE: object,
    CREATE: object,
    DELETE: object
}
