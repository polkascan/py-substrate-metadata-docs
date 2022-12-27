# PySubstrate Metadata docs

Documentation of Substrate metadata for well known runtimes and how to use it with [py-substrate-interface](https://github.com/polkascan/py-substrate-interface).

## How to read the type information

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
3. In case of (b) it is a `dict` (in RUST a `struct`) containing an `account` (`AccountID`), `fee` (128-bit int) and `fields` (64-bit int) 

Example of output of this storage function:

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
* `{'Id': '15wHrzgaZA1gt8GyAFqWLG8Pt5RJBm5sYEGmppKDafqiaDUD'}`
* `{'Address20': '0x0CAC409596b076487517263441282DBa6B7dc137'}`
* `{'Index': 54}` 

## Library resources 

* [Installation and usage of py-substrate-interface](https://github.com/polkascan/py-substrate-interface#readme)
* [Function reference of py-substrate-interface](https://polkascan.github.io/py-substrate-interface/)
* [Information about SCALE-encoding](https://github.com/polkascan/py-scale-codec#examples-of-different-types)
* [Substrate Stackexchange](https://substrate.stackexchange.com/questions/tagged/python)

## Polkadot Ecosystem Runtimes

* [Polkadot](polkadot.md)
* [Statemint](statemint.md)
* [Collectives](collectives.md)
* [Moonbeam](moonbeam.md)
* [Acala](acala.md)
* [Ajuna Polkadot](ajuna.md)
* [Astar](astar.md)
* [Bifrost Polkadot](bifrost_polkadot.md)
* [Bitgreen](bitgreen-parachain.md)
* [Centrifuge](centrifuge.md)
* [Clover](clover-mainnet.md)
* [Composable Finance](composable.md)
* [KILT Spiritnet](kilt-spiritnet.md)
* [Darwinia Parachain](darwinia-parachain.md)
* [Efinity](efinity.md)
* [Equilibrium parachain](equilibrium-parachain.md)
* [Frequency](frequency.md)
* [Hashed Network](hashed.md)
* [HydraDX](hydradx.md)
* [Integritee Shell](integritee-parachain.md)
* [Interlay](interlay-parachain.md)
* [Kapex](totem-parachain.md)
* [Kylin Network](kylin.md)
* [Litentry](litentry-parachain.md)
* [OriginTrail Parachain](origintrail-parachain.md)
* [Parallel](parallel.md)
* [Phala](phala.md)
* [UNIQUE](unique.md)

## Kusama Ecosystem Runtimes

* [Kusama](kusama.md)
* [Statemine](statemine.md)
* [Altair](altair.md)
* [Amplitude](amplitude.md)
* [Bajun Kusama](bajun.md)
* [Basilisk](basilisk.md)
* [Bifrost](bifrost.md)
* [Dorafactory Network](dora-ksm-parachain.md)
* [Calamari Parachain](calamari.md)
* [Crab Parachain](crab-parachain.md)
* [Crust Shadow](crust-collator.md)
* [Ipci](ipci.md)
* [imbue kusama](imbue.md)
* [Integritee Network (Kusama)](integritee-parachain.md)
* [Kabocha](kabocha-parachain.md)
* [Karura](karura.md)
* [Khala](khala.md)
* [KICO](kico.md)
* [kintsugi](kintsugi-parachain.md)
* [Listen Network](listen-parachain.md)
* [Litmus](litmus-parachain.md)
* [Mangata Kusama Mainnet](mangata-parachain.md)
* [Moonriver](moonriver.md)
* [Parallel Heiko](heiko.md)
* [Picasso](picasso.md)
* [Pichiu Network](pichiu.md)
* [Pioneer Network](pioneer-runtime.md)
* [QUARTZ by UNIQUE](quartz.md)
* [Rio Kusama Mainnet](parachain-rio.md)
* [Robonomics](robonomics.md)
* [Snow Kusama](snow.md)
* [Shiden](shiden.md)
* [SORA Kusama](sora_ksm.md)
* [Turing Network](turing.md)
* [Zeitgeist](zeitgeist.md)


