VOWEL_COUNT_SCHEMA = {
    "type": "object",
    "properties": {"words": {"type": "array", "items": {"type": "string"}}},
    "required": ["words"],
}

SORT_SCHEMA = {
    "type": "object",
    "properties": {
        "words": {"type": "array", "items": {"type": "string"}},
        "order": {"type": "string", "enum": ["asc", "desc"], "default": "asc"},
    },
    "required": ["words"],
}
