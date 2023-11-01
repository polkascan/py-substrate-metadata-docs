
# Bonds

---------
## Calls

---------
### issue
Issue new fungible bonds.
New asset id is registered and assigned to the bonds.
The number of bonds the issuer receives is 1:1 to the `amount` of the underlying asset
minus the protocol fee.
The bond asset is registered with the empty string for the asset name,
and with the same existential deposit as of the underlying asset.
Bonds can be redeemed for the underlying asset once mature.
Protocol fee is applied to the amount, and transferred to `T::FeeReceiver`.
When issuing new bonds with the underlying asset and maturity that matches existing bonds,
new amount of these existing bonds is issued, instead of registering new bonds.
It&\#x27;s possible to issue new bonds for bonds that are already mature.

Parameters:
- `origin`: issuer of new bonds, needs to be `T::IssueOrigin`
- `asset_id`: underlying asset id
- `amount`: the amount of the underlying asset
- `maturity`: Unix time in milliseconds, when the bonds will be mature.

Emits `BondTokenCreated` event when successful and new bonds were registered.
Emits `BondsIssued` event when successful.

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
Redeem bonds for the underlying asset.
The amount of the underlying asset the `origin` receives is 1:1 to the `amount` of the bonds.
Anyone who holds the bonds is able to redeem them.
Bonds can be both partially or fully redeemed.

Parameters:
- `origin`: account id
- `asset_id`: bond asset id
- `amount`: the amount of the bonds to redeem for the underlying asset

Emits `BondsRedeemed` event when successful.

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
### DisallowedAsset
Asset type not allowed for underlying asset

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