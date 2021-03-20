#!/bin/bash

# Ethan Ruiz
echo -e "Welcome to the IPTABLE program"

# This function is the menu for checking the status and service options
# NO rules are added here. That is the function after ipstatus()
ipStatus()
{
  option=1
  while [ $choice!=6 ]
      do
        clear
    echo -e "1. Save Rule
      2. Start IPTABLE service
      3. Stop IPTABLE service
      4. Restart service
      5. Flush IPTABLES - Remove ALL RULES
      6. Go back to Main Menu
    "
    read choice "Please Choose an Option > "
      clear
    case $choice in
      1) echo -e "Saving Rule.... \n"
          /sbin/xtables-multi iptables-save
            echo -e "Press Enter to Continue..."
         read tempchoice;;
      2) echo -e "Starting IPTABLES..."
              /etc/init.d/ufw start
          read tempchoice;;
      3) echo -e "Stoping IPTABLE Service... \n"
              /etc/init.d/ufw stop
          read tempchoice;;
      4) echo -e "Restarting IPTABLE service... \n"
              /etc/init.d/ufw restart
          read tempchoice;;
      5) echo -e "Flushing IPTABLES \n"
        iptables -F
        read tempchoice;;
      6) main;;
      *) echo -e "ERROR WRONG OPTION INPUT"
esac
done
}

configure(){
  #This function configures the firewall by adding rules and protocols
#Chain
  echo -e "What Chain do we use?
            1.INPUT
            2.OUTPUT
            3.FORWARD"
            read chain_option
            case $chain_option in
              1) chain="INPUT";;
              2) chain="OUTPUT";;
              3) chain="FORWARD";;
              *) echo -e "WRONT INPUT"
            esac


  #Source IP
  echo -e "1. Firewall using SINGLE Source IP
           2. Firewall using Source Subnet
           3. Firewall using for ALL Source Networks"
      read ip_option
  case $ip_option in
    1) echo -e "Enter IP Adress of SOURCE \n"
        read source_ip;;
    2) echo -e "Enter The SOURCE Subnet (ie 192.168.10.0/24)"
        read source_ip;;
    3) source_ip="0/0";;
    *) echo -e "WRONG INPUT"
  esac

#Destination IP

  echo -e "\n1.Firewall using Single Destination IP\n
           2. Firewall using Destination Subnet\n
           3. Firewall using for All Destination Networks\n"
          read ip_option
            case $ip_option in
              1) echo -e "\n Enter IP Adress of DESTINATION"
                    read dest_ip;;
              2) echo -e "\nEnter the Destination Subnet (ie 192.168.10.0/24)"
                    read dest_ip;;
              3) dest_ip="0/0";;
              *) echo -e "WRONG INPUT"
            esac

#Protocol
  echo -e "1. Block All Traffic of TCP \n
           2. Block Specific TCP Service\n
           3. Block Specific Port \n
           4. Using NO Protocol"
        read prot_option
        case $prot_option in
          1) proto=TCP;;
          2) echo -e "Enter the TCP Service Name: USE CAPS!!"
                read proto;;
          3) echo -e "Etner the Port Name: USE CAPS!!"
              read proto;;
          4) proto="NULL";;
          *) echo -e "WRONG INPUT"
        esac

#Rules
echo -e "What do we do with the Rule?\n
          1. Accept Packet\n
          2. Reject Packet\n
          3. Drop Packet\n
          4. Create Log \n"
          read rule_option
          case $rule_option in
            1) rule="ACCEPT";;
            2) rule="REJECT";;
            3) rule="DROP";;
            4) rule="LOG";;
            *) echo -e "WRONG INPUT"
          esac

  echo -e "\n  Press Enter To Generate the Rule"
      read enter
  echo -e "The Generated Rule is... \n"
  if [ $proto=="NULL" ]; then
    echo -e "\n iptables -A $chain -s $source_ip -d $dest_ip -j $rule\n"
    gen=1
  else
    echo -e "\niptables -A $chain -s $source_ip -d $dest_ip -p $proto -j $rule\n"
    gen=2
  fi
  echo -e "\n Do you want to Enter Above Rule to IPTABLES? Yes=1, No=2"
    read choice
    if [ $choice==1 ] && [ $gen==1 ]; then
      iptables -A $chain -s $source_ip -d $dest_ip -j $rule
    else if [ $choice==1 ] && [ $gen==2 ]; then
      iptables -A $chain -s $source_ip -d $dest_ip -p $proto -j $rule

    else if [ $choice==2 ]; then
        main

    fi
  fi
fi
}

main(){
  ROOT=0
  if [ $UID == $ROOT ]; then
    clear
    main_choice=1
    while [[ true ]];
      do
      echo -e "*****************************************"
      echo -e "~~~~~ MAIN MENU ~~~~~~\n
      1. IPTABLES Service\n
      2. Build Firewall using IPTABLES\n
      3. Quit Program"
      read main_choice
      clear
      case $main_choice in
        1) ipStatus;;
        2) configure;;
        3) exit 0;;
        *) echo -e "WRONG INPUT"
      esac
    done
  else
    echo -e "MUST BE ROOT TO USE THIS!"
  fi
}
main
exit 0
