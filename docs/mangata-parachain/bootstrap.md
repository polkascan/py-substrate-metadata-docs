
# Bootstrap

---------
## Calls

---------
### cancel_bootstrap
Used to cancel active bootstrap. Can only be called before bootstrap is actually started
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Bootstrap', 'cancel_bootstrap', {}
)
```

---------
### claim_and_activate_liquidity_tokens
When bootstrap is in [`BootstrapPhase::Finished`] state user can claim his part of liquidity tokens comparing to `claim_liquidity_tokens` when calling `claim_and_activate_liquidity_tokens` tokens will be automatically activated.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Bootstrap', 'claim_and_activate_liquidity_tokens', {}
)
```

---------
### claim_liquidity_tokens
When bootstrap is in [`BootstrapPhase::Finished`] state user can claim his part of liquidity tokens.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Bootstrap', 'claim_liquidity_tokens', {}
)
```

---------
### claim_liquidity_tokens_for_account
Allows claiming rewards for some account that haven&\#x27;t done that yet. The only difference between
calling [`Pallet::claim_liquidity_tokens_for_account`] by some other account and calling [`Pallet::claim_liquidity_tokens`] directly by that account is account that will be charged for transaction fee.
\# Args:
- `other` - account in behalf of which liquidity tokens should be claimed
#### Attributes
| Name | Type |
| -------- | -------- | 
| account | `T::AccountId` | 
| activate_rewards | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Bootstrap', 'claim_liquidity_tokens_for_account', {
    'account': 'AccountId',
    'activate_rewards': 'bool',
}
)
```

---------
### finalize
Used to reset Bootstrap state and prepare it for running another bootstrap.
It should be called multiple times until it produces [`Event::BootstrapFinalized`] event.

\# Args:
* `limit` - limit of storage entries to be removed in single call. Should be set to some
reasonable balue like `100`.

**!!! Cleaning up storage is complex operation and pruning all storage items related to particular
bootstrap might not fit in a single block. As a result tx can be rejected !!!**
#### Attributes
| Name | Type |
| -------- | -------- | 
| limit | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Bootstrap', 'finalize', {'limit': 'u32'}
)
```

---------
### provision
Allows for provisioning one of the tokens from currently bootstrapped pair. Can only be called during:
- [`BootstrapPhase::Whitelist`]
- [`BootstrapPhase::Public`]

phases.

\# Args:
 - `token_id` - id of the token to provision (should be one of the currently bootstraped pair([`ActivePair`]))
 - `amount` - amount of the token to provision
#### Attributes
| Name | Type |
| -------- | -------- | 
| token_id | `TokenId` | 
| amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Bootstrap', 'provision', {'amount': 'u128', 'token_id': 'u32'}
)
```

---------
### schedule_bootstrap
Used for starting/scheduling new bootstrap

\# Args:
- `first_token_id` - first token of the tokens pair
- `second_token_id`: second token of the tokens pair
- `ido_start` - number of block when bootstrap will be started (people will be allowed to participate)
- `whitelist_phase_length`: - length of whitelist phase
- `public_phase_lenght`- length of public phase
- `promote_bootstrap_pool`- whether liquidity pool created by bootstrap should be promoted
- `max_first_to_second_ratio` - represented as (numerator,denominator) - Ratio may be used to limit participations of second token id. Ratio between first and second token needs to be held during whole bootstrap. Whenever user tries to participate (using [`Pallet::provision`] extrinsic) the following conditions is check.
```ignore
all previous first participations + first token participations             ratio numerator
----------------------------------------------------------------------- &lt;= ------------------
all previous second token participations + second token participations     ratio denominator
```
and if it evaluates to `false` extrinsic will fail.

**Because of above equation only participations with first token of a bootstrap pair are limited!**

\# Examples
Consider:

- user willing to participate 1000 of first token, when:
	- ratio set during bootstrap schedule is is set to (1/2)
	- sum of first token participations - 10_000
	- sum of second token participations - 20_000

participation extrinsic will **fail** because ratio condition **is not met**
```ignore
10_000 + 10_000      1
--------------- &lt;=  ---
    20_000           2
```

- user willing to participate 1000 of first token, when:
	- ratio set during bootstrap schedule is is set to (1/2)
	- sum of first token participations - 10_000
	- sum of second token participations - 40_000

participation extrinsic will **succeed** because ratio condition **is met**
```ignore
10_000 + 10_000      1
--------------- &lt;=  ---
    40_000           2
```


**If one doesn&\#x27;t want to limit participations in any way, ratio should be set to (u128::MAX,0) - then ratio requirements are always met**

```ignore
all previous first participations + first token participations                u128::MAX
----------------------------------------------------------------------- &lt;= ------------------
all previous second token participations + second token participations            1
```
#### Attributes
| Name | Type |
| -------- | -------- | 
| first_token_id | `TokenId` | 
| second_token_id | `TokenId` | 
| ido_start | `T::BlockNumber` | 
| whitelist_phase_length | `Option<u32>` | 
| public_phase_lenght | `u32` | 
| max_first_to_second_ratio | `Option<(u128, u128)>` | 
| promote_bootstrap_pool | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Bootstrap', 'schedule_bootstrap', {
    'first_token_id': 'u32',
    'ido_start': 'u32',
    'max_first_to_second_ratio': (
        None,
        ('u128', 'u128'),
    ),
    'promote_bootstrap_pool': 'bool',
    'public_phase_lenght': 'u32',
    'second_token_id': 'u32',
    'whitelist_phase_length': (
        None,
        'u32',
    ),
}
)
```

---------
### update_promote_bootstrap_pool
#### Attributes
| Name | Type |
| -------- | -------- | 
| promote_bootstrap_pool | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Bootstrap', 'update_promote_bootstrap_pool', {'promote_bootstrap_pool': 'bool'}
)
```

---------
### whitelist_accounts
Allows for whitelisting accounts, so they can participate in during whitelist phase. The list of
account is extended with every subsequent call
#### Attributes
| Name | Type |
| -------- | -------- | 
| accounts | `Vec<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'Bootstrap', 'whitelist_accounts', {'accounts': ['AccountId']}
)
```

---------
## Events

---------
### AccountsWhitelisted
account whitelisted
#### Attributes
No attributes

---------
### BootstrapFinalized
finalization process finished
#### Attributes
No attributes

---------
### BootstrapParitallyFinalized
finalization process tarted
#### Attributes
No attributes

---------
### Provisioned
Funds provisioned
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `TokenId` | ```u32```
| None | `Balance` | ```u128```

---------
### RewardsClaimed
Rewards claimed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `TokenId` | ```u32```
| None | `Balance` | ```u128```

---------
### RewardsLiquidityAcitvationFailed
The activation of the rewards liquidity tokens failed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `TokenId` | ```u32```
| None | `Balance` | ```u128```

---------
### VestedProvisioned
Funds provisioned using vested tokens
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `TokenId` | ```u32```
| None | `Balance` | ```u128```

---------
## Storage functions

---------
### ActivePair
 Currently bootstraped pair of tokens representaed as [ `first_token_id`, `second_token_id`]

#### Python
```python
result = substrate.query(
    'Bootstrap', 'ActivePair', []
)
```

#### Return value
```python
('u32', 'u32')
```
---------
### ArchivedBootstrap

#### Python
```python
result = substrate.query(
    'Bootstrap', 'ArchivedBootstrap', []
)
```

#### Return value
```python
[('u32', 'u32', 'u32', ('u128', 'u128'))]
```
---------
### BootstrapSchedule
 Active bootstrap parameters

#### Python
```python
result = substrate.query(
    'Bootstrap', 'BootstrapSchedule', []
)
```

#### Return value
```python
('u32', 'u32', 'u32', ('u128', 'u128'))
```
---------
### ClaimedRewards
  Maps ([`frame_system::Config::AccountId`], [`TokenId`] ) -&gt; [`Balance`] - where [`TokeinId`] is id of the token that user participated with. This storage item is used to identify how much liquidity tokens has been claim by the user. If user participated with 2 tokens there are two entries associated with given account (`Address`, `first_token_id`) and (`Address`, `second_token_id`)

#### Python
```python
result = substrate.query(
    'Bootstrap', 'ClaimedRewards', ['AccountId', 'u32']
)
```

#### Return value
```python
'u128'
```
---------
### MintedLiquidity

#### Python
```python
result = substrate.query(
    'Bootstrap', 'MintedLiquidity', []
)
```

#### Return value
```python
('u32', 'u128')
```
---------
### Phase
 Current state of bootstrap as [`BootstrapPhase`]

#### Python
```python
result = substrate.query(
    'Bootstrap', 'Phase', []
)
```

#### Return value
```python
('BeforeStart', 'Whitelist', 'Public', 'Finished')
```
---------
### PromoteBootstrapPool
 Wheter to automatically promote the pool after [`BootstrapPhase::PublicPhase`] or not.

#### Python
```python
result = substrate.query(
    'Bootstrap', 'PromoteBootstrapPool', []
)
```

#### Return value
```python
'bool'
```
---------
### ProvisionAccounts
 List of accouts that provisioned funds to bootstrap and has not claimed liquidity tokens yet

#### Python
```python
result = substrate.query(
    'Bootstrap', 'ProvisionAccounts', ['AccountId']
)
```

#### Return value
```python
()
```
---------
### Provisions
 maps ([`frame_system::Config::AccountId`], [`TokenId`]) -&gt; [`Balance`] - identifies how much tokens did account provisioned in active bootstrap

#### Python
```python
result = substrate.query(
    'Bootstrap', 'Provisions', ['AccountId', 'u32']
)
```

#### Return value
```python
'u128'
```
---------
### Valuations
 Total sum of provisions of `first` and `second` token in active bootstrap

#### Python
```python
result = substrate.query(
    'Bootstrap', 'Valuations', []
)
```

#### Return value
```python
('u128', 'u128')
```
---------
### VestedProvisions
 maps ([`frame_system::Config::AccountId`], [`TokenId`]) -&gt; [`Balance`] - identifies how much vested tokens did account provisioned in active bootstrap

#### Python
```python
result = substrate.query(
    'Bootstrap', 'VestedProvisions', ['AccountId', 'u32']
)
```

#### Return value
```python
('u128', 'u128', 'u128')
```
---------
### WhitelistedAccount
 list ([`Vec&lt;AccountId&gt;`]) of whitelisted accounts allowed to participate in [`BootstrapPhase::Whitelist`] phase

#### Python
```python
result = substrate.query(
    'Bootstrap', 'WhitelistedAccount', ['AccountId']
)
```

#### Return value
```python
()
```
---------
## Constants

---------
### BootstrapUpdateBuffer
#### Value
```python
300
```
#### Python
```python
constant = substrate.get_constant('Bootstrap', 'BootstrapUpdateBuffer')
```
---------
### DefaultBootstrapPromotedPoolWeight
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('Bootstrap', 'DefaultBootstrapPromotedPoolWeight')
```
---------
### TreasuryPalletId
#### Value
```python
'0x70792f7472737279'
```
#### Python
```python
constant = substrate.get_constant('Bootstrap', 'TreasuryPalletId')
```
---------
## Errors

---------
### AlreadyStarted
Bootstrate event already started

---------
### BootstrapFinished
Bootstrap already Finished

---------
### BootstrapNotReadyToBeFinished
no rewards to claim

---------
### BootstrapNotSchduled
Bootstrap not scheduled

---------
### BootstrapStartInThePast
Bootstrap cant be scheduled in past

---------
### FirstProvisionInSecondTokenId
First provision must be in non restricted token

---------
### MathOverflow
Math problem

---------
### NotEnoughAssets
Not enough funds for provision

---------
### NotEnoughVestedAssets
Not enough funds for provision (vested)

---------
### NotFinishedYet
Cannot claim rewards before bootstrap finish

---------
### NothingToClaim
no rewards to claim

---------
### PhaseLengthCannotBeZero
Bootstarap phases cannot lasts 0 blocks

---------
### PoolAlreadyExists
Bootstraped pool already exists

---------
### SameToken
Tokens used in bootstrap cannot be the same

---------
### TokenIdDoesNotExists
Token does not exists

---------
### TokensActivationFailed
Token activations failed

---------
### TooLateToUpdateBootstrap
Bootstrap can only be updated or cancelled
BootstrapUpdateBuffer blocks or more before bootstrap start

---------
### Unauthorized
User cannot participate at this moment

---------
### UnsupportedTokenId
Only scheduled token pair can be used for provisions

---------
### ValuationRatio
Valuation ratio exceeded

---------
### WrongRatio
wrong ratio

---------