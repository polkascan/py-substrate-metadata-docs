
# EVMAccounts

---------
## Calls

---------
### add_contract_deployer
See [`Pallet::add_contract_deployer`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| address | `EvmAddress` | 

#### Python
```python
call = substrate.compose_call(
    'EVMAccounts', 'add_contract_deployer', {'address': '[u8; 20]'}
)
```

---------
### bind_evm_address
See [`Pallet::bind_evm_address`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'EVMAccounts', 'bind_evm_address', {}
)
```

---------
### remove_contract_deployer
See [`Pallet::remove_contract_deployer`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| address | `EvmAddress` | 

#### Python
```python
call = substrate.compose_call(
    'EVMAccounts', 'remove_contract_deployer', {'address': '[u8; 20]'}
)
```

---------
### renounce_contract_deployer
See [`Pallet::renounce_contract_deployer`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'EVMAccounts', 'renounce_contract_deployer', {}
)
```

---------
## Events

---------
### Bound
Binding was created.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| address | `EvmAddress` | ```[u8; 20]```

---------
### DeployerAdded
Deployer was added.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `EvmAddress` | ```[u8; 20]```

---------
### DeployerRemoved
Deployer was removed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `EvmAddress` | ```[u8; 20]```

---------
## Storage functions

---------
### AccountExtension
 Maps an EVM address to the last 12 bytes of a substrate account.

#### Python
```python
result = substrate.query(
    'EVMAccounts', 'AccountExtension', ['[u8; 20]']
)
```

#### Return value
```python
'[u8; 12]'
```
---------
### ContractDeployer
 Whitelisted addresses that are allowed to deploy smart contracts.

#### Python
```python
result = substrate.query(
    'EVMAccounts', 'ContractDeployer', ['[u8; 20]']
)
```

#### Return value
```python
()
```
---------
## Constants

---------
### FeeMultiplier
 Fee multiplier for the binding of addresses.
#### Value
```python
50
```
#### Python
```python
constant = substrate.get_constant('EVMAccounts', 'FeeMultiplier')
```
---------
## Errors

---------
### AddressAlreadyBound
Address is already bound

---------
### AddressNotWhitelisted
Address not whitelisted

---------
### BoundAddressCannotBeUsed
Bound address cannot be used

---------
### TruncatedAccountAlreadyUsed
EVM Account&\#x27;s nonce is not zero

---------