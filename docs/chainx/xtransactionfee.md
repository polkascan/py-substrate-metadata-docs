
# XTransactionFee

---------
## Events

---------
### BTCFeePaid
Transaction BTC fee
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `u128` | ```u128```

---------
### FeePaid
Transaction fee was paid to the block author and its reward pot in 1:9.
[author, author_fee, reward_pot, reward_pot_fee]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------