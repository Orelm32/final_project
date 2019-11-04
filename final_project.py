import boto3
from time import sleep
import os

yeslist = ["yes", "Yes", "YES", "y"]
nolist = ["no", "No", "NO", "n"]
ec2 = boto3.resource('ec2')
boolean = 0
while boolean == 0:
    print("""Menu:
    1.Deploy EC2 machines
    2.Describe EC2
    3.Deploy VM with all conf & installation
    4.Deploy containers & check it
    5.Installation &  conf of nagios
    6.Montoring - Environments
    7.Install J-M + S on containers
    8.Push all jobs to Github
    9.Pull all jobs from Github""")
    answer = input("    please choose one of the above:\n")
    if answer == "1":
        instance_type = input("Which instance type would you like to install?\n(t2.micro is for free tier)\n")
        instance_os = input(
            "Please choose Operation System you wish to install:\n1. Ubuntu 18.04\n2. Your own AMI(if you have one)\n")
        if instance_os == "1":
            instance_num = input("Please choose the number of instances that you would like to install:\n")
            print("""Select an existing key pair or create a new key pair:
	            1. Choose an existing key pair
	            2. Create a new key pair
	            3. Proceed without a key pair""")
            key_choose = input("What do you want to do?\n")
            if key_choose is "1":
                instance_key = raw_input("Please type in the key file name (.pem file):\n")
                print("Creating instances...\n")
                instances = ec2.create_instances(
                    ImageId='ami-026d0c119070c9849',
                    MinCount=1,
                    MaxCount=int(instance_num),
                    InstanceType=instance_type,
                    KeyName=instance_key
                )
                print("Done!")
                sleep(1)
                a = 0
                while a == 0:
                    back = input("Do you want to go back to the main menu?\n")
                    if back == "yes" or back == "Yes" or back == "YES":
                        print("Going back...")
                        sleep(1)
                        a = 1
                    elif back == "no" or back == "No" or back == "NO":
                        print("that`s ok!")
                        a = 1
                        boolean = 1
                    else:
                        print("Please choose yes or no")
                        sleep(1)

            elif key_choose is "2":
                instance_key = raw_input("Please choose a key name:\n")
                keypairlog = ec2.create_key_pair(KeyName=instance_key)
                keyfile = instance_key + ".txt"
                with open(keyfile, 'w+') as file:
                    file.write(repr(keypairlog))
                print("keypair created, launching the instance..")
                instances = ec2.create_instances(
                    ImageId='ami-026d0c119070c9849',
                    MinCount=1,
                    MaxCount=int(instance_num),
                    InstanceType=instance_type,
                    KeyName=instance_key
                )
                print("Done")
                a = 0
                while a == 0:
                    back = input("Do you want to go back to the main menu?\n")
                    if back == "yes" or back == "Yes" or back == "YES":
                        print("Going back...")
                        sleep(1)
                        a = 1
                    elif back == "no" or back == "No" or back == "NO":
                        print("that`s ok!")
                        a = 1
                        boolean = 1
                    else:
                        print("Please choose yes or no")
                        sleep(1)
            elif key_choose is "3":
                print("Creating instances...\n")
                instances = ec2.create_instances(
                    ImageId='ami-026d0c119070c9849',
                    MinCount=1,
                    MaxCount=int(instance_num),
                    InstanceType=instance_type
                )
                print("Done")
                a = 0
                while a == 0:
                    back = input("Do you want to go back to the main menu?\n")
                    if back == "yes" or back == "Yes" or back == "YES":
                        print("Going back...")
                        sleep(1)
                        a = 1
                    elif back == "no" or back == "No" or back == "NO":
                        print("that`s ok!")
                        a = 1
                        boolean = 1
                    else:
                        print("Please choose yes or no")
                        sleep(1)
        elif instance_os == "2":
            ami = input("What is your AMI?\n")
            instance_num = input("Please choose the number of instances that you would like to install:\n")
            print("""Select an existing key pair or create a new key pair:
            1. Choose an existing key pair
            2. Create a new key pair
            3. Proceed without a key pair""")
            key_choose = input("What do you want to do?\n")
            if key_choose is "1":
                instance_key = input("Please type in the key file name (.pem file):\n")
                print("Creating instances...\n")
                instances = ec2.create_instances(
                    ImageId=ami,
                    MinCount=1,
                    MaxCount=int(instance_num),
                    InstanceType=instance_type,
                    KeyName=instance_key
                )
                print("Done")
                a = 0
                while a == 0:
                    back = input("Do you want to go back to the main menu?\n")
                    if back == "yes" or back == "Yes" or back == "YES":
                        print("Going back...")
                        sleep(1)
                        a = 1
                    elif back == "no" or back == "No" or back == "NO":
                        print("that`s ok!")
                        a = 1
                        boolean = 1
                    else:
                        print("Please choose yes or no")
                        sleep(1)

            elif key_choose is "2":
                instance_key = input("Please choose a key name:\n")
                keypairlog = ec2.create_key_pair(KeyName=instance_key)
                keyfile = instance_key + ".txt"
                with open(keyfile, 'w+') as file:
                    file.write(repr(keypairlog))
                print("keypair created, launching the instance..")
                instances = ec2.create_instances(
                    ImageId=ami,
                    MinCount=1,
                    MaxCount=int(instance_num),
                    InstanceType=instance_type,
                    KeyName=instance_key
                )
                a = 0
                while a == 0:
                    back = input("Do you want to go back to the main menu?\n")
                    if back == "yes" or back == "Yes" or back == "YES":
                        print("Going back...")
                        sleep(1)
                        a = 1
                    elif back == "no" or back == "No" or back == "NO":
                        print("that`s ok!")
                        a = 1
                        boolean = 1
                    else:
                        print("Please choose yes or no")
                        sleep(1)
            elif key_choose is "3":
                print("Creating instances...\n")
                instances = ec2.create_instances(
                    ImageId=ami,
                    MinCount=1,
                    MaxCount=int(instance_num),
                    InstanceType=instance_type
                )
                print("Done")
                a = 0
                while a == 0:
                    back = input("Do you want to go back to the main menu?\n")
                    if back == "yes" or back == "Yes" or back == "YES":
                        print("Going back...")
                        sleep(1)
                        a = 1
                    elif back == "no" or back == "No" or back == "NO":
                        print("that`s ok!")
                        a = 1
                        boolean = 1
                    else:
                        print("Please choose yes or no")
                        sleep(1)




    elif answer == "2":
        print("Getting all instances information...\n")
        sleep(2)
        for instance in ec2.instances.all():
            print(
                "Id: {0}\nPlatform: {1}\nType: {2}\nPublic IPv4: {3}\nAMI: {4}\nState: {5}\n".format(
                    instance.id, instance.platform, instance.instance_type, instance.public_ip_address,
                    instance.image.id, instance.state
                )
            )
        a = 0
        while a == 0:
            back = input("Do you want to go back to the main menu?\n")
            if back == "yes" or back == "Yes" or back == "YES":
                print("Going back...")
                sleep(1)
                a = 1
            elif back == "no" or back == "No" or back == "NO":
                print("that`s ok!")
                a = 1
                boolean = 1
            else:
                print("Please choose yes or no")
                sleep(1)

    elif answer == "3":
        ip = input("Type your IP address: \n")
        passwd = input("Type your root password:\n")
        pack = input("packges:\n1. Nginx\n2. Net-Tools\n3. Jenkins\n4. SSH\n5. iPerf\n")
        os.system(sshpass - p $passwd
        ssh
        root @$ip )
