
# DigitalTwin

---------
## Calls

---------
### create
Create new digital twin.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'DigitalTwin', 'create', {}
)
```

---------
### set_source
Set data source account for difital twin.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `u32` | 
| topic | `H256` | 
| source | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'DigitalTwin', 'set_source', {
    'id': 'u32',
    'source': 'AccountId',
    'topic': 'scale_info::9',
}
)
```

---------
## Events

---------
### NewDigitalTwin
New digital twin was registered: [sender, id].
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `u32` | ```u32```

---------
### TopicChanged
Digital twin topic was changed: [sender, id, topic, source]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `u32` | ```u32```
| None | `H256` | ```scale_info::9```
| None | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### DigitalTwin
 Get internal structure of difital twin in format: topic hash -&gt; source account.

#### Python
```python
result = substrate.query(
    'DigitalTwin', 'DigitalTwin', ['u32']
)
```

#### Return value
```python
'scale_info::356'
```
---------
### Owner
 Get owner of digital twin with given id.

#### Python
```python
result = substrate.query(
    'DigitalTwin', 'Owner', ['u32']
)
```

#### Return value
```python
'AccountId'
```
---------
### Total
 Total count of registered digital twins.

#### Python
```python
result = substrate.query(
    'DigitalTwin', 'Total', []
)
```

#### Return value
```python
'u32'
```
---------