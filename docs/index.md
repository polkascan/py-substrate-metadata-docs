# PySubstrate Metadata docs

Documentation of Substrate metadata for well known runtimes and how to use it with [py-substrate-interface](https://github.com/polkascan/py-substrate-interface).

## Overview of available runtimes

* [Polkadot Ecosystem Runtimes](polkadot-runtimes.md)
* [Kusama Ecosystem Runtimes](kusama-runtimes.md)
* [Standalone Runtimes](standalone-runtimes.md)

## How to read the type information

### Core types

| Type                    | Description                                                                             | Type information example                                             |
|-------------------------|-----------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| `u8`, `u16`, `u32`, etc | Unsigned 8/16/32/etc bit integer                                                        | 1                                                                    |
| `bool`                  | Boolean                                                                                 | `True`                                                               |
| `[u8; 32]`              | Fixed sized array with in this case 32 `u8` elements. Can also be written as hex-string | `0xe1781813275653a970b4260298b3858b36d38e072256dad674f7c786a0cae236` |
| `Bytes`                 | Arbitrary length `str`. Internally same as a `Vec<u8>`                                  | `'test'`                                                             |
| `AccountId`             | SS58 encoded account                                                                    | `'5GrwvaEF5zXb26Fz9rcQpDWS57CtERHpNehXCPcNoHGKutQY'`                     |
| `Call`                  | Substrate `RuntimeCall` to place into an extrinsic or nest in another call              | Result of `substrate.compose_call()`                                 |
| Enum                    | Enumeration of possible variants, represented as a `dict` with CamelCase variants       | `{'Id': 'AccountId','Index': 'u32'}`                                 |
| Option                  | Special enumeration provided 'None' and 'Some' variants represented as a `tuple`        | `(None, 'u32')`                                                      |
| Struct                  | Data structure, represented as a `dict` with snake_case properties                      | `{'account': 'AccountId', 'fee': 'u128', 'fields': 'u64'}`           |
| Vec                     | Variable size array containing a certain type, for example a `u32`                      | `['u32']`                                                            |


### Example 1: Storage function parameters

```python
call = substrate.query(
    'RmrkCore', 'Properties', ['u32', (None, 'u32'), 'Bytes']
)
```
This should be interpreted as follows:

* The first parameter is of type `u32`, which is a 32-bit integer

* The second parameter is a tuple, which represents all possible variants of the `Enum` in RUST (more specific an `Option` in this case). Only one variant must be selected, so `(None, 'u32')` means _either_ `None` _or_ a `u32`

* The third parameter `Bytes` is an arbitrary `str`, `bytes` or hex-string

So an example would be:

```python
result = substrate.query(
    'RmrkCore', 'Properties', [10324, 31, '0x068500be5822de000000000000000000']
)
```

Or 

```python
result = substrate.query(
    'RmrkCore', 'Properties', [10324, None, '0x068500be5822de000000000000000000']
)
```

### Example 2: Storage function return value 

```python
call = substrate.query(
    'Identity', 'Registrars', []
)
```
The return function is defined as: 
```python
[(None, {'account': 'AccountId', 'fee': 'u128', 'fields': 'u64'})]
```

Which should be interpreted as:

1. The return value is a Python list containing elements of definition `(None, {'account': 'AccountId', 'fee': 'u128', 'fields': 'u64'})`
2. Each of these elements are in RUST of type `Enum` (like the example above an `Option`) and again only one value must be selected of `tuple` so _either_ (a) `None` _or_  (b) `{'account': 'AccountId', 'fee': 'u128', 'fields': 'u64'}`  
3. In case of (b) it is a `dict` (in RUST a `struct`) containing an "account" (type `AccountID`), "fee" (128-bit int) and "fields" (64-bit int) 

Example output of this storage function:

```python
[{'account': '15wHrzgaZA1gt8GyAFqWLG8Pt5RJBm5sYEGmppKDafqiaDUD', 'fee': 121321321, 'fields': 1231}, None, {'account': '1297caNVrdbg9tQew1kJSHJuMQr93Z4vcD1offK6AzgV4KSE', 'fee': 0, 'fields': 0}]
```

### Example 3: Call parameters

```python
call = substrate.compose_call(
    'Treasury', 'spend', {
        'amount': 'u128',
        'beneficiary': {
            'Address20': '[u8; 20]',
            'Address32': '[u8; 32]',
            'Id': 'AccountId',
            'Index': 'u32',
            'Raw': 'Bytes',
        },
})
```
This call requires two parameters, "amount" which is a 128-bit int and "beneficiary" which expects an `Enum`.

Like the `struct` data-type in Example 2 this is shown as a `dict` in Python, but the difference is that now all 
possible variants are shown, and only one of those variants must be provided. The difference between an `Enum` and a 
`Struct` `dict` is that `Enum` variants are in CamelCase, as 
`Struct` parameters are in snake_case.  

So examples of valid input for `beneficiary` are:
```python
{'Id': '15wHrzgaZA1gt8GyAFqWLG8Pt5RJBm5sYEGmppKDafqiaDUD'}

{'Address20': '0x0CAC409596b076487517263441282DBa6B7dc137'}

{'Index': 54}
``` 

## Library resources 

* [Getting started with py-substrate-interface](https://polkascan.github.io/py-substrate-interface/getting-started/installation/)
* [Function reference of py-substrate-interface](https://polkascan.github.io/py-substrate-interface/reference/base/)
* [Information about SCALE-encoding](https://polkascan.github.io/py-scale-codec/)
* [Substrate Stackexchange](https://substrate.stackexchange.com/questions/tagged/python)
