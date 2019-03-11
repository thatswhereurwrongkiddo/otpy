# otpy v0.0.5_b3 (TESTING REPO)

otpy is a python rewrite of the popular 1974 game "The Oregon Trail",
developed by Don Rawitsch, Bill Heinemann, and Paul Dillenberger and
published by the Minnesota Educational Computing Consortium (MECC).

otpy was made simply to improve my python skills, I'm not trying to
make exactly the next big thing here. otpy currently only runs on Windows due to batch file usage, cross-platform support (with bash) coming in near future.

//THIS CODE IS UNSTABLE AND **WILL** CRASH (maybe)//

//IF YOU'RE LOOKING FOR SOMETHING TO RUN AS A CONSUMER, CHECK OUT THE MORE STABLE "MASTER" BRANCH//

//FILES IN THIS REPOSITORY SHOULD ONLY BE USED BY DEVELOPERS, TESTERS, AND COLLABORATORS//

---
TO-DO LIST
----
- change name storage from temp program-generated sqlite database to python list

  - PROGRESS: *not started*

- add following features code in HitTheTrail.menu():

  - Hunt

    - PROGRESS: *finished*

  - Rest

    - PROGRESS: *working (on health monitor)*

  - Check Supplies

    - PROGRESS: *finished*

- add calamities to HitTheTrail class

  - PROGRESS: *not started*

- create food usage system and hunger/health monitor

  - PROGRESS: *finished (partly)*
---

////////////////

/ KNOWN ISSUES /

////////////////

// ISSUE NUMBER | 001

// DESCRIPTION | there is a loop in HitTheTrail.exit() that
brings you back to Store.checkout()

// REASON | caused by improperly formatted if/else statement in Store.checkout(), issue resolved

// BUGFIX STATUS | FIXED 3.1.19

// FIXED BY | adding a sys.exit() to the end of HitTheTrail.exit(), and fixing Store.checkout() if/else statement

// BUGFIX DEV | thatswhereurwrongkiddo

---
How to run otpy:
----

Windows:

- navigate to the main "otpy" directory
- double click "otpy_Launcher.bat"
- program will begin
