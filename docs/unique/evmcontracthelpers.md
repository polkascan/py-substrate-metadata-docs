
# EvmContractHelpers

---------
## Calls

---------
### migrate_from_self_sponsoring
See [`Pallet::migrate_from_self_sponsoring`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| addresses | `Vec<H160>` | 

#### Python
```python
call = substrate.compose_call(
    'EvmContractHelpers', 'migrate_from_self_sponsoring', {'addresses': ['[u8; 20]']}
)
```

---------
## Events

---------
### ContractSponsorRemoved
Collection sponsor was removed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `H160` | ```[u8; 20]```

---------
### ContractSponsorSet
Contract sponsor was set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `H160` | ```[u8; 20]```
| None | `T::AccountId` | ```AccountId```

---------
### ContractSponsorshipConfirmed
New sponsor was confirm.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `H160` | ```[u8; 20]```
| None | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### Allowlist
 Storage for users that allowed for sponsorship.

 \#\#\# Usage
 Prefer to delete record from storage if user no more allowed for sponsorship.

 * **Key1** - contract address.
 * **Key2** - user that allowed for sponsorship.
 * **Value** - allowance for sponsorship.

#### Python
```python
result = substrate.query(
    'EvmContractHelpers', 'Allowlist', ['[u8; 20]', '[u8; 20]']
)
```

#### Return value
```python
'bool'
```
---------
### AllowlistEnabled
 Storege for contracts with [`Allowlisted`](SponsoringModeT::Allowlisted) sponsoring mode.

 \#\#\# Usage
 Prefer to delete collection from storage if mode chaged to non `Allowlisted`, than set **Value** to **false**.

 * **Key** - contract address.
 * **Value** - is contract in [`Allowlisted`](SponsoringModeT::Allowlisted) mode.

#### Python
```python
result = substrate.query(
    'EvmContractHelpers', 'AllowlistEnabled', ['[u8; 20]']
)
```

#### Return value
```python
'bool'
```
---------
### Owner
 Store owner for contract.

 * **Key** - contract address.
 * **Value** - owner for contract.

#### Python
```python
result = substrate.query(
    'EvmContractHelpers', 'Owner', ['[u8; 20]']
)
```

#### Return value
```python
'[u8; 20]'
```
---------
### SelfSponsoring
 Deprecated: this storage is deprecated

#### Python
```python
result = substrate.query(
    'EvmContractHelpers', 'SelfSponsoring', ['[u8; 20]']
)
```

#### Return value
```python
'bool'
```
---------
### SponsorBasket

#### Python
```python
result = substrate.query(
    'EvmContractHelpers', 'SponsorBasket', ['[u8; 20]', '[u8; 20]']
)
```

#### Return value
```python
'u32'
```
---------
### Sponsoring
 Store for contract sponsorship state.

 * **Key** - contract address.
 * **Value** - sponsorship state.

#### Python
```python
result = substrate.query(
    'EvmContractHelpers', 'Sponsoring', ['[u8; 20]']
)
```

#### Return value
```python
{
    'Confirmed': {'Ethereum': '[u8; 20]', 'Substrate': 'AccountId'},
    'Disabled': None,
    'Unconfirmed': {'Ethereum': '[u8; 20]', 'Substrate': 'AccountId'},
}
```
---------
### SponsoringFeeLimit
 Storage for last sponsored block.

 * **Key1** - contract address.
 * **Key2** - sponsored user address.
 * **Value** - last sponsored block number.

#### Python
```python
result = substrate.query(
    'EvmContractHelpers', 'SponsoringFeeLimit', ['[u8; 20]']
)
```

#### Return value
```python
'scale_info::649'
```
---------
### SponsoringMode
 Store for sponsoring mode.

 \#\#\# Usage
 Prefer to delete collection from storage if mode chaged to [`Disabled`](SponsoringModeT::Disabled).

 * **Key** - contract address.
 * **Value** - [`sponsoring mode`](SponsoringModeT).

#### Python
```python
result = substrate.query(
    'EvmContractHelpers', 'SponsoringMode', ['[u8; 20]']
)
```

#### Return value
```python
('Disabled', 'Allowlisted', 'Generous')
```
---------
### SponsoringRateLimit
 Storage for sponsoring rate limit in blocks.

 * **Key** - contract address.
 * **Value** - amount of sponsored blocks.

#### Python
```python
result = substrate.query(
    'EvmContractHelpers', 'SponsoringRateLimit', ['[u8; 20]']
)
```

#### Return value
```python
'u32'
```
---------
## Constants

---------
### ContractAddress
 Address, under which magic contract will be available
#### Value
```python
'0x842899ecf380553e8a4de75bf534cdf6fbf64049'
```
#### Python
```python
constant = substrate.get_constant('EvmContractHelpers', 'ContractAddress')
```
---------
## Errors

---------
### NoPendingSponsor
No pending sponsor for contract.

---------
### NoPermission
This method is only executable by contract owner

---------
### TooManyMethodsHaveSponsoredLimit
Number of methods that sponsored limit is defined for exceeds maximum.

---------