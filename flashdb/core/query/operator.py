from flashdb.core.utils.enum import EnumOnSteroid


class Operator(EnumOnSteroid):
    AND = "and"
    OR = "or"


class Order(EnumOnSteroid):
    ASC = "asc"
    DESC = "desc"
