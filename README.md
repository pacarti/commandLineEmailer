# commandLineEmailer
The script logs into a given Protonmail e-mail address and automatically sends a message from it into address given in 1st parameter. <br><br> A modified "Command Line Emailer" practice project from 12th chapter of the Automate the Boring Stuff book by Al Sweigart(http://automatetheboringstuff.com).

<h2>Functionality</h2>
The script takes the recipient e-mail adress and Protonmail login address as its first two parameters. With the regular expression, it checks the corectness of the first and second email and if second email belongs to Protonmail domain. Then it asks the password for the e-mail address so it can log in(the password is masked). After, if the password is correct, with Selenium module, it sends the e-mail automatically to the given in 1st parameter address.

<h2>Syntax</h2>
<code>python3 commandLineEmailer.py &lt;recipient_email&gt; &lt;login_email&gt;</code><br><br>
Please remember that login e-mail adress must be in Protonmail domain('proton.me', 'protonmail.com' or 'pm.me').