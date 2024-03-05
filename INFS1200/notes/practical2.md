# Module 1 Case Study


### Task
Using the correspondence on the pages below, complete the following task. Please ask your tutors for help if you require clarification on any aspects of the brief. 

---
#### Correspondence 1:
From: peter@dirtroaddriving.com.au

To: INFS1200_7900@uq.edu.au

Date: 17/3/2020 11:42 AM

Subject: Student Support for Industry Project


Dear INFS1200/7900 Student Team,

I am emailing in regard to your lecturer’s offer for student assistance in a database project our company is undertaking. I am the cofounder of a rural rideshare company called “Dirt Road Driving.” We specialise in offering our clients rideshare services in locations which are not serviced by other companies such as DiDi or Uber.

We are currently storing our data in an excel spreadsheet, however, to accommodate future growth we would like to implement a database system to track our ridesharing activities. I have tried to summarise the data stored currently in the excel sheet below. Would you please be able to create an Entity-Relationship diagram for us to use in our planning phase?

**Users:** When a user signs up to create an account with us we ask them to provide their full name and DOB. We also assign them a unique id number. A user can also register **emergency contact(s)** specific to their account. Each emergency contact includes a *name* and *contact details*, with the name being *unique* per user account.

**Staff**: We *split staff into two categories*, **Administration** and **Drivers**. All staff members have a *staffID* but for administration staff their *desk number* is also recorded. By law we are required to record the *licence number* of each driver. A staff member could work *both* as a driver and in administration.

**Vehicles**: We store the *VIN* number, *make* and *model* of each car used in our ride sharing service. However, *if the car* is a **4WD** then we also record the *ride height* and *wheel type*. For **2WD** cars we record if the car is *front wheel drive or back wheel drive*.

Trip: A trip is made up of a **user**, a **vehicle** and a **driver** as well as a *time stamp* of when the booking is made. Two additional timestamps demonstrating the *start* and *end* of the trip are also recorded. This allows us to calculate a ride *fare*. In a trip, the user may *request to stop* at several locations, which are all recorded for safety purposes. After a trip is made the user can submit a *rating*.

On behalf of the company I would like to extend our sincere thanks for your help and assistance.

Kind regards,
Peter Thompson
Director of Innovation | Dirt Road Driving  


### Correspondence 3: 

From: peter@dirtroaddriving.com.au 

To: INFS1200_7900@uq.edu.au 

Date: 27/3/2020 08:56 AM 

Subject: RE: Student Support for Industry Project 
 
Hi Elaine, 
 
Sorry for my late response. Thank you for your email requesting clarification. After checking with 
our administration staff, I can provide the following information in response to your questions. 
 
What “contact details” are stored for an emergency contact? 
We just store an *email address* and a *phone number*. 
 
Just out of interest, why do you record the vehicle used for each trip? Wouldn’t a driver just drive 
the same vehicle each time? 
Actually, a <u> driver could potentially drive any vehicle in our system </u> when they complete a trip. 
 Drivers often switch cars depending on the trip, especially in areas where there are no roads or just 
dirt tracks. As such we need to <u> record the vehicle used for each individual trip as well </u>. A driver is 
never permanently assigned to a specific vehicle. 
 
Do you store any personal information regarding staff members (name, DOB, address) in addition 
to their staffID? 
Yes, we record each staff members *full name (first, middle and last)*, *DOB, address* and their 
*phone number(s)* as well. 
> who else stores these kinds of details? What would it mean if these details are common?
 
Regarding Ratings… 
After a trip is completed the user is encouraged to rate the driver and the vehicle. However, they 
<u> rate the driver and the vehicle separately </u>. Each rating is stored as an integer out of 10. If a user 
takes another trip with the same driver or vehicle and decides to submit another rating, a new 
rating is not created, instead their old rating is updated. 
 
I hope this helps! Please feel free to contact me if you require any more information/clarifications. I 
look forward to viewing the student responses! 
 
Kind regards, 
Peter Thompson 
Director of Innovation | Dirt Road Driving   