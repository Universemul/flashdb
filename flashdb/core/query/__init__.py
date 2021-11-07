'''
Example of json sending to the FlashDB API

{

    "where": {
        "operator": "and", # Available values: "and", "or". Default is "and"
        "filters": [
            {
                "name": "test",
                "condition": [condition]
                "nested_filter": { # Not required
                    "operator": "and", # Available values: "and", "or". Default is "and"
                    "filter": {
                        new nested filter. Same structure
                    }
                }
            },
            ...
        ]
    },
}
'''