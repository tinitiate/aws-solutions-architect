# Lambda Function Creation

1. Open the AWS Management Console and navigate to the Lambda service.

  ![](C:\Users\sriat\OneDrive\Desktop\chc\Lambda\lambda\Lambda-1.png)

  

2. Click on the "Create function" button.

3. Select `Author from scratch`.

4. Enter the `Function Name` `sbp-aws-ora-dblink-data-load-to-s3`.

5. Select the `Runtime`  **"Python 3.7"**

6. Select `x86_64` as the Architecture.

  ![](C:\Users\sriat\OneDrive\Desktop\chc\Lambda\Lambda\Lambda-2.png)

7. Under "**Change default execution role**", select " Use an existing role".

   ![](C:\Users\sriat\OneDrive\Desktop\chc\Lambda\Lambda\Lambda-3.png)

8. In the drop down select this role`tg_ora_db_link-role-4gnl75db `

   ![](C:\Users\sriat\OneDrive\Desktop\chc\Lambda\Lambda\Lambda-4.png)

9. If the Function is not accessing any resources inside the **"VPC"** click on the **Create Function**.

   ![](C:\Users\sriat\OneDrive\Desktop\chc\Lambda\Lambda\Create-function-Lambda.png)

10. If the Function is accessing any resources inside the **"VPC"** please continue with the steps before selecting **Create Function**.

11. Under "Advanced Settings", select "Enable VPC".

    ![](C:\Users\sriat\OneDrive\Desktop\chc\Lambda\Lambda\Lambda-vpc.png)

12. In the drop down select this **VPC** **"vpc-0421d97f"**.

    ![](C:\Users\sriat\OneDrive\Desktop\chc\Lambda\Lambda\Lambda-vpc-2.png)

13. After Selecting the VPC, dropdowns for "**Subnets**"  and "**Security groups**" will appear.

    ![](C:\Users\sriat\OneDrive\Desktop\chc\Lambda\Lambda\Lambda-vpc-3.png)

14. In the drop down for **Subnets** select this **Subnet** **"subnet-cc0bdb90"**.

    ![](C:\Users\sriat\OneDrive\Desktop\chc\Lambda\Lambda\Lambda-vpc-4.png)

15. In the drop down **Security groups** select this **Security group** **"sg-37384340"**.

    ![](C:\Users\sriat\OneDrive\Desktop\chc\Lambda\Lambda\Lambda-vpc-5.png)

16. Once all steps 11 through 15 are done click on the **'Create Function'**.

    ![](C:\Users\sriat\OneDrive\Desktop\chc\Lambda\Lambda\Create-function-Lambda-vpc.png)