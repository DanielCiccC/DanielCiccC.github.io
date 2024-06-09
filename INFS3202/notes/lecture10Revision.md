# Lecture 10 Revision

### Concepts and Definitions


**Amazon EC2 (Elastic Compute Cloud)** Amazon EC2 provides scalable computing capacity in the AWS cloud. Using EC2, you can launch virtual servers, configure security and networking, and manage storage. EC2 enables you to scale up or down to handle changes in requirements or spikes in popularity, reducing your need to invest in hardware up front.

**Amazon Machine Image (AMI)** An AMI is a template that contains the software configuration (operating system, application server, and applications) required to launch your instance. You can select an AMI provided by AWS, the user community, or you can create your own AMIs. When you launch an instance, you select an AMI to use as the template for the instance. You can launch multiple instances from a single AMI when you need multiple instances with the same configuration.

**Virtual Private Cloud (VPC)** A VPC is a virtual network dedicated to your AWS account. It is logically isolated from other virtual networks in the AWS Cloud. You can define and control a virtual network space in which you can launch AWS resources in a virtual network that you define. This virtual networking environment includes IP address ranges, subnets, route tables, network gateways, and security settings.

**Security Groups** A security group acts as a virtual firewall that controls the traffic for one or more EC2 instances. When you launch an instance, you can associate one or more security groups with the instance. You can add rules to each security group that allow traffic to or from its associated instances. You can modify the rules for a security group at any time; the new rules are automatically applied to all instances associated with the security group.

**Subnets** A subnet is a range of IP addresses in your VPC. You can launch AWS resources into a specified subnet. Use a public subnet for resources that must be connected to the internet, and a private subnet for resources that won’t be connected to the internet. To protect the AWS resources in each subnet, you can use multiple layers of security, including security groups and network access control lists (ACL).