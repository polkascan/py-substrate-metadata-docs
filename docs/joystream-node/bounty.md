
# Bounty

---------
## Calls

---------
### announce_work_entry
Announce work entry for a successful bounty.
\# &lt;weight&gt;

\#\# weight
`O (W + M)` where:
- `W` is the work_description size in kilobytes.
- `M` is closed contract member list length.
- db:
   - `O(1)` doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| member_id | `MemberId<T>` | 
| bounty_id | `T::BountyId` | 
| staking_account_id | `T::AccountId` | 
| work_description | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Bounty', 'announce_work_entry', {
    'bounty_id': 'u64',
    'member_id': 'u64',
    'staking_account_id': 'AccountId',
    'work_description': 'Bytes',
}
)
```

---------
### contributor_remark
Bounty Contributor made a remark

\# &lt;weight&gt;

\#\# weight
`O (N)`
- `N` is msg size in kilobytes
- db:
   - `O(1)` doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| contributor | `BountyActor<MemberId<T>>` | 
| bounty_id | `T::BountyId` | 
| msg | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Bounty', 'contributor_remark', {
    'bounty_id': 'u64',
    'contributor': {
        'Council': None,
        'Member': 'u64',
    },
    'msg': 'Bytes',
}
)
```

---------
### create_bounty
Creates a bounty. Metadata stored in the transaction log but discarded after that.
&lt;weight&gt;

\#\# Weight
`O (W)` where:
- `W` is the _metadata size in kilobytes.
- `M` is closed contract member list length.
- DB:
   - O(M) (O(1) on open contract)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| params | `BountyCreationParameters<T>` | 
| metadata | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Bounty', 'create_bounty', {
    'metadata': 'Bytes',
    'params': {
        'cherry': 'u128',
        'contract_type': {
            'Closed': 'scale_info::84',
            'Open': None,
        },
        'creator': {
            'Council': None,
            'Member': 'u64',
        },
        'entrant_stake': 'u128',
        'funding_type': {
            'Limited': {
                'funding_period': 'u32',
                'target': 'u128',
            },
            'Perpetual': {
                'target': 'u128',
            },
        },
        'oracle': {
            'Council': None,
            'Member': 'u64',
        },
        'oracle_reward': 'u128',
    },
}
)
```

---------
### creator_remark
Bounty Oracle made a remark

\# &lt;weight&gt;

\#\# weight
`O (N)`
- `N` is msg size in kilobytes
- db:
   - `O(1)` doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| creator | `BountyActor<MemberId<T>>` | 
| bounty_id | `T::BountyId` | 
| msg | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Bounty', 'creator_remark', {
    'bounty_id': 'u64',
    'creator': {
        'Council': None,
        'Member': 'u64',
    },
    'msg': 'Bytes',
}
)
```

---------
### end_working_period
end bounty working period.
\# &lt;weight&gt;

\#\# weight
`O (1)`
- db:
   - `O(1)` doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| bounty_id | `T::BountyId` | 

#### Python
```python
call = substrate.compose_call(
    'Bounty', 'end_working_period', {'bounty_id': 'u64'}
)
```

---------
### entrant_remark
Bounty Entrant Worker made a remark

\# &lt;weight&gt;

\#\# weight
`O (N)`
- `N` is msg size in kilobytes
- db:
   - `O(1)` doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| entrant_id | `MemberId<T>` | 
| bounty_id | `T::BountyId` | 
| entry_id | `T::EntryId` | 
| msg | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Bounty', 'entrant_remark', {
    'bounty_id': 'u64',
    'entrant_id': 'u64',
    'entry_id': 'u64',
    'msg': 'Bytes',
}
)
```

---------
### fund_bounty
Provides bounty funding.
\# &lt;weight&gt;

\#\# weight
`O (1)`
- db:
   - `O(1)` doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| funder | `BountyActor<MemberId<T>>` | 
| bounty_id | `T::BountyId` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Bounty', 'fund_bounty', {
    'amount': 'u128',
    'bounty_id': 'u64',
    'funder': {
        'Council': None,
        'Member': 'u64',
    },
}
)
```

---------
### oracle_remark
Bounty Oracle made a remark

\# &lt;weight&gt;

\#\# weight
`O (N)`
- `N` is msg size in kilobytes
- db:
   - `O(1)` doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| oracle | `BountyActor<MemberId<T>>` | 
| bounty_id | `T::BountyId` | 
| msg | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Bounty', 'oracle_remark', {
    'bounty_id': 'u64',
    'msg': 'Bytes',
    'oracle': {
        'Council': None,
        'Member': 'u64',
    },
}
)
```

---------
### submit_oracle_judgment
Submits an oracle judgment for a bounty, slashing the entries rejected
by an arbitrary percentage and rewarding the winners by an arbitrary amount
(not surpassing the total fund amount)
\# &lt;weight&gt;

\#\# weight
`O (J + K + W + R)`
- `J` is rationale size in kilobytes,
- `K` is the sum of all action_justification sizes (in kilobytes) inside OracleJudgment,
- `W` is number of winner judgment entries,
- `R` is number of rejected judgment entries,
- db:
   - `O(W + R)`
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| bounty_id | `T::BountyId` | 
| judgment | `OracleJudgment<T::EntryId, BalanceOf<T>>` | 
| rationale | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Bounty', 'submit_oracle_judgment', {
    'bounty_id': 'u64',
    'judgment': 'scale_info::91',
    'rationale': 'Bytes',
}
)
```

---------
### submit_work
Submit work for a bounty.
\# &lt;weight&gt;

\#\# weight
`O (N)`
- `N` is the work_data size in kilobytes,
- db:
   - `O(1)` doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| member_id | `MemberId<T>` | 
| bounty_id | `T::BountyId` | 
| entry_id | `T::EntryId` | 
| work_data | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Bounty', 'submit_work', {
    'bounty_id': 'u64',
    'entry_id': 'u64',
    'member_id': 'u64',
    'work_data': 'Bytes',
}
)
```

---------
### switch_oracle
Oracle switches himself to a new one
\# &lt;weight&gt;

\#\# weight
`O (1)`
- db:
   - `O(1)` doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;

#### Attributes
| Name | Type |
| -------- | -------- | 
| new_oracle | `BountyActor<MemberId<T>>` | 
| bounty_id | `T::BountyId` | 

#### Python
```python
call = substrate.compose_call(
    'Bounty', 'switch_oracle', {
    'bounty_id': 'u64',
    'new_oracle': {
        'Council': None,
        'Member': 'u64',
    },
}
)
```

---------
### terminate_bounty
Terminates a bounty in funding, funding expired,
worksubmission, judging period.
\# &lt;weight&gt;

\#\# weight
`O (1)`
- db:
   - `O(1)` doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| bounty_id | `T::BountyId` | 

#### Python
```python
call = substrate.compose_call(
    'Bounty', 'terminate_bounty', {'bounty_id': 'u64'}
)
```

---------
### withdraw_entrant_stake
Unlocks the stake related to a work entry
After the oracle makes the judgment or the council terminates the bounty by calling terminate_bounty(...),
each worker whose entry has not been judged, can unlock the totality of their stake.
\# &lt;weight&gt;

\#\# weight
`O (1)`
- db:
   - `O(1)` doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| member_id | `MemberId<T>` | 
| bounty_id | `T::BountyId` | 
| entry_id | `T::EntryId` | 

#### Python
```python
call = substrate.compose_call(
    'Bounty', 'withdraw_entrant_stake', {
    'bounty_id': 'u64',
    'entry_id': 'u64',
    'member_id': 'u64',
}
)
```

---------
### withdraw_funding
Withdraw bounty funding by a member or a council.
\# &lt;weight&gt;

\#\# weight
`O (1)`
- db:
   - `O(1)` doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| funder | `BountyActor<MemberId<T>>` | 
| bounty_id | `T::BountyId` | 

#### Python
```python
call = substrate.compose_call(
    'Bounty', 'withdraw_funding', {
    'bounty_id': 'u64',
    'funder': {
        'Council': None,
        'Member': 'u64',
    },
}
)
```

---------
### withdraw_oracle_reward
Withraws the oracle reward to oracle
If bounty is successfully, Failed or Cancelled oracle must call this
extrinsic to withdraw the oracle reward,
\# &lt;weight&gt;

\#\# weight
`O (1)`
- db:
   - `O(1)` doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| bounty_id | `T::BountyId` | 

#### Python
```python
call = substrate.compose_call(
    'Bounty', 'withdraw_oracle_reward', {'bounty_id': 'u64'}
)
```

---------
## Events

---------
### BountyContributorRemarked
Bounty contributor made a message remark
Params:
- contributor
- bounty id
- message
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BountyActor<MemberId>` | ```{'Council': None, 'Member': 'u64'}```
| None | `BountyId` | ```u64```
| None | `Vec<u8>` | ```Bytes```

---------
### BountyCreated
A bounty was created.
Params:
- bounty ID
- creation parameters
- bounty metadata
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BountyId` | ```u64```
| None | `BountyCreationParameters` | ```{'oracle': {'Council': None, 'Member': 'u64'}, 'contract_type': {'Open': None, 'Closed': 'scale_info::84'}, 'creator': {'Council': None, 'Member': 'u64'}, 'cherry': 'u128', 'oracle_reward': 'u128', 'entrant_stake': 'u128', 'funding_type': {'Perpetual': {'target': 'u128'}, 'Limited': {'target': 'u128', 'funding_period': 'u32'}}}```
| None | `Vec<u8>` | ```Bytes```

---------
### BountyCreatorCherryWithdrawal
A bounty creator has withdrawn the cherry (member or council).
Params:
- bounty ID
- bounty creator
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BountyId` | ```u64```
| None | `BountyActor<MemberId>` | ```{'Council': None, 'Member': 'u64'}```

---------
### BountyCreatorOracleRewardWithdrawal
A bounty creator has withdrawn the oracle reward (member or council).
Params:
- bounty ID
- bounty creator
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BountyId` | ```u64```
| None | `BountyActor<MemberId>` | ```{'Council': None, 'Member': 'u64'}```

---------
### BountyCreatorRemarked
Bounty creator made a message remark
Params:
- creator
- bounty id
- message
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BountyActor<MemberId>` | ```{'Council': None, 'Member': 'u64'}```
| None | `BountyId` | ```u64```
| None | `Vec<u8>` | ```Bytes```

---------
### BountyEntrantRemarked
Bounty entrant made a message remark
Params:
- entrant_id
- bounty id
- entry id
- message
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MemberId` | ```u64```
| None | `BountyId` | ```u64```
| None | `EntryId` | ```u64```
| None | `Vec<u8>` | ```Bytes```

---------
### BountyFunded
A bounty was funded by a member or a council.
Params:
- bounty ID
- bounty funder
- funding amount
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BountyId` | ```u64```
| None | `BountyActor<MemberId>` | ```{'Council': None, 'Member': 'u64'}```
| None | `Balance` | ```u128```

---------
### BountyFundingWithdrawal
A member or a council has withdrawn the funding.
Params:
- bounty ID
- bounty funder
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BountyId` | ```u64```
| None | `BountyActor<MemberId>` | ```{'Council': None, 'Member': 'u64'}```

---------
### BountyMaxFundingReached
A bounty has reached its target funding amount.
Params:
- bounty ID
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BountyId` | ```u64```

---------
### BountyOracleRemarked
Bounty oracle made a message remark
Params:
- oracle
- bounty id
- message
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BountyActor<MemberId>` | ```{'Council': None, 'Member': 'u64'}```
| None | `BountyId` | ```u64```
| None | `Vec<u8>` | ```Bytes```

---------
### BountyOracleRewardWithdrawal
A Oracle has withdrawn the oracle reward (member or council).
Params:
- bounty ID
- bounty creator
- Oracle Reward
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BountyId` | ```u64```
| None | `BountyActor<MemberId>` | ```{'Council': None, 'Member': 'u64'}```
| None | `Balance` | ```u128```

---------
### BountyOracleSwitched
Bounty Oracle Switched by current oracle or council.
Params:
- bounty ID
- switcher
- current_oracle,
- new oracle
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BountyId` | ```u64```
| None | `BountyActor<MemberId>` | ```{'Council': None, 'Member': 'u64'}```
| None | `BountyActor<MemberId>` | ```{'Council': None, 'Member': 'u64'}```
| None | `BountyActor<MemberId>` | ```{'Council': None, 'Member': 'u64'}```

---------
### BountyRemoved
A bounty was removed.
Params:
- bounty ID
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BountyId` | ```u64```

---------
### BountyTerminated
A bounty was terminated by council.
Params:
- bounty ID
- bounty terminator
- bounty creator
- bounty oracle
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BountyId` | ```u64```
| None | `BountyActor<MemberId>` | ```{'Council': None, 'Member': 'u64'}```
| None | `BountyActor<MemberId>` | ```{'Council': None, 'Member': 'u64'}```
| None | `BountyActor<MemberId>` | ```{'Council': None, 'Member': 'u64'}```

---------
### CreatorStateBloatBondWithdrawn
A member or a council creator has withdrawn the creator state bloat bond.
Params:
- bounty ID
- bounty creator
- Creator State bloat bond amount
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BountyId` | ```u64```
| None | `BountyActor<MemberId>` | ```{'Council': None, 'Member': 'u64'}```
| None | `Balance` | ```u128```

---------
### FunderStateBloatBondWithdrawn
A member or a council funder has withdrawn the funder state bloat bond.
Params:
- bounty ID
- bounty funder
- funder State bloat bond amount
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BountyId` | ```u64```
| None | `BountyActor<MemberId>` | ```{'Council': None, 'Member': 'u64'}```
| None | `Balance` | ```u128```

---------
### OracleJudgmentSubmitted
Submit oracle judgment.
Params:
- bounty ID
- oracle
- judgment data
- rationale
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BountyId` | ```u64```
| None | `BountyActor<MemberId>` | ```{'Council': None, 'Member': 'u64'}```
| None | `OracleJudgment` | ```scale_info::91```
| None | `Vec<u8>` | ```Bytes```

---------
### WorkEntrantFundsWithdrawn
Work entry was slashed.
Params:
- bounty ID
- entry ID
- entrant member ID
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BountyId` | ```u64```
| None | `EntryId` | ```u64```
| None | `MemberId` | ```u64```

---------
### WorkEntrantStakeSlashed
Work entry stake slashed.
Params:
- bounty ID
- entry ID
- stake account
- slashed amount
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BountyId` | ```u64```
| None | `EntryId` | ```u64```
| None | `AccountId` | ```AccountId```
| None | `Balance` | ```u128```

---------
### WorkEntrantStakeUnlocked
Work entry stake unlocked.
Params:
- bounty ID
- entry ID
- stake account
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BountyId` | ```u64```
| None | `EntryId` | ```u64```
| None | `AccountId` | ```AccountId```

---------
### WorkEntryAnnounced
Work entry was announced.
Params:
- bounty ID
- created entry ID
- entrant member ID
- staking account ID
- work description
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BountyId` | ```u64```
| None | `EntryId` | ```u64```
| None | `MemberId` | ```u64```
| None | `AccountId` | ```AccountId```
| None | `Vec<u8>` | ```Bytes```

---------
### WorkSubmissionPeriodEnded
Work entry was slashed.
Params:
- bounty ID
- oracle (caller)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BountyId` | ```u64```
| None | `BountyActor<MemberId>` | ```{'Council': None, 'Member': 'u64'}```

---------
### WorkSubmitted
Submit work.
Params:
- bounty ID
- created entry ID
- entrant member ID
- work data (description, URL, BLOB, etc.)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BountyId` | ```u64```
| None | `EntryId` | ```u64```
| None | `MemberId` | ```u64```
| None | `Vec<u8>` | ```Bytes```

---------
## Storage functions

---------
### Bounties
 Bounty storage.

#### Python
```python
result = substrate.query(
    'Bounty', 'Bounties', ['u64']
)
```

#### Return value
```python
{
    'active_work_entry_count': 'u32',
    'creation_params': {
        'cherry': 'u128',
        'contract_type': {'Closed': 'scale_info::84', 'Open': None},
        'creator': {'Council': None, 'Member': 'u64'},
        'entrant_stake': 'u128',
        'funding_type': {
            'Limited': {'funding_period': 'u32', 'target': 'u128'},
            'Perpetual': {'target': 'u128'},
        },
        'oracle': {'Council': None, 'Member': 'u64'},
        'oracle_reward': 'u128',
    },
    'has_unpaid_oracle_reward': 'bool',
    'milestone': {
        'BountyMaxFundingReached': None,
        'Created': {'created_at': 'u32', 'has_contributions': 'bool'},
        'JudgmentSubmitted': {'successful_bounty': 'bool'},
        'Terminated': None,
        'WorkSubmitted': None,
    },
    'total_funding': 'u128',
}
```
---------
### BountyContributions
 Double map for bounty funding. It stores a member or council funding for bounties.

#### Python
```python
result = substrate.query(
    'Bounty', 'BountyContributions', [
    'u64',
    {'Council': None, 'Member': 'u64'},
]
)
```

#### Return value
```python
{'amount': 'u128', 'funder_state_bloat_bond_amount': 'u128'}
```
---------
### BountyCount
 Count of all bounties that have been created.

#### Python
```python
result = substrate.query(
    'Bounty', 'BountyCount', []
)
```

#### Return value
```python
'u32'
```
---------
### Entries
 Work entry storage map.

#### Python
```python
result = substrate.query(
    'Bounty', 'Entries', ['u64', 'u64']
)
```

#### Return value
```python
{
    'member_id': 'u64',
    'staking_account_id': 'AccountId',
    'submitted_at': 'u32',
    'work_submitted': 'bool',
}
```
---------
### EntryCount
 Count of all work entries that have been created.

#### Python
```python
result = substrate.query(
    'Bounty', 'EntryCount', []
)
```

#### Return value
```python
'u32'
```
---------
## Constants

---------
### ClosedContractSizeLimit
 Exports const - max work entry number for a closed assurance type contract bounty.
#### Value
```python
50
```
#### Python
```python
constant = substrate.get_constant('Bounty', 'ClosedContractSizeLimit')
```
---------
### CreatorStateBloatBondAmount
 Exports const - creator state bloat bond amount for a bounty.
#### Value
```python
1826887182
```
#### Python
```python
constant = substrate.get_constant('Bounty', 'CreatorStateBloatBondAmount')
```
---------
### FunderStateBloatBondAmount
 Exports const - funder state bloat bond amount for a bounty.
#### Value
```python
1824556112
```
#### Python
```python
constant = substrate.get_constant('Bounty', 'FunderStateBloatBondAmount')
```
---------
### MinWorkEntrantStake
 Exports const - min work entrant stake for a bounty.
#### Value
```python
1842581141
```
#### Python
```python
constant = substrate.get_constant('Bounty', 'MinWorkEntrantStake')
```
---------
## Errors

---------
### ArithmeticError
Unexpected arithmetic error (overflow / underflow)

---------
### BountyDoesntExist
Bounty doesnt exist.

---------
### CannotSubmitWorkToClosedContractBounty
Incompatible assurance contract type for a member: cannot submit work to the &\#x27;closed
assurance&\#x27; bounty contract.

---------
### CherryLessThenMinimumAllowed
Cherry less than minimum allowed.

---------
### ClosedContractMemberListIsEmpty
Cannot create a &\#x27;closed assurance contract&\#x27; bounty with empty member list.

---------
### ClosedContractMemberListIsTooLarge
Cannot create a &\#x27;closed assurance contract&\#x27; bounty with member list larger
than allowed max work entry limit.

---------
### ClosedContractMemberNotFound
&\#x27;closed assurance contract&\#x27; bounty member list can only include existing members

---------
### ConflictingStakes
The conflicting stake discovered. Cannot stake.

---------
### EntrantStakeIsLessThanMininum
Cannot create a bounty with an entrant stake is less than required minimum.

---------
### FundingAmountCannotBeZero
Cannot create a bounty with zero funding amount parameter.

---------
### FundingPeriodCannotBeZero
Cannot create a bounty with zero funding period parameter.

---------
### InsufficientBalanceForBounty
Insufficient balance for a bounty cherry.

---------
### InsufficientBalanceForStake
There is not enough balance for a stake.

---------
### InvalidContributorActorSpecified
Bounty contributor not found

---------
### InvalidCreatorActorSpecified
Invalid Creator Actor for Bounty specified

---------
### InvalidEntrantWorkerSpecified
Member specified is not an entrant worker

---------
### InvalidOracleActorSpecified
Bounty oracle not found

---------
### InvalidOracleMemberId
Provided oracle member id does not belong to an existing member

---------
### InvalidStageUnexpectedCancelled
Unexpected bounty stage for an operation: Cancelled.

---------
### InvalidStageUnexpectedFailedBountyWithdrawal
Unexpected bounty stage for an operation: FailedBountyWithdrawal.

---------
### InvalidStageUnexpectedFunding
Unexpected bounty stage for an operation: Funding.

---------
### InvalidStageUnexpectedJudgment
Unexpected bounty stage for an operation: Judgment.

---------
### InvalidStageUnexpectedNoFundingContributed
Unexpected bounty stage for an operation: NoFundingContributed.

---------
### InvalidStageUnexpectedSuccessfulBountyWithdrawal
Unexpected bounty stage for an operation: SuccessfulBountyWithdrawal.

---------
### InvalidStageUnexpectedWorkSubmission
Unexpected bounty stage for an operation: WorkSubmission.

---------
### InvalidStakingAccountForMember
Staking account doesn&\#x27;t belong to a member.

---------
### MinFundingAmountCannotBeGreaterThanMaxAmount
Min funding amount cannot be greater than max amount.

---------
### NoBountyContributionFound
Cannot found bounty contribution.

---------
### OracleRewardAlreadyWithdrawn
Oracle have already been withdrawn

---------
### SwitchOracleOriginIsRoot
Origin is root, so switching oracle is not allowed in this extrinsic. (call switch_oracle_as_root)

---------
### TotalRewardShouldBeEqualToTotalFunding
The total reward for winners should be equal to total bounty funding.

---------
### WinnerShouldHasWorkSubmission
Invalid judgment - all winners should have work submissions.

---------
### WorkEntryDoesntBelongToWorker
Worker tried to access a work entry that doesn&\#x27;t belong to him

---------
### WorkEntryDoesntExist
Work entry doesnt exist.

---------
### ZeroWinnerReward
Cannot set zero reward for winners.

---------