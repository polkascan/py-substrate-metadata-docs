
# Alliance

---------
## Calls

---------
### abdicate_fellow_status
See [`Pallet::abdicate_fellow_status`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Alliance', 'abdicate_fellow_status', {}
)
```

---------
### add_unscrupulous_items
See [`Pallet::add_unscrupulous_items`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| items | `Vec<UnscrupulousItemOf<T, I>>` | 

#### Python
```python
call = substrate.compose_call(
    'Alliance', 'add_unscrupulous_items', {
    'items': [
        {
            'AccountId': 'AccountId',
            'Website': 'Bytes',
        },
    ],
}
)
```

---------
### announce
See [`Pallet::announce`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| announcement | `Cid` | 

#### Python
```python
call = substrate.compose_call(
    'Alliance', 'announce', {
    'announcement': {
        'codec': 'u64',
        'hash': {
            'code': 'u64',
            'digest': 'Bytes',
        },
        'version': ('V0', 'V1'),
    },
}
)
```

---------
### close
See [`Pallet::close`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| proposal_hash | `T::Hash` | 
| index | `ProposalIndex` | 
| proposal_weight_bound | `Weight` | 
| length_bound | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Alliance', 'close', {
    'index': 'u32',
    'length_bound': 'u32',
    'proposal_hash': 'scale_info::12',
    'proposal_weight_bound': {
        'proof_size': 'u64',
        'ref_time': 'u64',
    },
}
)
```

---------
### disband
See [`Pallet::disband`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| witness | `DisbandWitness` | 

#### Python
```python
call = substrate.compose_call(
    'Alliance', 'disband', {
    'witness': {
        'ally_members': 'u32',
        'fellow_members': 'u32',
    },
}
)
```

---------
### elevate_ally
See [`Pallet::elevate_ally`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| ally | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Alliance', 'elevate_ally', {
    'ally': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### give_retirement_notice
See [`Pallet::give_retirement_notice`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Alliance', 'give_retirement_notice', {}
)
```

---------
### init_members
See [`Pallet::init_members`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| fellows | `Vec<T::AccountId>` | 
| allies | `Vec<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'Alliance', 'init_members', {
    'allies': ['AccountId'],
    'fellows': ['AccountId'],
}
)
```

---------
### join_alliance
See [`Pallet::join_alliance`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Alliance', 'join_alliance', {}
)
```

---------
### kick_member
See [`Pallet::kick_member`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Alliance', 'kick_member', {
    'who': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### nominate_ally
See [`Pallet::nominate_ally`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Alliance', 'nominate_ally', {
    'who': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### propose
See [`Pallet::propose`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| threshold | `u32` | 
| proposal | `Box<<T as Config<I>>::Proposal>` | 
| length_bound | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Alliance', 'propose', {
    'length_bound': 'u32',
    'proposal': 'Call',
    'threshold': 'u32',
}
)
```

---------
### remove_announcement
See [`Pallet::remove_announcement`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| announcement | `Cid` | 

#### Python
```python
call = substrate.compose_call(
    'Alliance', 'remove_announcement', {
    'announcement': {
        'codec': 'u64',
        'hash': {
            'code': 'u64',
            'digest': 'Bytes',
        },
        'version': ('V0', 'V1'),
    },
}
)
```

---------
### remove_unscrupulous_items
See [`Pallet::remove_unscrupulous_items`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| items | `Vec<UnscrupulousItemOf<T, I>>` | 

#### Python
```python
call = substrate.compose_call(
    'Alliance', 'remove_unscrupulous_items', {
    'items': [
        {
            'AccountId': 'AccountId',
            'Website': 'Bytes',
        },
    ],
}
)
```

---------
### retire
See [`Pallet::retire`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Alliance', 'retire', {}
)
```

---------
### set_rule
See [`Pallet::set_rule`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| rule | `Cid` | 

#### Python
```python
call = substrate.compose_call(
    'Alliance', 'set_rule', {
    'rule': {
        'codec': 'u64',
        'hash': {
            'code': 'u64',
            'digest': 'Bytes',
        },
        'version': ('V0', 'V1'),
    },
}
)
```

---------
### vote
See [`Pallet::vote`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| proposal | `T::Hash` | 
| index | `ProposalIndex` | 
| approve | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Alliance', 'vote', {
    'approve': 'bool',
    'index': 'u32',
    'proposal': 'scale_info::12',
}
)
```

---------
## Events

---------
### AllianceDisbanded
Alliance disbanded. Includes number deleted members and unreserved deposits.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| fellow_members | `u32` | ```u32```
| ally_members | `u32` | ```u32```
| unreserved | `u32` | ```u32```

---------
### AllyElevated
An ally has been elevated to Fellow.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| ally | `T::AccountId` | ```AccountId```

---------
### Announced
A new announcement has been proposed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| announcement | `Cid` | ```{'version': ('V0', 'V1'), 'codec': 'u64', 'hash': {'code': 'u64', 'digest': 'Bytes'}}```

---------
### AnnouncementRemoved
An on-chain announcement has been removed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| announcement | `Cid` | ```{'version': ('V0', 'V1'), 'codec': 'u64', 'hash': {'code': 'u64', 'digest': 'Bytes'}}```

---------
### FellowAbdicated
A Fellow abdicated their voting rights. They are now an Ally.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| fellow | `T::AccountId` | ```AccountId```

---------
### MemberKicked
A member has been kicked out with its deposit slashed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| member | `T::AccountId` | ```AccountId```
| slashed | `Option<BalanceOf<T, I>>` | ```(None, 'u128')```

---------
### MemberRetired
A member has retired with its deposit unreserved.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| member | `T::AccountId` | ```AccountId```
| unreserved | `Option<BalanceOf<T, I>>` | ```(None, 'u128')```

---------
### MemberRetirementPeriodStarted
A member gave retirement notice and their retirement period started.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| member | `T::AccountId` | ```AccountId```

---------
### MembersInitialized
Some accounts have been initialized as members (fellows/allies).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| fellows | `Vec<T::AccountId>` | ```['AccountId']```
| allies | `Vec<T::AccountId>` | ```['AccountId']```

---------
### NewAllyJoined
An account has been added as an Ally and reserved its deposit.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| ally | `T::AccountId` | ```AccountId```
| nominator | `Option<T::AccountId>` | ```(None, 'AccountId')```
| reserved | `Option<BalanceOf<T, I>>` | ```(None, 'u128')```

---------
### NewRuleSet
A new rule has been set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| rule | `Cid` | ```{'version': ('V0', 'V1'), 'codec': 'u64', 'hash': {'code': 'u64', 'digest': 'Bytes'}}```

---------
### UnscrupulousItemAdded
Accounts or websites have been added into the list of unscrupulous items.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| items | `Vec<UnscrupulousItemOf<T, I>>` | ```[{'AccountId': 'AccountId', 'Website': 'Bytes'}]```

---------
### UnscrupulousItemRemoved
Accounts or websites have been removed from the list of unscrupulous items.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| items | `Vec<UnscrupulousItemOf<T, I>>` | ```[{'AccountId': 'AccountId', 'Website': 'Bytes'}]```

---------
## Storage functions

---------
### Announcements
 The current IPFS CIDs of any announcements.

#### Python
```python
result = substrate.query(
    'Alliance', 'Announcements', []
)
```

#### Return value
```python
[
    {
        'codec': 'u64',
        'hash': {'code': 'u64', 'digest': 'Bytes'},
        'version': ('V0', 'V1'),
    },
]
```
---------
### DepositOf
 Maps members to their candidacy deposit.

#### Python
```python
result = substrate.query(
    'Alliance', 'DepositOf', ['AccountId']
)
```

#### Return value
```python
'u128'
```
---------
### Members
 Maps member type to members of each type.

#### Python
```python
result = substrate.query(
    'Alliance', 'Members', [('Fellow', 'Ally', 'Retiring')]
)
```

#### Return value
```python
['AccountId']
```
---------
### RetiringMembers
 A set of members who gave a retirement notice. They can retire after the end of retirement
 period stored as a future block number.

#### Python
```python
result = substrate.query(
    'Alliance', 'RetiringMembers', ['AccountId']
)
```

#### Return value
```python
'u32'
```
---------
### Rule
 The IPFS CID of the alliance rule.
 Fellows can propose a new rule with a super-majority.

#### Python
```python
result = substrate.query(
    'Alliance', 'Rule', []
)
```

#### Return value
```python
{
    'codec': 'u64',
    'hash': {'code': 'u64', 'digest': 'Bytes'},
    'version': ('V0', 'V1'),
}
```
---------
### UnscrupulousAccounts
 The current list of accounts deemed unscrupulous. These accounts non grata cannot submit
 candidacy.

#### Python
```python
result = substrate.query(
    'Alliance', 'UnscrupulousAccounts', []
)
```

#### Return value
```python
['AccountId']
```
---------
### UnscrupulousWebsites
 The current list of websites deemed unscrupulous.

#### Python
```python
result = substrate.query(
    'Alliance', 'UnscrupulousWebsites', []
)
```

#### Return value
```python
['Bytes']
```
---------
## Constants

---------
### AllyDeposit
 The deposit required for submitting candidacy.
#### Value
```python
10000000000000
```
#### Python
```python
constant = substrate.get_constant('Alliance', 'AllyDeposit')
```
---------
### MaxAnnouncementsCount
 The maximum number of announcements.
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('Alliance', 'MaxAnnouncementsCount')
```
---------
### MaxMembersCount
 The maximum number of members per member role.
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('Alliance', 'MaxMembersCount')
```
---------
### MaxUnscrupulousItems
 The maximum number of the unscrupulous items supported by the pallet.
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('Alliance', 'MaxUnscrupulousItems')
```
---------
### MaxWebsiteUrlLength
 The maximum length of a website URL.
#### Value
```python
255
```
#### Python
```python
constant = substrate.get_constant('Alliance', 'MaxWebsiteUrlLength')
```
---------
## Errors

---------
### AccountNonGrata
Account has been deemed unscrupulous by the Alliance and is not welcome to join or be
nominated.

---------
### AllianceAlreadyInitialized
The Alliance has been initialized, therefore cannot be initialized again.

---------
### AllianceNotYetInitialized
The Alliance has not been initialized yet, therefore accounts cannot join it.

---------
### AlreadyElevated
Account is already an elevated (fellow) member.

---------
### AlreadyMember
Account is already a member.

---------
### AlreadyRetiring
Account already gave retirement notice

---------
### AlreadyUnscrupulous
Item is already listed as unscrupulous.

---------
### BadWitness
Invalid witness data given.

---------
### FellowsMissing
Fellows must be provided to initialize the Alliance.

---------
### InsufficientFunds
Balance is insufficient for the required deposit.

---------
### MissingAnnouncement
The announcement is not found.

---------
### MissingProposalHash
The proposal hash is not found.

---------
### NoVotingRights
Account does not have voting rights.

---------
### NotAlly
Account is not an ally.

---------
### NotListedAsUnscrupulous
Item has not been deemed unscrupulous.

---------
### NotMember
Account is not a member.

---------
### RetirementNoticeNotGiven
Account did not give a retirement notice required to retire.

---------
### RetirementPeriodNotPassed
Retirement period has not passed.

---------
### TooLongWebsiteUrl
Length of website URL exceeds `MaxWebsiteUrlLength`.

---------
### TooManyAnnouncements
Number of announcements exceeds `MaxAnnouncementsCount`.

---------
### TooManyMembers
Number of members exceeds `MaxMembersCount`.

---------
### TooManyUnscrupulousItems
The number of unscrupulous items exceeds `MaxUnscrupulousItems`.

---------
### WithoutGoodIdentityJudgement
The account&\#x27;s identity has no good judgement.

---------
### WithoutIdentityDisplayAndWebsite
The account&\#x27;s identity does not have display field and website field.

---------