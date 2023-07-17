
# XGatewayBitcoin

---------
## Calls

---------
### create_taproot_withdraw_tx
Trustee create a proposal for a withdrawal list. `tx` is the proposal withdrawal transaction.
#### Attributes
| Name | Type |
| -------- | -------- | 
| withdrawal_id_list | `Vec<u32>` | 
| tx | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'XGatewayBitcoin', 'create_taproot_withdraw_tx', {
    'tx': 'Bytes',
    'withdrawal_id_list': ['u32'],
}
)
```

---------
### push_header
if use `BtcHeader` struct would export in metadata, cause complex in front-end
#### Attributes
| Name | Type |
| -------- | -------- | 
| header | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'XGatewayBitcoin', 'push_header', {'header': 'Bytes'}
)
```

---------
### push_transaction
if use `RelayTx` struct would export in metadata, cause complex in front-end
#### Attributes
| Name | Type |
| -------- | -------- | 
| raw_tx | `Vec<u8>` | 
| relayed_info | `Vec<u8>` | 
| prev_tx | `Option<Vec<u8>>` | 

#### Python
```python
call = substrate.compose_call(
    'XGatewayBitcoin', 'push_transaction', {
    'prev_tx': (None, 'Bytes'),
    'raw_tx': 'Bytes',
    'relayed_info': 'Bytes',
}
)
```

---------
### remove_pending
Allow root or trustees could remove pending deposits for an address and decide whether
deposit to an account id. if pass `None` to `who`, would just remove pending, if pass
Some, would deposit to this account id.
#### Attributes
| Name | Type |
| -------- | -------- | 
| addr | `BtcAddress` | 
| who | `Option<OpReturnAccount<T::AccountId>>` | 

#### Python
```python
call = substrate.compose_call(
    'XGatewayBitcoin', 'remove_pending', {
    'addr': 'Bytes',
    'who': (
        None,
        {
            'Aptos': '[u8; 32]',
            'Evm': '[u8; 20]',
            'Named': (
                'Bytes',
                'Bytes',
            ),
            'Wasm': 'AccountId',
        },
    ),
}
)
```

---------
### remove_proposal
Dangerous! remove current withdrawal proposal directly. Please check business logic before
do this operation.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'XGatewayBitcoin', 'remove_proposal', {}
)
```

---------
### set_best_index
Dangerous! Be careful to set BestIndex
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `BtcHeaderIndex` | 

#### Python
```python
call = substrate.compose_call(
    'XGatewayBitcoin', 'set_best_index', {
    'index': {
        'hash': '[u8; 32]',
        'height': 'u32',
    },
}
)
```

---------
### set_btc_deposit_limit
Set bitcoin deposit limit
#### Attributes
| Name | Type |
| -------- | -------- | 
| value | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'XGatewayBitcoin', 'set_btc_deposit_limit', {'value': 'u64'}
)
```

---------
### set_btc_withdrawal_fee
Set bitcoin withdrawal fee
#### Attributes
| Name | Type |
| -------- | -------- | 
| fee | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'XGatewayBitcoin', 'set_btc_withdrawal_fee', {'fee': 'u64'}
)
```

---------
### set_coming_bot
Set coming bot
#### Attributes
| Name | Type |
| -------- | -------- | 
| bot | `Option<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'XGatewayBitcoin', 'set_coming_bot', {'bot': (None, 'AccountId')}
)
```

---------
### set_confirmed_index
Dangerous! Be careful to set ConfirmedIndex
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `BtcHeaderIndex` | 

#### Python
```python
call = substrate.compose_call(
    'XGatewayBitcoin', 'set_confirmed_index', {
    'index': {
        'hash': '[u8; 32]',
        'height': 'u32',
    },
}
)
```

---------
### set_confirmed_number
Dangerous! Be careful to set ConfirmationNumber
#### Attributes
| Name | Type |
| -------- | -------- | 
| number | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'XGatewayBitcoin', 'set_confirmed_number', {'number': 'u32'}
)
```

---------
## Events

---------
### Deposited
An account deposited some token. [tx_hash, who, amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `H256` | ```[u8; 32]```
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
### DepositedAptos
An account deposited some token for aptos address. [tx_hash, who, amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `H256` | ```[u8; 32]```
| None | `H256` | ```[u8; 32]```
| None | `BalanceOf<T>` | ```u128```

---------
### DepositedEvm
An account deposited some token for evm address. [tx_hash, who, amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `H256` | ```[u8; 32]```
| None | `H160` | ```[u8; 20]```
| None | `BalanceOf<T>` | ```u128```

---------
### DepositedNamed
An account deposited some token for named address. [tx_hash, prefix, who, amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `H256` | ```[u8; 32]```
| None | `Vec<u8>` | ```Bytes```
| None | `Vec<u8>` | ```Bytes```
| None | `BalanceOf<T>` | ```u128```

---------
### HeaderInserted
A Bitcoin header was validated and inserted. [btc_header_hash]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `H256` | ```[u8; 32]```

---------
### PendingDepositAptosRemoved
A unclaimed deposit record was removed for aptos address. [depositor, deposit_amount, tx_hash, btc_address]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `H256` | ```[u8; 32]```
| None | `BalanceOf<T>` | ```u128```
| None | `H256` | ```[u8; 32]```
| None | `BtcAddress` | ```Bytes```

---------
### PendingDepositEvmRemoved
A unclaimed deposit record was removed for evm address. [depositor, deposit_amount, tx_hash, btc_address]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `H160` | ```[u8; 20]```
| None | `BalanceOf<T>` | ```u128```
| None | `H256` | ```[u8; 32]```
| None | `BtcAddress` | ```Bytes```

---------
### PendingDepositNamedRemoved
A unclaimed deposit record was removed for named address. [prefix, depositor, deposit_amount, tx_hash, btc_address]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Vec<u8>` | ```Bytes```
| None | `Vec<u8>` | ```Bytes```
| None | `BalanceOf<T>` | ```u128```
| None | `H256` | ```[u8; 32]```
| None | `BtcAddress` | ```Bytes```

---------
### PendingDepositRemoved
A unclaimed deposit record was removed for wasm address. [depositor, deposit_amount, tx_hash, btc_address]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```
| None | `H256` | ```[u8; 32]```
| None | `BtcAddress` | ```Bytes```

---------
### TxProcessed
A Bitcoin transaction was processed. [tx_hash, block_hash, tx_state]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `H256` | ```[u8; 32]```
| None | `H256` | ```[u8; 32]```
| None | `BtcTxState` | ```{'tx_type': ('Withdrawal', 'Deposit', 'HotAndCold', 'TrusteeTransition', 'Irrelevance'), 'result': ('Success', 'Failure')}```

---------
### UnclaimedDeposit
A new record of unclaimed deposit. [tx_hash, btc_address]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `H256` | ```[u8; 32]```
| None | `BtcAddress` | ```Bytes```

---------
### WithdrawalFatalErr
A fatal error happened during the withdrawal process. [tx_hash, proposal_hash]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `H256` | ```[u8; 32]```
| None | `H256` | ```[u8; 32]```

---------
### WithdrawalProposalCreated
A new withdrawal proposal was created. [proposer, withdrawal_ids]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `Vec<u32>` | ```['u32']```

---------
### WithdrawalProposalVoted
A trustee voted/vetoed a withdrawal proposal. [trustee, vote_status]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `bool` | ```bool```

---------
### Withdrawn
A list of withdrawal applications were processed successfully. [tx_hash, withdrawal_ids, total_withdrawn]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `H256` | ```[u8; 32]```
| None | `Vec<u32>` | ```['u32']```
| None | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### BestIndex
 best header info

#### Python
```python
result = substrate.query(
    'XGatewayBitcoin', 'BestIndex', []
)
```

#### Return value
```python
{'hash': '[u8; 32]', 'height': 'u32'}
```
---------
### BlockHashFor
 block hash list for a height, include forked header hash

#### Python
```python
result = substrate.query(
    'XGatewayBitcoin', 'BlockHashFor', ['u32']
)
```

#### Return value
```python
['[u8; 32]']
```
---------
### BtcMinDeposit
 min deposit value limit, default is 10w sotashi(0.001 BTC)

#### Python
```python
result = substrate.query(
    'XGatewayBitcoin', 'BtcMinDeposit', []
)
```

#### Return value
```python
'u64'
```
---------
### BtcWithdrawalFee
 get BtcWithdrawalFee from genesis_config

#### Python
```python
result = substrate.query(
    'XGatewayBitcoin', 'BtcWithdrawalFee', []
)
```

#### Return value
```python
'u64'
```
---------
### ComingBot
 Coming bot helps update btc withdrawal transaction status

#### Python
```python
result = substrate.query(
    'XGatewayBitcoin', 'ComingBot', []
)
```

#### Return value
```python
'AccountId'
```
---------
### ConfirmationNumber
 get ConfirmationNumber from genesis_config

#### Python
```python
result = substrate.query(
    'XGatewayBitcoin', 'ConfirmationNumber', []
)
```

#### Return value
```python
'u32'
```
---------
### ConfirmedIndex
 confirmed header info

#### Python
```python
result = substrate.query(
    'XGatewayBitcoin', 'ConfirmedIndex', []
)
```

#### Return value
```python
{'hash': '[u8; 32]', 'height': 'u32'}
```
---------
### GenesisInfo
 get GenesisInfo (header, height)

#### Python
```python
result = substrate.query(
    'XGatewayBitcoin', 'GenesisInfo', []
)
```

#### Return value
```python
(
    {
        'bits': 'u32',
        'merkle_root_hash': '[u8; 32]',
        'nonce': 'u32',
        'previous_header_hash': '[u8; 32]',
        'time': 'u32',
        'version': 'u32',
    },
    'u32',
)
```
---------
### Headers
 all valid blockheader (include forked blockheader)

#### Python
```python
result = substrate.query(
    'XGatewayBitcoin', 'Headers', ['[u8; 32]']
)
```

#### Return value
```python
{
    'header': {
        'bits': 'u32',
        'merkle_root_hash': '[u8; 32]',
        'nonce': 'u32',
        'previous_header_hash': '[u8; 32]',
        'time': 'u32',
        'version': 'u32',
    },
    'height': 'u32',
}
```
---------
### MainChain
 mark this blockhash is in mainchain

#### Python
```python
result = substrate.query(
    'XGatewayBitcoin', 'MainChain', ['[u8; 32]']
)
```

#### Return value
```python
'bool'
```
---------
### MaxWithdrawalCount
 max withdraw account count in bitcoin withdrawal transaction

#### Python
```python
result = substrate.query(
    'XGatewayBitcoin', 'MaxWithdrawalCount', []
)
```

#### Return value
```python
'u32'
```
---------
### NetworkId
  NetworkId for testnet or mainnet

#### Python
```python
result = substrate.query(
    'XGatewayBitcoin', 'NetworkId', []
)
```

#### Return value
```python
('Mainnet', 'Testnet', 'DogeCoinMainnet', 'DogeCoinTestnet')
```
---------
### ParamsInfo
 get ParamsInfo from genesis_config

#### Python
```python
result = substrate.query(
    'XGatewayBitcoin', 'ParamsInfo', []
)
```

#### Return value
```python
{
    'block_max_future': 'u32',
    'max_bits': 'u32',
    'max_timespan': 'u32',
    'min_timespan': 'u32',
    'retargeting_factor': 'u32',
    'retargeting_interval': 'u32',
    'target_spacing_seconds': 'u32',
    'target_timespan_seconds': 'u32',
}
```
---------
### PendingDeposits
 unclaimed deposit info, addr =&gt; tx_hash, btc value,

#### Python
```python
result = substrate.query(
    'XGatewayBitcoin', 'PendingDeposits', ['Bytes']
)
```

#### Return value
```python
[{'balance': 'u64', 'txid': '[u8; 32]'}]
```
---------
### TxState
 mark tx has been handled, in case re-handle this tx, and log handle result

#### Python
```python
result = substrate.query(
    'XGatewayBitcoin', 'TxState', ['[u8; 32]']
)
```

#### Return value
```python
{
    'result': ('Success', 'Failure'),
    'tx_type': (
        'Withdrawal',
        'Deposit',
        'HotAndCold',
        'TrusteeTransition',
        'Irrelevance',
    ),
}
```
---------
### Verifier

#### Python
```python
result = substrate.query(
    'XGatewayBitcoin', 'Verifier', []
)
```

#### Return value
```python
('Recover', 'RuntimeInterface')
```
---------
### WithdrawalProposal
 withdrawal tx outs for account, tx_hash =&gt; outs ( out index =&gt; withdrawal account )

#### Python
```python
result = substrate.query(
    'XGatewayBitcoin', 'WithdrawalProposal', []
)
```

#### Return value
```python
{
    'sig_state': ('Unfinish', 'Finish'),
    'trustee_list': [('AccountId', 'bool')],
    'tx': {
        'inputs': [
            {
                'previous_output': {'index': 'u32', 'txid': '[u8; 32]'},
                'script_sig': 'Bytes',
                'script_witness': ['Bytes'],
                'sequence': 'u32',
            },
        ],
        'lock_time': 'u32',
        'outputs': [{'script_pubkey': 'Bytes', 'value': 'u64'}],
        'version': 'i32',
    },
    'withdrawal_id_list': ['u32'],
}
```
---------
## Errors

---------
### AncientFork
Fork is too long to proceed

---------
### BadMerkleProof
Invalid merkle proof

---------
### DeserializeErr
Cannot deserialize the header or tx vec

---------
### DuplicateVote
already vote for this withdrawal proposal

---------
### DuplicatedKeys
duplicated pubkey for trustees

---------
### ExistingHeader
Header already exists

---------
### GenerateMultisigFailed
can&\#x27;t generate multisig address

---------
### HeaderFuturisticTimestamp
Futuristic timestamp

---------
### HeaderNBitsNotMatch
nBits do not match difficulty rules

---------
### InvalidAddr
load addr from bytes error

---------
### InvalidAddress
invalid bitcoin address

---------
### InvalidBase58
parse base58 addr error

---------
### InvalidPoW
Invalid proof-of-work (Block hash does not satisfy nBits)

---------
### InvalidPrevTx
Previous tx id not equal input point hash

---------
### InvalidPublicKey
invalid bitcoin public key

---------
### InvalidTrusteeCount
invalid trustee count

---------
### NoProposal
no proposal for current withdrawal

---------
### NoWithdrawalRecord
no withdrawal record for this id

---------
### NotFinishProposal
last proposal not finished yet

---------
### NotTrustee
not set trustee yet

---------
### PrevHeaderNotExisted
Can&\#x27;t find previous header

---------
### ProcessTxFailed
process tx failed

---------
### ReplayedTx
reject replay proccessed tx

---------
### TrusteeTransitionPeriod
Trustee transition period

---------
### TxNotFullAmount
The total amount of the trust must be transferred out in full

---------
### TxOutputNotColdAddr
The output address must be a cold address during the trust transition process

---------
### TxOutputsNotMatch
tx&\#x27;s outputs not match withdrawal id list

---------
### UnconfirmedTx
The tx is not yet confirmed, i.e, the block of which is not confirmed.

---------
### WrongWithdrawalCount
unexpected withdraw records count

---------