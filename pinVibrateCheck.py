### This script checks whether the phone vibration facility works fine.
### If the correct pin is entered by user the phone should vibrate for 4 seconds

# Imporing libraries
import android

droid=android.Android()

# Enabling user to enter pin
droid.dialogGetInput("Pincode","Please enter 4 digit pin")
str=droid.dialogGetResponse()
pin=str[1]['value']
# Pin check
if pin=="1234":
    droid.vibrate(4000)
else:
    droid.makeToast("Wrong pin entered")
    exit()

# Enabling user to verify if phone vibrates or not
droid.dialogCreateInput("Vibration Check","Did the phone vibrate?",None,None)
droid.dialogSetPositiveButtonText("Yes")
droid.dialogSetNegativeButtonText("No")
droid.dialogShow()
str=droid.dialogGetResponse()
q=str[1]['which']
# Output of Program
if q=="positive":
    droid.makeToast("Phone vibration works")
elif q=="negative":
    droid.makeToast("Phone vibration does not work")
exit()
