#
# Script to take user details and store in file details.out 
#

echo -n Enter Name:             #Ask user to enter name
read name                       #Take input name from user
echo Name: $name > details.out  #Redirect name to details.out

echo -n Enter Address:                  #Ask user to enter address
read address                            #Take input address from user
echo Address: $address >> details.out   #Redirect address to details.out

echo -n Enter phone number:                  #Ask user to enter phone number
read phone                                  #Take input phone from user
echo Phone Number: $phone >> details.out    #Redirect phone to details.out

echo "details stored inside \"details.out\""