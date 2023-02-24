
# MintWithFee

---------
## Calls

---------
### change_fee_percent
Change the value of the fee percentage in storage

`set_fee` will change the value of the fee percentage in storage,
affecting the next calls to `mint`

The dispatch origin for this call must be `Signed` by the root.
#### Attributes
| Name | Type |
| -------- | -------- | 
| percentage | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'MintWithFee', 'change_fee_percent', {'percentage': 'u128'}
)
```

---------
### mint
Mints the given amount of value on the target account,
and mint a percent of the amount on the fee account, if provided

`mint` will increase the total issuance, and increase the amounts of the targets
accounts.

The dispatch origin for this call must be `Signed` by the root.

\# &lt;weight&gt;

Related functions:
- `mint_to_account` can be one or two times, depending on if the fee account is provided
  or not.
#### Attributes
| Name | Type |
| -------- | -------- | 
| target_account | `T::AccountId` | 
| fee_target_account | `Option<T::AccountId>` | 
| amount | `BalanceOf<T>` | 
| metadata | `BoundedVec<u8, T::MaxMetadataSize>` | 

#### Python
```python
call = substrate.compose_call(
    'MintWithFee', 'mint', {
    'amount': 'u128',
    'fee_target_account': (
        None,
        'AccountId',
    ),
    'metadata': 'Bytes',
    'target_account': 'AccountId',
}
)
```

---------
## Events

---------
### FeeChanged
the percentage have been changed
[new_percentage]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BalanceOf<T>` | ```u128```

---------
### FeeMinted
the fees have been minted on the nsm account
[nsp_account, value, metadata]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```
| None | `BoundedVec<u8, T::MaxMetadataSize>` | ```Bytes```

---------
### ValueMinted
the value have been minted on the target accout
[target_account, value, metadata]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```
| None | `BoundedVec<u8, T::MaxMetadataSize>` | ```Bytes```

---------
## Storage functions

---------
### FeePercent
 Holds the percentage of the amount that will be minted on the fee account (if provided)

#### Python
```python
result = substrate.query(
    'MintWithFee', 'FeePercent', []
)
```

#### Return value
```python
'u128'
```
---------
## Errors

---------
### Overflow
Overflow

---------
### TooLongMetadata
Too long metadata

---------