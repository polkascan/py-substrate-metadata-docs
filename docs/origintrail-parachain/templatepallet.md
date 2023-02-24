
# TemplatePallet

---------
## Calls

---------
### cause_error
An example dispatchable that may throw a custom error.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'TemplatePallet', 'cause_error', {}
)
```

---------
### do_something
An example dispatchable that takes a singles value as a parameter, writes the value to
storage and emits an event. This function must be dispatched by a signed extrinsic.
#### Attributes
| Name | Type |
| -------- | -------- | 
| something | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'TemplatePallet', 'do_something', {'something': 'u32'}
)
```

---------
## Events

---------
### SomethingStored
Event documentation should end with an array that provides descriptive names for event
parameters. [something, who]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u32` | ```u32```
| None | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### Something

#### Python
```python
result = substrate.query(
    'TemplatePallet', 'Something', []
)
```

#### Return value
```python
'u32'
```
---------
## Errors

---------
### NoneValue
Error names should be descriptive.

---------
### StorageOverflow
Errors should have helpful documentation associated with them.

---------