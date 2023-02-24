
# ExtrinsicFilter

---------
## Calls

---------
### block_extrinsics
block the given extrinsics
(pallet_name_bytes, function_name_bytes) can uniquely identify an extrinsic
if function_name_bytes is None, all extrinsics in `pallet_name_bytes` will be blocked
#### Attributes
| Name | Type |
| -------- | -------- | 
| pallet_name_bytes | `Vec<u8>` | 
| function_name_bytes | `Option<Vec<u8>>` | 

#### Python
```python
call = substrate.compose_call(
    'ExtrinsicFilter', 'block_extrinsics', {
    'function_name_bytes': (
        None,
        'Bytes',
    ),
    'pallet_name_bytes': 'Bytes',
}
)
```

---------
### set_mode
Set the mode

The storage of `BlockedExtrinsics` is unaffected.
The reason is we&\#x27;d rather have this pallet behave conservatively:
having extra blocked extrinsics is better than having unexpected whitelisted extrinsics.
See the test `set_mode_should_not_clear_blocked_extrinsics()`

Weights should be 2 DB writes: 1 for mode and 1 for event
#### Attributes
| Name | Type |
| -------- | -------- | 
| mode | `OperationalMode` | 

#### Python
```python
call = substrate.compose_call(
    'ExtrinsicFilter', 'set_mode', {'mode': ('Normal', 'Safe', 'Test')}
)
```

---------
### unblock_extrinsics
unblock the given extrinsics
(pallet_name_bytes, function_name_bytes) can uniquely identify an extrinsic
if function_name_bytes is None, all extrinsics in `pallet_name_bytes` will be unblocked
#### Attributes
| Name | Type |
| -------- | -------- | 
| pallet_name_bytes | `Vec<u8>` | 
| function_name_bytes | `Option<Vec<u8>>` | 

#### Python
```python
call = substrate.compose_call(
    'ExtrinsicFilter', 'unblock_extrinsics', {
    'function_name_bytes': (
        None,
        'Bytes',
    ),
    'pallet_name_bytes': 'Bytes',
}
)
```

---------
## Events

---------
### ExtrinsicsBlocked
some extrinsics are blocked
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pallet_name_bytes | `Vec<u8>` | ```Bytes```
| function_name_bytes | `Option<Vec<u8>>` | ```(None, 'Bytes')```

---------
### ExtrinsicsUnblocked
some extrinsics are unblocked
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pallet_name_bytes | `Vec<u8>` | ```Bytes```
| function_name_bytes | `Option<Vec<u8>>` | ```(None, 'Bytes')```

---------
### ModeSet
a new mode was just sent
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| new_mode | `OperationalMode` | ```('Normal', 'Safe', 'Test')```

---------
## Storage functions

---------
### BlockedExtrinsics
 a tuple (pallet_name_bytes, Option&lt;function_name_bytes&gt;) to represent blocked extrinsics
 if `Option&lt;function_name_bytes&gt;` is None, then all extrinsics in `pallet_name_bytes` are
 blocked

#### Python
```python
result = substrate.query(
    'ExtrinsicFilter', 'BlockedExtrinsics', [('Bytes', 'Bytes')]
)
```

#### Return value
```python
()
```
---------
### Mode
 current mode, ValueQuery as it can&#x27;t be None

#### Python
```python
result = substrate.query(
    'ExtrinsicFilter', 'Mode', []
)
```

#### Return value
```python
('Normal', 'Safe', 'Test')
```
---------
## Errors

---------
### CannotBlock
Error when a given extrinsic cannot be blocked (e.g. this pallet)

---------
### CannotConvertToString
Error during conversion bytes to utf8 string

---------
### ExtrinsicAlreadyBlocked
Error when trying to block extrinsic more than once

---------
### ExtrinsicNotBlocked
Error when trying to unblock a non-existent extrinsic

---------