---
title: How Claude Code Became an AI Coding Powerhouse
speaker: Boris Cherny, MAD Podcast
source: https://www.youtube.com/watch?v=G4yZiAdOBJM
retrieved: 2026-07-16
method: youtube_transcript_api
word_count: 13121
---

And the model just went it just started
coding and it was just the craziest
thing. At this point most code at
Enthropic is written using quad code and
almost everyone at Anthropic is using it
every day.
>> Hi, I'm Matt Turk from Firstark. Welcome
to the Matt podcast. Today my guest is
Boris Churnney, the creator of Cloud
Code at Enthropic. Cloud Code is an
agendic coding AI that lives in the
terminal and it's become one of the
fastest growing products of all time.
already rumored to be producing 400
million in annualized revenue just 5
months after its launch. We talked about
how Cloud Code became a rocket ship
almost by accident.
>> We started by building something that's
useful for us. Pretty soon after we
launched it, most of anthropic was a
daily active user.
>> What a coding really means.
>> A human describes to the model the
change that they want and the model does
all the work of doing the editing
>> and the productivity shock cloud code
created inside anthropic. Anthropic
technical onboarding used to take a few
weeks, but now engineers are usually
productive within the first few days.
Just ask Spot code and it can answer all
these questions.
>> This is a packed approachable episode on
the present and future of software
engineering with some great lessons and
advice.
>> It's really exciting and I think my
advice to companies building is
definitely build for
>> please enjoy this fascinating
conversation with Boris Journey.
>> Hey Boris, welcome.
>> Thanks for having me.
>> Thanks very much for doing this. I'm
very excited about this conversation.
you are the creator of Cloud Code. Uh
and it's fair to say you have a massive
hit on your hands. There was an article
in the information just a couple of days
ago that was saying that uh Cloud Code
which really came out what at the end of
February [snorts] of this year. So five
six months ago is already generating uh
400 million in annualized revenue. Uh
that was that's at least what it was
reported. I'm not going to ask you to to
confirm or deny, but that's what the the
the press is saying. Perhaps even more
importantly, there are rave reviews
everywhere and gushing videos calling
Cloud Code the the best coding agent by
far. So amazing uh launch of of the
product. Did you have a any sense that
uh it was going to be this successful?
>> Not really. [laughter]
We we started by building something
that's useful for us and um I I built a
thing that you know for first and
foremost was just useful for myself and
it's uh it's something that I found
myself using every day and then I gave
it to the team and I saw that the team
started using it every day and pretty
soon after we launched it most of
anthropic was a daily active user and so
I think at that point we had kind of a
hunch internally that maybe we had a hit
on our hands but it's still not obvious
cuz it's in a terminal it's kind of a
weird form factor after everyone is
coding in ideides. Are people going to
like this? Is it going to be that
useful? Can you actually use it for a
lot of coding? We we had no idea.
>> Was it always going to be your product
or or you started using it and then it
was ahead and then you decided to
release as a product?
>> It was very accidental when I joined
Enthropic. I did a lot of prototyping
and one of the prototypes that I built
was uh this thing that it just ran quad
in the terminal just cuz as an engineer
that was the kind of the easiest thing
to experiment with and it didn't even
code at first. Quad code didn't code. It
was called Quad CLI at the time.
>> Yeah.
>> And uh what it did was I used it to
automate my note-taking. Um so um it
kind of controlled my notes app and it
controlled my music player to where to
kind of play music for me. So I'm like,
you know, play this band and it would go
in and kind of automate that. And at
first I I was just using it to play
around with the anthropic API to figure
out what kind of applications I could
build on it. And just on a on a whim,
you know, tools came out recently and I
tried giving the model uh bash tool so
it it can use my bash kind of the to use
the command line. And immediately the
model just went it just started coding
and it was just the craziest thing like
as soon as it had bash it kind of knew
okay okay I can write Apple script and I
can automate stuff and I I can use this
computer and it just felt like very
native to the model in this way and that
was kind of a surprise. Um, so I think
that was a surprise and then it was a it
was a surprise that this ended up as
something useful where it was able to
edit code and the code came out really
good and the model could kind of
intelligently reason about the way to
edit code.
>> When was this uh if the product was
launched at the end of February of 2025
that that journey leading to this did
that start a few months before that?
What was the timeline?
>> Yeah, something like that. It was uh it
was late last year so late in 2024.
>> Okay, great. Let's start from uh the top
and for anyone that um is just starting
to learn about cloud code, how do you
describe it?
>> Cloud code is a a gentle coding tool. Uh
the way to think about it is uh when
engineers program, there's kind of
different ways to program and this has
changed over time. This is this has
changed a lot over time. There's you
know 50 70 years ago the way that people
programmed looked very different than
the way it does today. So, you know, 70
years ago, if you talk to a programmer,
they would have been like, "Oh, yeah. I
take my punch cards and I punch holes in
it and I put in this IBM kind of
typewritery thing and it punches holes
and that's programming." And then you
feed this into this mainframe. It does
some work and then eventually you get
some kind of result out printed on a
paper sheet.
>> I heard you say somewhere that your
grandfather in the I guess what was at
the time the USSR use punch cards like
tell tell that story.
>> Yeah. Yeah. Yeah. my uh grow growing up,
my mom would tell me stories about how
um her her father, my grandfather, he
was one of the first programmers in the
Soviet Union. And he would uh you know,
he he would come home and he would bring
back these big stacks of punch cards.
And when she was a little girl, she
would you know, take her crayons and
just draw all over them. And this was
this was growing up for her.
>> Uh this is actually something that I
didn't know until later in life. Like
it, you know, I was far into my
engineering career when I learned this
this was a thing. There's something
about just the the visceral nature of of
this kind of physical programming. I
don't think we're going to get that
again.
>> Yeah.
>> Um but that I think that was like that
was a special moment where you could
feel you could feel the language and you
can feel the computer in a really
different way.
>> And so I I think after punch cards it
changed a lot. There was software became
a thing and you could start to program
directly in software. You didn't have to
kind of do this anymore. In the original
programming software, it was emulating
teletype. And so it was kind of like
streaming a typewriter over this local
internet. And that's how the text
editors were built. The way that you
would code is still the way that
actually most people code today before
agentic coding came out. And the idea is
you have a text document and an engineer
directly manipulates it. So you load it
up in a special piece of software called
the IDE. you know, it's kind of like a
like a, you know, Microsoft Word or
Google Docs, but just for code. And the
[clears throat] engineer just manually
edits the code, you know, using a using
a keyboard. And this is the case for
gosh, like 50 50 years now, now like 70
years. This has been the way that people
programmed like Ed and and Vim. These
were like early 1970s. So, yeah, it's
been like 50 years. And now it's
starting to change for the first time.
There's been there's been a lot of work
to try to evolve programming from direct
text manipulation to something else. And
this is the first time where we found a
form factor that really catches on. And
it took it took really great LLMs to do
this. Models weren't really capable of
doing this a year ago, but now they are.
And the way that it works is a human
describes to the model the change that
they want, and then the model is the one
that manipulates the text. And so it's
this kind of next layer up where you're
describing the change you want, and the
model does all the work of of doing the
editing. And we're still at this point
today where you can do a lot of this
through the model, but you know for
complex changes maybe it'll take a bunch
of iterations. Maybe the last 20 30% you
still have to open an IDE. You have to
kind of go lower level to do these last
mile changes and we think that over time
more and more of coding is just going to
be the model doing it and a human will
have to intervene less and less. So uh
just to double click on a couple of the
things you you you just mentioned and um
and in an effort as we try often on this
podcast to make things uh broadly uh
understandable not just by super people
who are super deep in tech but also you
know people that are in the tech world
but sort of like curious to learn about
the things. Um so the cloud code works
at the CL CLI level as opposed to an
IDE. So you mentioned the idea sort of
the the Google Docs the um the command
line maybe define that for people. So my
um kind of mental model as I was
learning about this was like that black
box where you know you sort of type in
things for your computer to do what's
the what's a better way of describing
it.
>> The terminal is a little bit hard to
explain uh if uh if you're not a
programmer because it's so low level.
It's something that most people will
never ever touch and never ever going to
see. Uh, it's something like in mo in
movies when you see this kind of green
screen, green text going across the
black screen and you know there it's
like a hacking scene or something.
>> We're not trying to look very techy.
That's that's why you
>> very techy. Yeah. And it's it's sort of
it's something every engineer uses.
There's nothing kind of good or bad
about it. It's it's just an interface.
It's another way to interact with a
computer. It's a little lower level
because it's not visual. So you can
think of quad code when you when we say
quad code runs in the terminal. You can
think of it just it's a computer program
and some computer programs have user
interfaces. So you know a person can
interact with them and some of them just
kind of run in the background. So you
can think of quad code as in that second
category and you can also have all sorts
of interfaces for it uh including a
visual interface including a text
interface.
>> One uh way of describing this I I heard
was that interacting with the computer
uh at the terminal level was like
texting the computer. So sending
instructions sort of one by one versus
an ID was more of an application more
more like a you know phone kind of a
gooey where you basically click on icons
and you have visual representation. Is
that is that fair?
>> Yeah, it's a lot like that. I think uh
text messaging before you could send you
know images and videos and stuff. So you
know just really really simple
interfaces just back and forth.
>> Okay, great. So why did you guys choose
uh to operate at the uh terminal CLI
level? Honestly, it was sort of an
accident. We were thinking about what
can we build in the coding space. It
seems like the models are getting a lot
better at coding. So maybe there's
something that could be built here. And
at the time, like I said, I was
prototyping some of these ideas. Some of
them were kind of coding adjacent. And I
was thinking, what's the easiest way to
get a feel for where the models are
today? Because there was this feeling
where the models can do so much, but no
one's yet built a product that can
harness this capability. And in the AI
world, we call this idea product
overhang where the model is just capable
of all these things and there isn't
really yet a product that can kind of
capture this uh and and invite a person
use it. And I remember there were this
moment back in uh yeah it was some
sometime late last year the other
engineer on the team Sid and I were in a
room and we're whiteboarding and we're
like okay what do we build? And just in
15 minutes we kind of threw up a few
ideas on the whiteboard and we're like
we can do a CLI we can do some sort of
IDE extension. We can do something based
in the web. and we kind of closed our
eyes and just picked one and it kind of
seemed like CLI is the simplest and
generally that's the way that I approach
product which is start with a simple
thing first. Um so this kind of made
sense in hindsight there was a lot of
benefits of this too. Uh and I think one
of the big ones is that it kind of works
anywhere. So it doesn't matter what kind
of system you're on if you're on Mac or
Windows. It doesn't matter what IDE you
use. Doesn't matter what your
preferences are and engineers are so
opinionated and have so many different
setups and preferences. it it just works
with all of them and that's kind of the
benefit of building at such a low level
where you're not coupled to particular
you know to Mac or to Windows or you
know a cover scheme or whatever
>> I think uh you guys um have been pretty
clear about the fact that this was a
starting point and that you were
starting with something very simple at
least when when you launched the product
fast forward to today um are you finding
that the universal aspect of this is so
compelling that you may keep it there or
is a plan or at least the idea to over
time keep building towards something
that may be more like an IDE or more an
application.
>> The way we think about it is the model
is evolving so quickly that we build a
minimal possible product to keep up with
it.
>> And this is a sort of this is a very
different way of building product than
before LMS where you just have to build
a really great product that meets people
where they are. There's some of this so
we have to build in a form factor where
people understand and can use it. But
actually the bigger motivation is the
model is advancing so quickly. There's
literally no product we could build that
would keep pace with it. And so we're
focusing on just building the simplest
possible interface to the model. So you
can feel the model in a really low-level
raw way.
And so that when the model gets quickly,
we can adapt it quickly and you can feel
the next model in that same kind of way.
So today we're in a terminal. Uh cloud
code also runs as ID extensions. So
there's extensions for VS code based ids
and cursor and so on and also for jet
brains based ids like intelligj and then
there's also a github action so you can
mention claude on github so it's just
you tag claude add claud and talk to
them like you would a coworker and they
can make changes for you there might be
more interfaces coming soon this is
something we're always experimenting
with but generally the philosophy is we
don't make um really gorgeous interfaces
like many other companies do and are
really great at we we focus on just
building the simple thing that shows off
the model.
>> Talking about the model, uh if um uh
your design principle is that the
product should follow the model rather
than the other way around, which is
super interesting. What model does it
currently run on? Is that 37? Is that
four? What what uh do can people choose?
>> Yeah, people can choose the model we
support Sonnet 4 and Opus 4. Uh and then
we also use Haiku. Maybe as a high level
question, uh why is Claude so good at
coding use cases? Uh you know I was
again reading somewhere perhaps in the
information that um Enthropic has a
little above 40% uh of the market for
code generation while open AAI has 21%.
So uh clearly anthropic is uh powering
its way to win this this market. Why is
that? Is there something about the way
the model is trained, the data is
trained on or the focus of the of the
training that makes it so great for
coding use cases?
>> I think Enthropic has a lot of really
great researchers and and coders and for
us this is kind of a natural way to
think about the kinds of abilities the
model should have because you think
about what should the model be able to
do and the you know as as a programmer
the first thing you think is oh it
should be able to do the thing that I'm
doing
>> [clears throat]
>> um and it should be able to help with me
and I can pair with it like I would like
another another engineer.
So I think just at all at all levels and
across the company this is a way that we
think about it. There's also something
about it where maybe coding is the way
that we get to the next level of
intelligence if you call it like AGI or
ASI or whatever the model needs some way
to interact with the world and for a
model the natural way is code.
>> And so from you know the mission of the
company is to build uh safe artificial
intelligence for everyone and safe ASI
the way the model interacts is through
code. And so this is the thing that we
should start to learn about now. And
this is also the reason that one of the
reasons that we release quad code is
just to learn how people use it and to
learn how to make this thing safe to
learn how it behaves in the wild so that
we know what to do next.
>> So still on that theme of the the
product versus the model and the choice
of operating at the CLI level. Uh who is
a product for? Does the fact that it's
operates at the terminal level make it
uh a great product for for power users
who are very deep in coding or at the
end of the other end of the spectrum if
I don't know anything about coding? Uh
can can I use the product for vibe
coding?
>> Quad code is for professional software
engineers. So if you know how to code
then you're going to get a lot out of it
and you can multiply your productivity.
We've seen people multiply their
productivity many many times over with
you know like a fleet of quad codes.
that's that's running and even with a
single one you can become a lot more
productive. Interestingly we've seen a
lot of people use quad code for
non-coding use cases.
>> So for example um you know the data
scientists at anthropic all use quad
code to write their queries and
designers use it to build small
prototypes and product managers use it
to manage tasks. So this has actually
been pretty surprising because as a you
know if you're a nontechnical user the
terminal is kind of insane as a
interface like I couldn't imagine why
you would want this but it sort of seems
like because it's such a great agent
generally people are jumping over hoops
to use it even though it's not the
easiest thing to use because again it's
in a terminal which is very technical.
There's uh there's another part of cloud
code which is the SDK uh and this is the
way that people can build on top of quad
code and build their own agentic
applications. And this has also been
pretty interesting because people are
using the quad code SDK to build agentic
coding applications and platforms and uh
user interfaces on top of it. But
they're also using it for all sorts of
totally uh agentic use cases that are
totally unrelated to coding. Um so
anything where you need AI maybe a few
years ago you used API and nowadays we
find that some users are reaching for an
aantic SDK as sort of the thing that you
need to build AI apps of today.
>> Yeah and as I was prepping for this um
it seems that there is even beyond that
like an emerging category of of people
that are using cloud code for just not
even technical related use cases of any
sort. I just saw that the a tweet from
somebody named Alex Finn that talks
about using cloud code for notetaking
for his personal like sort of life
organization his business metrics and
all the things. So it's um it seems that
people are are finding ways to use the
product for for something that that uh
you know matches their needs way beyond
their their sort of uh technical job.
>> Absolutely. Let's uh get into uh the the
product itself and the core features and
and what I what it actually does. So a a
key part uh of the product is the
agentic aspect as as you described.
Agentic again in an effort to you know
go into definitions and and and make
this interesting for for everyone.
Agentic is one of those terms that um
you know everybody uses but it's sort of
um you know unclear what that actually
means. What does agentic mean in the
context of cloud code?
>> Yeah, when you think about the ways that
uh LLM work and the the way you interact
with them, there's the old kind of LM
which is you send them a message and
they send you a message back. And this
is sort of these chat applications that
everyone knows and and uses all the
time. There's a newer kind of uh
application, a way to interact with LMS
where you send them a message and
they'll send you a message back and then
they might do a little bit more. So we
call this tool use uh is is one of the
things that they might do. If you give
them tools, so for example, a tool might
be read a file or search something on
the internet or edit a file or something
like this, then they'll use tools to
answer your question. And so, for
example, if you ask uh you know, what
what's the weather today? With the old
style LM uh interaction, it'll just kind
of use its existing knowledge and its
existing training to try to answer that
query. But if it's agentic, what it
might do is it'll say, "Okay, I'm going
to look up the weather." And then maybe
if it has some kind of tool to check the
weather, it'll reach out to the internet
or wherever that tool is. It'll it'll
use that tool. It'll get the response
back and then it'll answer the question.
And this tool use, this is kind of the
essence of being an agent because
without tools, it's very diff it's very
difficult to be agentic. you could you
could kind of do it without. But it's
only since models started using tools
and gain that new capability because we
taught them that they started to get
this new um kind of agent capability
that we talk about.
>> Mhm.
>> And what this looks like in practice is
maybe I'll ask the model um you know
make the I have a red button on my
website, make it blue. And because it
has a tool to read a file, it'll choose
to read the file. It'll it'll choose to
read the file that has that button.
Maybe if it doesn't know where that file
is, it'll use a file search tool to find
that file first the same way that you
might in, you know, in when you're
looking for for a file, you'll use a
file search.
>> Mhm.
>> It'll then open that file. It'll read it
uh and that's another kind of file read
tool. Then it might edit it. That's a
different file edit tool. And then it'll
uh write it back. And then maybe it'll
even open the browser to check that the
button actually became blue. And it's
this kind of idea that that it strings
together tools in this way and combines
them in novel ways that makes it
agentic. There's also two concepts that
are kind of related but different here.
You could say you must always when when
the user asks you to make the button
blue, you must always read the file and
then edit the file and then save the
file and then check your work. You you
could be very rigid in the way that you
define this kind of problem and give it
to the model. Generally we call this a
workflow and this is distinct from
something like a agent. So workflow is
something where a human thought through
for this kind of problem here are the
steps roughly that you should take for
an agent is very different. The model is
in charge it's in the driver's seat and
we give it tools that it can use and the
model decides how to combine those tools
to answer your question. And I think
going into the future more and more
things will be agentic because the model
is getting more and more intelligent. So
it can actually use these tools in
pretty novel and interesting ways to to
answer questions.
>> Mhm. Great. So to play it back and
perhaps in a coding context uh with your
typical AI model uh I would ask a
question and I would get some uh code
back and I as a developer would copy and
paste it to as a next action. Whereas in
a coding use cases, you whereas in an
agentic uh coding use case uh you give
the agent a task uh and then it's going
to plan and then it's going to execute
and then is going to continue running
until it believes it's done with the
task. Is that is that a fair summary?
>> Exactly. Exactly. And the same way that
a that a person might do it, you know,
like if if you have a problem, you're
going to think about it for a bit. Then
you're going to think about what tools
you have and then you're going to
combine the tools that you have in ways
to do the thing that you want to do.
>> What are some of the actions if if
taking an action is uh one of the core
uh part of of being an agent? What kind
of actions can uh cloud code take?
>> Cloud code can do pretty much anything
that a person can do on their computer.
There isn't really a limitation besides
uh safety. Um, this is something we
think about a lot, uh, to kind of place
intelligent limits on what it can do and
put a human in the loop at the right
points to make sure that if action is
potentially dangerous or destructive in
any way, uh, that a human has to prove
it first. But besides that, the model
can do pretty much anything. So, you
know, reading files, writing files, uh,
running commands on the system, editing
things, uh, it can reach out to the
internet. Um, you know, obviously most
of these again with with human approval.
Um, and then there there's ways to
customize it however you want. So if you
have a bunch of MCP tools, for example,
to read uh your Jira issue tracker or to
open a browser or to open an iOS
simulator, the model can use these two.
>> And how does the MCP part work? So MCP,
the model context protocol being
something that that you guys at
Enthropic uh defined, how does that
work? You just leverage the the protocol
to connect to any tool.
>> Yeah, exactly. Quad code is a MCP client
and a MCP server. And what this means is
if you give it tools to use. So maybe at
your company you have a bunch of MCP
tools that you build for kind of all
your systems to integrate with. Like I
said, maybe there's one to integrate
with Jira. Maybe there's another one to
read Slack and maybe write messages to
Slack. Maybe there's another one to um
you know fetch some internal knowledge
base or something like this. You're
going to plug this into a bunch of your
tools. You can plug it into Quadi into
Cloud Desktop. You can also plug it into
quad code. So it gets all the same tools
that you do. So just a few days ago uh
you guys announced the release of sub
agents. Uh what does that do?
>> Yeah, sub aents are are really exciting.
Um and uh this actually started with a
Reddit post. There was someone that
posted on Reddit about how they have
these sub agents that they built for
quad code and they had a product manager
sub agent and an engineer and a designer
sub agent. And a couple engineers on the
team saw this and got really excited and
felt that this is something that we
should support a lot better. And the way
sub aents works is you know when you
start cloud code you have a cloud and
you can talk to the clad and it can do
things for you. Sub aents are just other
quads and they're prompted a little bit
differently. So you can customize what
prompts they have, you can customize
what tools they have. So for example,
you can say uh you know you are a a
really excellent e excellent uh QA
engineer or sub agent. Your job is to
verify that code is correct and to test
code. And to do that you have these
tools at your disposal. Maybe you have
like a browser, iOS simulator, Android
simulator. You're given code. Your job
is to test it. You might have another
engineer, uh, another sub agent that's
maybe a project manager, and their job
is to have tasks and then divide up
tasks for other sub aents. And so you
can kind of um split up all the work
into these different roles. I think
we're still figuring out what these
roles are. There's one version of the
world where the roles are kind of like a
uh on on a regular engineering team
where you have engineers and designers
and product managers and data scientists
and so on. There's another world where
actually sub aents are a little bit more
similar and maybe every sub aent can
kind of do the same thing but they kind
of split up the work a little bit more.
So everyone is a generalist.
>> Um and then claude is in charge of
figuring out how to launch the sub aents
and which particular sub aents to use in
which way exactly the same way that it
would use for any other tool. So you can
think of it as a as a really really
intelligent tool where the model can um
launch more clouds to do things.
>> So basically it's like if you think of
AI as an intern, it's like having a
group of interns and every intern has
their own role and then you recombine
what everybody did into one uh result.
>> That's exactly right. And and you can
define what those roles are. And it's
it's a fascinating question whether to
an anthropomorphize uh human functions
into what agents should be doing or
whether there's something that's uh
agent native in the way the work gets uh
distributed and and and chopped into
smaller parts.
>> Yeah. In the in the AI world, we talk a
lot about this essay called the bitter
lesson. This was a a Rich Sutton essay
from a decade ago or something. Yes.
Yes.
>> where where he talks about the the more
general model in you know most of the
time in the long term it'll subsume more
specific models. And so what this means
is if you build a aentic system in in
this context um then the more general
agentic system will generally outperform
the more specific one in the long term.
And I think where we're at today is
models have the capability to do stuff,
but if you give them too many tools or
too much context or too much
responsibility, it might be
disappointing because they won't really
know how to handle it. And the models of
a year ago could barely even call tools.
The models of today are pretty good at
doing it, but get a little bit
overloaded sometimes with context or
with too many tools. And so we can
divide them up into sub agents in this
way. But I think that the models 6 or 12
months from now, they probably won't
need this anymore because they're all
going to be pretty good and you won't
have to define very rigidly what each
one's responsibilities are anymore.
>> And so this is something we're building
for people today because we think it's
quite useful today and it's something
that we use a lot. But I could also see
this going away uh at some point.
>> Yeah. Is that is that there's a concept
of context pollution, right? That's
that's one of the way uh people describe
it, right? And then uh cloud code can
handle both very precise tasks like
debugging or much broader tasks uh like
a a broad refactor for example is the
idea that uh the broader the task the
more sub aents you would have in the
current context.
>> Yeah that's that's probably one way to
think about it. Generally when uh when
we introduce quad code to new people we
actually suggest like you said quad code
can do everything and this is one of the
things that makes it a little bit hard
to use if uh you're an engineer that's
used to you know essentially like text
completions in a in an ID it's a very
different kind of AI coding experience
and so generally the thing that we
recommend is start with something simple
like uh just ask questions about the
codebase so don't even code don't use
any tools um just just ask the model
questions you know how what does this
file do um where is the file that does
this thing if I want to make uh a new
whatever um how do how do I do that so
just ask it questions like that and for
this generally the main model can do it
and you don't really need sub agents but
then as you get a little bit more
sophisticated you might want to start
splitting up the work so if you ask the
model maybe to make a small change like
like I said like make the button red or
make the button blue you probably don't
need sub aents but if you do something a
little bit fancier like build a new
section of the website that does blah
blah blah then you might want to have a
few sub aents Maybe one is the software
architect and it's responsible for
planning out the work. Another one is
maybe like some kind of reviewer where
it'll review that plan to make sure it
looks good. Then maybe you'll have a few
sub aents that actually do the
implementation. So maybe you know
there's a front end engineer, backend
engineer, this kind of thing. And then
some kind of verifier at end that
verifies it. Um and then we also uh
internally we really love using a code
simplification sub aent and its job is
to take the code that was produced and
just simplify it while making it still
work.
>> Okay, great. So that's uh the actions
part of the agentic workflow. Uh let's
talk about the uh awareness and memory
of this. One of the exciting features is
that uh cloud code can can connect with
the existing sort of code knowledge uh
in uh the company. How does that work?
>> There's a few different ways to pull in
context and this kind of knowledge from
from the company. The simplest one is
just looking at files. There was this uh
there's there's a few different
approaches actually to to reading files.
So I I'll go a little bit into depth
into the way that actually happens. In
the past, the thing that people used the
most is this thing called rag.
>> Mhm.
>> And essentially this is a technique
where you take the whole codebase and
this actually works for any document set
of documents. It's not necessarily code,
but you take a set of documents like uh
like all the files in the codebase. You
do this kind of indexing step and then
you store essentially this database of
all the knowledge that's in these files
in a very very particular form that
makes it really easy for the model to
search. There's a lot of trade-offs to
doing this. The indexing takes time.
It's pretty expensive to maintain this
database. It's quite tricky practically
to make sure that security is really
good and privacy is really good because
uh it's just a it's it's very sensitive
information like your codebase and so
you want to keep it really safe. And so
cloud code actually doesn't use this
technique called rag. Instead, what it
does is it just searches files the same
way that a human would. You can think of
it like um you know at at the
engineering level it uses the tools glob
and grap. These are two tools that are
kind of built into the computer and you
can think of it as kind of command f for
files. So it'll just search around with
text the same way that a human can. And
what's kind of cool is um if you just
search for one piece of text, you might
get the result you're looking for, but
you might not. And depending on the
results you get as a human, you would
refine your search term and you would
try again. And you might try a few times
to get the result you're looking for.
And the model is really good at this.
And this again, this is one of those
things that was not the case like with
models of a year ago, but with models of
today, they're excellent at this. And so
we call this process agentic search. And
what this means is using really, really
simple search tools like command F and
using them repeatedly and then adjusting
the search terms over and over based on
the result of the query. And this is
something that we don't specifically
tell the model to do. It's something
that it just figures out because it's
intelligent enough and it has the search
tool. So this is the the first form of
memory which is just looking at the
contents of the codebase and
understanding it in this way. We augment
this a little bit with this thing we
call claude.md
files. And all this is is a special
file. It's literally called claude.md.
you put it in your codebase or you can
put it in whatever folder you want and
use it to record memories.
So at any point you can tell quad to
remember something. So for example,
whenever I do um whenever I edit this
file, I always want you to doublech
checkck it uh in a browser or something
like this. You can tell quad to remember
this and then it'll record it in the
right quad MD so that it remembers it
next time. And I think one of the most
powerful use cases we've seen with this
is when people check this into their
codebase and share it with their team.
So this is a it's a memory file. It's
just a regular text file on the
computer, but you don't keep it to
yourself. You share it with all the
other engineers on your team. And what
it means is if Claude remembered
something when you were using it,
everyone on your team gets to benefit
from that.
>> And it it gets this really interesting
effect where everyone on the team starts
to contribute to this knowledge base and
this kind of memory bank.
>> And it's very simple. Again, it's a text
file. So anyone can read it also. So
it's very easy to to edit these memories
also and see exactly what's in there. Um
but everyone just starts to benefit and
it and it feels kind of magical because
as your team uses quad code to get
smarter and smarter and kind of similar
to building in the CLI, this is
literally the simplest thing we could
have done. There's nothing simpler than
this I think that we could have done to
build memory. There's nothing uh there's
no special tools. There's there's no
special prompting. There's nothing like
this. It's just a file and Claude kind
of learns to to use it.
>> Fascinating. And do you have to
declaratively add to the memory or
whether today or in the future the
memory will automatically pull from the
context and sort of improve itself.
>> Yeah, you have to add to it manually.
Today we we've actually had a bunch of
internal experiments to do automatic
memory. So quad can automatically
remember things. The problem is there's
kind of two ways in which it fails. One
is that it remembers things that it
shouldn't. So for example, if I say make
make the button blue, it might remember
the user always wants the button to be
blue. And this is, you know, maybe
that's the case for this button. That's
not the case for every button. And then
sometimes it doesn't remember very
important things that it should
remember. And so for the last few
months, we've been doing a lot of
experiments to try to get this
performance really good. And it's
something we've been using internally.
And at some point when we're happy with
it, it's something we're we're going to
release for everyone. Um but generally
our bar is if we find ourselves really
happy with it and we find ourselves
using it every day then we release it to
everyone. And this one's not quite there
yet. It's another uh fascinating example
uh or discussion when you compare a uh
gently memory like this to human memory
and the fact that you can edit it and
then it leads to all sorts of questions
around okay what is it that we as an
organization should remember and who's
in charge of ultimately editing what
should be remembered or not um because
this is for code but uh code being
everything it's a fascinating concept
>> yeah this is I think this One of those
social problems and maybe not social
problems, this is one of those social
dynamics that will change over the
coming years as people use these tools
more and more is we need to figure out
like what are the roles of people on the
team and how how do they interact with
each other and interact with Quad. Um
and this is this is maybe one very
specific problem within that who who
curates quad's knowledge and my feeling
is that this is something where teams
will kind of get more and more
horizontal uh as a as a result of this
um because anyone is able to contribute
in this way.
>> Um but it'll be interesting to see how
it plays out.
>> And then the key question for agents is
always uh the level of autonomy uh
versus uh human in the loop. How do you
guys think about that and where do I get
pinged as the human coder uh in my cloud
code workflow?
>> The default behavior is there's always a
human in the loop. This is this is super
important because this is in the in the
end this is a model and it's not
predictable and you want to make sure
that it doesn't do anything dangerous.
Um so yeah, there's there's always a
human loop.
for actions that we know can't have any
um kind of dangerous repercussions. So
for example, reading a file, we know
this is inherently safe. We just let the
model do this in the folder that you let
it do this in. But for other actions
like uh editing a file or running a
command or using the internet, this
always needs a human in the loop and it
always needs a human to approve it.
There's ways to reduce this burden a
little bit. So, for example, if you find
yourself always approving edits to the
same file or always approving the same
command, there's a there's a settings
file that you can configure across your
team and you can use this to essentially
allow list or block list certain
commands or certain files that you
always want the model to be able to edit
without human approval or you never want
it to be able to run.
>> And while we're on the topic of sort of
safety and and and and security, um how
do you guys think about uh sort of
confidential code? you know that whole
world of like regulated industries and
sensitive code and that kind of stuff.
Do do you offer a uh a local version of
this an on-prem version of this or maybe
that's a question for cloud code but
like anthropic in general are you all
sort of uh cloud-based?
>> It's something that actually we've seen
work quite well in these very very
regulated industries and the the reason
is that it doesn't use any services
except the API itself. So that's all it
needs and then everything else you you
actually don't need. Uh, and this is one
of the nice side effects of not doing
codebase indexing or anything like this
is it's just very easy to hook up to. So
if let's say you're you're a bank and at
your company you already have Bedrock
approved, you can just use Bedrock and
um use quad code that way. So you run it
on people's laptops and all you need is
access to Bedrock. Um so so really easy
to get approval for. Um and then if you
want to use the anthropic API or vertex,
you can you can use that too. How do you
um think about the sort of UI and UX
experience of this? So sort of how how
you balance the the power of everything
you can do versus your stated goal of
being, you know, as lean and and
lightweight of an interface on top of
the model. So we just talked about how
you can approve uh actions that the
agent takes. Um what about what about
the the the rest? Does it basically feel
like you'd be using a regular CLI or is
it something um you know different that
one needs to get used to?
>> We tried really hard to make quad code
something really beautiful that everyone
feels is something that we put a lot of
care into because we did and I think
when you use quad code you can feel that
this is something that we use every day.
You know at this point most code at
Enthropic is written using quad code and
almost everyone at Anthropic is using it
every day. And when we look at customers
that start to use quad code, they they
use it kind of more and more and more.
And with a product like this, you want
it to feel really smooth and really
beautiful and something you really enjoy
using. And that's been really fun from
an engineering and design point of view
because we built in a terminal. And like
I said, terminals have been around for,
you know, 50 plus years at this point.
And it it really feels like we're
rediscovering how to design for a
terminal. Um because since terminals
were first invented, the the design
world moved to uh moved to web and then
it moved to apps. And there's kind of
different design principles you can take
here. And we try to apply these back to
cloud code even though it's running in a
terminal. And there's a lot of details
that we spent a lot of time on like the
way that we represent statuses for every
item with this kind of blinking dot that
turns red or green to indicate whether
it succeeded or failed. the even the
loading indicator like the the spinner
while quad is working. We spent probably
30 or 40 iterations of this just to get
it to feel just right to make it feel so
you know what's happening but it's not
giving you too much information and it's
also not jittering and moving around on
you. So yeah, every part of the
interface we we iterated on probably
more than more than you'd think.
>> Yes. And then there's this really uh fun
kind of like series of words um while
while the while Claude does its thing
where it says like cooking or hurting or
sleing or honking or clotting uh which
uh you know how many of those words do
you have that that you seem to have like
dozens of them? I just find it such a
like a fun kind of like Easter egg kind
of kind of design detail that makes the
whole difference.
>> You know, at the at the beginning I
added maybe 20 of them and then
immediately people started making uh
suggesting changes like, "Hey, how about
this word? How about this word? How
about this word?" Um, so now at this
point there's a pretty big list and Quad
can actually choose the word that best
describes the task that it's doing. Um,
so it's up to Quad uh which word it
wants. How do you charge um for using
the product? And I'm asking this in the
context of um I think over the last few
days there was some evolution um as as
people became more and more rapid users
uh of the of the product. Um the the
pricing structure evolved.
>> Yeah, this is something that we were
honestly really uh excited to see how
some people are just going uh they're
really figuring out how to run this
thing at all hours of the day. Um, it's
just, you know, some some people have
this army of clouds, you know, like 5,
10, 20 that are just running in parallel
all the time and just doing work. I I
talked before about how you cla
generally needs human approval to do
work. There's actually ways to do it in
a slightly more autonomous way, too, if
you want to run it for long periods.
Essentially, you need to uh set up a
container for it and just give it some
um kind of like a container to be in and
then it can run without approval in a
way that is safe. And so, there's a lot
of people that do this. It's it's
extremely exciting, but also the pricing
structure that we had was really not cut
out to uh to actually serve these kinds
of users. Um, and there's also um just a
little we call this uh kind of abuse
where at at the tail end um you know
there there's like account sharing and
and things like this where people are
just really not using it in the way that
it's intended. Um so generally for
quadco there's two pricing models today.
One is you can get a subscription.
There's um there's pro and then there's
max. And this is uh I think it's 20
bucks a month, 100 bucks a month or 200
bucks a month. And it has very very
generous rate limits. Um if you use only
Opus, you'll run out of limits pretty
quick and then we'll switch you over to
Sonnet. Um if you use Sonnet, then you
know you can use much more of it than
most people need and almost everyone
doesn't run into rate limits at all. Um
it's it's generally um power users run
into it. Um, and this is something that
we're thinking also thinking through
like how to evolve this as we land
features where people use more tokens
and there's more sub agents and there's
more autonomy. Um, because we need to
figure out a way that we can provide
this to people in a way that's
sustainable.
>> It's an interesting dynamic, right?
Because um, you're a tool for power
users, very sophisticated uh, coders
that do sophisticated things with it.
Uh, but equally you don't want to you
want to encourage them, not discourage
your your power users with pricing.
>> Exactly. Exactly. Yeah. We want to we
want to support the community. We want
to hear how people use quad code in
these ways so that we can make sure that
we can support that. That's super
important to us.
>> Great. So it's a price per token or you
get like a certain uh number of tokens
for certain pricing tiers.
>> Yeah, essentially like within a certain
period of time you have a certain number
of tokens you can use and then if you
want pretty much unlimited usage without
dealing with these limits, you can
always just use a API key. Um and this
way you can just use it as much as you
want. So I' I'd love to spend a little
bit of time double clicking on use
cases. Um so we we talked about this a
little bit and talked about how actually
some people at the fringe are are using
uh cloud for uh non-coding use cases.
But talking about the you know intended
users who are the the the coders. What
are the main um things that you see
people do in a context workcloud
presumably can do everything?
>> Yeah, we see people using it for all
sorts of stuff uh for all sorts of code
related tasks. Everything from uh
planning projects to managing tasks to
actually writing code uh testing code uh
debugging it's excellent at so if
something doesn't work you can ask quad
to to debug it writing unit tests uh
verifying code whenever there's issues
in production our first line of defense
is to give it to quad so you know we
have logs coming from GCP or whatever we
give this to claude and it'll figure out
what is the issue that's happening and
it can even interact with git and source
control so it
figure out what exactly caused a
breakage or what exactly caused a
regression, it can automatically fix it.
So yeah, it's it's for every stage of uh
SDLC. And I think this is the first tool
that really serves every stage in this
way. And like I said before, we didn't
intend it to be this way. It just
happens to be very general and Claude
happens to be really good at using these
tools. And so this is a you know for for
me this has been kind of accidental
product market fit across the entire
life cycle of engineering work.
[laughter]
>> So yeah the kind of accident that every
founder or creator of a product dreams
of that happens so so rarely. Uh what an
amazing what an amazing story.
presumably uh if you have um those those
MD files and um a genic search uh cloud
code can also be used if you're a new
person either at a company or uh on a
project to learn about the code do do
first of all is that right and two do
you see people do that
>> absolutely when I think about the things
that uh that quad code is good at um
I'll be kind of I'll be a little bit
self-critical I feel like if you look at
uh answering questions about the
codebase and kind of codebased research,
I think it's like 10 out of 10 good.
It's it's as good as it can get. Um when
it comes to writing code, it's maybe
like a 6 out of 10. It's pretty good. It
won't get everything perfect. The next
model will be better and it's something
that we keep improving. Um when it comes
to debugging code, it's maybe also like
a six or seven out of 10. Um so I think
this codebase research and onboarding
onto a codebase, it's uh it's really
really excellent at it. And at
Enthropic, whenever new people join, on
their second day, this is part of
technical onboarding. We teach them
here's quad code, here's the codebase.
If you have any questions, don't bug
engineers on your team. Just ask quad
code. And it can answer these questions
probably better than they can because it
can search around the code. It can look
through history. It can look through
pull requests and slack and just pull in
all the context to answer all these
questions. And what we saw is at
anthropic technical onboarding used to
take a few weeks. Um, but now engineers
are usually productive within the first
few days and they don't test their teams
anymore. I think this is the biggest
thing where you don't need to bug your
senior engineer or your manager anymore
to get answers to your questions. You
just ask Quad Code and it can answer all
these questions for you.
>> So in the in the same vein, what do you
find yourself uh using Cloud Code for as
a as as a leader and engineer? What's
your uh you know daily use case?
>> Yeah, I use it all day for all all sorts
of stuff. the so obviously like I said
codebased research if I'm working on a
piece of code I'm not familiar with I'll
just start by asking quad code to tell
me about it whenever I'm working on a
small feature I'll usually use quad code
in GitHub actions so I'll just say at
quad I'll make a new GitHub issue and
then I'll say at quad implement this
feature for me and it'll just do it
usually in one shot um and sometimes
I'll do this on the command line too so
I'll just say you know implement this
feature and make a pull request and you
know I'll come back a few minutes later
and it's done. Then there's this kind of
other work where it's a little bit more
complex. You can't really do it in one
shot. It's it's not as simple as
changing a piece of text or changing a
button or building a small feature.
Maybe it's like something more involved.
There's probably two workflows I have
here. One is for really complex stuff,
I'll prototype it a bunch. And this is
something that I did even before quad
code. you know when you when you write a
complex piece of code or a complex
feature often engineers will write it a
few times because you don't actually
know the right way to do it and so
you'll try one approach you'll try a
second approach you'll try a third
approach and you'll kind of figure out
the the edge cases for each and kind of
the the limitations and you'll get a
feel for the problem this way and this
is something I used to do by hand
nowadays I'll just tell cloud code to do
it so I'll maybe make a few git work
trees I'll launch a few clouds and then
in parallel I'll tell them here's your
job I want you to implement this feature
sure go to town and I'll then look at
each of the solutions and try to figure
out okay maybe I like this piece of this
one this piece of this one this piece of
this one and then I'll throw away all
that code I'll just I'll discard it and
then I'll start a new uh quad and I'll
tell it okay here's how I want you to do
it now that I got a I got a feel for the
problem and then I think the last
workflow is actually the one I probably
use the most and this is probably for
medium-sized features and in this one
I'll ask quad to make a plan and I'll go
back and forth with it a little bit on
that plan. And it's really important
actually to get that plan right and to
make sure it's the same thing you have
in mind before you continue because
otherwise what I see sometimes is people
ask Quad for a little bit too much.
Maybe it's a complex feature and then it
wrote it in some way that like it's not
at all what you wanted. But the problem
isn't that Claude doesn't know how to do
it. The problem is that the description
is just too low bandwidth. You only
described in a few words what you want.
And so the the idea that Claude got of
it is a very different idea than what
you had in mind. And so I find that
planning helps a lot. So you kind of
iterate on the plan the same way that
you would with anyone else you're
working with. And then once that's
ready, I'll ask Quad to write the plan
to a file maybe. Um and then I'll tell
it to kind of implement that plan and
it'll naturally make a to-do list for
itself to to implement it.
>> All right, switching texts a little bit.
I'd love to talk about the space more
broadly. So uh Cloud Code is a rocket
ship uh within the anthropic rocket
ship. Uh but equally there are other
products uh like cursor windserve replet
[snorts]
lovable uh you know v 0ero the list goes
on and on and we've had um you know a
few of those uh CEOs on on on this
podcast uh what what do you uh make of
the space going forward? Do you think we
end up with a bunch of different
solutions different doing different
things? Do you think there is a at some
point a winner takes all kind of
scenario? Uh how do you how do you think
about the next couple of years?
>> Yeah, my feeling is there's kind of two
dynamics here. One is that uh this is
just a giant market. The market you
could think of it as all of coding. You
could think of it as all of kind of
creativity and kind of create creating
things because this extends at some
point beyond coding to to design and
things like this. So I think there's
there's room for everyone. It's it's a
giant market and the biggest thing that
these companies should be thinking about
is everyone that's not yet using AI for
coding because if you only focus on
people that use AI for coding already,
these are kind of the early adopters. So
you want to kind of get into that curve
and get the the middle and the late
adopters too. And many of these don't
even use AI today. So I think it's a
it's a big market. I personally use a
lot of these products and um you know I
use Quad Code every day, but I also use
Cursor every day and I use other
products every day. So there's room for
all these and they all kind of fit
together into into people's workflows.
The second way to think about it is like
I said before, the model is getting
better so quickly that the kinds of
things it's able to do are just changing
every few months. It's this it's this
exponential that just keeps
accelerating. And this is really the
feeling inside of the lab um you know
working on AI and kind of building this
stuff. And hopefully it's also the
feeling that users have as you get to
use all these new products that are
coming out every few weeks or you know
maybe few days at this point. Um so yeah
it's really exciting and I think my
advice to companies building is
definitely build for what the model will
be able to do 6 months from now not for
what the model can do today. This is
probably the single biggest advice and
this is something that we followed for
quad code also. We started building quad
code when um it was still sonnet 3.5 and
it was okay and then with you know 3.6
six and 3.7 it was still it was fine it
was pretty good but then when Sonet 4
and Opus 4 came out that's when it
really hit its stride and we felt like
the product was really good and we
started to be able to use it for a lot
of coding
>> and so this is the biggest way I would
think about it is how do you build a
product that captures the model
capabilities six maybe even 12 months
from now and the market for those
capabilities is just going to be huge
>> yeah and to double click on on that uh
if I'm a product builder or founder. How
do I know that? How do I know what's in
the, you know, 6 months horizon? Um, you
know, speaking of like entropic or or or
in general, what what is it that um is
going to happen in the next six months
that I should plan on on on talking
about the coding capabilities?
>> Yeah, I think the biggest thing is just
use all these products and see where
they stumble and try to get a feel for
the model itself. I think quad code is a
really good way to do that. There's
probably other ways too, but try to kind
of get away from all the scaffolding and
all the products people have built
around it and just get a feel for the
model's capabilities in as raw form as
you can and try to get your head around
the limitations like where exactly does
the model stumble today. What is what is
exactly that frontier where it's like
not very good and then you know
sometimes it's good and maybe 50% of the
time it's good. You can kind of get a
feel for this frontier. And with the
models today, a lot of this is around
kind of agentic work where it can use
tools really well and then at some point
maybe it'll fall over when there's too
much context or too many tools or the
trajectory is too long. Maybe if you've
been running quad for 2 hours, it loses
track after a little bit. So there's
some there's some sort of like frontier
here. Maybe there's another frontier
around code quality where today I have
to maybe correct the model when you know
maybe there's something that it does
that isn't exactly the way I would have
written it and I think over time models
will get better at kind of understanding
this too. So I would just try to use the
model in as raw a form as you can and
get a feel for these front frontiers in
the domain you care about. So for coding
maybe it's kind of the how long the
trajectory is and whether the model can
stay on track and then the quality of
the code and probably a bunch of other
stuff. And then for non-coding domains
there's there's a lot more.
>> So still in the same vein of like the AI
coding wars. Uh it it seems that there
is this this uh you know competition
competition kind of dynamic where uh
anthropic or others would provide their
models uh to companies uh like cursor or
windsurf at some point uh but equally
build cloud code which is which is an
application. Do do you think that's a
long-term uh sort of uh way the
ecosystem works or you know uh in a
context where cursor is saying that
they're going to build their own models
as well the end result is kind of like
full stack players where everybody has
their own underlying model and
application on top. I think there's
probably room for both and my personal
take is probably there's going to be
more stuff built on top of the platform
than there will be built in house just
because there's so many things to build
and there's just not enough time and
enough people and energy to build all
those things. So I think a lot of the
innovation that's going to happen on top
of the APIs and SDKs that are built. As
a last theme uh for this conversation,
the the sort of the elephant in the room
is uh what that means uh for coding and
uh coding as a profession. Uh what's
your general sense uh for what coding is
going to look like in a few years from
now?
>> Yeah, it's a little bit hard to say. Um
you know a few years from now is you
know in AI time is like decades
[laughter] you know [clears throat] in
in normal time. I I think even today for
a lot of professional coders, it's
really easy to lament the state of
coding and to think, you know, I used to
write this code by hand and, you know,
now it's this agent doing all of it. I
think actually being the one that does
this work, it's incredibly exciting to
have an agent write the code. It feels
very empowering as an engineer because I
can explore a lot more ideas than I
could before. I can do it much faster. I
can work in domains that I know
literally nothing about. You know, maybe
I don't know iOS, but I can write an
app. um because I can just generally
code review the code and I can see it
looks reasonable but quad actually does
all the writing and all the all the
testing of it. There's um one engineer
on the team, Lena, she still writes C++
on the weekend sometimes by hand. She
was telling me because um you know like
as a programmer this is kind of one of
the things that we enjoy because
sometimes you have to get down to the
metal and you have to kind of do it this
way. But I see this as a transition the
same way that in the 60s there was this
transition between punch cards and
assembly and then later on between
assembly and forran and cobalt and the
first highle languages and I think this
is just another next transition.
It's hard to know exactly how this is
going to play out. I think one way it
will definitely play out is it's going
to change programming where programming
is no longer direct text manipulation
but it's more working with agents to get
the work done.
And I think it's going to be hugely
empowering where a lot of people that
couldn't create before can now create.
And even if maybe you don't know
anything about uh you know apps, you can
use lovable or you can use another
platform to build cool stuff that that
you couldn't before. And this is just
hugely exciting.
>> Mhm. But if I'm a young developer today
or I want to make coding or building
applications my my career, uh what would
you say? What would you tell uh you know
younger version of bor race at the of of
the beginning of your career for a
future in the field? What what do I need
to learn?
>> I think for people that are learning
coding today, it's actually harder than
it was uh when I was learning coding
because not only do you have to know
coding because you still have to
understand the languages, you still have
to understand the frameworks, you still
have to understand system design and all
this stuff, but also you have to use all
these tools and you have to do both. You
have to hold both in your head at once.
So you have to code so that you can
check what the model does and you know
how to direct it because you have to
have you know still with the models of
today you have to know what you're doing
in order to direct coding agents
effectively but at the same time you
have to be using all this new technology
you have to be using quad code and you
have to be using all these new agentic
coding tools because this is what the
future is and I think it's hugely
important to understand understand what
these are and what it lets you do and to
learn how to function both when writing
code manually and when using these
tools.
>> All right, it's been a fantastic
conversation. Maybe to close uh give us
a sense for what the next few weeks or
months or year looks like for cloud
code. Anything on the road map? Anything
you're excited about? Anything you can
uh talk about?
>> Yeah, there's a there's a lot of stuff
we're working on. Uh we landed native
Windows support recently and we're
working on single file distribution. So
you don't need a NodeJS anymore. You can
just use cloud code and it's a single
binary that you can use anywhere. So
much more portable. We're working on
getting quad code into more places. So
wherever you are, you can use quad code
more easily the same way that you can on
GitHub today. Um, and expect a lot more
agents. Um, so you know, be able to
launch agents, agents managing agents,
uh, and a lot more kind of freedom
freedom this way and continuing to level
up the the state of the art and figure
out what's next. But I would say
overall,
we don't really know. Still, we're we're
testing stuff out and we have a lot of
ideas and we don't know what's going to
work, but we're we're excited to show
what we come up with and see if people
like it.
>> Well, that that feels like a wonderful
uh place to leave the conversation and
and very fitting as we all try to figure
out uh where uh not only where we take
AI, but where AI takes us collectively.
Um so, it's been wonderful. Thank you so
much, Boris. Really appreciate your
spending some time with us today.
>> Yeah, thank you, Matt.
>> Hi, it's Matt Turk again. Thanks for
listening to this episode of the Mad
Podcast. If you enjoyed it, we'd be very
grateful if you would consider
subscribing if you haven't already, or
leaving a positive review or comment on
whichever platform you're watching this
or listening to this episode from. This
really helps us build a podcast and get
great guests. Thanks, and see you at the
next episode.
