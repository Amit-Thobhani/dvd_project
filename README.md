# dvd_project
To Simulate a DVD Inventory System which will allow to Add, Delete, Modify and List records

Details:
 A DVD store needs to maintain an inventory and keep track of records.
 Users can search for DVDs, based on certain criterion.
 User may add new DVD records or delete existing ones
 User can also modify existing information of records
 Intention is to facilitate querying from database, with basic UI at command

Python Module:

Design Approach
 Simulate a Menu driven Main screen with following options
Title
  1. Add a DVD
  2. Search
  3. Modify a DVD
  4. Delete a DVD
  5. Exit

 Script to have the following fields for a DVD record
  (Title, Star name, Year of Release and Genre as Drama, Horror, Comedy, Romance,
  Action etc.)
 The ADD and Modify operations should be based on the above mentioned fields
 The Delete operation should be based on Movie Title only
 The Search operation should have a sub menu for Genre, besides conducting a search
  on other fields of the DVD record
  Sensitivity: Internal & Restricted
 Provide necessary exception handling mechanism wherever required
 The project to use MySQL as Database. This assignment will require user to install
  MySQL dB package for python.
 Use Selenium to Test the Menu driven main screen
