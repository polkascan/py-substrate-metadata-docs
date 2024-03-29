
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
['scale_info::11']
```
---------
### Reports
 The primary structure that holds all offence records keyed by report identifiers.

#### Python
```python
result = substrate.query(
    'Offences', 'Reports', ['scale_info::11']
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
### ReportsByKindIndex
 Enumerates all reports of a kind along with the time they happened.

 All reports are sorted by the time of offence.

 Note that the actual type of this mapping is `Vec&lt;u8&gt;`, this is because values of
 different types are not supported at the moment so we are doing the manual serialization.

#### Python
```python
result = substrate.query(
    'Offences', 'ReportsByKindIndex', ['[u8; 16]']
)
```

#### Return value
```python
'Bytes'
```
---------