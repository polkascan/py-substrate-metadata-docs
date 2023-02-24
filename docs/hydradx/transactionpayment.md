
# TransactionPayment

---------
## Events

---------
### TransactionFeePaid
A transaction fee `actual_fee`, of which `tip` was added to the minimum inclusion fee,
has been paid by `who`.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| actual_fee | `BalanceOf<T>` | ```u128```
| tip | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### NextFeeMultiplier

#### Python
```python
result = substrate.query(
    'TransactionPayment', 'NextFeeMultiplier', []
)
```

#### Return value
```python
'u128'
```
---------
### StorageVersion

#### Python
```python
result = substrate.query(
    'TransactionPayment', 'StorageVersion', []
)
```

#### Return value
```python
('V1Ancient', 'V2')
```
---------
## Constants

---------
### OperationalFeeMultiplier
 A fee mulitplier for `Operational` extrinsics to compute &quot;virtual tip&quot; to boost their
 `priority`

 This value is multipled by the `final_fee` to obtain a &quot;virtual tip&quot; that is later
 added to a tip component in regular `priority` calculations.
 It means that a `Normal` transaction can front-run a similarly-sized `Operational`
 extrinsic (with no tip), by including a tip value greater than the virtual tip.

 ```rust,ignore
 // For `Normal`
 let priority = priority_calc(tip);

 // For `Operational`
 let virtual_tip = (inclusion_fee + tip) * OperationalFeeMultiplier;
 let priority = priority_calc(tip + virtual_tip);
 ```

 Note that since we use `final_fee` the multiplier applies also to the regular `tip`
 sent with the transaction. So, not only does the transaction get a priority bump based
 on the `inclusion_fee`, but we also amplify the impact of tips applied to `Operational`
 transactions.
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('TransactionPayment', 'OperationalFeeMultiplier')
```
---------