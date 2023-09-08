# Snapshot 1
The contents of this page outline the work I have completed on a weekly basis regarding the DECO3801 group project. It outlines my work, in addition to my feelings and concerns of the project over time. Each journal is written on a weekly basis. Please go to my website [danielCiccC.github.io](https://danielciccc.github.io/DECO3801/docs/main_DECO3801.html) for a styled and complete running list of my journals.

## Week 1 journal
- Not much to say at this stage. Our first class consisted of a few icebreaker sessions and introduction with the work to come. One of my friends has invited me to a work he is organising, and I have been introduced to my teammates for the semester.
- Next week we will officially form our teams

## Week 2 journal
- This week we didn't do much, besides put in for our team formations. We were told that we will be accepting our project briefs soon (sometime in the next couple days). As soon as that happens, will will read through the list and put in our preferences asap.

## Week 3 journal
- We put in our top preference for brief 38 - called 'New Curation', and received it too. This week, we began to have discussions about what the solution would look like, the technologies we would need to implement this and the business ops tools as we began to compile our statement of work.

We will be using jira to manage our tasks, and confluence any large documentation. It will be my responsibility to manage upcoming work and build jira's to manage to workflow of the developers. This is the [current jira workstation](https://deco3801.atlassian.net/jira/software/projects/PRO/boards/1)

![Alt text](assets/IMG1.PNG)

### Statement of work
Fortunately, the technologies we needed to implement were quite straightforward. As the project brief asked for a Large Language Model (LLM) be implemented to remove bias from news articles. This made the backend relatively simple to choose - only python has strong support with existing LLM's, and Darren's strong aptitude with React/node.js can be used to build our user interface. 

Our hurdles immediately ahead of our are understanding what we need to develop as part of our statement of work, and putting pen to paper to write down all of our design elements for this project. We have had several discussions already about what elements and features we choose to incorporate into our design, and whether we want to introduce AR (augmented reality) into the design as well (as it was labelled a potential feature to include). So far, we have plans to deliver three phases in our build:
1.  Outline all the biased keywords in the text, and explain why they are biased. Build UI to support this feature
2.  Develop a bias score (which will be a propeitary mix of different subversion techniques) which will outline how biased the news article is based on a variety of subversion techniques
3.  use search engine optimisation and google search to find similar and other relevant articles, and compare them to the one inputted in. Use this to compare the scores of related articles. In addition to this, summarise the key facts from the variety of sources inputted in.


There has still been some debate as to whether we should incorporate AR into our build. I will have a meeting with Yash and Sean to discuss this further, as they are soon to complete more interviews and testing.

Yash has begun developing our statement of work on [google drive](https://docs.google.com/document/d/1eian7Lq7jjnbPXbMV-p0AtF2zAB1gc1qQfj7hMRu_H4/edit?fbclid=IwAR1AXTNjgif_rL-OmYZxvU48EAIJtS1PnRWtFo_v0XJYS5bOp4J2F2Y4TDI) and Sean has begun work on developing wireframes to outline our build, although I don't believe this will be ready in time for our statement of work. 

## Week 4 Journal
Almost immediately after submitting our Statement of work, I had another conversation with Yash and Sean about the phases of our build, and the insights they have drawn from interviews and surveys. Sean urged (and convinced us) to pivot our existing phases to instead aim to create a site that can summarise out key facts from the article in the initial phase of our build, instead of finding keywords in text. All in all, this would mean re-arranging the phases our build plus addiing some additional functionality earlier on the phases of our build. 

[Our wireframe plans to date](Wireframes1.pdf)



## Week 5 Journal
- Passed our statement of work on our first try (team was very relieved) but received a lot of feedback from our tutor regarding some details we have to further refine
- biggest detail by far was our target demographic. Currently our application is suited for all users that are interested in reading facts from an unbiased perspective, but our tutor had concerns that our audience was not specific enough, and that we needed to further explore our target demograph and make features related to a more specific audience.
- Completed phase I, as per the specifications of Sean's wireframes. I am super impressed with the skillset of the fellow developers in our team. Darren and Manav have taken ownership of the UI, and built it almost identically to Sean's wireframes, and Ron has been busy implementing all the API endpoints and developing webscraping functions to make the URL work.
- Focus on our milestone presentation, which is due next week. I have been given the responsibility to present all the technical implementation regarding the work we have done so far.

## Week 6 Journal
-  Spent most of the week organising the milestone presentation alongside Yash and Sean. 
-  Spent the leftover time I had updated the summary prompt to be as efficient and consistent as possible
-  Pivoted the project a second time, to be targeted towards political bias. Concerns regarding creditbility of facts, in which Yash discussed the use of a polling system or commenting system to discuss the credibility of the facts we present, alongside a disclaimer.
-  In this pivot, we would also include a page for political figures to search for
-  Sean had spent time updating the wireframes to reflect changes in the build of our project.

[Our most up to date wireframe, outlining poltiical figure websites](WIREFRAMES3.0.pdf)

## Week 7 journal
- Sean has developed new wireframes that incorporate political figures, and accounts which maintain a running feed of news regarding their activities. 
- Working on connecting a database on AWS cloud to using that as a global database for our newscuration project. I also realised that I had not finished previous work creating a bias summary prompt for the frontend developers to begin implementing. I shall have to complete this before I begin building transaction tables and databases for backend.
- Pivoted a lot from out original project. From last week, we decided to narrow down our scope to specifically tailor our application to political bias. In this development, we have included the idea of a political figure homepage, where a user can see a feed of unbiased summaries of a political figure.
- While all our members are busy, I have concerns that we do not have a strong project structure of the phases of our new build, and the dependencies that will eventually develop as some people are waiting on implementation from others. The jira's desparately need to be updated to reflect the changes in scope. I will update this immediately after submitting this snapshot
- 