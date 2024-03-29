
# ProjectToken

---------
## Calls

---------
### burn
Burn tokens from specified account

Preconditions:
- `amount` is &gt; 0
- origin signer is a controller account of `member_id` member
- token by `token_id` exists
- an account exists for `token_id` x `member_id`
- account&\#x27;s tokens amount is &gt;= `amount`
- token supply can be modified (there is no active revenue split)

Postconditions:
- starting with `unprocessed` beeing equal to `amount`, account&\#x27;s vesting schedules
  are iterated over and:
  - updated with `burned_amount += uprocessed` if vesting schedule&\#x27;s unvested amount is
    greater than `uprocessed`
  - removed otherwise
  (after each iteration `unprocessed` is reduced by the amount of unvested tokens
  burned during that iteration)
- if the account has any `split_staking_status`, the `split_staking_status.amount`
  is reduced by `min(amount, split_staking_status.amount)`
- `account.amount` is reduced by `amount`
- token supply is reduced by `amount`

&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
  - `O(1)` - doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| token_id | `T::TokenId` | 
| member_id | `T::MemberId` | 
| amount | `TokenBalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'ProjectToken', 'burn', {
    'amount': 'u128',
    'member_id': 'u64',
    'token_id': 'u64',
}
)
```

---------
### buy_on_amm
Mint desired `token_id` amount into user account via JOY exchnage
Preconditions
- origin, member_id pair must be a valid authentication pair
- token_id must exist
- user usable JOY balance must be enough for buying (+ existential deposit)
- slippage tolerance constraints respected if provided
- token total supply and amount value must be s.t. `eval` function doesn&\#x27;t overflow

Postconditions
- `amount` CRT minted into account (which is created if necessary with existential deposit transferred to it)
- respective JOY amount transferred from user balance to amm treasury account
- event deposited
#### Attributes
| Name | Type |
| -------- | -------- | 
| token_id | `T::TokenId` | 
| member_id | `T::MemberId` | 
| amount | `<T as Config>::Balance` | 
| slippage_tolerance | `Option<(Permill, JoyBalanceOf<T>)>` | 

#### Python
```python
call = substrate.compose_call(
    'ProjectToken', 'buy_on_amm', {
    'amount': 'u128',
    'member_id': 'u64',
    'slippage_tolerance': (
        None,
        ('u32', 'u128'),
    ),
    'token_id': 'u64',
}
)
```

---------
### dust_account
Allow any user to remove an account

Preconditions:
- token by `token_id` must exist
- an account must exist for `token_id` x `member_id`
- if Permissioned token: `origin` signer must be `member_id` member&\#x27;s
  controller account
- `token_id` x `member_id` account must be an empty account
  (`account_data.amount` == 0)
Postconditions:
- Account information for `token_id` x `member_id` removed from storage
- bloat bond refunded to `member_id` controller account
  (or `bloat_bond.repayment_restricted_to` account)

&lt;weight&gt;

`O (1)`
- DB:
  - `O(1)` - doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| token_id | `T::TokenId` | 
| member_id | `T::MemberId` | 

#### Python
```python
call = substrate.compose_call(
    'ProjectToken', 'dust_account', {
    'member_id': 'u64',
    'token_id': 'u64',
}
)
```

---------
### exit_revenue_split
Split-participating user leaves revenue split
Preconditions
- `token` must exist for `token_id`
- `origin` signer must be `member_id` member controller account
- `account` must exist for `(token_id, member_id)`
- `account.staking status.is_some()&\#x27;
- if `(account.staking_status.split_id == token.next_revenue_split_id - 1`
   AND `token.revenue_split` is active) THEN split staking period  must be ended

Postconditions
- `account.staking_status` set to None

&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
  - `O(1)` - doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| token_id | `T::TokenId` | 
| member_id | `T::MemberId` | 

#### Python
```python
call = substrate.compose_call(
    'ProjectToken', 'exit_revenue_split', {
    'member_id': 'u64',
    'token_id': 'u64',
}
)
```

---------
### join_whitelist
Join whitelist for permissioned case: used to add accounts for token
Preconditions:
- &\#x27;token_id&\#x27; must be valid
- `origin` signer must be a controller account of `member_id`
- account for `member_id` must not already exist
- transfer policy is `Permissioned` and merkle proof must be valid

Postconditions:
- account for `member_id` created and added to pallet storage
- `bloat_bond` transferred from sender to treasury account

&lt;weight&gt;

\#\# Weight
`O (H)` where:
- `H` is the length of `proof.0`
- DB:
  - `O(1)` - doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| member_id | `T::MemberId` | 
| token_id | `T::TokenId` | 
| proof | `MerkleProofOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'ProjectToken', 'join_whitelist', {
    'member_id': 'u64',
    'proof': [
        (
            'scale_info::11',
            ('Right', 'Left'),
        ),
    ],
    'token_id': 'u64',
}
)
```

---------
### participate_in_split
Participate in the *latest* token revenue split (if ongoing)
Preconditions:
- `token` must exist for `token_id`
- `origin` signer must be `member_id` member controller account
- `amount` must be &gt; 0
- `account` must exist  for `(token_id, member_id)`
- `token.split_status` must be active AND THEN current_block in
   [split.start, split.start + split_duration)
- `account.staking_status.is_none()` OR `account.staking_status.split_id` refers to a past split
- `account.amount` &gt;= `amount`
- let `dividend = split_allocation * account.staked_amount / token.supply``
   then `treasury` must be able to transfer `dividend` amount of JOY.
   (This condition technically, should always be satisfied)

Postconditions
- `dividend` amount of JOYs transferred from `treasury_account` to `sender`
- `token` revenue split dividends payed tracking variable increased by `dividend`
- `account.staking_status` set to Some(..) with `amount` and `token.latest_split`

&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
  - `O(1)` - doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| token_id | `T::TokenId` | 
| member_id | `T::MemberId` | 
| amount | `TokenBalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'ProjectToken', 'participate_in_split', {
    'amount': 'u128',
    'member_id': 'u64',
    'token_id': 'u64',
}
)
```

---------
### purchase_tokens_on_sale
Purchase tokens on active token sale.

Preconditions:
- token by `token_id` must exist
- token by `token_id` must be in OfferingState::Sale
- `amount` cannot exceed number of tokens remaining on sale
- `origin` signer must be controller account of `member_id` member
- sender&\#x27;s available JOY balance must be:
  - &gt;= `joy_existential_deposit + amount * sale.unit_price`
    if AccountData already exist
  - &gt;= `joy_existential_deposit + amount * sale.unit_price + bloat_bond`
    if AccountData does not exist
- let `fee_amount` be `sale_platform_fee.mul_floor(amount * sale.unit_price)`
- if `sale.earnings_destination.is_some()` and `sale.earnings_destination` account has
  zero balance:
  - the amount to be transferred from `sender` to `sale.earnings_destination`,
    which is equal to `amount * sale.unit_price - fee_amount`, must be greater than
    `joy_existential_deposit`
- total number of tokens already purchased by the member on the current sale
  PLUS `amount` must not exceed sale&\#x27;s purchase cap per member
- if Permissioned token:
  - AccountInfoByTokenAndMember(token_id, &amp;member_id) must exist
- if `sale.vesting_schedule.is_some()`:
  - number of sender account&\#x27;s ongoing vesting schedules
    must be &lt; MaxVestingSchedulesPerAccountPerToken

Postconditions:
- if `sale.earnings_destination.is_some()`:
  - `amount * sale.unit_price - fee_amount` JOY tokens are transfered from `sender`
    to `sale.earnings_destination`
  - `fee_amount` JOY is slashed from `sender` balance
- if `sale.earnings_destination.is_none()`:
  - `amount * sale.unit_price` JOY is slashed from `sender` balance
- if new token account created: `bloat_bond` transferred from `sender` to treasury
- if `sale.vesting_schedule.is_some()`:
  - if buyer has no `vesting_schedule` related to the current sale:
    - a new vesting schedule (`sale.get_vesting_schedule(purchase_amount)`) is added to
      buyer&\#x27;s `vesing_schedules`
    - some finished vesting schedule is removed from buyer&\#x27;s account_data in case the
      number of buyer&\#x27;s vesting_schedules was == MaxVestingSchedulesPerAccountPerToken
  - if buyer already has a `vesting_schedule` related to the current sale:
    - current vesting schedule&\#x27;s `cliff_amount` is increased by
      `sale.get_vesting_schedule(purchase_amount).cliff_amount`
    - current vesting schedule&\#x27;s `post_cliff_total_amount` is increased by
      `sale.get_vesting_schedule(purchase_amount).post_cliff_total_amount`
- if `sale.vesting_schedule.is_none()`:
  - buyer&\#x27;s account token amount increased by `amount`
- if `token_data.sale.quantity_left - amount == 0` and `sale.auto_finalize` is `true`
  `token_data.sale` is set to None, otherwise `token_data.sale.quantity_left` is
  decreased by `amount` and `token_data.sale.funds_collected` in increased by
  `amount * sale.unit_price`

&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
  - `O(1)` - doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| token_id | `T::TokenId` | 
| member_id | `T::MemberId` | 
| amount | `TokenBalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'ProjectToken', 'purchase_tokens_on_sale', {
    'amount': 'u128',
    'member_id': 'u64',
    'token_id': 'u64',
}
)
```

---------
### sell_on_amm
Burn desired `token_id` amount from user account and get JOY from treasury account
Preconditions
- origin, member_id pair must be a valid authentication pair
- token_id must exist
- token_id, member_id must be valid account coordinates
- user usable CRT balance must be at least `amount`
- slippage tolerance constraints respected if provided
- token total supply and amount value must be s.t. `eval` function doesn&\#x27;t overflow
- amm treasury account must have sufficient JOYs for the operation

Postconditions
- `amount` burned from user account
- total supply decreased by amount
- respective JOY amount transferred from amm treasury account to user account
- event deposited
#### Attributes
| Name | Type |
| -------- | -------- | 
| token_id | `T::TokenId` | 
| member_id | `T::MemberId` | 
| amount | `<T as Config>::Balance` | 
| slippage_tolerance | `Option<(Permill, JoyBalanceOf<T>)>` | 

#### Python
```python
call = substrate.compose_call(
    'ProjectToken', 'sell_on_amm', {
    'amount': 'u128',
    'member_id': 'u64',
    'slippage_tolerance': (
        None,
        ('u32', 'u128'),
    ),
    'token_id': 'u64',
}
)
```

---------
### set_frozen_status
Allows to freeze or unfreeze this pallet. Requires root origin.

&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| freeze | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'ProjectToken', 'set_frozen_status', {'freeze': 'bool'}
)
```

---------
### transfer
Allow to transfer from `src_member_id` account to the various `outputs` beneficiaries
in the specified amounts.

Preconditions:
- origin signer must be `src_member_id` controller account
- token by `token_id` must exists
- account of `src_member_id` must exist for `token_id`
- sender must have enough JOYs to cover the total bloat bond required in case of
  destination(s) not existing.
- source account must have enough token funds to cover all the transfer(s)
- `outputs` must designate existing destination(s) for &quot;Permissioned&quot; transfers.
Postconditions:
- source account&\#x27;s tokens amount is decreased by `amount`.
- total bloat bond transferred from sender&\#x27;s JOY balance into the treasury account
  in case destination(s) have been added to storage
- `outputs.beneficiary` tokens amount increased by `amount`

&lt;weight&gt;

\#\# Weight
`O (T + M)` where:
- `T` is the length of `outputs`
- `M` is the size of `metadata` in kilobytes
- DB:
  - `O(T)` - from the the generated weights
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| src_member_id | `T::MemberId` | 
| token_id | `T::TokenId` | 
| outputs | `TransferOutputsOf<T>` | 
| metadata | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'ProjectToken', 'transfer', {
    'metadata': 'Bytes',
    'outputs': [('u64', 'u128')],
    'src_member_id': 'u64',
    'token_id': 'u64',
}
)
```

---------
## Events

---------
### AccountDustedBy
Account Dusted
Params:
- token identifier
- id of the dusted account owner member
- account that called the extrinsic
- ongoing policy
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `TokenId` | ```u64```
| None | `MemberId` | ```u64```
| None | `AccountId` | ```AccountId```
| None | `TransferPolicy` | ```{'Permissionless': None, 'Permissioned': 'scale_info::11'}```

---------
### AmmActivated
AMM activated
Params:
- token id
- member id
- params for the bonding curve
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `TokenId` | ```u64```
| None | `MemberId` | ```u64```
| None | `AmmCurve` | ```{'slope': 'u128', 'intercept': 'u128', 'provided_supply': 'u128'}```

---------
### AmmDeactivated
AMM deactivated
Params:
- token id
- member id
- amm treasury amount burned upon deactivation
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `TokenId` | ```u64```
| None | `MemberId` | ```u64```
| None | `JoyBalance` | ```u128```

---------
### FrozenStatusUpdated
Pallet Frozen status toggled
Params:
- new frozen status (true | false)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `bool` | ```bool```

---------
### MemberJoinedWhitelist
Member joined whitelist
Params:
- token identifier
- member id
- ongoing transfer policy
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `TokenId` | ```u64```
| None | `MemberId` | ```u64```
| None | `TransferPolicy` | ```{'Permissionless': None, 'Permissioned': 'scale_info::11'}```

---------
### PatronageCreditClaimed
Patronage credit claimed by creator
Params:
- token identifier
- credit amount
- member id
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `TokenId` | ```u64```
| None | `Balance` | ```u128```
| None | `MemberId` | ```u64```

---------
### PatronageRateDecreasedTo
Patronage rate decreased
Params:
- token identifier
- new patronage rate
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `TokenId` | ```u64```
| None | `YearlyRate` | ```u32```

---------
### RevenueSplitFinalized
Revenue Split finalized
Params:
- token identifier
- recovery account for the leftover funds
- leftover funds
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `TokenId` | ```u64```
| None | `AccountId` | ```AccountId```
| None | `JoyBalance` | ```u128```

---------
### RevenueSplitIssued
Revenue Split issued
Params:
- token identifier
- starting block for the split
- duration of the split
- JOY allocated for the split
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `TokenId` | ```u64```
| None | `BlockNumber` | ```u32```
| None | `BlockNumber` | ```u32```
| None | `JoyBalance` | ```u128```

---------
### RevenueSplitLeft
User left revenue split
Params:
- token identifier
- ex-participant&\#x27;s member id
- amount unstaked
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `TokenId` | ```u64```
| None | `MemberId` | ```u64```
| None | `Balance` | ```u128```

---------
### TokenAmountTransferred
Token amount is transferred from src to dst
Params:
- token identifier
- source member id
- map containing validated outputs (amount indexed by (member_id + account existance))
- transfer&\#x27;s metadata
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `TokenId` | ```u64```
| None | `MemberId` | ```u64```
| None | `ValidatedTransfers` | ```scale_info::197```
| None | `Vec<u8>` | ```Bytes```

---------
### TokenAmountTransferredByIssuer
Token amount transferred by issuer
Params:
- token identifier
- source (issuer) member id
- map containing validated outputs
  (amount, opt. vesting schedule, opt. vesting cleanup key) data indexed by
  (account_id + account existance)
- transfer&\#x27;s metadata
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `TokenId` | ```u64```
| None | `MemberId` | ```u64```
| None | `ValidatedTransfers` | ```scale_info::197```
| None | `Vec<u8>` | ```Bytes```

---------
### TokenDeissued
Token Deissued
Params:
- token id
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `TokenId` | ```u64```

---------
### TokenIssued
Token Issued
Params:
- token id
- token issuance parameters
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `TokenId` | ```u64```
| None | `TokenIssuanceParameters` | ```{'initial_allocation': 'scale_info::187', 'transfer_policy': {'Permissionless': None, 'Permissioned': {'commitment': 'scale_info::11', 'payload': (None, {'object_creation_params': 'scale_info::136', 'expected_data_size_fee': 'u128', 'expected_data_object_state_bloat_bond': 'u128'})}}, 'patronage_rate': 'u32', 'revenue_split_rate': 'u32', 'metadata': 'Bytes'}```

---------
### TokenSaleFinalized
Token Sale Finalized
Params:
- token id
- token sale id
- amount of unsold tokens recovered
- amount of JOY collected
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `TokenId` | ```u64```
| None | `TokenSaleId` | ```u32```
| None | `Balance` | ```u128```
| None | `JoyBalance` | ```u128```

---------
### TokenSaleInitialized
Toke Sale was Initialized
Params:
- token id
- token sale id
- token sale data
- token sale metadata
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `TokenId` | ```u64```
| None | `TokenSaleId` | ```u32```
| None | `TokenSale` | ```{'unit_price': 'u128', 'quantity_left': 'u128', 'funds_collected': 'u128', 'tokens_source': 'u64', 'earnings_destination': (None, 'AccountId'), 'start_block': 'u32', 'duration': 'u32', 'vesting_schedule_params': (None, {'linear_vesting_duration': 'u32', 'blocks_before_cliff': 'u32', 'cliff_amount_percentage': 'u32'}), 'cap_per_member': (None, 'u128'), 'auto_finalize': 'bool'}```
| None | `Option<Vec<u8>>` | ```(None, 'Bytes')```

---------
### TokensBoughtOnAmm
Tokens Bought on AMM
Params:
- token id
- member id
- amount of CRT minted
- amount of JOY deposited into curve treasury
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `TokenId` | ```u64```
| None | `MemberId` | ```u64```
| None | `Balance` | ```u128```
| None | `JoyBalance` | ```u128```

---------
### TokensBurned
Tokens Burned
Params:
- token id
- member id
- number of tokens burned
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `TokenId` | ```u64```
| None | `MemberId` | ```u64```
| None | `Balance` | ```u128```

---------
### TokensPurchasedOnSale
Tokens Purchased On Sale
Params:
- token id
- token sale id
- amount of tokens purchased
- buyer&\#x27;s member id
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `TokenId` | ```u64```
| None | `TokenSaleId` | ```u32```
| None | `Balance` | ```u128```
| None | `MemberId` | ```u64```

---------
### TokensSoldOnAmm
Tokens Sold on AMM
Params:
- token id
- member id
- amount of CRT burned
- amount of JOY withdrawn from curve treasury
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `TokenId` | ```u64```
| None | `MemberId` | ```u64```
| None | `Balance` | ```u128```
| None | `JoyBalance` | ```u128```

---------
### TransferPolicyChangedToPermissionless
Transfer Policy Changed To Permissionless
Params:
- token id
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `TokenId` | ```u64```

---------
### UpcomingTokenSaleUpdated
Upcoming Token Sale was Updated
Params:
- token id
- token sale id
- new sale start block
- new sale duration
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `TokenId` | ```u64```
| None | `TokenSaleId` | ```u32```
| None | `Option<BlockNumber>` | ```(None, 'u32')```
| None | `Option<BlockNumber>` | ```(None, 'u32')```

---------
### UserParticipatedInSplit
User partipated in a revenue split
Params:
- token identifier
- participant&\#x27;s member id
- user allocated staked balance
- dividend amount (JOY) granted
- revenue split identifier
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `TokenId` | ```u64```
| None | `MemberId` | ```u64```
| None | `Balance` | ```u128```
| None | `JoyBalance` | ```u128```
| None | `RevenueSplitId` | ```u32```

---------
## Storage functions

---------
### AccountInfoByTokenAndMember
 Double map TokenId x MemberId =&gt; AccountData for managing account data

#### Python
```python
result = substrate.query(
    'ProjectToken', 'AccountInfoByTokenAndMember', ['u64', 'u64']
)
```

#### Return value
```python
{
    'amount': 'u128',
    'bloat_bond': {
        'amount': 'u128',
        'repayment_restricted_to': (None, 'AccountId'),
    },
    'last_sale_total_purchased_amount': (None, ('u32', 'u128')),
    'next_vesting_transfer_id': 'u64',
    'split_staking_status': (None, {'amount': 'u128', 'split_id': 'u32'}),
    'vesting_schedules': 'scale_info::589',
}
```
---------
### AmmBuyTxFees
 AMM buy transaction fee percentage

#### Python
```python
result = substrate.query(
    'ProjectToken', 'AmmBuyTxFees', []
)
```

#### Return value
```python
'u32'
```
---------
### AmmDeactivationThreshold
 Percentage threshold for deactivating the amm functionality

#### Python
```python
result = substrate.query(
    'ProjectToken', 'AmmDeactivationThreshold', []
)
```

#### Return value
```python
'u32'
```
---------
### AmmSellTxFees
 AMM sell transaction fee percentage

#### Python
```python
result = substrate.query(
    'ProjectToken', 'AmmSellTxFees', []
)
```

#### Return value
```python
'u32'
```
---------
### BloatBond
 Bloat Bond value used during account creation

#### Python
```python
result = substrate.query(
    'ProjectToken', 'BloatBond', []
)
```

#### Return value
```python
'u128'
```
---------
### MaxYearlyPatronageRate
 Max patronage rate allowed

#### Python
```python
result = substrate.query(
    'ProjectToken', 'MaxYearlyPatronageRate', []
)
```

#### Return value
```python
'u32'
```
---------
### MinAmmSlopeParameter
 Minimum slope parameters allowed for AMM curve

#### Python
```python
result = substrate.query(
    'ProjectToken', 'MinAmmSlopeParameter', []
)
```

#### Return value
```python
'u128'
```
---------
### MinRevenueSplitDuration
 Minimum revenue split duration constraint

#### Python
```python
result = substrate.query(
    'ProjectToken', 'MinRevenueSplitDuration', []
)
```

#### Return value
```python
'u32'
```
---------
### MinRevenueSplitTimeToStart
 Minimum revenue split time to start constraint

#### Python
```python
result = substrate.query(
    'ProjectToken', 'MinRevenueSplitTimeToStart', []
)
```

#### Return value
```python
'u32'
```
---------
### MinSaleDuration
 Minimum duration of a token sale

#### Python
```python
result = substrate.query(
    'ProjectToken', 'MinSaleDuration', []
)
```

#### Return value
```python
'u32'
```
---------
### NextTokenId
 Token Id nonce

#### Python
```python
result = substrate.query(
    'ProjectToken', 'NextTokenId', []
)
```

#### Return value
```python
'u64'
```
---------
### PalletFrozen
 Current frozen state.

#### Python
```python
result = substrate.query(
    'ProjectToken', 'PalletFrozen', []
)
```

#### Return value
```python
'bool'
```
---------
### SalePlatformFee
 Platform fee (percentage) charged on top of each sale purchase (in JOY) and burned

#### Python
```python
result = substrate.query(
    'ProjectToken', 'SalePlatformFee', []
)
```

#### Return value
```python
'u32'
```
---------
### TokenInfoById
 map TokenId =&gt; TokenData to retrieve token information

#### Python
```python
result = substrate.query(
    'ProjectToken', 'TokenInfoById', ['u64']
)
```

#### Return value
```python
{
    'accounts_number': 'u64',
    'amm_curve': (
        None,
        {'intercept': 'u128', 'provided_supply': 'u128', 'slope': 'u128'},
    ),
    'next_revenue_split_id': 'u32',
    'next_sale_id': 'u32',
    'patronage_info': {
        'last_unclaimed_patronage_tally_block': 'u32',
        'rate': 'u32',
        'unclaimed_patronage_tally_amount': 'u128',
    },
    'revenue_split': {
        'Active': {
            'allocation': 'u128',
            'dividends_claimed': 'u128',
            'timeline': {'duration': 'u32', 'start': 'u32'},
        },
        'Inactive': None,
    },
    'revenue_split_rate': 'u32',
    'sale': (
        None,
        {
            'auto_finalize': 'bool',
            'cap_per_member': (None, 'u128'),
            'duration': 'u32',
            'earnings_destination': (None, 'AccountId'),
            'funds_collected': 'u128',
            'quantity_left': 'u128',
            'start_block': 'u32',
            'tokens_source': 'u64',
            'unit_price': 'u128',
            'vesting_schedule_params': (
                None,
                {
                    'blocks_before_cliff': 'u32',
                    'cliff_amount_percentage': 'u32',
                    'linear_vesting_duration': 'u32',
                },
            ),
        },
    ),
    'tokens_issued': 'u128',
    'total_supply': 'u128',
    'transfer_policy': {
        'Permissioned': 'scale_info::11',
        'Permissionless': None,
    },
}
```
---------
## Errors

---------
### AccountAlreadyExists
Account Already exists

---------
### AccountInformationDoesNotExist
Requested account data does not exist

---------
### ArithmeticError
Unexpected arithmetic error (overflow / underflow)

---------
### AttemptToRemoveNonEmptyAccount
Attempt to remove an account with some outstanding tokens

---------
### AttemptToRemoveNonOwnedAccountUnderPermissionedMode
Attempt to remove non owned account under permissioned mode

---------
### BurnAmountGreaterThanAccountTokensAmount
Amount of tokens to burn exceeds total amount of tokens owned by the account

---------
### BurnAmountIsZero
Provided amount to burn is == 0

---------
### CannotDeissueTokenWithOutstandingAccounts
Cannot Deissue Token with outstanding accounts

---------
### CannotInitSaleIfAmmIsActive
No Sale if Amm is active

---------
### CannotIssueSplitWithZeroAllocationAmount
Attempt to issue in a split with zero allocation amount

---------
### CannotJoinWhitelistInPermissionlessMode
Cannot join whitelist in permissionless mode

---------
### CannotModifySupplyWhenRevenueSplitsAreActive
Attempt to modify supply when revenue split is active

---------
### CannotParticipateInSplitWithZeroAmount
Attempt to participate in a split with zero token to stake

---------
### CurveSlopeParametersTooLow
Curve slope parameters below minimum allowed

---------
### DeadlineExpired
Deadline constraint not satisfied

---------
### InitialAllocationToNonExistingMember
At least one of the members provided as part of InitialAllocation does not exist

---------
### InsufficientBalanceForSplitParticipation
User does not posses enough balance to participate in the revenue split

---------
### InsufficientBalanceForTokenPurchase
Account&\#x27;s JOY balance is insufficient to make the token purchase

---------
### InsufficientJoyBalance
Insufficient JOY Balance to cover the transaction costs

---------
### InsufficientTokenBalance
Creator token balance is insufficient

---------
### InsufficientTransferrableBalance
Account&\#x27;s transferrable balance is insufficient to perform the transfer or initialize token sale

---------
### InvalidCurveParameters
Invalid bonding curve construction parameters

---------
### JoyTransferSubjectToDusting
The amount of JOY to be transferred is not enough to keep the destination account alive

---------
### MaxVestingSchedulesPerAccountPerTokenReached
Cannot add another vesting schedule to an account.
Maximum number of vesting schedules for this account-token pair was reached.

---------
### MerkleProofVerificationFailure
Merkle proof verification failed

---------
### NoActiveSale
The token has no active sale at the moment

---------
### NoTokensToRecover
There are no remaining tokes to recover from the previous token sale.

---------
### NoUpcomingSale
The token has no upcoming sale

---------
### NotEnoughTokenMintedByAmmForThisSale
Attempting to sell more than amm provided supply

---------
### NotEnoughTokensOnSale
Amount of tokens to purchase on sale exceeds the quantity of tokens still available on the sale

---------
### NotInAmmState
------ AMM ---------------------------------------------------------
not in AMM state

---------
### OutstandingAmmProvidedSupplyTooLarge
Oustanding AMM-provided supply constitutes too large percentage of the token&\#x27;s total supply

---------
### PalletFrozen
Attempt to perform an action when pallet is frozen

---------
### PreviousSaleNotFinalized
Previous sale was still not finalized, finalize it first.

---------
### RevenueSplitAlreadyActiveForToken
Attempt to activate split with one ongoing

---------
### RevenueSplitDidNotEnd
Revenue Split has not ended yet

---------
### RevenueSplitDurationTooShort
Revenue Split duration is too short

---------
### RevenueSplitNotActiveForToken
Attempt to make revenue split operations with token not in active split state

---------
### RevenueSplitNotOngoing
Revenue Split for token active, but not ongoing

---------
### RevenueSplitRateIsZero
Revenue split rate cannot be 0

---------
### RevenueSplitTimeToStartTooShort
Specified revenue split starting block is in the past

---------
### SaleAccessProofParticipantIsNotSender
Participant in sale access proof provided during `purchase_tokens_on_sale`
does not match the sender account

---------
### SaleAccessProofRequired
Only whitelisted participants are allowed to access the sale, therefore access proof is required

---------
### SaleCapPerMemberIsZero
Purchase cap per member cannot be zero

---------
### SaleDurationIsZero
Sale duration cannot be zero

---------
### SaleDurationTooShort
Specified sale duration is shorter than MinSaleDuration

---------
### SalePurchaseAmountIsZero
Amount of tokens to purchase on sale cannot be zero

---------
### SalePurchaseCapExceeded
Sale participant&\#x27;s cap (either cap_per_member or whitelisted participant&\#x27;s specific cap)
was exceeded with the purchase

---------
### SaleStartingBlockInThePast
Specified sale starting block is in the past

---------
### SaleUnitPriceIsZero
Token&\#x27;s unit price cannot be zero

---------
### SaleUpperBoundQuantityIsZero
Upper bound quantity cannot be zero

---------
### SlippageToleranceExceeded
Slippage tolerance constraint tolerance not satisfied

---------
### TargetPatronageRateIsHigherThanCurrentRate
-------- Patronage --------------------------------------------------
Target Rate is higher than current patronage rate

---------
### TokenDoesNotExist
Requested token does not exist

---------
### TokenIssuanceNotInIdleState
Token&\#x27;s current offering state is not Idle

---------
### TokenSymbolAlreadyInUse
Symbol already in use

---------
### TooManyTransferOutputs
Transfer destination member id invalid

---------
### TransferDestinationMemberDoesNotExist
At least one of the transfer destinations is not an existing member id

---------
### UserAlreadyParticipating
User already participating in the revenue split

---------
### UserNotParticipantingInAnySplit
User is not participating in any split

---------
### YearlyPatronageRateLimitExceeded
Provided value for patronage is too big (yearly format)

---------