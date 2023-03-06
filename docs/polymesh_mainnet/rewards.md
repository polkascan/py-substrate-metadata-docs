
# Rewards

---------
## Calls

---------
### claim_itn_reward
Claim an ITN reward.

\#\# Arguments
* `itn_address` specifying the awarded address on ITN.
* `signature` authenticating the claim to the reward.
   The signature should contain `reward_address` followed by the suffix `&quot;claim_itn_reward&quot;`,
   and must have been signed by `itn_address`.

\# Errors
* `InsufficientBalance` - Itn rewards has insufficient funds to issue the reward.
* `InvalidSignature` - `signature` had an invalid signer or invalid message.
* `ItnRewardAlreadyClaimed` - Reward issued to the `itn_address` has already been claimed.
* `UnknownItnAddress` - `itn_address` is not in the rewards table and has no reward to be claimed.
#### Attributes
| Name | Type |
| -------- | -------- | 
| _reward_address | `T::AccountId` | 
| _itn_address | `T::AccountId` | 
| _signature | `T::OffChainSignature` | 

#### Python
```python
call = substrate.compose_call(
    'Rewards', 'claim_itn_reward', {
    '_itn_address': 'AccountId',
    '_reward_address': 'AccountId',
    '_signature': {
        'Ecdsa': '[u8; 65]',
        'Ed25519': '[u8; 64]',
        'Sr25519': '[u8; 64]',
    },
}
)
```

---------
### set_itn_reward_status
#### Attributes
| Name | Type |
| -------- | -------- | 
| _itn_address | `T::AccountId` | 
| _status | `ItnRewardStatus` | 

#### Python
```python
call = substrate.compose_call(
    'Rewards', 'set_itn_reward_status', {
    '_itn_address': 'AccountId',
    '_status': {
        'Claimed': None,
        'Unclaimed': 'u128',
    },
}
)
```

---------
## Events

---------
### ItnRewardClaimed
Itn reward was claimed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountId` | ```AccountId```
| None | `Balance` | ```u128```

---------
## Storage functions

---------
### ItnRewards
 Map of (Itn Address `AccountId`) -&gt; (Reward `ItnRewardStatus`).

#### Python
```python
result = substrate.query(
    'Rewards', 'ItnRewards', ['AccountId']
)
```

#### Return value
```python
{'Claimed': None, 'Unclaimed': 'u128'}
```
---------
## Errors

---------
### InvalidSignature
Provided signature was invalid.

---------
### ItnRewardAlreadyClaimed
Itn reward was already claimed.

---------
### UnableToCovertBalance
Balance can not be converted to a primitive.

---------
### UnknownItnAddress
Address was not found in the list of Itn addresses.

---------