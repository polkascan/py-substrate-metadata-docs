
# XGatewayCommon

---------
## Calls

---------
### cancel_trustee_election
Force cancel trustee transition

This is called by the root.
#### Attributes
| Name | Type |
| -------- | -------- | 
| chain | `Chain` | 

#### Python
```python
call = substrate.compose_call(
    'XGatewayCommon', 'cancel_trustee_election', {
    'chain': (
        'ChainX',
        'Bitcoin',
        'Ethereum',
        'Polkadot',
    ),
}
)
```

---------
### cancel_withdrawal
Cancel the withdrawal by the applicant.

WithdrawalRecord State: `Applying` ==&gt; `NormalCancel`
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `WithdrawalRecordId` | 

#### Python
```python
call = substrate.compose_call(
    'XGatewayCommon', 'cancel_withdrawal', {'id': 'u32'}
)
```

---------
### claim_trustee_reward
Assign trustee reward

Any trust can actively call this to receive the
award for the term the trust is in after the change
of term.

If a trust has not renewed for a long period of time
(no change in council membership or no unusual
circumstances to not renew), but they want to receive
their award early, they can call this through the council.
#### Attributes
| Name | Type |
| -------- | -------- | 
| chain | `Chain` | 
| session_num | `i32` | 

#### Python
```python
call = substrate.compose_call(
    'XGatewayCommon', 'claim_trustee_reward', {
    'chain': (
        'ChainX',
        'Bitcoin',
        'Ethereum',
        'Polkadot',
    ),
    'session_num': 'i32',
}
)
```

---------
### excute_trustee_election
Manual execution of the election by admin.
#### Attributes
| Name | Type |
| -------- | -------- | 
| chain | `Chain` | 

#### Python
```python
call = substrate.compose_call(
    'XGatewayCommon', 'excute_trustee_election', {
    'chain': (
        'ChainX',
        'Bitcoin',
        'Ethereum',
        'Polkadot',
    ),
}
)
```

---------
### force_set_referral_binding
Set the referral binding of corresponding chain and account.
#### Attributes
| Name | Type |
| -------- | -------- | 
| chain | `Chain` | 
| who | `<T::Lookup as StaticLookup>::Source` | 
| referral | `<T::Lookup as StaticLookup>::Source` | 

#### Python
```python
call = substrate.compose_call(
    'XGatewayCommon', 'force_set_referral_binding', {
    'chain': (
        'ChainX',
        'Bitcoin',
        'Ethereum',
        'Polkadot',
    ),
    'referral': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
    'who': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
}
)
```

---------
### force_trustee_election
Force trustee election

Mandatory trustee renewal if the current trustee is not doing anything

This is called by the root.
#### Attributes
| Name | Type |
| -------- | -------- | 
| chain | `Chain` | 

#### Python
```python
call = substrate.compose_call(
    'XGatewayCommon', 'force_trustee_election', {
    'chain': (
        'ChainX',
        'Bitcoin',
        'Ethereum',
        'Polkadot',
    ),
}
)
```

---------
### force_update_trustee
Force update trustee info

This is called by the root.
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `T::AccountId` | 
| proxy_account | `Option<T::AccountId>` | 
| chain | `Chain` | 
| about | `Text` | 
| hot_entity | `Vec<u8>` | 
| cold_entity | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'XGatewayCommon', 'force_update_trustee', {
    'about': 'Bytes',
    'chain': (
        'ChainX',
        'Bitcoin',
        'Ethereum',
        'Polkadot',
    ),
    'cold_entity': 'Bytes',
    'hot_entity': 'Bytes',
    'proxy_account': (
        None,
        'AccountId',
    ),
    'who': 'AccountId',
}
)
```

---------
### move_trust_into_black_room
Move a current trustee into a small black room.

This is to allow for timely replacement in the event of a problem with a particular trustee.
The trustee will be moved into the small black room.

This is called by the trustee admin and root.
\# &lt;weight&gt;
Since this is a root call and will go into trustee election, we assume full block for now.
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| chain | `Chain` | 
| trustees | `Option<Vec<T::AccountId>>` | 

#### Python
```python
call = substrate.compose_call(
    'XGatewayCommon', 'move_trust_into_black_room', {
    'chain': (
        'ChainX',
        'Bitcoin',
        'Ethereum',
        'Polkadot',
    ),
    'trustees': (None, ['AccountId']),
}
)
```

---------
### move_trust_out_black_room
Move member out small black room.

This is called by the trustee admin and root.
\# &lt;weight&gt;
Since this is a root call and will go into trustee election, we assume full block for now.
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| chain | `Chain` | 
| members | `Vec<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'XGatewayCommon', 'move_trust_out_black_room', {
    'chain': (
        'ChainX',
        'Bitcoin',
        'Ethereum',
        'Polkadot',
    ),
    'members': ['AccountId'],
}
)
```

---------
### register_dst_chain_config
Add named dst chain config
#### Attributes
| Name | Type |
| -------- | -------- | 
| prefix | `Vec<u8>` | 
| length | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'XGatewayCommon', 'register_dst_chain_config', {'length': 'u32', 'prefix': 'Bytes'}
)
```

---------
### set_dst_chain_proxy_address
Set dst chain proxy address

Used to proxy the address of a certain target chain and help
users to deposit and withdraw from that chain.

In earlier schemes, the proxy address was a multi-signature address to
ensure basic security. Removed after subsequent use of ultra-light node
scheme.
#### Attributes
| Name | Type |
| -------- | -------- | 
| dst_chain | `DstChain` | 
| proxy_account | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'XGatewayCommon', 'set_dst_chain_proxy_address', {
    'dst_chain': {
        'Aptos': None,
        'ChainX': None,
        'ChainXEvm': None,
        'Named': 'Bytes',
    },
    'proxy_account': 'AccountId',
}
)
```

---------
### set_trustee_admin
Set the trustee admin.

The trustee admin is the account who can change the trustee list.
#### Attributes
| Name | Type |
| -------- | -------- | 
| admin | `T::AccountId` | 
| chain | `Chain` | 

#### Python
```python
call = substrate.compose_call(
    'XGatewayCommon', 'set_trustee_admin', {
    'admin': 'AccountId',
    'chain': (
        'ChainX',
        'Bitcoin',
        'Ethereum',
        'Polkadot',
    ),
}
)
```

---------
### set_trustee_admin_multiply
Set trustee admin multiply

In order to incentivize trust administrators, a weighted multiplier
for award distribution to trust administrators is set.
#### Attributes
| Name | Type |
| -------- | -------- | 
| chain | `Chain` | 
| multiply | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'XGatewayCommon', 'set_trustee_admin_multiply', {
    'chain': (
        'ChainX',
        'Bitcoin',
        'Ethereum',
        'Polkadot',
    ),
    'multiply': 'u64',
}
)
```

---------
### set_trustee_info_config
Set the config of trustee information.

This is a root-only operation.
#### Attributes
| Name | Type |
| -------- | -------- | 
| chain | `Chain` | 
| config | `TrusteeInfoConfig` | 

#### Python
```python
call = substrate.compose_call(
    'XGatewayCommon', 'set_trustee_info_config', {
    'chain': (
        'ChainX',
        'Bitcoin',
        'Ethereum',
        'Polkadot',
    ),
    'config': {
        'max_trustee_count': 'u32',
        'min_trustee_count': 'u32',
    },
}
)
```

---------
### set_trustee_proxy
Set trustee&\#x27;s proxy account
#### Attributes
| Name | Type |
| -------- | -------- | 
| proxy_account | `T::AccountId` | 
| chain | `Chain` | 

#### Python
```python
call = substrate.compose_call(
    'XGatewayCommon', 'set_trustee_proxy', {
    'chain': (
        'ChainX',
        'Bitcoin',
        'Ethereum',
        'Polkadot',
    ),
    'proxy_account': 'AccountId',
}
)
```

---------
### setup_trustee
Setup the trustee info.

The hot and cold public keys of the current trustee cannot be replaced at will. If they
are randomly replaced, the hot and cold public keys of the current trustee before the
replacement will be lost, resulting in the inability to reconstruct the `Mast` tree and
generate the corresponding control block.

There are two solutions:
- the first is to record the hot and cold public keys for each
trustee renewal, and the trustee can update the hot and cold public keys at will.
- The second is to move these trusts into the `lttle_black_house` when it is necessary
to update the hot and cold public keys of trusts, and renew the trustee.
After the renewal of the trustee is completed, the hot and cold public keys can be
updated.

The second option is currently selected. `The time when the second option
allows the hot and cold public keys to be updated is that the member is not in the
current trustee and is not in a state of renewal of the trustee`.
The advantage of the second scheme is that there is no need to change the storage
structure and record the hot and cold public keys of previous trusts.
The disadvantage is that the update of the hot and cold public keys requires the
participation of the admin account and the user cannot update the hot and cold public
keys at will.
#### Attributes
| Name | Type |
| -------- | -------- | 
| proxy_account | `Option<T::AccountId>` | 
| chain | `Chain` | 
| about | `Text` | 
| hot_entity | `Vec<u8>` | 
| cold_entity | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'XGatewayCommon', 'setup_trustee', {
    'about': 'Bytes',
    'chain': (
        'ChainX',
        'Bitcoin',
        'Ethereum',
        'Polkadot',
    ),
    'cold_entity': 'Bytes',
    'hot_entity': 'Bytes',
    'proxy_account': (
        None,
        'AccountId',
    ),
}
)
```

---------
### unregister_dst_chain_config
Remove named dst chain config
#### Attributes
| Name | Type |
| -------- | -------- | 
| prefix | `Vec<u8>` | 
| length | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'XGatewayCommon', 'unregister_dst_chain_config', {'length': 'u32', 'prefix': 'Bytes'}
)
```

---------
### withdraw
Create a withdrawal.
Withdraws some balances of `asset_id` to address `addr` of target chain.

WithdrawalRecord State: `Applying`

NOTE: `ext` is for the compatibility purpose, e.g., EOS requires a memo when doing the transfer.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `AssetId` | 
| value | `BalanceOf<T>` | 
| addr | `AddrStr` | 
| ext | `Memo` | 

#### Python
```python
call = substrate.compose_call(
    'XGatewayCommon', 'withdraw', {
    'addr': 'Bytes',
    'asset_id': 'u32',
    'ext': 'Bytes',
    'value': 'u128',
}
)
```

---------
## Events

---------
### AllocNativeReward
The native asset of trustee multi_account is assigned. [multi_account, session_number, total_reward]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `u32` | ```u32```
| None | `BalanceOf<T>` | ```u128```

---------
### AllocNotNativeReward
The not native asset of trustee multi_account is assigned. [multi_account, session_number, asset_id, total_reward]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `u32` | ```u32```
| None | `AssetId` | ```u32```
| None | `BalanceOf<T>` | ```u128```

---------
### ReferralBinded
An account set its referral_account of some chain. [who, chain, referral_account]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `Chain` | ```('ChainX', 'Bitcoin', 'Ethereum', 'Polkadot')```
| None | `T::AccountId` | ```AccountId```

---------
### SetTrusteeProps
A (potential) trustee set the required properties. [who, chain, trustee_props]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `Chain` | ```('ChainX', 'Bitcoin', 'Ethereum', 'Polkadot')```
| None | `GenericTrusteeIntentionProps<T::AccountId>` | ```{'proxy_account': (None, 'AccountId'), 'about': 'Bytes', 'hot_entity': 'Bytes', 'cold_entity': 'Bytes'}```

---------
### SetTrusteeProxy
A trustee set proxy account. [who, chain, proxy_account]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `Chain` | ```('ChainX', 'Bitcoin', 'Ethereum', 'Polkadot')```
| None | `T::AccountId` | ```AccountId```

---------
### TransferAssetReward
Asset reward to trustee multi_account. [target, asset_id, reward_total]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `AssetId` | ```u32```
| None | `BalanceOf<T>` | ```u128```

---------
### TransferTrusteeReward
Treasury transfer to trustee. [source, target, chain, session_number, reward_total]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```
| None | `Chain` | ```('ChainX', 'Bitcoin', 'Ethereum', 'Polkadot')```
| None | `u32` | ```u32```
| None | `BalanceOf<T>` | ```u128```

---------
### TrusteeSetChanged
The trustee set of a chain was changed. [chain, session_number, session_info, script_info]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Chain` | ```('ChainX', 'Bitcoin', 'Ethereum', 'Polkadot')```
| None | `u32` | ```u32```
| None | `GenericTrusteeSessionInfo<T::AccountId, T::BlockNumber>` | ```{'trustee_list': [('AccountId', 'u64')], 'threshold': 'u16', 'hot_address': 'Bytes', 'cold_address': 'Bytes', 'multi_account': (None, 'AccountId'), 'start_height': (None, 'u32'), 'end_height': (None, 'u32')}```
| None | `u32` | ```u32```

---------
## Storage functions

---------
### AddressBindingOf
 The account of the corresponding chain and chain address.

#### Python
```python
result = substrate.query(
    'XGatewayCommon', 'AddressBindingOf', [
    (
        'ChainX',
        'Bitcoin',
        'Ethereum',
        'Polkadot',
    ),
    'Bytes',
]
)
```

#### Return value
```python
'AccountId'
```
---------
### AddressBindingOfDstChain
 Record the source chain address to the destination chain address.
 (src_chain, dst_chain, src_address) -&gt; dst_address

#### Python
```python
result = substrate.query(
    'XGatewayCommon', 'AddressBindingOfDstChain', [
    (
        'ChainX',
        'Bitcoin',
        'Ethereum',
        'Polkadot',
    ),
    {
        'Aptos': None,
        'ChainX': None,
        'ChainXEvm': None,
        'Named': 'Bytes',
    },
    'Bytes',
]
)
```

#### Return value
```python
'Bytes'
```
---------
### AggPubkeyInfo
 Each aggregated public key corresponds to a set of trustees used
 to confirm a set of trustees for processing withdrawals.

#### Python
```python
result = substrate.query(
    'XGatewayCommon', 'AggPubkeyInfo', [
    (
        'ChainX',
        'Bitcoin',
        'Ethereum',
        'Polkadot',
    ),
    'Bytes',
]
)
```

#### Return value
```python
['AccountId']
```
---------
### BoundAddressOf
 The bound address of the corresponding account and chain.

#### Python
```python
result = substrate.query(
    'XGatewayCommon', 'BoundAddressOf', [
    'AccountId',
    (
        'ChainX',
        'Bitcoin',
        'Ethereum',
        'Polkadot',
    ),
]
)
```

#### Return value
```python
['Bytes']
```
---------
### BoundAddressOfDstChain
 Record all source chain addresses corresponding to the destination chain address
 (dst_address, src_address, dst_address) -&gt; src_addresses

#### Python
```python
result = substrate.query(
    'XGatewayCommon', 'BoundAddressOfDstChain', [
    'Bytes',
    (
        'ChainX',
        'Bitcoin',
        'Ethereum',
        'Polkadot',
    ),
    {
        'Aptos': None,
        'ChainX': None,
        'ChainXEvm': None,
        'Named': 'Bytes',
    },
]
)
```

#### Return value
```python
['Bytes']
```
---------
### DefaultDstChain
 Multiple chains of addresses currently exist, so need to determine
 which chain to recharge to by default.

#### Python
```python
result = substrate.query(
    'XGatewayCommon', 'DefaultDstChain', ['Bytes']
)
```

#### Return value
```python
{'Aptos': None, 'ChainX': None, 'ChainXEvm': None, 'Named': 'Bytes'}
```
---------
### DstChainProxyAddress
 Dst chain&#x27;s cross-chain proxy address

#### Python
```python
result = substrate.query(
    'XGatewayCommon', 'DstChainProxyAddress', [
    {
        'Aptos': None,
        'ChainX': None,
        'ChainXEvm': None,
        'Named': 'Bytes',
    },
]
)
```

#### Return value
```python
'AccountId'
```
---------
### LittleBlackHouse
 Members not participating in trustee elections.

 The current trustee members did not conduct multiple signings and put the members in the
 little black room. Filter out the member in the next trustee election

#### Python
```python
result = substrate.query(
    'XGatewayCommon', 'LittleBlackHouse', [
    (
        'ChainX',
        'Bitcoin',
        'Ethereum',
        'Polkadot',
    ),
]
)
```

#### Return value
```python
['AccountId']
```
---------
### NamedDstChainConfig
 Named chain config

 For unsupported named chains need to be filtered to store the transactions
 in pending deposit.

#### Python
```python
result = substrate.query(
    'XGatewayCommon', 'NamedDstChainConfig', []
)
```

#### Return value
```python
[{'length': 'u32', 'prefix': 'Bytes'}]
```
---------
### PreTotalSupply
 Record the total number of cross-chain assets at the time of each trust exchange

#### Python
```python
result = substrate.query(
    'XGatewayCommon', 'PreTotalSupply', [
    (
        'ChainX',
        'Bitcoin',
        'Ethereum',
        'Polkadot',
    ),
    'u32',
]
)
```

#### Return value
```python
'u128'
```
---------
### ReferralBindingOf
 The referral account of the corresponding account and chain.

#### Python
```python
result = substrate.query(
    'XGatewayCommon', 'ReferralBindingOf', [
    'AccountId',
    (
        'ChainX',
        'Bitcoin',
        'Ethereum',
        'Polkadot',
    ),
]
)
```

#### Return value
```python
'AccountId'
```
---------
### TrusteeAdmin

#### Python
```python
result = substrate.query(
    'XGatewayCommon', 'TrusteeAdmin', [
    (
        'ChainX',
        'Bitcoin',
        'Ethereum',
        'Polkadot',
    ),
]
)
```

#### Return value
```python
'AccountId'
```
---------
### TrusteeAdminMultiply

#### Python
```python
result = substrate.query(
    'XGatewayCommon', 'TrusteeAdminMultiply', [
    (
        'ChainX',
        'Bitcoin',
        'Ethereum',
        'Polkadot',
    ),
]
)
```

#### Return value
```python
'u64'
```
---------
### TrusteeInfoConfigOf
 Trustee info config of the corresponding chain.

#### Python
```python
result = substrate.query(
    'XGatewayCommon', 'TrusteeInfoConfigOf', [
    (
        'ChainX',
        'Bitcoin',
        'Ethereum',
        'Polkadot',
    ),
]
)
```

#### Return value
```python
{'max_trustee_count': 'u32', 'min_trustee_count': 'u32'}
```
---------
### TrusteeIntentionPropertiesOf
 Trustee intention properties of the corresponding account and chain.

#### Python
```python
result = substrate.query(
    'XGatewayCommon', 'TrusteeIntentionPropertiesOf', [
    'AccountId',
    (
        'ChainX',
        'Bitcoin',
        'Ethereum',
        'Polkadot',
    ),
]
)
```

#### Return value
```python
{
    'about': 'Bytes',
    'cold_entity': 'Bytes',
    'hot_entity': 'Bytes',
    'proxy_account': (None, 'AccountId'),
}
```
---------
### TrusteeMultiSigAddr

#### Python
```python
result = substrate.query(
    'XGatewayCommon', 'TrusteeMultiSigAddr', [
    (
        'ChainX',
        'Bitcoin',
        'Ethereum',
        'Polkadot',
    ),
]
)
```

#### Return value
```python
'AccountId'
```
---------
### TrusteeSessionInfoLen
 Next Trustee session info number of the chain.

 Auto generate a new session number (0) when generate new trustee of a chain.
 If the trustee of a chain is changed, the corresponding number will increase by 1.

 NOTE: The number can&#x27;t be modified by users.

#### Python
```python
result = substrate.query(
    'XGatewayCommon', 'TrusteeSessionInfoLen', [
    (
        'ChainX',
        'Bitcoin',
        'Ethereum',
        'Polkadot',
    ),
]
)
```

#### Return value
```python
'u32'
```
---------
### TrusteeSessionInfoOf
 Trustee session info of the corresponding chain and number.

#### Python
```python
result = substrate.query(
    'XGatewayCommon', 'TrusteeSessionInfoOf', [
    (
        'ChainX',
        'Bitcoin',
        'Ethereum',
        'Polkadot',
    ),
    'u32',
]
)
```

#### Return value
```python
{
    'cold_address': 'Bytes',
    'end_height': (None, 'u32'),
    'hot_address': 'Bytes',
    'multi_account': (None, 'AccountId'),
    'start_height': (None, 'u32'),
    'threshold': 'u16',
    'trustee_list': [('AccountId', 'u64')],
}
```
---------
### TrusteeSigRecord

#### Python
```python
result = substrate.query(
    'XGatewayCommon', 'TrusteeSigRecord', [
    (
        'ChainX',
        'Bitcoin',
        'Ethereum',
        'Polkadot',
    ),
    'AccountId',
]
)
```

#### Return value
```python
'u64'
```
---------
### TrusteeTransitionStatus
 The status of the of the trustee transition

#### Python
```python
result = substrate.query(
    'XGatewayCommon', 'TrusteeTransitionStatus', [
    (
        'ChainX',
        'Bitcoin',
        'Ethereum',
        'Polkadot',
    ),
]
)
```

#### Return value
```python
'bool'
```
---------
## Errors

---------
### DuplicatedAccountId
existing duplicate account

---------
### ExistCurrentTrustee
exist in current trustee

---------
### InvalidAboutLen
exceed the maximum length of the about field of trustess session info

---------
### InvalidGenericData
convert generic data into trustee session info error

---------
### InvalidMultiAccount
invalid multi account

---------
### InvalidMultisig
invalid multisig

---------
### InvalidSessionNum
invalid session number

---------
### InvalidTrusteeHisMember
invalid trustee history member

---------
### InvalidTrusteeSession
trustee session info not found

---------
### InvalidTrusteeWeight
invalid trustee weight

---------
### InvalidWithdrawal
the value of withdrawal less than than the minimum value

---------
### LastTransitionNotCompleted
the last trustee transition was not completed.

---------
### NotRegistered
not registered as trustee

---------
### NotSupportedChain
unsupported chain

---------
### NotTrusteePreselectedMember
just allow trustee preselected members to set their trustee information

---------
### TrusteeMembersNotEnough
the trustee members was not enough.

---------
### WithdrawalProposalExist
prevent transition when the withdrawal proposal exists.

---------