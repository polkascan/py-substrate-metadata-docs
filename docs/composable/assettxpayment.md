
# AssetTxPayment

---------
## Calls

---------
### set_payment_asset
Sets or resets payment asset.

If `asset_id` is `None`, then native asset is used.
Else new asset is configured and ED is on hold.
#### Attributes
| Name | Type |
| -------- | -------- | 
| payer | `T::AccountId` | 
| asset_id | `Option<ChargeAssetIdOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'AssetTxPayment', 'set_payment_asset', {'asset_id': (None, 'u128'), 'payer': 'AccountId'}
)
```

---------
## Storage functions

---------
### PaymentAssets
 Stores default payment asset of user with ED locked.

#### Python
```python
result = substrate.query(
    'AssetTxPayment', 'PaymentAssets', ['AccountId']
)
```

#### Return value
```python
('u128', 'u128')
```
---------
## Constants

---------
### UseUserConfiguration
 where to allow configuring default asset per user
#### Value
```python
True
```
#### Python
```python
constant = substrate.get_constant('AssetTxPayment', 'UseUserConfiguration')
```
---------