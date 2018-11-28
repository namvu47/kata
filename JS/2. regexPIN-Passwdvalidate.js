/*
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
If the function is passed a valid PIN string, return true, else return false.
eg:
validatePIN("1234") === true
validatePIN("12345") === false
validatePIN("a234") === false
*/

function validatePIN (pin) {
  return /^(\d{4}|\d{6})$/.test(pin);
}

/* password regex
regex = /^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*])[\w!@#$%^&*]{8,}$/;
/^
(?=.*[\d])        : contain at least 1 number
(?=.*[A-Z])       : contain at least 1 uppercase
(?=.*[a-z])       : contain at least 1 lowercase
(?=.*[!@#$%^&*])  : contain at least !@#$%^&*
[\w!@#$%^&*]{8,}  : match [\w!@#$%^&*] 8 times (\w = [A-Za-z0-9_])
$/
