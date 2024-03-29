
# Members

---------
## Calls

---------
### add_staking_account_candidate
Add staking account candidate for a member.
The membership must be confirmed before usage.

&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| member_id | `T::MemberId` | 

#### Python
```python
call = substrate.compose_call(
    'Members', 'add_staking_account_candidate', {'member_id': 'u64'}
)
```

---------
### buy_membership
Non-members can buy membership.

&lt;weight&gt;

\#\# Weight
`O (W + M)` where:
- `W` is the handle size in kilobytes
- `M` is the metadata size in kilobytes
- DB:
   - O(1)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| params | `BuyMembershipParameters<T::AccountId, T::MemberId>` | 

#### Python
```python
call = substrate.compose_call(
    'Members', 'buy_membership', {
    'params': {
        'controller_account': 'AccountId',
        'handle': (None, 'Bytes'),
        'metadata': 'Bytes',
        'referrer_id': (None, 'u64'),
        'root_account': 'AccountId',
    },
}
)
```

---------
### confirm_staking_account
Confirm staking account candidate for a member.

&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| member_id | `T::MemberId` | 
| staking_account_id | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Members', 'confirm_staking_account', {
    'member_id': 'u64',
    'staking_account_id': 'AccountId',
}
)
```

---------
### create_member
Create a member profile as root.

&lt;weight&gt;

\#\# Weight
`O (I + J)` where:
- `I` is the handle size in kilobytes
- `J` is the metadata size in kilobytes
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| params | `CreateMemberParameters<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'Members', 'create_member', {
    'params': {
        'controller_account': 'AccountId',
        'handle': 'Bytes',
        'is_founding_member': 'bool',
        'metadata': 'Bytes',
        'root_account': 'AccountId',
    },
}
)
```

---------
### gift_membership
Gift a membership using own funds. Gifter does not need to be a member.
Can optinally apply a lock on a portion of the funds transferred to root and controller
accounts. Gifter also pays the membership fee.
#### Attributes
| Name | Type |
| -------- | -------- | 
| params | `GiftMembershipParameters<T::AccountId, BalanceOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Members', 'gift_membership', {
    'params': {
        'apply_controller_account_invitation_lock': (
            None,
            'u128',
        ),
        'apply_root_account_invitation_lock': (
            None,
            'u128',
        ),
        'controller_account': 'AccountId',
        'credit_controller_account': 'u128',
        'credit_root_account': 'u128',
        'handle': (None, 'Bytes'),
        'metadata': 'Bytes',
        'root_account': 'AccountId',
    },
}
)
```

---------
### invite_member
Invite a new member.

&lt;weight&gt;

\#\# Weight
`O (W + M)` where:
- `W` is the handle size in kilobytes
- `M` is the metadata size in kilobytes
- DB:
   - O(1)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| params | `InviteMembershipParameters<T::AccountId, T::MemberId>` | 

#### Python
```python
call = substrate.compose_call(
    'Members', 'invite_member', {
    'params': {
        'controller_account': 'AccountId',
        'handle': (None, 'Bytes'),
        'inviting_member_id': 'u64',
        'metadata': 'Bytes',
        'root_account': 'AccountId',
    },
}
)
```

---------
### member_remark
Member makes a remark

&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| member_id | `T::MemberId` | 
| msg | `Vec<u8>` | 
| payment | `Option<(T::AccountId, T::Balance)>` | 

#### Python
```python
call = substrate.compose_call(
    'Members', 'member_remark', {
    'member_id': 'u64',
    'msg': 'Bytes',
    'payment': (
        None,
        ('AccountId', 'u128'),
    ),
}
)
```

---------
### remove_staking_account
Remove staking account for a member.

&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| member_id | `T::MemberId` | 

#### Python
```python
call = substrate.compose_call(
    'Members', 'remove_staking_account', {'member_id': 'u64'}
)
```

---------
### set_initial_invitation_balance
Updates initial invitation balance for a invited member. Requires root origin.

&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_initial_balance | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Members', 'set_initial_invitation_balance', {'new_initial_balance': 'u128'}
)
```

---------
### set_initial_invitation_count
Updates initial invitation count for a member. Requires root origin.

&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_invitation_count | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Members', 'set_initial_invitation_count', {'new_invitation_count': 'u32'}
)
```

---------
### set_leader_invitation_quota
Updates leader invitation quota. Requires root origin.

&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| invitation_quota | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Members', 'set_leader_invitation_quota', {'invitation_quota': 'u32'}
)
```

---------
### set_membership_price
Updates membership price. Requires root origin.

&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_price | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Members', 'set_membership_price', {'new_price': 'u128'}
)
```

---------
### set_referral_cut
Updates membership referral cut percent value. Requires root origin.

&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| percent_value | `u8` | 

#### Python
```python
call = substrate.compose_call(
    'Members', 'set_referral_cut', {'percent_value': 'u8'}
)
```

---------
### transfer_invites
Transfers invites from one member to another.

&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| source_member_id | `T::MemberId` | 
| target_member_id | `T::MemberId` | 
| number_of_invites | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Members', 'transfer_invites', {
    'number_of_invites': 'u32',
    'source_member_id': 'u64',
    'target_member_id': 'u64',
}
)
```

---------
### update_accounts
Updates member root or controller accounts. No effect if both new accounts are empty.

&lt;weight&gt;

&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| member_id | `T::MemberId` | 
| new_root_account | `Option<T::AccountId>` | 
| new_controller_account | `Option<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'Members', 'update_accounts', {
    'member_id': 'u64',
    'new_controller_account': (
        None,
        'AccountId',
    ),
    'new_root_account': (
        None,
        'AccountId',
    ),
}
)
```

---------
### update_profile
Update member&\#x27;s all or some of name, handle, avatar and about text.
No effect if no changed fields.

&lt;weight&gt;

\#\# Weight
`O (W + M)` where:
- `W` is the handle size in kilobytes
- `M` is the metadata size in kilobytes
- DB:
   - O(1)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| member_id | `T::MemberId` | 
| handle | `Option<Vec<u8>>` | 
| metadata | `Option<Vec<u8>>` | 

#### Python
```python
call = substrate.compose_call(
    'Members', 'update_profile', {
    'handle': (None, 'Bytes'),
    'member_id': 'u64',
    'metadata': (None, 'Bytes'),
}
)
```

---------
### update_profile_verification
Updates member profile verification status. Requires working group member origin.

&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| worker_id | `T::ActorId` | 
| target_member_id | `T::MemberId` | 
| is_verified | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Members', 'update_profile_verification', {
    'is_verified': 'bool',
    'target_member_id': 'u64',
    'worker_id': 'u64',
}
)
```

---------
## Events

---------
### InitialInvitationBalanceUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Balance` | ```u128```

---------
### InitialInvitationCountUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u32` | ```u32```

---------
### InvitesTransferred
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MemberId` | ```u64```
| None | `MemberId` | ```u64```
| None | `u32` | ```u32```

---------
### LeaderInvitationQuotaUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u32` | ```u32```

---------
### MemberAccountsUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MemberId` | ```u64```
| None | `Option<AccountId>` | ```(None, 'AccountId')```
| None | `Option<AccountId>` | ```(None, 'AccountId')```

---------
### MemberCreated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MemberId` | ```u64```
| None | `CreateMemberParameters` | ```{'root_account': 'AccountId', 'controller_account': 'AccountId', 'handle': 'Bytes', 'metadata': 'Bytes', 'is_founding_member': 'bool'}```
| None | `u32` | ```u32```

---------
### MemberInvited
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MemberId` | ```u64```
| None | `InviteMembershipParameters` | ```{'inviting_member_id': 'u64', 'root_account': 'AccountId', 'controller_account': 'AccountId', 'handle': (None, 'Bytes'), 'metadata': 'Bytes'}```
| None | `Balance` | ```u128```

---------
### MemberProfileUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MemberId` | ```u64```
| None | `Option<Vec<u8>>` | ```(None, 'Bytes')```
| None | `Option<Vec<u8>>` | ```(None, 'Bytes')```

---------
### MemberRemarked
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MemberId` | ```u64```
| None | `Vec<u8>` | ```Bytes```
| None | `Option<(AccountId, Balance)>` | ```(None, ('AccountId', 'u128'))```

---------
### MemberVerificationStatusUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MemberId` | ```u64```
| None | `bool` | ```bool```
| None | `ActorId` | ```u64```

---------
### MembershipBought
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MemberId` | ```u64```
| None | `BuyMembershipParameters` | ```{'root_account': 'AccountId', 'controller_account': 'AccountId', 'handle': (None, 'Bytes'), 'metadata': 'Bytes', 'referrer_id': (None, 'u64')}```
| None | `u32` | ```u32```

---------
### MembershipGifted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MemberId` | ```u64```
| None | `GiftMembershipParameters` | ```{'root_account': 'AccountId', 'controller_account': 'AccountId', 'handle': (None, 'Bytes'), 'metadata': 'Bytes', 'credit_controller_account': 'u128', 'apply_controller_account_invitation_lock': (None, 'u128'), 'credit_root_account': 'u128', 'apply_root_account_invitation_lock': (None, 'u128')}```

---------
### MembershipPriceUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Balance` | ```u128```

---------
### ReferralCutUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u8` | ```u8```

---------
### StakingAccountAdded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountId` | ```AccountId```
| None | `MemberId` | ```u64```

---------
### StakingAccountConfirmed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountId` | ```AccountId```
| None | `MemberId` | ```u64```

---------
### StakingAccountRemoved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountId` | ```AccountId```
| None | `MemberId` | ```u64```

---------
## Storage functions

---------
### InitialInvitationBalance
 Initial invitation balance for the invited member.

#### Python
```python
result = substrate.query(
    'Members', 'InitialInvitationBalance', []
)
```

#### Return value
```python
'u128'
```
---------
### InitialInvitationCount
 Initial invitation count for the newly bought membership.

#### Python
```python
result = substrate.query(
    'Members', 'InitialInvitationCount', []
)
```

#### Return value
```python
'u32'
```
---------
### MemberIdByHandleHash
 Registered unique handles hash and their mapping to their owner.

#### Python
```python
result = substrate.query(
    'Members', 'MemberIdByHandleHash', ['scale_info::11']
)
```

#### Return value
```python
'u64'
```
---------
### MembershipById
 Mapping of member&#x27;s id to their membership profile.

#### Python
```python
result = substrate.query(
    'Members', 'MembershipById', ['u64']
)
```

#### Return value
```python
{
    'controller_account': 'AccountId',
    'handle_hash': 'scale_info::11',
    'invites': 'u32',
    'root_account': 'AccountId',
    'verified': 'bool',
}
```
---------
### MembershipPrice
 Current membership price.

#### Python
```python
result = substrate.query(
    'Members', 'MembershipPrice', []
)
```

#### Return value
```python
'u128'
```
---------
### NextMemberId
 MemberId to assign to next member that is added to the registry, and is also the
 total number of members created. MemberIds start at Zero.

#### Python
```python
result = substrate.query(
    'Members', 'NextMemberId', []
)
```

#### Return value
```python
'u64'
```
---------
### ReferralCut
 Referral cut percent of the membership fee to receive on buying the membership.

#### Python
```python
result = substrate.query(
    'Members', 'ReferralCut', []
)
```

#### Return value
```python
'u8'
```
---------
### StakingAccountIdMemberStatus
 Double of a staking account id and member id to the confirmation status.

#### Python
```python
result = substrate.query(
    'Members', 'StakingAccountIdMemberStatus', ['AccountId']
)
```

#### Return value
```python
{'confirmed': 'bool', 'member_id': 'u64'}
```
---------
## Constants

---------
### CandidateStake
 Exports const - Stake needed to candidate as staking account.
#### Value
```python
1666666666660
```
#### Python
```python
constant = substrate.get_constant('Members', 'CandidateStake')
```
---------
### DefaultInitialInvitationBalance
 Exports const - default balance for the invited member.
#### Value
```python
83333333300
```
#### Python
```python
constant = substrate.get_constant('Members', 'DefaultInitialInvitationBalance')
```
---------
### DefaultMembershipPrice
 Exports const - default membership fee.
#### Value
```python
166666666666
```
#### Python
```python
constant = substrate.get_constant('Members', 'DefaultMembershipPrice')
```
---------
### InvitedMemberLockId
 Exports const - invited member lock id.
#### Value
```python
'0x696e766974656d62'
```
#### Python
```python
constant = substrate.get_constant('Members', 'InvitedMemberLockId')
```
---------
### ReferralCutMaximumPercent
 Exports const - maximum percent value of the membership fee for the referral cut.
#### Value
```python
50
```
#### Python
```python
constant = substrate.get_constant('Members', 'ReferralCutMaximumPercent')
```
---------
### StakingCandidateLockId
 Exports const - staking candidate lock id.
#### Value
```python
'0x626f756e64737461'
```
#### Python
```python
constant = substrate.get_constant('Members', 'StakingCandidateLockId')
```
---------
## Errors

---------
### CannotExceedReferralCutPercentLimit
Cannot set a referral cut percent value. The limit was exceeded.

---------
### CannotTransferInvitesForNotMember
Should be a member to receive invites.

---------
### ConflictStakesOnAccount
Staking account contains conflicting stakes.

---------
### ConflictingLock
Cannot invite a member. The controller account has an existing conflicting lock.

---------
### ControllerAccountRequired
Controller account required.

---------
### GifLockExceedsCredit
Locked amount is greater than credit amount

---------
### HandleAlreadyRegistered
Handle already registered.

---------
### HandleMustBeProvidedDuringRegistration
Handle must be provided during registration.

---------
### InsufficientBalanceToCoverPayment
Insufficient balance to cover payment.

---------
### InsufficientBalanceToCoverStake
Insufficient balance to cover stake.

---------
### InsufficientBalanceToGift
Gifter doesn&\#x27;t have sufficient balance to credit

---------
### MemberProfileNotFound
Member profile not found (invalid member id).

---------
### NotEnoughBalanceToBuyMembership
Not enough balance to buy membership.

---------
### NotEnoughInvites
Not enough invites to perform an operation.

---------
### ReferrerIsNotMember
Cannot find a membership for a provided referrer id.

---------
### RootAccountRequired
Root account required.

---------
### StakingAccountAlreadyConfirmed
Staking account has already been confirmed.

---------
### StakingAccountDoesntExist
Staking account for membership doesn&\#x27;t exist.

---------
### StakingAccountIsAlreadyRegistered
Staking account is registered for some member.

---------
### UnsignedOrigin
Unsigned origin.

---------
### WorkingGroupBudgetIsNotSufficientForInviting
Cannot invite a member. Working group balance is not sufficient to set the default
balance.

---------
### WorkingGroupLeaderNotSet
Membership working group leader is not set.

---------