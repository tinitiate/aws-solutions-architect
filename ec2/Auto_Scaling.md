# Auto Scaling 

## Vertical Scaling 

- Vertical Scaling means upgrading the current resource.
- For Example upgrading the instance to higher instance type.

## Horizontal Scaling 

- Horizontal Scaling means adding more resources.
- For Example adding more instances.

![Scaling](/ec2/images/Scaling.PNG)

## AWS Auto Scaling

- EC2 Auto Scaling helps you ensure that you have the correct number of Amazon EC2 instances available to handle the load for your application. 
- We create collections of EC2 instances, called **Auto Scaling groups**.
- We can specify the minimum number of instances in each Auto Scaling group, and Amazon EC2 Auto Scaling ensures that your group never goes below this size. 
-  If we specify the desired capacity, either when you create the group or at any time thereafter, Amazon EC2 Auto Scaling ensures that your group has this many instances. 
- If we specify scaling policies, then Amazon EC2 Auto Scaling can launch or terminate instances as demand on your application increases or decreases.

![as-basic-diagram](/ec2/images/as-basic-diagram.png)

## Auto Scaling components

### **Groups**

Your EC2 instances are organized into *groups* so that they are treated as a logical unit for scaling and management. When you create a group, you can specify its minimum, maximum, and desired number of EC2 instances.

### Configuration templates

Your group uses a *launch template or launch configuration (fewer features)* as a template for its EC2 instances. When you create a launch template, you can specify information such as the AMI ID, instance type, key pair, security groups, and block device mapping for your instances.

### **Scaling options**

Amazon EC2 Auto Scaling provides several ways for you to scale your Auto Scaling groups. For example, you can configure a group to scale based on the occurrence of specified conditions (dynamic scaling) or on a schedule. 

- Scale to maintain current instance levels at all times
- Manual Scaling
- Scale based on a schedule
- Scale based on a demand
- Use predictive scaling

## Auto Scaling instance lifecycle

- The EC2 instances in an Auto Scaling group have a path, or lifecycle, that differs from that of other EC2 instances.

- The lifecycle starts when the Auto Scaling group launches an instance and puts it into service. 

- The lifecycle ends when you terminate the instance, or the Auto Scaling group takes the instance out of service and terminates it.

  

![auto_scaling_lifecycle](/ec2/images/auto_scaling_lifecycle.png)



### Scaling Policy Types

- **Target tracking scaling**—Increase or decrease the current capacity of the group based on a target value for a specific metric.
- **Step scaling**—Increase or decrease the current capacity of the group based on a set of scaling adjustments, known as step adjustments, that vary based on the size of the alarm breach.
- **Simple scaling**—Increase or decrease the current capacity of the group based on a single scaling adjustment.

- The size of your Auto Scaling group is restricted by *capacity limits*, which can be resized between the minimum and maximum size limits.

- The 

  cooldown period

   is a configurable setting that helps ensure to not launch or terminate additional instances before previous scaling activities take effect.

  - EC2 Auto Scaling supports cooldown periods when using simple scaling policies, but not when using target tracking policies, step scaling policies, or scheduled scaling.

- You can use the **default instance** **warmup** to improve CloudWatch metrics used for dynamic scaling. This feature lets your EC2 instances finish warming up before they contribute the usage data.

- Dynamic scaling can better react to the demand curve of your application if you utilize a target tracking scaling policy based on a custom Amazon SQS queue metric.

- Amazon EC2 Auto Scaling marks an instance as unhealthy if the instance is in a state other than *running*, the system status is *impaired*, or Elastic Load Balancing reports that the instance failed the health checks.

- Termination of Instances

  - When you configure automatic scale in, you must decide which instances should terminate first and set up a **termination policy**. You can also use **instance protection** to prevent specific instances from being terminated during automatic scale in.
  - Default Termination Policy

![TerminationPolicy](/ec2/images/TerminationPolicy.png)

- **Custom Termination Policies**
  - *OldestInstance* – Terminate the oldest instance in the group.
  - *NewestInstance* – Terminate the newest instance in the group.
  - *OldestLaunchConfiguration* – Terminate instances that have the oldest launch configuration.
  - *ClosestToNextInstanceHour* – Terminate instances that are closest to the next billing hour.
- An instance can be temporarily removed from an Auto Scaling group by changing its state from *InService* into *Standby.*
- You can create **launch templates** that specifies instance configuration information when you launch EC2 instances, and allows you to have multiple versions of a template.
- A launch configuration is an instance configuration template that an Auto Scaling group uses to launch EC2 instances, and you specify information for the instances.
  - You can specify your launch configuration with multiple Auto Scaling groups.
  - You can only specify one launch configuration for an Auto Scaling group at a time, and you can’t modify a launch configuration after you’ve created it.
  - When you create a VPC, by default its tenancy attribute is set to *default*. You can launch instances with a tenancy value of *dedicated* so that they run as single-tenancy instances. Otherwise, they run as shared-tenancy instances by default.
  - If you set the tenancy attribute of a VPC to *dedicated*, all instances launched in the VPC run as single-tenancy instances.
  - When you create a launch configuration, the default value for the instance placement tenancy is *null* and the instance tenancy is controlled by the tenancy attribute of the VPC.
