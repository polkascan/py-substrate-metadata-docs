
# Bounties

---------
## Calls

---------
### accept_curator
Accept the curator role for a bounty.
A deposit will be reserved from curator and refund upon successful payout.

May only be called from the curator.

\# &lt;weight&gt;
- O(1).
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| bounty_id | `BountyIndex` | 

#### Python
```python
call = substrate.compose_call(
    'Bounties', 'accept_curator', {'bounty_id': 'u32'}
)
```

---------
### approve_bounty
Approve a bounty proposal. At a later time, the bounty will be funded and become active
and the original deposit will be returned.

May only be called from `T::ApproveOrigin`.

\# &lt;weight&gt;
- O(1).
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| bounty_id | `BountyIndex` | 

#### Python
```python
call = substrate.compose_call(
    'Bounties', 'approve_bounty', {'bounty_id': 'u32'}
)
```

---------
### award_bounty
Award bounty to a beneficiary account. The beneficiary will be able to claim the funds
after a delay.

The dispatch origin for this call must be the curator of this bounty.

- `bounty_id`: Bounty ID to award.
- `beneficiary`: The beneficiary account whom will receive the payout.

\# &lt;weight&gt;
- O(1).
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| bounty_id | `BountyIndex` | 
| beneficiary | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Bounties', 'award_bounty', {
    'beneficiary': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
    'bounty_id': 'u32',
}
)
```

---------
### claim_bounty
Claim the payout from an awarded bounty after payout delay.

The dispatch origin for this call must be the beneficiary of this bounty.

- `bounty_id`: Bounty ID to claim.

\# &lt;weight&gt;
- O(1).
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| bounty_id | `BountyIndex` | 

#### Python
```python
call = substrate.compose_call(
    'Bounties', 'claim_bounty', {'bounty_id': 'u32'}
)
```

---------
### close_bounty
Cancel a proposed or active bounty. All the funds will be sent to treasury and
the curator deposit will be unreserved if possible.

Only `T::RejectOrigin` is able to cancel a bounty.

- `bounty_id`: Bounty ID to cancel.

\# &lt;weight&gt;
- O(1).
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| bounty_id | `BountyIndex` | 

#### Python
```python
call = substrate.compose_call(
    'Bounties', 'close_bounty', {'bounty_id': 'u32'}
)
```

---------
### extend_bounty_expiry
Extend the expiry time of an active bounty.

The dispatch origin for this call must be the curator of this bounty.

- `bounty_id`: Bounty ID to extend.
- `remark`: additional information.

\# &lt;weight&gt;
- O(1).
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| bounty_id | `BountyIndex` | 
| remark | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Bounties', 'extend_bounty_expiry', {
    'bounty_id': 'u32',
    'remark': 'Bytes',
}
)
```

---------
### propose_bounty
Propose a new bounty.

The dispatch origin for this call must be _Signed_.

Payment: `TipReportDepositBase` will be reserved from the origin account, as well as
`DataDepositPerByte` for each byte in `reason`. It will be unreserved upon approval,
or slashed when rejected.

- `curator`: The curator account whom will manage this bounty.
- `fee`: The curator fee.
- `value`: The total payment amount of this bounty, curator fee included.
- `description`: The description of this bounty.
#### Attributes
| Name | Type |
| -------- | -------- | 
| value | `BalanceOf<T, I>` | 
| description | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Bounties', 'propose_bounty', {
    'description': 'Bytes',
    'value': 'u128',
}
)
```

---------
### propose_curator
Assign a curator to a funded bounty.

May only be called from `T::ApproveOrigin`.

\# &lt;weight&gt;
- O(1).
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| bounty_id | `BountyIndex` | 
| curator | `AccountIdLookupOf<T>` | 
| fee | `BalanceOf<T, I>` | 

#### Python
```python
call = substrate.compose_call(
    'Bounties', 'propose_curator', {
    'bounty_id': 'u32',
    'curator': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
    'fee': 'u128',
}
)
```

---------
### unassign_curator
Unassign curator from a bounty.

This function can only be called by the `RejectOrigin` a signed origin.

If this function is called by the `RejectOrigin`, we assume that the curator is
malicious or inactive. As a result, we will slash the curator when possible.

If the origin is the curator, we take this as a sign they are unable to do their job and
they willingly give up. We could slash them, but for now we allow them to recover their
deposit and exit without issue. (We may want to change this if it is abused.)

Finally, the origin can be anyone if and only if the curator is &quot;inactive&quot;. This allows
anyone in the community to call out that a curator is not doing their due diligence, and
we should pick a new curator. In this case the curator should also be slashed.

\# &lt;weight&gt;
- O(1).
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| bounty_id | `BountyIndex` | 

#### Python
```python
call = substrate.compose_call(
    'Bounties', 'unassign_curator', {'bounty_id': 'u32'}
)
```

---------
## Events

---------
### BountyAwarded
A bounty is awarded to a beneficiary.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `BountyIndex` | ```u32```
| beneficiary | `T::AccountId` | ```AccountId```

---------
### BountyBecameActive
A bounty proposal is funded and became active.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `BountyIndex` | ```u32```

---------
### BountyCanceled
A bounty is cancelled.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `BountyIndex` | ```u32```

---------
### BountyClaimed
A bounty is claimed by beneficiary.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `BountyIndex` | ```u32```
| payout | `BalanceOf<T, I>` | ```u128```
| beneficiary | `T::AccountId` | ```AccountId```

---------
### BountyExtended
A bounty expiry is extended.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `BountyIndex` | ```u32```

---------
### BountyProposed
New bounty proposal.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `BountyIndex` | ```u32```

---------
### BountyRejected
A bounty proposal was rejected; funds were slashed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `BountyIndex` | ```u32```
| bond | `BalanceOf<T, I>` | ```u128```

---------
## Storage functions

---------
### Bounties
 Bounties that have been made.

#### Python
```python
result = substrate.query(
    'Bounties', 'Bounties', ['u32']
)
```

#### Return value
```python
{
    'bond': 'u128',
    'curator_deposit': 'u128',
    'fee': 'u128',
    'proposer': 'AccountId',
    'status': {
        'Active': {'curator': 'AccountId', 'update_due': 'u32'},
        'Approved': None,
        'CuratorProposed': {'curator': 'AccountId'},
        'Funded': None,
        'PendingPayout': {
            'beneficiary': 'AccountId',
            'curator': 'AccountId',
            'unlock_at': 'u32',
        },
        'Proposed': None,
    },
    'value': 'u128',
}
```
---------
### BountyApprovals
 Bounty indices that have been approved but not yet funded.

#### Python
```python
result = substrate.query(
    'Bounties', 'BountyApprovals', []
)
```

#### Return value
```python
['u32']
```
---------
### BountyCount
 Number of bounty proposals that have been made.

#### Python
```python
result = substrate.query(
    'Bounties', 'BountyCount', []
)
```

#### Return value
```python
'u32'
```
---------
### BountyDescriptions
 The description of each bounty.

#### Python
```python
result = substrate.query(
    'Bounties', 'BountyDescriptions', ['u32']
)
```

#### Return value
```python
'Bytes'
```
---------
## Constants

---------
### BountyDepositBase
 The amount held on deposit for placing a bounty proposal.
#### Value
```python
1000000000000
```
#### Python
```python
constant = substrate.get_constant('Bounties', 'BountyDepositBase')
```
---------
### BountyDepositPayoutDelay
 The delay period for which a bounty beneficiary need to wait before claim the payout.
#### Value
```python
57600
```
#### Python
```python
constant = substrate.get_constant('Bounties', 'BountyDepositPayoutDelay')
```
---------
### BountyUpdatePeriod
 Bounty duration in blocks.
#### Value
```python
648000
```
#### Python
```python
constant = substrate.get_constant('Bounties', 'BountyUpdatePeriod')
```
---------
### BountyValueMinimum
 Minimum value for a bounty.
#### Value
```python
10000000000000
```
#### Python
```python
constant = substrate.get_constant('Bounties', 'BountyValueMinimum')
```
---------
### CuratorDepositMax
 Maximum amount of funds that should be placed in a deposit for making a proposal.
#### Value
```python
200000000000000
```
#### Python
```python
constant = substrate.get_constant('Bounties', 'CuratorDepositMax')
```
---------
### CuratorDepositMin
 Minimum amount of funds that should be placed in a deposit for making a proposal.
#### Value
```python
10000000000000
```
#### Python
```python
constant = substrate.get_constant('Bounties', 'CuratorDepositMin')
```
---------
### CuratorDepositMultiplier
 The curator deposit is calculated as a percentage of the curator fee.

 This deposit has optional upper and lower bounds with `CuratorDepositMax` and
 `CuratorDepositMin`.
#### Value
```python
500000
```
#### Python
```python
constant = substrate.get_constant('Bounties', 'CuratorDepositMultiplier')
```
---------
### DataDepositPerByte
 The amount held on deposit per byte within the tip report reason or bounty description.
#### Value
```python
10000000000
```
#### Python
```python
constant = substrate.get_constant('Bounties', 'DataDepositPerByte')
```
---------
### MaximumReasonLength
 Maximum acceptable reason length.

 Benchmarks depend on this value, be sure to update weights file when changing this value
#### Value
```python
16384
```
#### Python
```python
constant = substrate.get_constant('Bounties', 'MaximumReasonLength')
```
---------
## Errors

---------
### HasActiveChildBounty
The bounty cannot be closed because it has active child bounties.

---------
### InsufficientProposersBalance
Proposer&\#x27;s balance is too low.

---------
### InvalidFee
Invalid bounty fee.

---------
### InvalidIndex
No proposal or bounty at that index.

---------
### InvalidValue
Invalid bounty value.

---------
### PendingPayout
A bounty payout is pending.
To cancel the bounty, you must unassign and slash the curator.

---------
### Premature
The bounties cannot be claimed/closed because it&\#x27;s still in the countdown period.

---------
### ReasonTooBig
The reason given is just too big.

---------
### RequireCurator
Require bounty curator.

---------
### TooManyQueued
Too many approvals are already queued.

---------
### UnexpectedStatus
The bounty status is unexpected.

---------