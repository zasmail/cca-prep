---
title: Built an AI-Native Sales Org from Scratch
speaker: Eleanor Dorfman, SaaStr AI 2026
source: https://www.youtube.com/watch?v=ra0-ZvVApGk
retrieved: 2026-07-16
method: youtube-transcript-api
word_count: 5026
---

Give a warm welcome to Anthropic's head
of industries, Elenore Dorfman.
All right. Hi everyone. My name is
Elenore Dorfman.
I lead the commercial and industries
sales team at Anthropic. And I've been
at Anthropic for a little over a year
and a half now.
We've had a commercial product for the
last 3 years. But it wasn't until the
Claude 3 family of models when Claude
started getting really good at coding
that things started to accelerate. And
it wasn't until December of 2025
when things really took off. The launch
of Opus 4.6 in December was a bit of a
sea change for us. And we came back from
what was in hindsight an incredibly
restful
winter break
to demand
going vertical.
We had not hired for it. We had not
prepped our processes for it. We had
done extensive planning for the year.
And what we thought the year, or at
least the first quarter, was going to
look like.
We were not prepared.
Even if we were prepared to hire and
onboard and 3x or 4x or 5x the sales
team, you simply can't absorb that
number of bodies at the pace
that we needed to absorb them in order
to deliver a density demand and in order
to deliver a positive customer
experience.
So the question we had to answer early
in January of this year, which
now feels like a lifetime ago,
was how do you build an AI native sales
org from scratch because we
fundamentally had to turn everything
we'd been doing on its head in order to
meet the moment that the market had put
in front of us.
Our thesis was that we actually had
invested in a really incredible stack of
existing tools.
All of these tools had thread or had
threaded Claude natively within them.
They had a thing we just heard from from
someone who had put Claude inside of
their tools.
And if we had a strong stack and a
foundation,
we could build coherence and a holistic
approach to the customer journey in
those tools and then thread Claude where
we didn't have solutions.
So build on the stack we already had and
lean on Claude for everything around
that stack, in between that stack, and
making sure Claude was the narrative
thread and the connective tissue. So it
wasn't just six tools with Claude bolted
on, it was a cohesive customer
experience built on top of our existing
investments with Claude doing things we
hadn't even imagined it was capable of
before Opus 46.
We'd invested in tools and we use them.
So we use Lean Data for routing, we use
Clay for enrichment, Salesforce is our
system of record and source of truth. We
use Jira for tickets, Intercom's Fin
product we use for customer customer
support as well as for sales support.
I joke with the Iron Cloud team that I'm
a daily active user. I am in Iron Cloud
every day working on contracts. We have
Snowflake, we have BigQuery, we are the
heaviest Slack users you can imagine.
We use the G Suite, all of the above.
And these were all working for us and we
decided to double down on our investment
in them.
So we fundamentally made four
investments around the four constraints
that we couldn't move.
We had demand, we couldn't staff.
We had Claude of our existing stack.
We have functions around sales. Sales
doesn't operate on its own. Sales sits
around legal and deal desk and rev ops
and billing and compliance and customer
support and customer success. Sales is
not alone on an island delivering a
great customer journey. Many, many teams
needed to meet the moment alongside of
sales. And we had to just aggressively
grow AE capacity without killing them,
which is also a constraint I probably
should have put on this slide.
So, we couldn't kill our sales team.
But, we couldn't grow head count
overnight. We have an extensive
recruiting process. We weren't going to
sacrifice our bar, our culture, or
anything like that in order to service
the demand. So, we were left with no
choice but to build to support it.
There are a lot of orthodoxies that have
governed and really defined the last 15
years of enterprise software.
I've been in developer tooling and
infrastructure
for 12 or for actually not going to do
the math for a very large part of those
last 15 years. And this is one that I
really stood behind. There's product led
growth and there's sales led growth.
And never the two shall meet.
Self-service wasn't the enemy, it was
just a different team. It wasn't part of
what the sales team did. And we had to
throw that orthodoxy aside at the
beginning of this year.
So, I've always thought and I've always
operated with my product counterparts
that enterprise plans should be dated by
a human.
Customers want to talk to an AE during
this buying journey. And we no longer
could meet that the case. So, we no
longer have enterprise plans dated by
humans. We've launched enterprise
self-service. We launched an MVP in
January. We launched it into production,
I think, in February.
And it's been a huge success. We do not
think of self-service as a downgrade. We
think of it as a part of the buying
journey and a way that we can move
remove friction and make sure that we
get the right customer, the right buyer
with the right plan at the right time.
All of our leads are enriched and
evaluated and qualified by Clay and by
Claude. And then there are two funnels.
And we're still working on nailing this,
so you might hear some people who feel
that they ended up in neither funnel.
But we're willing to make sure we're
really investing to make sure that
everyone who wants to talk to Claude
can, anyone who wants to talk to a sales
member can, and anyone who wants to buy
Claude can. So, Claude and Clay do the
qualification, they do the enrichment,
and then you can go into the self-serve
funnel where Finn from Intercom guides
you on their journey. We partnered
really closely with the Finn team to
build take their flagship support
product and make it a viable tool for
sales and it's been amazing.
Then they did set up with an enterprise
plan, it's real ACV, they have terms of
service, they can do invoicing, we get
them enrolled and provisioned, enrolled
in training, and kickstart their journey
completely self-serve using Claude and
our tech stack.
If Claude and Clay qualify you for the
sales funnel, the lead goes to the BDR
team, they're qualified, and they're AE
routed. So, we're running these two in
parallel at any given time. And since we
launched this, soft launched in January,
hard launched in February,
54 54% of our new enterprise logos have
come through the self-serve funnel in
2026.
So, this has been an incredibly
important funnel and a way that we've
tried to meet the moment and drive a
more effective sales funnel.
The second investment is that we knew
that Claude lived inside of the tools
that we had already bought
and spent the last 3 years building
around our needs.
We have six core tools that really
define the journey of a lead.
We've talked about Clay, I'm a huge Clay
fan.
Clay for Enrichments, Lead data main
data for routing, Salesforce for op
creation and opportunity management,
Gong for tall coaching, we are heavy
heavy Gong users,
Ironclad for contracts redlines and
Slack for close one feels like a really
small way of describing the role Slack
plays, but Slack is for deal
coordination. It's for comms. It's for
many other things as I'll show you in a
few slides. But for the purposes of a
lead working its way through our
architecture and our plumbing, these are
the six tools.
However, I imagine you don't want to
just see an architecture slide that
talks about the tools we built. And as I
said earlier, Claude isn't just the
seventh tool we built it on we bolted
on.
Claude is what makes the tools we've
already bought talk to one another, work
together, and create a seamless customer
journey.
So, let's talk a little bit about how
that shows up for the AEs in the sales
team on a Tuesday morning, a Monday
morning,
any day.
When a new lead comes in and the
account's created in Salesforce, we're
working on getting all of them in, but
it's a work in progress.
Prioritization is done. Claude and Clay
do the account research up front. They
do the prioritization. They update the
account record. They pull in any
historical context from Slack, from
Google Docs, from previous Gong calls.
And when the AE is slotted in, they have
all of the contacts they need that helps
drive their prioritization and their
actions.
Every single customer facing rep starts
the day in Clod.
I'll talk about this a little more
later, but we've built a series of
skills
inside of Clod that enable the AEs to be
massively more productive. One is the
morning brief, which is built on top of
all of the connectors that we use to run
our business. So, on Gmail, on Gong, on
Slack, on Google Docs, on calendar, on
Salesforce, on Intercom, on Greenhouse.
There are so many systems where little
pieces of context are incredibly
relevant to ensure you're prioritizing
your time,
you're operating efficiently,
and you're delivering a world-class
customer experience.
So, with one prompt, this is how every
AE starts their day. I have mine sent to
me in Slack every morning at 7:00 a.m.
Eastern, cuz I'm based in New York.
But it tracks everything. It looks at
your calendar, what do you have that
day? What emails have you not answered?
What Slacks have you not actioned? What
centralized initiatives do you still
need to deliver? What marketing events
are coming up where you need to
prioritize inviting customers?
That morning brief is deposited in your
inbox or Slack or in Clod.ai every
single day and prioritizes your day.
These three actions need to be taken.
These emails need to be responded to.
Further along in the deal cycle, we've
leveraged Clod inside of our tooling,
which we use uh
people use Outline for. So, where we put
and Google Docs, where we publish our
policies.
Inside of historical precedent and
policy, as well as context based on
Slack discussions, emails, and Gong
calls. So, when a AE is ready to draft
and ship a proposal to a customer,
Claude does it. Claude made sure it's
within policy.
Claude made sure it lines up with the
customer expectations.
Claude has all of the knowledge of our
products, of our models, of our road
map. Claude knows where we've won in the
past and why we've won. Claude knows who
the customer is, what they care about,
who are the stakeholders that had been
that had been involved, what has been
the shape of the negotiation. And with
one prompt instead of an AE opening up a
spreadsheet, opening up nine different
tabs with all of the deal desk guidance,
listening to gong calls and looking at
transcripts to find the history of what
had been negotiated,
Claude generates the proposal for you,
uploads it into Ironclad and kicks off
the process.
I will be honest. We still start every
forecast meeting with at minimum a
10-minute discussion on how we should be
forecast forecast.
We're doing a lot of forecasting. We're
trying to be disciplined. It is a moving
target and a work in progress when the
ground is shifting under your feet as
rapidly as it is in AI and for the labs
today.
It's definitely something where I'd like
to think we're getting a little bit
better at. This week felt like we had a
good forecast call yesterday, but we
still have a ways to go. What's most
important is forecasts are being largely
run by Claude and then inspected and
reviewed by managers.
So, AEs are using stills to make sure
their Salesforce is updated, next steps
are accurate, account notes and account
plans are current. We have a sense we're
a consumption business, so we know where
spend is, we know what the commit is
that we're talking about, we know what
historical patterns have shown for that
type of customer, in that cohort, with
that set of products. And AEs are
submitting their forecasts using Claude.
Managers are then reviewing them because
all of the reconciliation has happened
between Clod and our existing tools and
then submitting them and forecast calls
are for discussion.
They're not for dotches, they're action
oriented and they're focused around
where does the AE need help? Where do
the managers need help? Where do we need
to make sure that the customer needs are
on someone's radar?
What is hopefully coming soon is
forecast accuracy, but we are not quite
there yet.
One other way we've been leveraging our
existing stack that shows up for the AEs
and this one to me is critically
important.
Because when you're absorbing as many
new hires as we are
and when you're operating in an
environment where things change hourly,
I'm confident while I'm up here with you
something will have changed in the AE
ecosystem that I'll need to internalize.
But with product launches, with model
launches, with an incredibly dynamic
competitive ecosystem with many
different flavors of customer needs,
preserving a culture of coaching is
incredibly important. And so we have
tried to really make this part of our
culture for the AEs and for frontline
managers where every week Clod surfaces
six coaching moments and this isn't a
static set of coaching based on a
methodology. This is dynamic based on
how the needs of our business evolve
month over month. What was a priority
last month is not necessarily the top
priority this month, is not necessarily
the top priority next week. And
the most important thing we can do, the
scarcest resource we have is mind share
and ensuring that we're hitting the
coaching moments with the AEs focused on
the most important things as the moment
is the way to ensure we maintain a
culture of coaching.
We maintain focus in the field which is
an incredibly important thing in order
for the AEs to meet the demand and to be
effective.
And we maintain a growth mindset.
Nobody has done this before and if
anyone says they have, they they are
fooling themselves. We are all learning
together and making that part of our DNA
and how we work with our managers, how
we work with the sales team, how we work
with our customers is so important to
showing up authentically and ensuring
that every member of our go-to-market
team is getting even a little bit better
every day.
And what I always tell the team is your
job is to wake up every morning and
figure out how you can make Claude and
Anthropic incrementally better that day
with our customers, for our
cross-functional partners, or for your
deals.
Now, you have to do all of this. Closed
one is my favorite dopamine hit. It's
reliable, it gets me every time, it
never gets old, I never get sick of it.
But, it's a checklist. And when we're
growing as quickly as we are, the
governance of closed one really matters.
You need to make sure you have terms of
service in place, you have a
provisioning path for the customer,
they're getting enrolled in onboarding,
they're receiving an invoice, we have
mapped their orgs correctly. We're a
complex business, we're available on
first-party services as well as through
cloud partners
and sometimes just getting all of the
little admin pieces in place
can accidentally create a horrible
customer experience if you don't get
them all right. personally spent many
late nights inside of our billing system
trying to reconcile invoices when
customers get locked out. This is a very
important part of the cycle.
And so, we have one still per step for
closed one so that Claude can work
across the cross-functional systems and
ensure that everything is in place. We
do this for self-service, too,
to get the customer's account closed,
provisioned, billing set up, and getting
them on enrolled in an onboarding
training.
Again, sales is not an island. There are
so many supporting functions that needed
to have the same elasticity we were
trying to build in the AE org in order
to meet the demand. This is deal desk,
this is legal, this is RevOps, this is
customer support, and we had had I mean
we still do, but it was a gnarly system.
It was a sea of DMs. You needed to have
the institutional knowledge or just
simply be co-located on the same floor.
A lot of AEs would just walk by RevOps
and deal desk desk to try and get quotes
approved. A lot of people on the East
Coast and definitely in Europe were
staying up very late chasing approvals.
We were creating a very unhealthy cycle.
And reps So, what we did is we looked at
this and said,
"These functions play dual roles.
They are there to support the sales team
and enable a customer an excellent
customer experience, but they're also
there to protect the company
and to provide governance to ensure
you're doing good deals that are in
policy that you can stand behind in the
future."
So, with the supporting functions and
all of the systems that they
leverage, which are honestly even many
more than I had laid out, but Jira is a
critical one for us.
We structured this and invested in our
tools so that reps stopped going to
their systems, and rather their systems
came to them.
So, we made Slack the front door.
Slack comes in, ticket out, Claude does
the triaging.
So, Claude actually Co-work now does a
lot of this, and that's changed for us
probably in the last week since I made
these slides, but Co-work can check your
emails and can submit the Slack ticket
in your behalf, or the seller can submit
the Slack ticket. Claude will triage and
either resolve the ticket based on
precedent and policy or it will escalate
the ticket with all of the requisite
customer contacts, all of the history
pulled from email, from Salesforce, from
Gong, and will assign it to a human and
let the AE know that they're in the
queue so that the AE can set
expectations for the customer and can
follow along so that the quote is
resolved, the terms of service is
resolved, the vendor onboarding, the
security questionnaire, all of the
compliance pieces that are required to
unblock and get a customer started.
So, we made Slack the front door for all
of the support functions.
And so then the last investment we made,
and this is the more fun one, the last
investment we made was taking the best
practices of our best reps
and encoding them as stills.
So, this is how we looked at all of the
spaces in between our existing tech
stack, all of the activities and the
patterns that our best reps were doing.
We don't have time or the luxury of
having incredibly handheld onboarding
and a detailed methodology so that we
know when a new rep starts on their
seventh day they'll get their first
account, on their second week they'll
take their first call, on their fourth
week they'll be able to start working
with customers on their sixth week we
expect their first deal.
We aren't able to model out productive
capacity like that anymore. We have to
get reps in the door, they go through
boot camp, we give them a territory, and
we give them a sales plug-in.
And a plug-in is a combination of MCP
connectors and stills,
and we build a sales plug-in that
documented what our top reps do
and turned them into five stills that we
encoded in Claude that every rep uses
every single day.
The first one is the one I talked about
before, but it's so helpful and so
simple
that it merits a second call out, the
morning briefing. I I simply do not know
how I used to operate without it. I am
someone who gets lost taking the subway
home, and it's incomprehensible to me
that I used to navigate my day or week
without Clod telling me every morning
what's important.
So, this is the one we talked about
earlier. The second one is call prep.
The morning briefing will give you the
bird's-eye view of what to prioritize
and how to think about your day.
But before calls, your best reps used to
go on LinkedIn and research
stakeholders.
They used to go through Slack and
Salesforce history to find contacts from
previously closed lost ops.
They would spend time thinking about how
did they want to position? What was
their exit criteria for the call? What
are the right discovery questions?
Clod is now their co-pilot.
We do that back Slash is the shortcut to
summon a still backslash call prep, and
the rep gets a briefing. Who's on the
call? What do they care about? What is
the historical context? What is a great
outcome look like for the call? What are
some discovery questions they should
ask? How should they position? What's
the competitive landscape? What has this
company been saying publicly about their
needs are and where Clod could fit in?
What partners are they working with?
What other tools are they using? Assists
sent one-pager before every call
directly to the AE to ensure even if
they're back-to-back-to-back-to-back,
they can get on that call and provide a
seamless, tailored, and personalized
customer experience. Now, they still
have to read it. Clod does not do that
for them
yet, but I think ever. But
this is a way that even with 5 minutes,
an AE can show up on a call
and know in their bones and manage the
context switching that happens
throughout their day.
The third one is my favorite. Many
things keep me up at night. One of them
is wondering AEs following up on
everything. When they tell a customer
they're going to do something, do they
do it?
The customer follow-up still solves for
exactly this. It will extract action
items from your email, from your Gong
calls, from your Salesforce notes. If
you're working with a customer or a
partner on Slack, it will extract the
follow-ups for you there. It will draft
responses and put them directly in your
email provider and send you a summary of
everything you need to do. And then a
reminder in your morning brief the next
day if you didn't actually go in review
and click send, which you still need to
do because humans in the loop are still
a critically important part of the sales
cycle.
So, the customer follow-up still is so
you can manage all of the volume and the
context switching without missing a beat
and go to bed every night knowing you
have followed up and responded to your
customer. We try to set internally
a 24-hour SLA to follow up with
customers and deliver on action items.
The next still is called competitive
intel. This is a competitive environment
and it is changing hourly, certainly
daily, absolutely weekly.
And there's a lot going on. AEs spend
their days on the phone with customers
and they're not able to necessarily keep
track of every AI newsletter, every
competitive release,
every small product update from our
team, and it's happening over a ton of
surface areas.
So, with the competitive intel still,
rather than having a battle card that
product marketing maintains every
quarter, Claude will generate an
interactive battle card. It will have a
matrix of the customers. It will be
tailored to the customer you're working
on. It's dynamic, it's up-to-date, you
can interact with it, and this enables
AEs to always be ready from a
competitive perspective, and to make
sure on every call and in every customer
interaction, they're positioning Clod in
order to win the deal and provide the
best customer experience.
The last one is very whimsical. It's my
favorite. It's called create an asset.
Previously in prior lives, if you wanted
to build custom collateral for a deal,
you either had to be working on a top
five deal, or you had to have a friend
on the marketing or design team who
would prioritize your work.
With create an asset inside of Clod, for
any deal, any stakeholder, at any stage,
you can generate a completely custom
piece of collateral, and Clod will
surprise you. You can tell Clod what you
want it to do, but you can also let Clod
decide what is the best asset for this
moment in this deal,
with this stakeholder, at this moment in
time, and Clod will generate a
prototype, a one-pager,
a landing page, an interactive HTML
file, a
puppet show, probably not a puppet show,
usually one of the ones I just said, but
Clod will generate that asset for you.
You can generate it while you're on the
call. Some of our reps like to take down
calls when they've had a really good
discovery call and drop them into Clod
code, so that Clod code can build a
prototype,
but they can build a completely tailored
asset. It could be a proposal, it could
be an ROI calculator.
It's designed to assess the deal, assess
the stakeholders, and assess what the
needs are at that time.
This is the only one that got a
follow-up slide, cuz I really do like
this one.
And it's the one where the teams are
really using it all the time.
The stills also know your brand, and
it's so, so nice to not have to worry on
if you've selected the right color or if
your AE is in the right position. We are
very very
you know, we're protective of our brand.
We care a lot about it. We invest a lot
in it. We work really hard.
And we don't want AEs shipping a I heard
AI slop mentioned a lot in the previous
session. So, we don't want them shipping
AI slop to customers. We want it to be
tailored. We want it to be on brand. We
want it to help them win.
This would not be a TED Talk at a
conference if I did not end with four
ways that you can get started today
to make your team a little more I I call
it AGI pills. How can we be an AI native
sales team?
How do we do one thing manually once and
then make sure we've trained Claude to
do it the next time? How can we have
Claude spotting the patterns before we
can because Claude is the co-pilot on
every deal and context is flowing in
between Salesforce and Slack the AE's
brain and back into Claude and Claude is
just getting better and better at our
sales motion and delivering for our
customers.
So, number one, turn on Claude where
it's already embedded.
It's not even just flipping a switch.
It's making sure you're being
intentional and not just saying, "Okay,
great. We're using this AI feature in
Salesforce." It's how are we using it?
And how does it connect to the rest of
the customer journey?
Thread Claude through the sales cycle
you're already running. It's an
accelerant.
And with new capabilities, we've moved
from just deterministic workflows for
probabilistic ones. It is fun to
experiment with Claude and to use Claude
as your coach, as your partner, as your
co-pilot in the deal and to let it make
you better and let it push you outside
of what always got you here and think
about new ways that you can honestly win
and close deals.
The sales cycle you're running works.
So, thread clawed through the sales
cycle you're already running and think
about it from what is the customer
experience, what is the AE experience,
and how can I track and accelerate these
at every single stage. Getting tickets
submitted for deal desk in legal was a
massive accelerant for us. This is not
something you normally spend time
thinking about as a sales leader,
but sales leaders are rapidly becoming
systems thinkers over deal strategists,
and you have to think about the system
in its entirety.
Number three,
really double down there. Make Slack or
Teams the front door of one of your
support functions.
It is a massive enabler, and for
document what your best reps do and ship
it as a scale as a still.
I cannot fully explain the cognitive
relief that comes from knowing that I
can take the best practices of my best
reps and make them baseline for how
everyone else operates, and have total
confidence
that I have made that the baseline.
This was entire depth was brought to you
by Cloudera Design. I did not actually
try to
pitch any product, so we'll put that to
the side,
but it isn't a new stack, and I think
that's the thing I really wanted to
convey today. It's being intentional
about your existing stack. These tools
are incredible. We have spent years
learning them, building around them, and
investing in them, designing them to fit
our sales motion, but if you have clawed
in between and clawed around it to
enable the reps, your people, your
processes,
you can massively increase the
adaptability of your team and the
capacity and productivity that they can
manage.
Thank you.
