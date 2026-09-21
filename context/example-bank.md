**Give an example of a time where you've optimized a process.**

When I was SRE manager at Smarsh, the SRE team had a prioritization problem. Errors, alerts, and customer-reported issues were all dumped into a single kanban board. At the beginning of the day, the SRE team would decide what to work on, but their work would inevitably be interrupted by a Support Manager or a Sales Enablement lead telling them that a different issue was higher priority. 

The result was significant thrashing. We had an extremely high WIP rate. The SRE team felt unproductive due to constant context switching. The business teams felt like their issues were languishing on the board. 

The first step to solving the problem was to figure out where in the workflow the real bottleneck existed. What was regarded internally as an output problem (not enough tickets resolved) was actually an input and communication problem (inadequate triage and stakeholder engagement). 

We started by improving triage. All tickets, regardless of their source, were augmented with a customer impact statement, provided by support. This helped the SRE team to prioritize the relative impact of an issue based on how many customers (and which customers) were impacted. An added bonus was that it forced greater collaboration between the SRE team and the support team, which over time led to the SRE team better understanding the needs of our customers. 

Secondly, we implemented a short weekly stakeholder engagement meeting, where leaders of various teams across the business would briefly report on long-standing projects that they were working through. This allowed us to dedicate bandwidth to helping move these larger, longer-running initiatives forward while still preserving time to deal with more urgent tickets that came up throughout the week. 

Lastly, we made the Kanban board publicly accessible to all stakeholders so they could better understand what we were working through at any given time. This visibility was key in mitigating the perception that the SRE team were working on "less important" tickets. 

The result was a ~30% reduction in WIP, as well as greater velocity in high-priority ticket completion. Less measurable but no less important, the satisfaction of both the SRE team and the adjacent business teams significantly improved. 

——

**Give an example of a time you've had to convince stakeholders to invest in a project.** 

For the last two years of my tenure as VP of Tech for Cirium, I designed and executed an organizational transformation program to relocate our employee base from the US to the UK and India. While this ultimately yielded $10M annual operational savings for the company, because I wanted the transformation to be people-focused, it also came at a significant up-front cost ($10M). 

We would announce the plan at the beginning of the year, and then work over the course of the year to hire the new roles and perform knowledge transfer. The up-front $10M covered overlap costs while we hired new staff post-announcement, retention packages for key employees, and travel costs to allow existing and new employees to execute knowledge transfer. 

It depended on huge levels of trust from our executive team and corporate sponsors, as well as the remaining and departing employees. 

For the executive team and our corporate stakeholders, I demonstrated how a people-focused approach (rather than simply cutting 10% of our workforce) would result in stronger teams post-program and would enable us to maintain the high culture of trust that we had built across the organization over the years.

For the impacting engineering teams, I maintained a policy of over-communication. I met virtually with each group several times every month, traveled to our US, UK, and Indian locations to run AMA sessions, and kept regular office hours where folks could drop in and ask any questions about the program and how it affected them. 

Some of those meetings were incredibly challenging, but the end result was a strong community of departing employees who felt like they had been well-supported and fairly treated throughout the process. For the remaining employees, they felt informed and (relatively) secure in their future with the company. 

The program overall was a massive success. We hit our budget and timeline, and the organization is now delivering software faster and with less friction than ever before. 

 —
**Give an example of AI automations you've used.** 

In my coaching practice, I use several AI-assisted automations: 

- My new client onboarding process uses a combination of code-based and AI automations. I use scripts to generate enrollment links and update my database, and the process is orchestrated by a series of Hermes agents. These particular automations have not only saved me hours in manual work, but have also led to a more consistent and professional experience for my clients. 

- I manage several calendars (a personal Gmail, a business Gmail, and a business Outlook), and it used to cost me several minutes a day to click through the calendar UIs to set up meetings on each calendar. I created a Claude Code skill that calls an n8n workflow to allow me to send events from any calendar using natural language. 

- Client work generates a lot of admin that is easy to let slip: meeting notes, follow up actions, updating who said what to whom. I used to do all of that by hand after every call, and it was easy to miss things. I built a skill in Claude Code that pulls the transcript from a call, pulls out the real key points and action items, updates that person's file in my CRM, and adds any follow ups straight onto my task list for the day. Every external call gets processed and actioned the same day, instead of sitting in a backlog of notes.

—

**How do you prioritize multiple deliveries?** 

My process is: 

1. Prioritize by business impact
2. Be transparent
3. Over-communicate 

The SRE triage problem above is a good example of this, but a more recent one was during my final year at Cirium. 

We were coming to the end of the workforce transformation project (Project Horizon) and tolerance was waning for our previously agreed rule: "Nothing is more important than Horizon". The reality was that the business needed to move forward on new initiatives even as we tried to stick the landing of Horizon. 

In particular, one element of the corporate organization was mandating that we change out our observability platform to avoid a large renewal cost from the existing vendor. This required that we spin up a new team dedicated to replatforming and task that team with enabling all of our other teams to perform the migration. 

Ultimately, we successfully finished Horizon and completed the observability migration project (Project Beacon). 

The trick was to be transparent about the impact and trade-offs, and come to consensus as a leadership team about where we should spend our resources. In some cases, it was necessary for me to bring people together to discuss these trade-offs. In other cases, I would use my understanding of the situation to make a decision and move forward. In all cases, communication was key in multiple formats: one-on-one, small group, and cross-company. 

—
**Give an example of an organizational transformation that you've accomplished.** 

One of the reasons Project Beacon (our observability platform migration) was successful was because it was the proof point of our new SRE ways of working that I'd introduced the year before. 

Cirium was the result of multiple acquisitions, and each of those acquisition teams had a slightly different operating model when it came to the relationship between software engineers, quality assurance, and site reliability/devops engineers. Some teams had embedded devops. Some teams shared from a pool of SRE engineers, and some teams just tried to do the work themselves as best they could. The result was a patchwork of processes and widespread confusion about how work got done, especially when changes were required across multiple teams, which was often the case with infrastructure initiatives. 

The fix was to restructure the SRE team so they operated as a platform team. This required them to break away from their long-standing teams and work together to develop platforms that could benefit all other engineering teams. 

For some teams, this was a significant cultural change. Many SREs had become domain experts in a specific part of the stack and derived identity from that position. In addition to the tenets of transparency and over-communication, retraining and emphasizing a culture of learning and development was important to make this initiative stick. 

We also listened closely to feedback during the transition and made sure to adopt the solution where it made sense, rather than rigidly following a new org structure. For example, our teams in Chennai found it difficult to participate in UK-based team meetings, and the stacks that they managed were somewhat separate from the majority of our UK teams. In this case, we listened to their feedback and decided to exclude our Chennai teams from the new structure. 

Before the SRE org change, an initiative like Project Beacon would have taken several months and wasted thousands of dollars in rework across teams. As a result of the change, the new Platform team was able to stand up a single observability platform within weeks and then run a coordinated effort across the teams to migrate them from the old solution to the new platform.

**Tell me about a time you ran a workshop or training for a cross-functional group with mixed technical ability.**

A local mortgage company brought me in to help them identify use cases to automate with Microsoft Copilot. It was a genuinely mixed group. Some were loan officers, some were front office staff, and they came in with very different technology backgrounds. A few were already using Copilot regularly. Others didn't use a computer that often. Their understanding was low not just of AI but of technology in general, so I knew I had to take it all the way back and explain some very basic concepts about how the tools actually work before anything else would land.

The thing I did first was listen to how they dealt with their customers. Being a loan officer is relationship-driven work, and you are often dealing with people in high-stakes situations who are very stressed out. Once I understood what the customer actually needed from them, it was obvious that sending out a bunch of AI-generated emails was going to cost them trust. So we did not walk through that workflow, even though it is the one everybody reaches for first.

What was genuinely valuable to them was different. Loan officers often keep a caseload even while they are on vacation, so they come back to an inbox they have to triage fast. We built a specific prompt for that, not just the generic summarize-my-emails button, so they could quickly see what actually needed digging out that day.

It sounds like small fish, but they went from an organization that barely used technology to its full extent to one that felt comfortable using AI for the right tasks and confident leaving it out of the wrong ones. It came down to listening and building what they actually needed, not what was cool.
