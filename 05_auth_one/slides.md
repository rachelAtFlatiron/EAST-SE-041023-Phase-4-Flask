---

title: '05_auth_one'

---

# Authorization

---

Authentication: verifying identity
Authorization: Users' access rights

---

## Cookies

- memory IN YOUR BROWSER (client side) to track information about users
- can or can not persist
- ex. tracking ad information, keeping user logged in, seeing how many articles you've read on some site
- you can see cookies created in developer tools

---

## Cookies Are Sus
- best for things not important to user security
- susceptible to...

---

## Sessions

- stores user information ON THE SERVER SIDE
- information is encrypted and will be stored, in browser, encrypted
- info is only ever unencrypted on server side 
- Note: `db.session()` (opening up ability to add info to database) is different than browser sessions (place to store info about user, etc.)
