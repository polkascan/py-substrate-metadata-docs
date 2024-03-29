
# ProposalsCodex

---------
## Calls

---------
### create_proposal
Create a proposal, the type of proposal depends on the `proposal_details` variant

&lt;weight&gt;

\#\# Weight
`O (T + D + I)` where:
- `T` is the title size in kilobytes
- `D` is the description size in kilobytes
- `I` is the size of any parameter in `proposal_details`
  (in kilobytes if it&\#x27;s metadata)
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| general_proposal_parameters | `GeneralProposalParameters<T>` | 
| proposal_details | `ProposalDetailsOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'ProposalsCodex', 'create_proposal', {
    'general_proposal_parameters': {
        'description': 'Bytes',
        'exact_execution_block': (
            None,
            'u32',
        ),
        'member_id': 'u64',
        'staking_account_id': (
            None,
            'AccountId',
        ),
        'title': 'Bytes',
    },
    'proposal_details': {
        'AmendConstitution': 'Bytes',
        'CancelWorkingGroupLeadOpening': (
            'u64',
            (
                'Forum',
                'Storage',
                'Content',
                'OperationsAlpha',
                'App',
                'Distribution',
                'OperationsBeta',
                'OperationsGamma',
                'Membership',
            ),
        ),
        'CreateWorkingGroupLeadOpening': {
            'description': 'Bytes',
            'group': (
                'Forum',
                'Storage',
                'Content',
                'OperationsAlpha',
                'App',
                'Distribution',
                'OperationsBeta',
                'OperationsGamma',
                'Membership',
            ),
            'reward_per_block': (
                None,
                'u128',
            ),
            'stake_policy': {
                'leaving_unstaking_period': 'u32',
                'stake_amount': 'u128',
            },
        },
        'DecreaseWorkingGroupLeadStake': (
            'u64',
            'u128',
            (
                'Forum',
                'Storage',
                'Content',
                'OperationsAlpha',
                'App',
                'Distribution',
                'OperationsBeta',
                'OperationsGamma',
                'Membership',
            ),
        ),
        'FillWorkingGroupLeadOpening': {
            'application_id': 'u64',
            'opening_id': 'u64',
            'working_group': (
                'Forum',
                'Storage',
                'Content',
                'OperationsAlpha',
                'App',
                'Distribution',
                'OperationsBeta',
                'OperationsGamma',
                'Membership',
            ),
        },
        'FundingRequest': [
            {
                'account': 'AccountId',
                'amount': 'u128',
            },
        ],
        'RuntimeUpgrade': 'Bytes',
        'SetCouncilBudgetIncrement': 'u128',
        'SetCouncilorReward': 'u128',
        'SetInitialInvitationBalance': 'u128',
        'SetInitialInvitationCount': 'u32',
        'SetMaxValidatorCount': 'u32',
        'SetMembershipLeadInvitationQuota': 'u32',
        'SetMembershipPrice': 'u128',
        'SetPalletFozenStatus': (
            'bool',
            ('ProjectToken', ),
        ),
        'SetReferralCut': 'u8',
        'SetWorkingGroupLeadReward': (
            'u64',
            (None, 'u128'),
            (
                'Forum',
                'Storage',
                'Content',
                'OperationsAlpha',
                'App',
                'Distribution',
                'OperationsBeta',
                'OperationsGamma',
                'Membership',
            ),
        ),
        'Signal': 'Bytes',
        'SlashWorkingGroupLead': (
            'u64',
            'u128',
            (
                'Forum',
                'Storage',
                'Content',
                'OperationsAlpha',
                'App',
                'Distribution',
                'OperationsBeta',
                'OperationsGamma',
                'Membership',
            ),
        ),
        'TerminateWorkingGroupLead': {
            'group': (
                'Forum',
                'Storage',
                'Content',
                'OperationsAlpha',
                'App',
                'Distribution',
                'OperationsBeta',
                'OperationsGamma',
                'Membership',
            ),
            'slashing_amount': (
                None,
                'u128',
            ),
            'worker_id': 'u64',
        },
        'UpdateChannelPayouts': {
            'channel_cashouts_enabled': (
                None,
                'bool',
            ),
            'commitment': (
                None,
                'scale_info::11',
            ),
            'max_cashout_allowed': (
                None,
                'u128',
            ),
            'min_cashout_allowed': (
                None,
                'u128',
            ),
            'payload': (
                None,
                {
                    'expected_data_object_state_bloat_bond': 'u128',
                    'expected_data_size_fee': 'u128',
                    'object_creation_params': {
                        'ipfs_content_id': 'Bytes',
                        'size': 'u64',
                    },
                },
            ),
        },
        'UpdateGlobalNftLimit': (
            ('Daily', 'Weekly'),
            'u64',
        ),
        'UpdateWorkingGroupBudget': (
            'u128',
            (
                'Forum',
                'Storage',
                'Content',
                'OperationsAlpha',
                'App',
                'Distribution',
                'OperationsBeta',
                'OperationsGamma',
                'Membership',
            ),
            ('Positive', 'Negative'),
        ),
        'VetoProposal': 'u32',
    },
}
)
```

---------
## Events

---------
### ProposalCreated
A proposal was created
Params:
- Id of a newly created proposal after it was saved in storage.
- General proposal parameter. Parameters shared by all proposals
- Proposal Details. Parameter of proposal with a variant for each kind of proposal
- Id of a newly created proposal thread
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ProposalId` | ```u32```
| None | `GeneralProposalParameters` | ```{'member_id': 'u64', 'title': 'Bytes', 'description': 'Bytes', 'staking_account_id': (None, 'AccountId'), 'exact_execution_block': (None, 'u32')}```
| None | `ProposalDetailsOf` | ```{'Signal': 'Bytes', 'RuntimeUpgrade': 'Bytes', 'FundingRequest': [{'account': 'AccountId', 'amount': 'u128'}], 'SetMaxValidatorCount': 'u32', 'CreateWorkingGroupLeadOpening': {'description': 'Bytes', 'stake_policy': {'stake_amount': 'u128', 'leaving_unstaking_period': 'u32'}, 'reward_per_block': (None, 'u128'), 'group': ('Forum', 'Storage', 'Content', 'OperationsAlpha', 'App', 'Distribution', 'OperationsBeta', 'OperationsGamma', 'Membership')}, 'FillWorkingGroupLeadOpening': {'opening_id': 'u64', 'application_id': 'u64', 'working_group': ('Forum', 'Storage', 'Content', 'OperationsAlpha', 'App', 'Distribution', 'OperationsBeta', 'OperationsGamma', 'Membership')}, 'UpdateWorkingGroupBudget': ('u128', ('Forum', 'Storage', 'Content', 'OperationsAlpha', 'App', 'Distribution', 'OperationsBeta', 'OperationsGamma', 'Membership'), ('Positive', 'Negative')), 'DecreaseWorkingGroupLeadStake': ('u64', 'u128', ('Forum', 'Storage', 'Content', 'OperationsAlpha', 'App', 'Distribution', 'OperationsBeta', 'OperationsGamma', 'Membership')), 'SlashWorkingGroupLead': ('u64', 'u128', ('Forum', 'Storage', 'Content', 'OperationsAlpha', 'App', 'Distribution', 'OperationsBeta', 'OperationsGamma', 'Membership')), 'SetWorkingGroupLeadReward': ('u64', (None, 'u128'), ('Forum', 'Storage', 'Content', 'OperationsAlpha', 'App', 'Distribution', 'OperationsBeta', 'OperationsGamma', 'Membership')), 'TerminateWorkingGroupLead': {'worker_id': 'u64', 'slashing_amount': (None, 'u128'), 'group': ('Forum', 'Storage', 'Content', 'OperationsAlpha', 'App', 'Distribution', 'OperationsBeta', 'OperationsGamma', 'Membership')}, 'AmendConstitution': 'Bytes', 'CancelWorkingGroupLeadOpening': ('u64', ('Forum', 'Storage', 'Content', 'OperationsAlpha', 'App', 'Distribution', 'OperationsBeta', 'OperationsGamma', 'Membership')), 'SetMembershipPrice': 'u128', 'SetCouncilBudgetIncrement': 'u128', 'SetCouncilorReward': 'u128', 'SetInitialInvitationBalance': 'u128', 'SetInitialInvitationCount': 'u32', 'SetMembershipLeadInvitationQuota': 'u32', 'SetReferralCut': 'u8', 'VetoProposal': 'u32', 'UpdateGlobalNftLimit': (('Daily', 'Weekly'), 'u64'), 'UpdateChannelPayouts': {'commitment': (None, 'scale_info::11'), 'payload': (None, {'object_creation_params': {'size': 'u64', 'ipfs_content_id': 'Bytes'}, 'expected_data_size_fee': 'u128', 'expected_data_object_state_bloat_bond': 'u128'}), 'min_cashout_allowed': (None, 'u128'), 'max_cashout_allowed': (None, 'u128'), 'channel_cashouts_enabled': (None, 'bool')}, 'SetPalletFozenStatus': ('bool', ('ProjectToken',))}```
| None | `ThreadId` | ```u64```

---------
## Storage functions

---------
### ThreadIdByProposalId
 Map proposal id to its discussion thread id

#### Python
```python
result = substrate.query(
    'ProposalsCodex', 'ThreadIdByProposalId', ['u32']
)
```

#### Return value
```python
'u64'
```
---------
## Constants

---------
### AmendConstitutionProposalParameters
 Exports &#x27;Amend Constitution&#x27; proposal parameters.
#### Value
```python
{
    'approval_quorum_percentage': 80,
    'approval_threshold_percentage': 100,
    'constitutionality': 2,
    'grace_period': 14400,
    'required_stake': 16666666666600,
    'slashing_quorum_percentage': 60,
    'slashing_threshold_percentage': 80,
    'voting_period': 72200,
}
```
#### Python
```python
constant = substrate.get_constant('ProposalsCodex', 'AmendConstitutionProposalParameters')
```
---------
### CancelWorkingGroupLeadOpeningProposalParameters
 Exports &#x27;Cancel Working Group Lead Opening&#x27; proposal parameters.
#### Value
```python
{
    'approval_quorum_percentage': 66,
    'approval_threshold_percentage': 66,
    'constitutionality': 1,
    'grace_period': 1200,
    'required_stake': 8333333333300,
    'slashing_quorum_percentage': 100,
    'slashing_threshold_percentage': 100,
    'voting_period': 43200,
}
```
#### Python
```python
constant = substrate.get_constant('ProposalsCodex', 'CancelWorkingGroupLeadOpeningProposalParameters')
```
---------
### CreateWorkingGroupLeadOpeningProposalParameters
 Exports &#x27;Create Working Group Lead Opening&#x27; proposal parameters.
#### Value
```python
{
    'approval_quorum_percentage': 66,
    'approval_threshold_percentage': 66,
    'constitutionality': 1,
    'grace_period': 1200,
    'required_stake': 16666666666600,
    'slashing_quorum_percentage': 100,
    'slashing_threshold_percentage': 100,
    'voting_period': 43200,
}
```
#### Python
```python
constant = substrate.get_constant('ProposalsCodex', 'CreateWorkingGroupLeadOpeningProposalParameters')
```
---------
### DecreaseWorkingGroupLeadStakeProposalParameters
 Exports &#x27;Decrease Working Group Lead Stake&#x27; proposal parameters.
#### Value
```python
{
    'approval_quorum_percentage': 100,
    'approval_threshold_percentage': 100,
    'constitutionality': 1,
    'grace_period': 1200,
    'required_stake': 8333333333300,
    'slashing_quorum_percentage': 100,
    'slashing_threshold_percentage': 100,
    'voting_period': 43200,
}
```
#### Python
```python
constant = substrate.get_constant('ProposalsCodex', 'DecreaseWorkingGroupLeadStakeProposalParameters')
```
---------
### FillWorkingGroupOpeningProposalParameters
 Exports &#x27;Fill Working Group Lead Opening&#x27; proposal parameters.
#### Value
```python
{
    'approval_quorum_percentage': 66,
    'approval_threshold_percentage': 66,
    'constitutionality': 1,
    'grace_period': 1200,
    'required_stake': 8333333333300,
    'slashing_quorum_percentage': 100,
    'slashing_threshold_percentage': 100,
    'voting_period': 43200,
}
```
#### Python
```python
constant = substrate.get_constant('ProposalsCodex', 'FillWorkingGroupOpeningProposalParameters')
```
---------
### FundingRequestProposalMaxAccounts
 Max number of accounts per funding request proposal
#### Value
```python
20
```
#### Python
```python
constant = substrate.get_constant('ProposalsCodex', 'FundingRequestProposalMaxAccounts')
```
---------
### FundingRequestProposalMaxTotalAmount
 Maximum total amount in funding request proposal
#### Value
```python
1666666666660000
```
#### Python
```python
constant = substrate.get_constant('ProposalsCodex', 'FundingRequestProposalMaxTotalAmount')
```
---------
### FundingRequestProposalParameters
 Exports &#x27;Funding Request&#x27; proposal parameters.
#### Value
```python
{
    'approval_quorum_percentage': 66,
    'approval_threshold_percentage': 66,
    'constitutionality': 1,
    'grace_period': 1200,
    'required_stake': 1666666666660,
    'slashing_quorum_percentage': 100,
    'slashing_threshold_percentage': 100,
    'voting_period': 43200,
}
```
#### Python
```python
constant = substrate.get_constant('ProposalsCodex', 'FundingRequestProposalParameters')
```
---------
### RuntimeUpgradeProposalParameters
 Exports &#x27;Runtime Upgrade&#x27; proposal parameters.
#### Value
```python
{
    'approval_quorum_percentage': 100,
    'approval_threshold_percentage': 100,
    'constitutionality': 2,
    'grace_period': 72000,
    'required_stake': 1666666666660000,
    'slashing_quorum_percentage': 100,
    'slashing_threshold_percentage': 100,
    'voting_period': 100800,
}
```
#### Python
```python
constant = substrate.get_constant('ProposalsCodex', 'RuntimeUpgradeProposalParameters')
```
---------
### SetCouncilBudgetIncrementProposalParameters
 Exports `Set Council Budget Increment` proposal parameters.
#### Value
```python
{
    'approval_quorum_percentage': 100,
    'approval_threshold_percentage': 100,
    'constitutionality': 2,
    'grace_period': 72000,
    'required_stake': 333333333332000,
    'slashing_quorum_percentage': 100,
    'slashing_threshold_percentage': 100,
    'voting_period': 72000,
}
```
#### Python
```python
constant = substrate.get_constant('ProposalsCodex', 'SetCouncilBudgetIncrementProposalParameters')
```
---------
### SetCouncilorRewardProposalParameters
 Exports `Set Councilor Reward Proposal Parameters` proposal parameters.
#### Value
```python
{
    'approval_quorum_percentage': 100,
    'approval_threshold_percentage': 100,
    'constitutionality': 2,
    'grace_period': 43200,
    'required_stake': 333333333332000,
    'slashing_quorum_percentage': 100,
    'slashing_threshold_percentage': 100,
    'voting_period': 28800,
}
```
#### Python
```python
constant = substrate.get_constant('ProposalsCodex', 'SetCouncilorRewardProposalParameters')
```
---------
### SetInitialInvitationBalanceProposalParameters
 Exports `Set Initial Invitation Balance` proposal parameters.
#### Value
```python
{
    'approval_quorum_percentage': 66,
    'approval_threshold_percentage': 66,
    'constitutionality': 1,
    'grace_period': 1200,
    'required_stake': 33333333333200,
    'slashing_quorum_percentage': 100,
    'slashing_threshold_percentage': 100,
    'voting_period': 28800,
}
```
#### Python
```python
constant = substrate.get_constant('ProposalsCodex', 'SetInitialInvitationBalanceProposalParameters')
```
---------
### SetInvitationCountProposalParameters
#### Value
```python
{
    'approval_quorum_percentage': 66,
    'approval_threshold_percentage': 66,
    'constitutionality': 1,
    'grace_period': 1200,
    'required_stake': 8333333333300,
    'slashing_quorum_percentage': 100,
    'slashing_threshold_percentage': 100,
    'voting_period': 43200,
}
```
#### Python
```python
constant = substrate.get_constant('ProposalsCodex', 'SetInvitationCountProposalParameters')
```
---------
### SetMaxValidatorCountProposalMaxValidators
 Max allowed number of validators in set max validator count proposal
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('ProposalsCodex', 'SetMaxValidatorCountProposalMaxValidators')
```
---------
### SetMaxValidatorCountProposalParameters
 Exports &#x27;Set Max Validator Count&#x27; proposal parameters.
#### Value
```python
{
    'approval_quorum_percentage': 100,
    'approval_threshold_percentage': 100,
    'constitutionality': 2,
    'grace_period': 72000,
    'required_stake': 1666666666660000,
    'slashing_quorum_percentage': 100,
    'slashing_threshold_percentage': 100,
    'voting_period': 100800,
}
```
#### Python
```python
constant = substrate.get_constant('ProposalsCodex', 'SetMaxValidatorCountProposalParameters')
```
---------
### SetMembershipLeadInvitationQuotaProposalParameters
#### Value
```python
{
    'approval_quorum_percentage': 66,
    'approval_threshold_percentage': 66,
    'constitutionality': 1,
    'grace_period': 1200,
    'required_stake': 8333333333300,
    'slashing_quorum_percentage': 100,
    'slashing_threshold_percentage': 100,
    'voting_period': 43200,
}
```
#### Python
```python
constant = substrate.get_constant('ProposalsCodex', 'SetMembershipLeadInvitationQuotaProposalParameters')
```
---------
### SetMembershipPriceProposalParameters
 Exports &#x27;Set Membership Price&#x27; proposal parameters.
#### Value
```python
{
    'approval_quorum_percentage': 66,
    'approval_threshold_percentage': 66,
    'constitutionality': 1,
    'grace_period': 1200,
    'required_stake': 8333333333300,
    'slashing_quorum_percentage': 100,
    'slashing_threshold_percentage': 100,
    'voting_period': 43200,
}
```
#### Python
```python
constant = substrate.get_constant('ProposalsCodex', 'SetMembershipPriceProposalParameters')
```
---------
### SetPalletFozenStatusProposalParameters
#### Value
```python
{
    'approval_quorum_percentage': 66,
    'approval_threshold_percentage': 66,
    'constitutionality': 1,
    'grace_period': 0,
    'required_stake': 8333333333300,
    'slashing_quorum_percentage': 100,
    'slashing_threshold_percentage': 100,
    'voting_period': 43200,
}
```
#### Python
```python
constant = substrate.get_constant('ProposalsCodex', 'SetPalletFozenStatusProposalParameters')
```
---------
### SetReferralCutProposalParameters
#### Value
```python
{
    'approval_quorum_percentage': 66,
    'approval_threshold_percentage': 66,
    'constitutionality': 1,
    'grace_period': 1200,
    'required_stake': 8333333333300,
    'slashing_quorum_percentage': 100,
    'slashing_threshold_percentage': 100,
    'voting_period': 43200,
}
```
#### Python
```python
constant = substrate.get_constant('ProposalsCodex', 'SetReferralCutProposalParameters')
```
---------
### SetWorkingGroupLeadRewardProposalParameters
 Exports &#x27;Set Working Group Lead Reward&#x27; proposal parameters.
#### Value
```python
{
    'approval_quorum_percentage': 66,
    'approval_threshold_percentage': 66,
    'constitutionality': 1,
    'grace_period': 1200,
    'required_stake': 8333333333300,
    'slashing_quorum_percentage': 100,
    'slashing_threshold_percentage': 100,
    'voting_period': 43200,
}
```
#### Python
```python
constant = substrate.get_constant('ProposalsCodex', 'SetWorkingGroupLeadRewardProposalParameters')
```
---------
### SignalProposalParameters
 Exports &#x27;Signal&#x27; proposal parameters.
#### Value
```python
{
    'approval_quorum_percentage': 100,
    'approval_threshold_percentage': 100,
    'constitutionality': 1,
    'grace_period': 1200,
    'required_stake': 166666666666000,
    'slashing_quorum_percentage': 100,
    'slashing_threshold_percentage': 100,
    'voting_period': 43200,
}
```
#### Python
```python
constant = substrate.get_constant('ProposalsCodex', 'SignalProposalParameters')
```
---------
### SlashWorkingGroupLeadProposalParameters
 Exports &#x27;Slash Working Group Lead&#x27; proposal parameters.
#### Value
```python
{
    'approval_quorum_percentage': 66,
    'approval_threshold_percentage': 66,
    'constitutionality': 1,
    'grace_period': 1200,
    'required_stake': 8333333333300,
    'slashing_quorum_percentage': 100,
    'slashing_threshold_percentage': 100,
    'voting_period': 43200,
}
```
#### Python
```python
constant = substrate.get_constant('ProposalsCodex', 'SlashWorkingGroupLeadProposalParameters')
```
---------
### TerminateWorkingGroupLeadProposalParameters
 Exports &#x27;Terminate Working Group Lead&#x27; proposal parameters.
#### Value
```python
{
    'approval_quorum_percentage': 66,
    'approval_threshold_percentage': 66,
    'constitutionality': 1,
    'grace_period': 1200,
    'required_stake': 8333333333300,
    'slashing_quorum_percentage': 100,
    'slashing_threshold_percentage': 100,
    'voting_period': 43200,
}
```
#### Python
```python
constant = substrate.get_constant('ProposalsCodex', 'TerminateWorkingGroupLeadProposalParameters')
```
---------
### UpdateChannelPayoutsProposalParameters
#### Value
```python
{
    'approval_quorum_percentage': 66,
    'approval_threshold_percentage': 100,
    'constitutionality': 1,
    'grace_period': 14400,
    'required_stake': 16666666666600,
    'slashing_quorum_percentage': 100,
    'slashing_threshold_percentage': 100,
    'voting_period': 100800,
}
```
#### Python
```python
constant = substrate.get_constant('ProposalsCodex', 'UpdateChannelPayoutsProposalParameters')
```
---------
### UpdateGlobalNftLimitProposalParameters
#### Value
```python
{
    'approval_quorum_percentage': 66,
    'approval_threshold_percentage': 66,
    'constitutionality': 1,
    'grace_period': 1200,
    'required_stake': 16666666666600,
    'slashing_quorum_percentage': 100,
    'slashing_threshold_percentage': 100,
    'voting_period': 28800,
}
```
#### Python
```python
constant = substrate.get_constant('ProposalsCodex', 'UpdateGlobalNftLimitProposalParameters')
```
---------
### UpdateWorkingGroupBudgetProposalParameters
 Exports &#x27;Update Working Group Budget&#x27; proposal parameters.
#### Value
```python
{
    'approval_quorum_percentage': 66,
    'approval_threshold_percentage': 66,
    'constitutionality': 1,
    'grace_period': 1200,
    'required_stake': 8333333333300,
    'slashing_quorum_percentage': 100,
    'slashing_threshold_percentage': 100,
    'voting_period': 43200,
}
```
#### Python
```python
constant = substrate.get_constant('ProposalsCodex', 'UpdateWorkingGroupBudgetProposalParameters')
```
---------
### VetoProposalProposalParameters
#### Value
```python
{
    'approval_quorum_percentage': 100,
    'approval_threshold_percentage': 100,
    'constitutionality': 1,
    'grace_period': 0,
    'required_stake': 166666666666000,
    'slashing_quorum_percentage': 100,
    'slashing_threshold_percentage': 100,
    'voting_period': 14400,
}
```
#### Python
```python
constant = substrate.get_constant('ProposalsCodex', 'VetoProposalProposalParameters')
```
---------
## Errors

---------
### ArithmeticError
Arithmeic Error

---------
### DecreasingStakeIsZero
Invalid &\#x27;decrease stake proposal&\#x27; parameter - cannot decrease by zero balance.

---------
### InsufficientFundsForBudgetUpdate
Insufficient funds for &\#x27;Update Working Group Budget&\#x27; proposal execution

---------
### InvalidChannelPayoutsProposalMinCashoutExceedsMaxCashout
The specified min channel cashout is greater than the specified max channel cashout in `Update Channel Payouts` proposal.

---------
### InvalidCouncilElectionParameterAnnouncingPeriod
Invalid council election parameter - announcing_period

---------
### InvalidCouncilElectionParameterCandidacyLimit
Invalid council election parameter - candidacy-limit

---------
### InvalidCouncilElectionParameterCouncilSize
Invalid council election parameter - council_size

---------
### InvalidCouncilElectionParameterMinCouncilStake
Invalid council election parameter - min_council_stake

---------
### InvalidCouncilElectionParameterMinVotingStake
Invalid council election parameter - min-voting_stake

---------
### InvalidCouncilElectionParameterNewTermDuration
Invalid council election parameter - new_term_duration

---------
### InvalidCouncilElectionParameterRevealingPeriod
Invalid council election parameter - revealing_period

---------
### InvalidCouncilElectionParameterVotingPeriod
Invalid council election parameter - voting_period

---------
### InvalidFundingRequestProposalBalance
Invalid balance value for the spending proposal

---------
### InvalidFundingRequestProposalNumberOfAccount
Invalid number of accounts recieving funding request for &\#x27;Funding Request&\#x27; proposal.

---------
### InvalidFundingRequestProposalRepeatedAccount
Repeated account in &\#x27;Funding Request&\#x27; proposal.

---------
### InvalidLeadApplicationId
Provided lead application id is not valid

---------
### InvalidLeadOpeningId
Provided lead opening id is not valid

---------
### InvalidLeadWorkerId
Provided lead worker id is not valid

---------
### InvalidProposalId
Provided proposal id is not valid

---------
### InvalidSetLeadParameterCannotBeCouncilor
Invalid &\#x27;set lead proposal&\#x27; parameter - proposed lead cannot be a councilor

---------
### InvalidValidatorCount
Invalid validator count for the &\#x27;set validator count&\#x27; proposal

---------
### InvalidWorkingGroupBudgetCapacity
Invalid working group budget capacity parameter

---------
### RequireRootOrigin
Require root origin in extrinsics

---------
### RuntimeProposalIsEmpty
Provided WASM code for the runtime upgrade proposal is empty

---------
### SignalProposalIsEmpty
Provided text for text proposal is empty

---------
### SlashingStakeIsZero
Invalid &\#x27;slash stake proposal&\#x27; parameter - cannot slash by zero balance.

---------