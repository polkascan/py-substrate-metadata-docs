
# ExtrinsicPause

---------
## Calls

---------
### pause_extrinsic
Pause execution of extrinsic(s)

The values of pallet_name and extrinsic_name are extracted from the `call` parameter.
Ex : To pause the multi_tokens pallet, the `call` parameter should be of the type
`pallet_multi_tokens::Call` If `pause_only_extrinsic` is true, then only the extrinsic
is paused, else the entire pallet is paused.

\# Errors

- [`Error::CannotProcessInput`] if the pallet name or extrinsic name is faulty.
- [`Error::CannotPauseSelf`] if the pallet name is the same as the name of this pallet.
#### Attributes
| Name | Type |
| -------- | -------- | 
| call | `Box<<T as Config>::Call>` | 
| pause_only_extrinsic | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'ExtrinsicPause', 'pause_extrinsic', {
    'call': 'Call',
    'pause_only_extrinsic': 'bool',
}
)
```

---------
### resume_extrinsic
Resume execution of extrinsic(s)

The values of pallet_name and extrinsic_name are extracted from the `call` parameter.
Ex : To resume the multi_tokens pallet, the `call` parameter should be of the type
`pallet_multi_tokens::Call` If `pause_only_extrinsic` is true, then only the extrinsic
is resumed, else the entire pallet is resumed.

\# Errors

- [`Error::CannotProcessInput`] if the pallet name or extrinsic name is faulty.
#### Attributes
| Name | Type |
| -------- | -------- | 
| call | `Box<<T as Config>::Call>` | 
| resume_only_extrinsic | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'ExtrinsicPause', 'resume_extrinsic', {
    'call': 'Call',
    'resume_only_extrinsic': 'bool',
}
)
```

---------
## Events

---------
### ExtrinsicPaused
Extrinsic is paused.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pallet_name | `BoundedStringOf<T>` | ```Bytes```
| extrinsic_name | `BoundedStringOf<T>` | ```Bytes```

---------
### ExtrinsicResumed
Extrinsic is resumed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pallet_name | `BoundedStringOf<T>` | ```Bytes```
| extrinsic_name | `BoundedStringOf<T>` | ```Bytes```

---------
### PalletPaused
All pallet extrinsics are paused.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pallet_name | `BoundedStringOf<T>` | ```Bytes```

---------
### PalletResumed
All pallet extrinsics are resumed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pallet_name | `BoundedStringOf<T>` | ```Bytes```

---------
## Storage functions

---------
### PausedExtrinsics
 Paused extrinsics map

 The key is tuple with the name of the pallet and the extrinsic name and value is
 an Option&lt;()&gt; which is None if the extrinsic is not paused and Some(()) if it is.

#### Python
```python
result = substrate.query(
    'ExtrinsicPause', 'PausedExtrinsics', [
    {
        'extrinsic_name': (
            None,
            'Bytes',
        ),
        'pallet_name': 'Bytes',
    },
]
)
```

#### Return value
```python
()
```
---------
## Constants

---------
### MaxNameLength
 Max number of characters in pallet or extrinsic name.
#### Value
```python
64
```
#### Python
```python
constant = substrate.get_constant('ExtrinsicPause', 'MaxNameLength')
```
---------
## Errors

---------
### CannotPauseSelf
Cannot pause this pallet or it&\#x27;s extrinsic

---------
### CannotProcessInput
Cannot read the pallet or extrinsic name

---------