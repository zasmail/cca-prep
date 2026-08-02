---
title: MCP: Origins and Requests For Startups
speaker: Theo Chu, AIEWF 2025
source: https://www.youtube.com/watch?v=x-8pBqWiTzk
retrieved: 2026-07-16
method: youtube-transcript-api
word_count: 3014
---

[Music]
right? Hello everyone. Who's excited to
chat about MCP today?
Okay, we can we can work on that. We can
get it a little bit better by the end of
this talk. Uh but I'm Theo. I am a
product manager at Anthropic work on
MCP. Uh prior to this was also a startup
founder uh working in the AI space. Um
couple fun facts about me because
everyone says make yourself a little bit
more personable. Uh is that I like
playing poker mostly losing money at
poker, not uh making money at poker. Uh
and I also really like coffee. So, uh,
if you're, you know, a huge coffee fan,
um, and want to talk about the best
coffee in San Francisco, hit me up after
the talk. But you didn't come here to
talk about me. You came here to learn
about MCP. So, let's talk about MCP.
I was told not to say MCP is the best
thing since sliced bread. Uh, which I
won't say, but mostly because I don't
actually think it's the best thing since
sliced bread. Uh my goal here today is
to really walk you through the origin
story of MCP, why we launched it, uh
give you a better sense of, you know,
where it can actually help you in your
workflow. Uh and then ultimately give
you a sense of the types of questions
that I'm frequently hearing, where I
think there's a lot of value to build in
the ecosystem, and let you decide for
yourself whether or not it is actually
the best thing since sliced bread.
So, scrolling all the way back to uh
midl last year, the co-creators of MCP,
David and Justin, had this idea. Uh they
were seeing that, you know, classic two
engineers in a garage style. They were
seeing that they were constantly copying
and pasting context from outside of the
context window into the context window.
So, you're doing your workflow and
suddenly you're remembering that there
was a Slack message. which was really
important that had a lot of context that
you could just copy in. Um, so you're
constantly kind of copying things back
and forth from Slack. Maybe you're
copying things in from Sentry, your
error logs. Uh, but they were kind of
realizing, hey, it would be so great if
Claude or any LLM could just kind of
climb out of its box, reach out into the
real world and bring that context and
those actions uh to the model. And so
the genesis of MCP was really around
this big question of uh not just context
but model agency. How do you actually
give the model the ability to interact
with the outside world?
And so as they started thinking about
this uh they came to the conclusion that
it had to be an open-source standardized
protocol in order for this to make sense
uh at scale. And the reason is of course
as you all know if you want to build an
integration uh and the you know the the
actor uh or the client in this case that
has to uh leverage that integration is a
is using a closed source ecosystem then
you need maybe a BD or partnerships uh
angle with that client to actually get
access to the team to integrate with
them. You then have to align on the
right interface and then you get to
actually build the thing itself. Um and
so the idea here was that model agency
was the biggest thing that was stopping
uh LLMs from actually reaching the next
stage of usefulness and intelligence. As
we saw that reasoning models were
becoming uh more and more the future
that tool calling was getting better. We
really wanted to make sure that we were
making it possible for everyone to get
involved in that ecosystem and actually
allow uh the models to again have
agency.
Uh so they form a small tiger team
internally uh work on this protocol and
launch it at our company hack week in uh
November of last year. And this was
really the first turning point of MCP.
It went viral as you can imagine.
Engineers from various teams were
working on building MCPs to automate
their own workflows. They were working
on MCPs to uh automate other teams
workflows. Uh this was really kind of a
cool moment to see how it went from
again like two engineers in a garage all
the way to uh this is a major moment in
turning point where we think we actually
unlocked some uh true value for for
other people. And so we ultimately ended
up open sourcing uh MCP in November of
last year and that's when uh we
introduced it to the rest of the world.
But as most builders know, uh when you
build something 0ero to one, you think
the launch moment is going to be really
impactful. But it actually usually is
not. Uh at launch, most people were
saying things like, "What's MCP?" or
even worse, or maybe, you know,
rightfully so, what's MPC? Uh and more
often than not, we got this question of
I don't really understand why you need a
new protocol. I don't really understand
why it has to be open source. Camp
models call tools already. Uh this was
the slew of questions that kind of came
uh again and again for probably from the
era of November all the way even to uh
early uh early this year. And it really
took uh making it possible for builders
to kind of get their hands dirty uh with
building MCPS to automate their own
workflow for for uh for this to take
off. And so the next turning point uh as
Henry alluded to was when Cursor kind of
adopted MCP and after that a lot of
other coding tools also adopted MCP um
VS Code uh source graph uh etc. But we
had a lot of coding ideides um start
adopting MCP and that's really where
that uh next stage of momentum came in
where agent uh agency was given to
builders to actually build uh MCPS for
themselves
and more recently we've seen uh kind of
another turning point where Google,
Microsoft, OpenAI uh and many others
have uh also adopted MCP. So really
excited to see this kind of become more
and more uh the standard. But ultimately
uh standards uh become standards because
they are actually useful to builders.
And so uh I uh kind of want to ask all
of you to to keep us honest. Um
contribute when you see you know issues
with uh the way that the the protocol is
built today. uh or uh if you uh even
want to take that one step further and
submit a PR directly to the GitHub repo
and uh fix the issue that'd be even
better. Um but our goal here is really
to make it maximally useful for uh for
you all and for uh model providers. So
uh thank you for for your help in even
getting us to the point where I can be
speaking on stage uh about this uh less
than one year later.
So just to get a little bit deeper into
uh what we were solving for at the start
of building MCP is again this kind of
idea of of model agency. Um and part of
that means uh agents is kind of the
direction that that we think is is going
to be the future. That's no surprise to
anyone in this room. You are probably
going to hear the word agents said in
every talk if not almost every talk. Uh
but the way that we think about agents
is that you are giving the model or
you're rather depending on the model's
intelligence to choose actions and
decide uh what to do. Uh in the same way
that you know maybe when you talk to a
human and you ask them uh for a
response, you don't know exactly what
the response is, but based on your
understanding of maybe the task that
you've given them, your hope is that
they are going to give you the right
response. And uh we want to kind of
enable that world where you're uh uh
depending on the model's intelligence
scaling over time. So uh that leads to
principles in how we actually build the
protocol itself. Uh recently we uh
launched the support for streamable HTTP
which uh changes the the transport from
SSE. uh and as you all might know
streamable HTTP is is more the uh
enables more birectionality and so that
was uh a very controversial decision
actually but uh if you're keeping agents
in mind as the future makes a lot of
sense because you want to make sure that
agents can kind of communicate with each
other. The other thing that we believe
uh is that there will be a lot more
servers than there are clients. Uh this
we could be totally wrong on this. Uh I
would love to see where the future plays
out. But because we think that there
will be a lot more servers than there
are clients, uh we optimized for server
simplicity and for the server uh server
builders to have better tooling. And
that does mean when we have to make a
trade-off between client complexity or
server complexity, we tend to optimize
for pushing the complexity down to the
client. So apologize in advance to
client builders. Uh but it was an
intentional decision. again uh would
would uh be curious to see if if this
plays out uh the way that that we
thought it would.
So I'm going to speedun through uh some
project updates mostly because other
talks are going to go much more in
detail here. Um but last six months we
launched uh ability for uh folks to
build remote MCPs.
We fixed o
which we got wrong initially. Thank you.
Uh I know that was a huge huge thing
that that we got wrong initially, but it
is now fixed uh in the draft spec and so
would love folks to you know continue
helping to push on on these things that
they see don't match their mental model.
Uh this was actually fixed via a series
of of people from the community jumping
in to work on saying hey this is how you
know uh O works with identity providers
and here's how we can update the
protocol. So very much a community uh
community effort. Um again uh launched
removable HTTP as the primary transport.
Uh and lastly made a couple of updates
uh to developer experience um by
updating our SDKs and also uh making
updates to inspector which if you aren't
familiar with is a really good uh
debugging tool for for your server. I
think it is probably our most
underutilized uh tool.
Looking forward, we're going to be
focusing a lot more on uh that agent
experience. So, we just added
elicitation uh to the draft spec. This
uh allows servers to ask for more
information from end users. So, you can
imagine you're building a uh maybe
you're building a flight booking tool
and uh the end user says, "Hey, book me
the best flight to Atlanta." And so as
the server you have a question which is
what does best mean to you? Is it
cheapest or is it fastest? So you ask
the end user uh and now you can pass
through that elicitation. The end user
can respond and have that response
ultimately sent back to the server. Uh
we are also making progress on the
registry API which would make it a lot
easier for models to actually find MCPS
that weren't already given to them up
front. So this is again kind of on that
theme of model agency. Uh we're really
betting on the intelligence of models
going up over time.
Again working on uh developer
experience. We've heard often from you
all that there are uh that you know
you'd love to understand what kind of
the best patterns are in the ecosystem
or what the standards are. And so we
want to make sure that there are open
source examples that uh that both we've
contributed to and also the community
can contribute to to kind of help build
those standards and patterns together.
And lastly uh we're making sure that MCP
stays open uh forever and we are
investing heavily in thinking about the
next phase of governance. Uh so there
will be more updates on that soon.
And just to do a quick call out to uh
the graphic in in the bottom. So a lot
of people have asked uh us what it looks
like to actually build an agent with
MCP. Our take is that an agent really
is, you know, just a server acting as a
client and vice versa. Uh where you can
then kind of chat back and forth with
other agents, uh other servers, other
clients. Um so I won't go into too much
detail there. I know a lot of other
people are going to be uh talking about
agents in more detail, but just wanted
to make sure that uh I call that out
here.
So, the uh thing that everyone has
probably been waiting for and that I've
been told uh over and over again when
when I talk to founders uh what they're
asking me about is uh what should I
build in this space? you know if uh MCP
becomes a standard what is where are the
interesting opportunities so before
jumping into this the first thing I'll
say is that we are really early right
now and that means that even if the
standard exists we still need the
ecosystem to be filled out and I uh
would urge you to build more and more
and more servers if I had to put a
waiting on these three bullet points I
would put 80% on the first one 10% on
the second one and 10% on the third one
Um so we have a lot of opportunity to
build a lot more servers uh that are
higher quality uh and for different
verticals. Um and just to touch quickly
on what I mean by higher quality. Uh a
lot of people you know maybe hot take
but I think a lot of people are wrapping
their API endpoints one to one and just
exposing that as tools. I don't think
that's the right way to build an MCP
server. That in and of itself could
probably be a 20-minute talk. Uh but
what you really have to remember when
you're building a server is that you
have three users. You have the end user,
the client developer, and the model. So
a lot of people forget that the model is
a user here as well. You want to uh just
as you would for API design, you want to
think about what are the use cases that
your end users are going to have. What
are the prompts that they might actually
be uh putting into the the model? and
ultimately what are the tools that you
then need to expose to the model to
enable the model to respond correctly to
those uh to those prompts. So uh higher
quality servers uh and also servers for
different verticals. A lot of the
servers today um have been for dev
tools. We would love to see uh this
expand to be useful beyond engineers
into verticals like sales, finance,
legal, education, pick your poison, uh
whatever you know best. um that uh we we
would just love to see more servers. The
next piece is on simplifying server
building. So again, as I mentioned, we
believe strongly that uh servers are
going to be the vast majority of the
ecosystem. There will of course be a lot
of clients as well, but we think the uh
order of magnitude of of servers is
going to uh outweigh the order of
magnitude of clients. And so would love
to see a lot more tooling to actually
make it easier and easier to build
servers. um both for enterprises uh that
are deploying MCPs internally uh as
interfaces between teams and for indie
hackers uh and everything in between
that uh are building MCPS for external
users. So anything from hosting tooling,
testing tooling, uh eval deployment,
etc.
And then uh I snuck a bullet in here
that's maybe a little bit more of a
moonshot and a bet on the future, but
the uh there's a bullet for automated
MCP server generation. And uh again, if
you kind of think back to our bet on
model intelligence and model agency for
the future, uh at some point models will
be so good at writing code and
interacting with the external world that
they will actually be able to write
their own MCPS on the fly in real time.
And so, uh, this might be a little early
for where we are today, but I do think
that there will be an opportunity for
automated MCP generation, um, as models
get smarter and smarter.
And, uh, last but not least, uh, wanted
to do a quick call out for any tooling
around AI security, observability, uh,
auditing, etc. I don't think this is
actually specific to MCP. This is true
for any AI application. But I think the
more that you enable those applications
to have access to the outside world to
start playing with uh real data uh of
course the security and privacy etc
implications also go up and so I think
if you're going to build uh a startup in
that space now is is the time.
So with that uh happy MCP. Thank you.
[Music]
