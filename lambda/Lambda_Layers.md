# Creating Lambda Layer

1. Sign in to the AWS Management Console and and navigate to the ` AWS CloudShell`.

   ![](/lambda/images/layers/cloud_shell.png)

2. Wait for `AWS CloudShell` to start. This may take a few moments.

  ![](/lambda/images/layers/cloud_shell_2.png)

3. Once `AWS CloudShell` is ready, you will see a shell prompt in the console. 

   ![](/lambda/images/layers/cloud_shell_3.png)

4. Make sure the python version on the `AWS CloudShell` matches the version of the `Runtime` of the Lambda Function.

   ![](/lambda/images/layers/cloud_shell_4.png)

   ```bash
   python3 --version
   ```

   

5. Create a working directory for creating the layers (one each for each layer ) .

   ![](/lambda/images/layers/cloud_shell_5.png)

   ```bash
   mkdir ~/cx_oracle
   ```

6. Change the current directory to `~/cx_oracle`

   ![](/lambda/images/layers/cloud_shell_6.png)

   ```bash
   cd ~/cx_oracle
   ```

6. Create the `python` and `lib` folders which are required for a Python Layer.

   ![](/lambda/images/layers/cloud_shell_7.png)

   ```bash
   mkdir python/ lib/
   ```

7. Install the `cx_Oracle` module using `pip` under `python` directory. 

   ![](/lambda/images/layers/cloud_shell_8.png)

   ```bash
   pip3 install cx_Oracle -t python/ 
   ```

8. Download the latest version of `Oracle Client` libraries.

  ![](/lambda/images/layers/cloud_shell_9.png)

   ```bash
   wget https://download.oracle.com/otn_software/linux/instantclient/193000/instantclient-basic-linux.x64-19.3.0.0.0dbru.zip -O oracle.zip
   ```

9. Unzip the libraries and extract the contents to the `lib` directory 

  ![](/lambda/images/layers/cloud_shell_10.png)

   ```bash
   unzip -j oracle.zip -d lib/
   ```

10. Create a ZIP archive with `python` and `lib` folders.

   ![](/lambda/images/layers/cloud_shell_11.png)

    ```bash
    zip -r -y cx_Oracle.zip python/ lib/
    ```

11. Copy the Zip file created in the `Step 10`  to an Amazon S3 bucket.

    ![](/lambda/images/layers/cloud_shell_12.png)

    ```bash
    aws s3 cp layer.zip s3://sbp-app-object/lambda_layers/cx_oracle.zip --region us-east-1
    ```

​		

> **_Note_** Please follow the steps 1 through 8 and 11 through 12 mentioned earlier, but this time replace `cx_Oracle` with the corresponding library name `pandas` and `psycopg2`. This will ensure that we install the pandas and psycopg2 layers and use them in your Python code.
