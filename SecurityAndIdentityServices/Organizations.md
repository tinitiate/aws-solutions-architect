# AWS Organizations
- AWS Organizations is an account management service that enables you to consolidate multiple AWS accounts into an organization 
  that you create and centrally manage. 
- AWS Organizations includes account management and consolidated billing capabilities.
- We can create groups of accounts and then apply policies to those groups.
- Organizations provides you a policy framework for multiple AWS accounts. 
- AWS Organizations, like many other AWS services, is eventually consistent. 
- It achieves high availability by replicating data across multiple servers in AWS data centers within its region.
- You can remove an AWS account from an organization and make it into a standalone account.

## Organization Hierarchy
- Including root and AWS accounts created in the lowest OUs, your hierarchy can be five levels deep.
- Policies inherited through hierarchical connections in an organization.
- Policies can be assigned at different points in the hierarchy.

## Administrative Actions in Organizations
- Create an AWS account and add it to your organization, or add an existing AWS account to your organization.
- Organize your AWS accounts into groups called organizational units (OUs).
- Organize your OUs into a hierarchy that reflects your company’s structure.
- Centrally manage and attach policies to the entire organization, OUs, or individual AWS accounts.

## Concepts
### Management account 
- Is the AWS account you use to create your organization. 
- Cannot change which account in your organization is the management account.
- From the management account, you can create other accounts in your organization, invite and manage invitations for other accounts 
    to join your organization, and remove accounts from your organization.
- You can also attach policies to entities such as administrative roots, organizational units (OUs), or accounts within your organization.
- The management account has the role of a payer account and is responsible for paying all charges accrued by the accounts in its organization.
- The management account has the responsibilities of a payer account and is responsible for paying all charges that are accrued by the member accounts.
  
### Member account 
- Is an AWS account, other than the management account, that is part of an organization. 
- Member account can belong to only one organization at a time.
- You can attach a policy to an account to apply controls to only that one account.

### Administrative Root
- The parent container for all the accounts for your organization. 
- If you apply a policy to the root, it applies to all organizational units (OUs) and accounts in the organization.

### Organizational unit (OU)
- A container for accounts within a root.
- An OU also can contain other OUs, enabling you to create a hierarchy that resembles an upside-down tree, 
  with a root at the top and branches of OUs that reach down, ending in accounts that are the leaves of the tree. 
  
### Policy 
-  Policy is a “document” with one or more statements that define the controls that you want to apply to a group of AWS accounts.
-  Service control policy (SCP)
  -  Is a policy that specifies the services and actions that users and roles can use in the accounts that the SCP affects. 
  -  SCPs are similar to IAM permission policies except that they don’t grant any permissions. 
  -  Instead, SCPs are filters that allow only the specified services and actions to be used in affected accounts.

![AccountOuDiagram](/SecurityAndIdentityServices/images/AccountOuDiagram.png)
