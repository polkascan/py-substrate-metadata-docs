
# Offences

---------
## Events

---------
### Offence
There is an offence reported of the given `kind` happened at the `session_index` and
(kind-specific) time slot. This event is not deposited for duplicate slashes.
\[kind, timeslot\].
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| kind | `Kind` | ```[u8; 16]```
| timeslot | `OpaqueTimeSlot` | ```Bytes```

---------
## Storage functions

---------
### ConcurrentReportsIndex
 A vector of reports of the same kind that happened at the same time slot.

#### Python
```python
result = substrate.query(
    'Offences', 'ConcurrentReportsIndex', ['[u8; 16]', 'Bytes']
)
```

#### Return value
```python
['scale_info::12']
```
---------
### Reports
 The primary structure that holds all offence records keyed by report identifiers.

#### Python
```python
result = substrate.query(
    'Offences', 'Reports', ['scale_info::12']
)
```

#### Return value
```python
{
    'offender': (
        'AccountId',
        {'others': [{'value': 'u128', 'who': 'AccountId'}], 'own': 'u128', 'total': 'u128'},
    ),
    'reporters': ['AccountId'],
}
```
---------