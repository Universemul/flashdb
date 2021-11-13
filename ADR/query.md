# FlashDB query Syntax

FlashDb provides a query DSL based on `JSON` to define a query.  
There is some basic commands (like `SELECT`), functions (like `AVG`) and conditions (like `IS_NULL`)

## Commands

#### SELECT
  
In a query context, the `SELECT` answers the question "Which columns do I want?".  
The `SELECT` is an array and each item must have this format:
```json
{
    "name": "",
    "as": "",
    "apply_function": ""
}
```

The `name` is the name of the column. The wildcard is represented by `*` and allows you to retrive all columns.   
The `as` is just the new name for the column but only available when returning the data. ** not required **.    
The `apply_function` is a bit more complicated. If you want to chain functions, you must use the operator `>` but the functions
are applied from the left to the right. ** not required **

Examples:

Basic example:
```json
{
  "select": [
    {
      "name": "age",
      "as": "avg_age",
      "apply_function": "avg"
    }
  ]
}
```
If I want to select the average of the length of a column:

```json
{
  "select": [
    {
      "name": "myColumn",
      "apply_function": "AVG>LENGTH"
    }
  ]
}
```

If I want to select all columns:

```json
{
  "select": [
    {
      "name": "*"
    }
  ]
}
```

#### FROM

Define the name of the index you want to perform the query

```json
{
  "from": "myIndex"
}
```

#### WHERE

Allows you to filter the data. 

```json
{
  "where": {
    "operator": "AND",
    "filters": [
    ]
  }
}
```

The `operator` field allows you to modify how your `filters` are computed.  
By default, `Flashdb` do an `AND` operator.  
Available values: `AND` or `OR`.

The `filters` field is the definition of your filters. Each item of the array must have this format:

```json
{
  "operator": "AND",
  "conditions": [
    "myColumn < 3",
    "myColumn2 > 5"
  ]
}
```

This field is a bit more complicated because you can have multiple filters.  
The main thing to know about filtering is a group a filters have 1 and only 1 operator (`AND` or `OR`).  
The condition is a string defined by a column and a condition ([here](#conditions))

#### AGGREGATE_BY

Allows you to aggregate your data in buckets by a field.  
For now, you can only aggregate your data by one field.  
**Not required**.
```json
{
  "aggregate_by": "myColumn"
}
```

#### SORT

Allows you to sort the data. Only one sort is available for now.  
Default is `ASC`.  
**Not required**.  

```json
{
  "sort": {
    "name": "",
    "order": "asc"
  }
}
```

The `name` is the name of the column you want to sort.  
The `order` allows you to sort by `ASC` or `DESC`. Default is `ASC`.  

#### LIMIT

Allows you to limit the number of results sending from `Flashdb`.  
**Not required**.

```json
{
  "limit": 5
}
```

The value must be an Integer.  
Dy default, there is no limit.  

#### UPDATE

`TODO`

#### CREATE

`TODO`

#### DELETE

`TODO`

## Functions

### Aggregate functions

- AVG
- COUNT
- MAX
- MIN
- SUM

### String functions

- LENGTH
- LOWER
- TRIM
- UPPER

### Time and Date functions

- NOW

### Others

- DISTINCT

## <a id="conditions"></a> Conditions

### Basic operators

- "="
- "<="
- "<"
- ">="
- ">"
- "!=" 

### Complex operators

- IN [value1, value2, value3, ...]
- IS_NULL
- IS_EMPTY  
- NOT (condition)
- EXISTS
