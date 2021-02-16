# Eric Altenburg \hfill CS-555 \hfill \today
## Week 1

1. How much planning?
	- Depends on task's:
		- Domain
		- Are the requirement complete?
		- Will the requirements change over time?
		- Risk (reworking/budgeting for fixing mistakes)
		- Risk of doing the right thing too slow
		- Rewards?

#. Software dev life cycle
	- Specification: what functionality must we support?
	- Development: how do we create the software that delivers the functionality?
	- Validation: How do we verify that the software does what it's supposed to do?
	- Evolution: how does the software evolve to meet customer needs?

#. Waterfall model
	- Sequential
	- requirements -> design -> implementation -> verification -> maintenance
	- Can't go backwards to other steps, only forward

#. V model 
	- Waterfall model with more rigorous validation/verification steps

#. Boehm's Spiral model
	- Incremental development and iterations
		1. objective setting
		#. Risk assessment and reduction
		#. Development and validation
		#. Planning for next iteration
	- After one iteration, you keep going back and starting over

#. Agile methods
	- Frequent iterations and deliverable
	- CLose collaboration between developers and customers
	- Support changing requirements
	- Frequent retrospection: learn and improvise from experience
	- Sprints (plan, design, build, test, and review)
		- Have retrospective meetings after each sprint to make changes in following sprints

#. Reason to use Agile Methods
	- Big upfront planning is not practical because of unstable changes and ambiguous requirements
	- Delivery through small baby steps through iterative and incremental development to reduce the chances of risk
	- Visibility with customers: customers are part of the term instead of being purely observers
	- Frequent reflections by the project team:
		- What are we doing well?
		- What can we improve?

#. Big Bang/Chaos (Ad-Hoc)
	- Little to no planning
	- Figure it out as you go 
	- Typically used for very small projects (course projects, start ups, etc.)
	- Not highly recommended....

#. Comparing software dev paradigms
	1. Lean
	#. Iterative
	#. Agile
	#. Ad-Hoc
	#. Traditional

#. Rational Unified Process (RUP)
	- 6 best practices of software engineering:
		1. develop iteratively
			- Solutions are too complex to get right first try
			- Use iterative approach and focus on high risk items in each pass
			- Customer involvement
			- Accommodate changes in requirements
		#. manage requirements
		#. use component-based architecture
			- Focus on early development and base lining of a robust architecture prior to full-scale development
			- Architecture should be flexible to accommodate changes
				- Modularization
		#. Model software visually (Unified modeling language UML)
		#. Continuously verify software quality
		#. Control changes
			- Change is inevitable
			- Manage the change request process
			- Control, track, and monitor changes

#. RUP phases
	- Inception: scope system for cost and budget, create basic use case models
	- Elaboration: mitigate risk by use case models
	- Construction: implement and test software
	- Transition: plan and execute delivery of system to customer

#. RUP disciplines
	- Used in each phase
	- Business modeling, requirements, analysis \& design, implementation test, development, Configuration \& change management, project management, and environment

#. Extreme Programming (XP)
	- An agile method
	- Combines best practices 

#. 12 XP practices
	1. The planning game
		- Main planning process
		- Occurs once per iteration  (once a week)
	#. Small releases
		- every release completely implements its new features
		- every release should contain most valuable business features
	#. Metaphor
		- Simple explanation of project
		- Agreed by members, simple for customers, and complete enough for architecture
	#. Simple design
		- Run all tests
		- No duplicated logic like parallel class hierarchies
		- States every intention important to the developers
		- Has the fewest possible classes and methods
	#. Testing
		- Developers continually write unit tests, which need to pass for development to continue
		- Customers write tests to verify features are implemented
		- Tests are automated so they are a part of system and continuously run to ensure the working of the system
	#. Refactoring
		- Devs reconstruct system without changing the behavior to remove problems with the code
		- How can we make the code simpler while still passing the tests?
	#. Pair programming
		- Driver:
			- Thinks about the best way to implement
		- Navigator:
			- Viability of whole approach
			- Thinks of new tests
			- Thinks of simpler ways
			- Switch roles frequently
	#. Collective ownership
		- Entire team takes ownership of whole system
		- Everyone knows a little bit of every part
		- If devs see opportunity to improve part of code, they do it
	#. Continuous integration
		- Integrate and test every few hours, at least once per day
			- Don't wait until end to integrate
		- All tests must pass
		- Easy to tell who broke code
			- Problem is likely to be in code most recently changed
	#. Sustainable pace
	#. Whole team
	#. Coding standards








