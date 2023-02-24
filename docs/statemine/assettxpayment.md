
# AssetTxPayment

---------
## Events

---------
### AssetTxFeePaid
A transaction fee `actual_fee`, of which `tip` was added to the minimum inclusion fee,
has been paid by `who` in an asset `asset_id`.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| actual_fee | `BalanceOf<T>` | ```u128```
| tip | `BalanceOf<T>` | ```u128```
| asset_id | `Option<ChargeAssetIdOf<T>>` | ```(None, 'u32')```

---------