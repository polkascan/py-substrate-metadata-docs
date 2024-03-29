
# DmpQueue

---------
## Events

---------
### CleanedSome
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| keys_removed | `u32` | ```u32```

---------
### Completed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| error | `bool` | ```bool```

---------
### CompletedExport
#### Attributes
No attributes

---------
### CompletedOverweightExport
#### Attributes
No attributes

---------
### ExportFailed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| page | `PageCounter` | ```u32```

---------
### ExportOverweightFailed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `OverweightIndex` | ```u64```

---------
### Exported
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| page | `PageCounter` | ```u32```

---------
### ExportedOverweight
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `OverweightIndex` | ```u64```

---------
### StartedCleanup
#### Attributes
No attributes

---------
### StartedExport
#### Attributes
No attributes

---------
### StartedOverweightExport
#### Attributes
No attributes

---------
## Storage functions

---------
### MigrationStatus

#### Python
```python
result = substrate.query(
    'DmpQueue', 'MigrationStatus', []
)
```

#### Return value
```python
{
    'Completed': None,
    'CompletedExport': None,
    'CompletedOverweightExport': None,
    'NotStarted': None,
    'StartedCleanup': {'cursor': (None, 'Bytes')},
    'StartedExport': {'next_begin_used': 'u32'},
    'StartedOverweightExport': {'next_overweight_index': 'u64'},
}
```
---------