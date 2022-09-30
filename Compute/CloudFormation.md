# AWS CloudFormation
- AWS CloudFormation gives developers and businesses an easy way to create a collection of related AWS resources 
  and provision them.
- CloudFormation allows you to model your entire infrastructure in a text file called a **template**.
- We can use JSON or YAML to describe what AWS resources we want to create and configure.
- We can design the teplate visually using AWS CloudFormation Designer.
- CloudFormation automates the provisioning and updating of the infrastructure. 
- We can use Rollback Triggers to specify the CloudWatch alarm that CloudFormation should monitor during the stack creation and update process.
- CloudFormation Change Sets allow you to preview how proposed changes to a stack might impact your running resources.
- AWS StackSets lets you provision a common set of AWS resources across multiple accounts and regions with a single CloudFormation template. 
- CloudFormation registry helps you discover and provision private and public extensions such as resources, modules, 
  and hooks in your AWS CloudFormation templates.
- **Templates**
  - A JSON or YAML formatted text file.
  - CloudFormation uses these templates as blueprints for building your AWS resources.

- **Stacks**
  - Manage related resources as a single unit.
  - All the resources in a stack are defined by the stack’s CloudFormation template.
  - If a resource cannot be created, CloudFormation rolls the stack back and automatically deletes any resources that were created. 

- **Change Sets**
  - Before updating your stack and making changes to your resources, you can generate a change set, which is a summary of your proposed changes.
  - Change sets allow you to see how your changes might impact your running resources, especially for critical resources, before implementing them.
  
## **Stacks**

- Stack update methods:
  - Direct update
  - Creating and executing change sets
- When you update a stack, CloudFormation will only update resources that have been modified in the current stack template.
- **Drift detection** enables us to detect whether a stack’s actual configuration differs, or has drifted, from its expected configuration.
  - A resource is considered to have drifted if any if its actual property values differ from the expected property values.
  - A stack is considered to have drifted if one or more of its resources have drifted.
- To share information between stacks, export a stack’s output values. Other stacks that are in the same AWS account and region can import the exported values.
- You can nest stacks and create Microsoft Windows stacks.
- Using resource import, you can import or manage AWS resources that are created outside CloudFormation. 
- You can also move resources between stacks by adding a *Retain* deletion policy.
- Stack failure options allows you to troubleshoot resources in a *CREATE_FAILED* or *UPDATE_FAILED* status without rolling back successfully provisioned resources.

## **Templates**

- Templates include several major sections. The Resources section is the only required section.
- **CloudFormation Designer** is a graphic tool for creating, viewing, and modifying CloudFormation templates.
- Custom resources enable you to write custom provisioning logic in templates that CloudFormation runs anytime you create, update , or delete stacks.
- Modules are building blocks that can be reused across different CloudFormation templates.
- You can use regular expressions when creating a template parameter.
- You can use CloudFormation to perform ECS blue/green deployments via AWS CodeDeploy.

## **StackSets**
- CloudFormation StackSets allow you to roll out CloudFormation stacks over multiple AWS accounts and in multiple Regions.
- StackSets is commonly used together with AWS Organizations to centrally deploy and manage services in different accounts.
- Stack sets – A *stack set* lets you create stacks in AWS accounts across regions by using a single CloudFormation template.
- A stack set is a regional resource.
- Stack instances – A *stack instance* is a reference to a stack in a target account within a region. A stack instance can exist without a stack; 
  for example, if the stack could not be created for some reason, the stack instance shows the reason for stack creation failure. 
  A stack instance can be associated with only one stack set.
- Stack set operations – Create stack set, update stack set, delete stacks, and delete stack set.
- Stack set operations options – Maximum concurrent accounts, failure tolerance, retain stacks, and region concurrency.
- For stack set operations and stack instances, StackSets generates status codes.
- You can also perform drift detection on a stack set to determine if any of the stack instances have drifted.
- Stack import operations:
  - Self-managed StackSets – Stacks can be imported into the administrator account or into other target accounts and AWS Regions.
  - Service-managed StackSets – Any stack in the same AWS Organizations as the management account can be imported.
  
## CloudFormation vs Elastic Beanstalk
- Elastic Beanstalk provides an environment to easily deploy and run applications in the cloud.
- CloudFormation is a convenient provisioning mechanism for a broad range of AWS resources.

