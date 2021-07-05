# 0x06. Regular expression

## Concepts

_For this project, students are expected to look at this concept:_

-   [Regular Expression](https://intranet.hbtn.io/concepts/29)

## Background Context

For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.

Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the  `//`:

```
sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a

```

## Resources

**Read or watch**:

-   [Regular expressions - basics](https://intranet.hbtn.io/rltoken/SJ2eQ7V2iQlCgLc-L96zWg "Regular expressions - basics")
-   [Regular expressions - advanced](https://intranet.hbtn.io/rltoken/qyjWL-J1_qUaZGR690gH1Q "Regular expressions - advanced")
-   [Rubular is your best friend](https://intranet.hbtn.io/rltoken/WCjn8NgohbQ5NGXEObWZvQ "Rubular is your best friend")
-   [Use a regular expression against a problem: now you have 2 problems](https://intranet.hbtn.io/rltoken/Zfvv_ydOCvJ_YaBB6eDqVw "Use a regular expression against a problem: now you have 2 problems")
-   [Learn Regular Expressions with simple, interactive exercises](https://intranet.hbtn.io/rltoken/Y-OVGcJ5cskdXWIBowiE_A "Learn Regular Expressions with simple, interactive exercises")

## Requirements

### General

-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files will be interpreted on Ubuntu 14.04 LTS
-   All your files should end with a new line
-   A  `README.md`  file, at the root of the folder of the project, is mandatory
-   All your Bash script files must be executable
-   The first line of all your Bash scripts should be exactly  `#!/usr/bin/env ruby`
-   All your regex must be built for the Oniguruma library

## Quiz questions

Show

## Tasks

### 0. Simply matching Holberton

mandatory

![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/ec65557f0da1fbfbff6659413885e4d4822f5b1d.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210705%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210705T185536Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0aa7323483fd6b774bd52ef0518058628da68cee8bbbbcda374ec9122fdac64e)

Requirements:

-   The regular expression must match  `Holberton`
-   Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

Example:

```
sylvain@ubuntu$ ./0-simply_match_holberton.rb Holberton | cat -e
Holberton$
sylvain@ubuntu$ ./0-simply_match_holberton.rb "Holberton School" | cat -e
Holberton$
sylvain@ubuntu$ ./0-simply_match_holberton.rb "Holberton School Holberton" | cat -e
HolbertonHolberton$
sylvain@ubuntu$ ./0-simply_match_holberton.rb "Grace Hopper" | cat -e
$

```

**Repo:**

-   GitHub repository:  `holberton-system_engineering-devops`
-   Directory:  `0x06-regular_expressions`
-   File:  `0-simply_match_holberton.rb`

### 1. Repetition Token #0

mandatory

![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/e7db3c377d46453588fc84f3a975661d142fee91.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210705%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210705T185536Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0c472c381286b615a4c9fd4f3dd6ea9ea21cf53457cf1928ade5c401d375d8ec)

Requirements:

-   Find the regular expression that will match the above cases
-   Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

**Repo:**

-   GitHub repository:  `holberton-system_engineering-devops`
-   Directory:  `0x06-regular_expressions`
-   File:  `1-repetition_token_0.rb`

### 2. Repetition Token #1

mandatory

![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/c59ff11db195d5cf17d1790a5141ae2f234786d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210705%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210705T185536Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a326332ba10866df5f6ff632ef2b9d639a40b29955a87e4d3214861cf5ea8f2a)

Requirements:

-   Find the regular expression that will match the above cases
-   Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

**Repo:**

-   GitHub repository:  `holberton-system_engineering-devops`
-   Directory:  `0x06-regular_expressions`
-   File:  `2-repetition_token_1.rb`


### 3. Repetition Token #2

mandatory

![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/3b6bf4aeca6a0c2de584e7f5d68d11eef57ce205.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210705%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210705T185536Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=3218babcab9d78c97342deb2cdb4b2d8768133d17fcdbfb239715018a4b5aad0)

Requirements:

-   Find the regular expression that will match the above cases
-   Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

**Repo:**

-   GitHub repository:  `holberton-system_engineering-devops`
-   Directory:  `0x06-regular_expressions`
-   File:  `3-repetition_token_2.rb`

### 4. Repetition Token #3

mandatory

![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/f8dbcb9cf5ae569a8645027dc46e81cb372ce28e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210705%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210705T185536Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=3e0a1c80b989df259ca99bfd666467b16d0241eea706fa313d7065ca06eb8453)

Requirements:

-   Find the regular expression that will match the above cases
-   Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
-   Your regex should not contain square brackets

**Repo:**

-   GitHub repository:  `holberton-system_engineering-devops`
-   Directory:  `0x06-regular_expressions`
-   File:  `4-repetition_token_3.rb`


### 5. Not quite HBTN yet

mandatory

Requirements:

-   The regular expression must be exactly matching a string that starts with  `h`  ends with  `n`  and can have any single character in between
-   Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

Example:

```
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hn' | cat -e
$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hbn' | cat -e
hbn$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hbtn' | cat -e
$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'h8n' | cat -e
h8n$
sylvain@ubuntu$
$

```

**Repo:**

-   GitHub repository:  `holberton-system_engineering-devops`
-   Directory:  `0x06-regular_expressions`
-   File:  `5-beginning_and_end.rb`

### 6. Call me maybe

mandatory

This task is brought to you by Holberton professional advisor  [Neha Jain](https://intranet.hbtn.io/rltoken/V4rEpseJEPRMMnfaZPbkgw "Neha Jain"), Senior Software Engineer at LinkedIn.

Requirement:

-   The regular expression must match a 10 digit phone number

Example:

```
sylvain@ubuntu$ ./6-phone_number.rb 4155049898 | cat -e
4155049898$
sylvain@ubuntu$ ./6-phone_number.rb " 4155049898" | cat -e
$
sylvain@ubuntu$ ./6-phone_number.rb "415 504 9898" | cat -e
$
sylvain@ubuntu$ ./6-phone_number.rb "415-504-9898" | cat -e
$
sylvain@ubuntu$

```

**Repo:**

-   GitHub repository:  `holberton-system_engineering-devops`
-   Directory:  `0x06-regular_expressions`
-   File:  `6-phone_number.rb`

### 7. OMG WHY ARE YOU SHOUTING?

mandatory

![](https://intranet.hbtn.io/images/contents/sysadmin/projects/78/shouting.jpg)

Requirement:

-   The regular expression must be only matching: capital letters

Example:

```
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "I realLy hOpe VancouvEr posseSs Yummy Soft vAnilla Dupper Mint Ice Nutella cream" | cat -e
ILOVESYSADMIN$
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "WHAT do you SAY?" | cat -e
WHATSAY$
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "cannot read you" | cat -e
$
sylvain@ubuntu$

```

**Repo:**

-   GitHub repository:  `holberton-system_engineering-devops`
-   Directory:  `0x06-regular_expressions`
-   File:  `7-OMG_WHY_ARE_YOU_SHOUTING.rb`


### 8. Textme

#advanced

This exercise was prepared for you by  [Guillaume Plessis](https://intranet.hbtn.io/rltoken/l2JCUH5R2qdg7YVMYR1UmA "Guillaume Plessis"), VP of Infrastructure at TextMe. It is something he uses daily. You can thank Guillaume for his project  [on Twitter](https://intranet.hbtn.io/rltoken/FuFAuWPWMeiCgyQkh3SwZA "on Twitter").

For this task, you’ll be taking over Guillaume’s responsibilities: one afternoon, a TextMe VoIP Engineer comes to you and explains she wants to run some statistics on the TextMe app text messages transactions.

Requirements:

-   Your script should output:  `[SENDER],[RECEIVER],[FLAGS]`
    -   The sender phone number or name (including country code if present)
    -   The receiver phone number or name (including country code if present)
    -   The flags that were used

You can find a  [log file here](http://intranet-projects-files.s3.amazonaws.com/holbertonschool-sysadmin_devops/78/text_messages.log "log file here").

Example:

```
$ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-0-11 mdr: 2016-02-01 11:00:00 Receive SMS [SMSC:SYBASE1] [SVC:] [ACT:] [BINF:] [FID:] [from:Google] [to:+16474951758] [flags:-1:0:-1:0:-1] [msg:127:This planet has - or rather had - a problem, which was this: most of the people on it were unhappy for pretty much of the time.] [udh:0:]'
Google,+16474951758,-1:0:-1:0:-1
$
$
$ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-64-10 mdr: 2016-02-01 11:00:00 Receive SMS [SMSC:SYBASE2] [SVC:] [ACT:] [BINF:] [FID:] [from:+17272713208] [to:+19172319348] [flags:-1:0:-1:0:-1] [msg:136:Orbiting this at a distance of roughly ninety-two million miles is an utterly insignificant little blue green planet whose ape-descended] [udh:0:]'
+17272713208,+19172319348,-1:0:-1:0:-1
$
$ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-64-11 mdr: 2016-02-01 11:00:00 Sent SMS [SMSC:SYBASE1] [SVC:backendtextme] [ACT:] [BINF:] [FID:] [from:18572406905] [to:14022180266] [flags:-1:0:-1:-1:-1] [msg:136:Far out in the uncharted backwaters of the unfashionable end of the western spiral arm of the Galaxy lies a small unregarded yellow sun.] [udh:0:]'
18572406905,14022180266,-1:0:-1:-1:-1
$
$
$ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-64-11 mdr: 2016-02-01 11:00:00 Sent SMS [SMSC:SYBASE1] [SVC:backendtextme] [ACT:] [BINF:] [FID:] [from:12392190384] [to:19148265919] [flags:-1:0:-1:-1:-1] [msg:99:life forms are so amazingly primitive that they still think digital watches are a pretty neat idea.] [udh:0:]'
12392190384,19148265919,-1:0:-1:-1:-1
$


```

**Repo:**

-   GitHub repository:  `holberton-system_engineering-devops`
-   Directory:  `0x06-regular_expressions`
-   File:  `100-textme.rb`


### 9. Pass LinkedIn technical interview level0

#advanced

One way to get started in getting a Software Engineering job at LinkedIn is to solve their regex puzzle.

Requirements:

-   Solve LinkedIn regex puzzle:  [https://engineering.linkedin.com/puzzle](https://intranet.hbtn.io/rltoken/u2xzwrPyylRY7dpGJJ9P-Q "https://engineering.linkedin.com/puzzle")
-   Provide as an answer file a screenshot of the “Congratulations” screen with the date and time of completion

Example:

![](https://assets.holbertonschool.com/media_images/files/000/001/208/thumb_1000/Screen_Shot_2020-02-25_at_12.56.14_PM.png)

Well, I guess I can get into LinkedIn hiring process:

![](https://s3.amazonaws.com/holbertonintranet/files/correction_system/78/passed-linkedin-regex-challenge.gif)

**It is your responsibility to request a review for this task from a peer. If no peers have been reviewed, you should request a review from a TA or staff member.**

**Repo:**

-   GitHub repository:  `holberton-system_engineering-devops`
-   Directory:  `0x06-regular_expressions`
-   File:  `101-passed_linkedin_regex_challenge.jpg`