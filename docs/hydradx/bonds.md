
# Bonds

---------
## Calls

---------
### issue
See [`Pallet::issue`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `AssetId` | 
| amount | `T::Balance` | 
| maturity | `Moment` | 

#### Python
```python
call = substrate.compose_call(
    'Bonds', 'issue', {
    'amount': 'u128',
    'asset_id': 'u32',
    'maturity': 'u64',
}
)
```

---------
### redeem
See [`Pallet::redeem`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| bond_id | `AssetId` | 
| amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Bonds', 'redeem', {'amount': 'u128', 'bond_id': 'u32'}
)
```

---------
## Events

---------
### Issued
New bond were issued
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| issuer | `T::AccountId` | ```AccountId```
| bond_id | `AssetId` | ```u32```
| amount | `T::Balance` | ```u128```
| fee | `T::Balance` | ```u128```

---------
### Redeemed
Bonds were redeemed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| bond_id | `AssetId` | ```u32```
| amount | `T::Balance` | ```u128```

---------
### TokenCreated
A bond asset was registered
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| issuer | `T::AccountId` | ```AccountId```
| asset_id | `AssetId` | ```u32```
| bond_id | `AssetId` | ```u32```
| maturity | `Moment` | ```u64```

---------
## Storage functions

---------
### BondIds
 Registered bond ids.
 Maps (underlying asset ID, maturity) -&gt; bond ID

#### Python
```python
result = substrate.query(
    'Bonds', 'BondIds', [('u32', 'u64')]
)
```

#### Return value
```python
'u32'
```
---------
### Bonds
 Registered bonds.
 Maps bond ID -&gt; (underlying asset ID, maturity)

#### Python
```python
result = substrate.query(
    'Bonds', 'Bonds', ['u32']
)
```

#### Return value
```python
('u32', 'u64')
```
---------
## Constants

---------
### FeeReceiver
 Protocol fee receiver.
#### Value
```python
'7L53bUTBopuwFt3mKUfmkzgGLayYa1Yvn1hAg9v5UMrQzTfh'
```
#### Python
```python
constant = substrate.get_constant('Bonds', 'FeeReceiver')
```
---------
### PalletId
 The pallet id, used for deriving its sovereign account ID.
#### Value
```python
'0x706c74626f6e6473'
```
#### Python
```python
constant = substrate.get_constant('Bonds', 'PalletId')
```
---------
### ProtocolFee
 Protocol fee.
#### Value
```python
20000
```
#### Python
```python
constant = substrate.get_constant('Bonds', 'ProtocolFee')
```
---------
## Errors

---------
### AssetNotFound
Asset is not registered in `AssetRegistry`

---------
### DisallowedAsset
Asset type not allowed for underlying asset

---------
### FailToParseName
Bond&\#x27;s name parsing was now successful

---------
### InvalidBondName
Generated name is not valid.

---------
### InvalidMaturity
Maturity not long enough

---------
### NotMature
Bond is not mature

---------
### NotRegistered
Bond not registered

---------