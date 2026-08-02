---
title: How to Use Claude Code Like the People Who Built It
speakers: Cat Wu & Boris Cherny
source: https://www.youtube.com/watch?v=IDSAMqip6ms
retrieved: 2026-07-16
method: youtube_transcript_api
word_count: 15293
---
What made it work really well is that
quad code has access to everything that
an engineer does at the terminal.
Everything you can do, quad code can do.
There's nothing in between.
>> There's actually an increasing number of
people internally at anthropic that are
using like a lot of credits [music] like
spending like over a,000 bucks every
month. We see this like power user
behavior. This is something that they
teach in YC. If you can solve your own
problem, it's much more likely you're
solving the problem for others. There's
this like really old idea in product
called latent demand. You build a
product in a way that is hackable that
is kind of open-ended enough that people
can abuse it for other use cases it
wasn't really designed for and you build
for that cuz you kind of know there's
demand for it. Do you think the CLI is
the final form [music] factor? Are we
going to using cloud code in the CLI
primarily in a year or in 3 years or is
there something else that's better
[music]
This podcast is sponsored by Google. Hey
folks, I'm Omar, product and design lead
at Google DeepMind. We just launched a
revamped vibe coding experience in AI
[music] Studio that lets you mix and
match AI capabilities to turn your ideas
into reality faster than ever. Just
describe your app and Gemini will
automatically wire up the right models
and APIs for you. And if you need a
spark, hit I'm feeling lucky and we'll
help you get started. Head to
a.studio/bild. studio/build to create
your first app.
>> Cat Boris, thank you so much for being
here.
>> Thanks for having us.
>> Yeah. Um, so for people who don't know
you, you are the creators of Claude
Code. Thank you very much from the
bottom of my heart. It's uh I love Cloud
Code.
>> That's amazing to hear. [laughter]
That's what we love to hear. Um I Okay,
I think the place I want to start is
when I first used it. Um, there was like
this moment like I think it was around
when uh Sonnet 37 came out where I was
like I used it and I was like, "Holy
 this is like a completely new
paradigm. It's a a completely new way of
thinking about code." And the the big
difference was um you went all the way
and just eliminated the text editor and
you're just like all you do is like talk
to the talk to the terminal and and
that's that's it. Um, and you know,
previous paradigms of AI programming,
pre previous harnesses have been like
you have a text editor and you have the
AI on the side and it's kind of like or
it's a tab complete. So, take me through
like that decision process that ar that
that process of of architecting this new
paradigm. How do you how did you think
about that?
>> Yeah, I think the the most important
thing is it was not intentional at all.
[laughter] Okay.
>> Uh, we we sort of ended up with it. So
at the time when I joined Enthropic um
we were still on different teams at the
time. Um there was this previous
predecessor to quad code. It was called
Clyde like CL C cliop.
And it was this like research project
you know it took like a minute to start
up. It was this kind of like really
heavy Python thing. It had to like run a
bunch of indexing and stuff. And when I
joined I wanted to ship my first PR and
I hand wrote it like a you know like a
noob in a in [laughter] a like I didn't
know about any of these tools.
>> Thank you for admitting that.
U I didn't know any better and then I I
put up this PR and um Adam Wolf who was
the um manager for our team for a while.
He was my ramp up buddy and he just like
rejected the PR and he was like you
wrote this by hand. What are you what
are you [laughter] doing? Use Quide. Um
cuz he was also hacking a lot on Quiet
at the time. And so I tried Quaid. I
gave it the description of the task and
it just like one shot at this thing
>> and this was like you know sonnet 35. So
I still had to fix a thing even for this
kind of basic task and the harness was
super old. So it took like 5 minutes to
turn this thing out and just took
forever and um but it but it worked and
I was just mind-blown that this this was
even possible and they just kind of got
the gears turning. maybe you don't
actually need an IDE.
>> And then later on I was prototyping
using the anthropic API and the easiest
way to do that was just building a
little app in the terminal cuz that way
I didn't have to build a UI or anything.
And I started just making a little chat
app and then I just started thinking
maybe we could do something a little bit
like Clyde. So let let me build like a
little Clyde and it actually ended up
being a lot more useful than that
without a lot of work.
And I think the biggest revelation for
me was when we started to give the model
tools. It just started using tools and
it was just it was this insane moment.
Like the model just wants to use tools.
Like we gave it bash and it just started
using bash writing apple script to like
automate stuff uh in response to
questions. And I was like this is just
the craziest thing. I've never seen
anything like this. Cuz at the time I
had only used IDE with like you know
like text editing a little like oneline
autocomplete, multi-line autocomplete,
whatever. Um, so that that's where this
came from. It was this kind of
convergence of like prototyping but also
kind of seeing what's possible in kind
of like a very um rough way.
>> Um, and this thing ended up being
surprisingly useful and and I think it
was the same for us. I think for me it
was like kind of sonnet 4 opus 4. That's
where that magic moment was. I was like,
"Oh my god, this this thing works."
>> That's interesting. So like tell me
about that that the tool moment because
I think that is one of the special
things about cloud code is it just
writes bash and it's really good at it.
And I think a lot of um previous agent
architectures or even anyone building
agent today, your first instinct might
be okay, we're going to give it a find
file tool and then we're going to give
it a uh open file tool and you you build
all these like custom wrappers for you
know uh all the different actions you
might want the agent to take, but Cloud
Code just uses bash and it's like really
good at it. So how do you think about um
how do you think about what you learned
from that?
Yeah, I think we're at this point right
now where Quad Code actually has a bunch
of tools. I think it's like a dozen or
something like this. We we actually like
add and remove tools most weeks. So,
this changes pretty often. Um, but today
there actually is a search uh there's a
tool for for searching. Um, and we do
this for two reasons. One is the UX, so
we can show the result a little bit
nicer to the user because there's still
a human in the loop right now for most
tasks. Uh, and the second one is for
permissions. So, if you say in your like
cloud code like settings.json JSON on
this file you cannot read. We we have to
kind of enforce this. Uh we enforce it
for bash but we can do it a little bit
more efficiently for if we have a
specific search tool. Um but definitely
we want to like unhip tools and kind of
keep it simple for the model. Um like
last week or two weeks ago we unchipped
the OS tool because in the past we
needed it but then we actually built a
way to enforce this kind of permission
system for bash. Um, so in Bash, if we
know that you're not allowed to read a
particular directory, Quad's not allowed
to OS that directory. And because we can
enforce that consistently, we don't need
this tool anymore. Um, and this is nice
because it's a it's a little less choice
for Quad. A little less stuff in
context.
>> Got it. And how do you guys split
responsibility on the team?
>> Um, I would say Boris sets the technical
direction and has been the product
visionary for a lot of the features that
we've come out with. I see myself as
more of like a supporting role to make
sure that um that one that like our
pricing and packaging resonates with our
users. Um two making sure that we're
shephering all our features across the
launch process. So from like deciding
all right like these are the prototypes
that we should definitely ant food to
like setting the quality threshold for
ant fooding through to communicating
that to our end users. And um there's
definitely some new initiatives that
we're working on that uh I would say
historically a lot of quad code has been
built bottoms up like Boris and a lot of
the core team members have just had
these great ideas for to-do list sub
agents hooks like all these are bottoms
up. As we think about expanding to more
services and bring cloud code to our
places, I think a lot of those are more
like, all right, let's talk to
customers. Let's bring engineers into
those conversations and prioritize those
services and knock them out.
>> Got it. What is ant fooding?
>> Oh, ant fooding is
>> Oh, ant fooding.
>> Oh, um it it means dog fooding.
[laughter] So,
>> anthropic ant. I [laughter] got it.
>> Yeah. Our nickname for um internal
employees is ant. And so uh ant fooding
is our version of dog fooding. Uh
internally over I think 70 or 80% of
ants uh technical anthropic employees
use cloud code every day. And so every
time we are thinking about a new
feature, we push it out to people
internally and we get so much feedback.
We have a feedback channel. I think we
get a post every five minutes. And so
you get really quick signal on whether
people like it, whether it's buggy, um
or whether
uh it's not good and we should unchip
it.
>> You can tell um you can tell that
someone that is building stuff is using
it all the time to build it. Uh because
the the like its ergonomics just makes
sense if you're trying to build stuff
and that that only happens if you're
like ant ant fooding. [laughter]
Um I Yeah. Yeah. And I I think that
that's a really interesting paradigm for
building new stuff like that sort of
bottoms up I make something for myself.
Um tell me about that.
>> Yeah. And C cat is also so humble. Um I
think cat has a really big role in the
product direction also like it comes
from everyone on the team and like these
specific examples this actually came
from everyone on the team like to-do
lists and sub aents that was Sid Hooks
Dixon shipped that plugins Daisy shipped
that.
>> So like everyone on the team like these
ideas come from everyone. Um, and so I
think for us like we build this core
agent loop and this kind of core
experience and then everyone on the team
uses the product all the time. Uh, and
so everyone outside the team uses the
product all the time. And so there's
just all these chances to build things
that serve these needs. Like for
example, like bash mode, you know, like
the exclamation mark and you can type in
bash commands. This was just like many
months ago. I was using quad code and I
I was going back and forth between two
terminals and just thought it was kind
of annoying. Uh, and just on a whim, my
asked squad to kind of think of ideas,
the thought of this like exclamation
mark bash mode. And then I was like,
great, make it pink and then ship it.
[laughter]
It just did it. And like that that's the
thing that still kind of persisted. And
you know, now you see kind of others
also kind of catching on to that.
>> That's funny. I actually didn't know
that. And that's extremely useful
because I always have to open up a new
tab to like run any bash commands. So
you just you just do an exclamation
point and then it just like runs it
directly instead of filtering it through
all all the cloud stuff.
>> Yeah. And quad code sees the full output
too.
>> Interesting. That's perfect. [laughter]
>> So anything you see in the cloud code
view, cloud code also sees.
>> Okay, that's really interesting.
>> And this is kind of a UX thing that
we're thinking about. Like in the past
tools were built for engineers, but now
it's equal parts engineers and model.
>> And so like as an engineer, you can see
the output, but it's actually quite
useful for the model also. And this is
part of the philosophy also like
everything is dual use. Um so for
example, the model can also call slash
commands. So like you know I have a
slash command for slashcomit where I run
through kind of a few different steps
like diffing and generating a reasonable
commit message and and this kind of
stuff. I run it manually but also Claude
can run this for me. Uh and this is
pretty useful because we get to share
this logic. We get to kind of define
this tool and then we we both get to use
it.
>> Yeah. What are the differences in uh
designing tools that are dual use from
designing tools that are you know used
by one or the other? Surprisingly, it's
the same.
>> Okay.
>> So far.
>> Yeah. I I I sort of feel like this kind
of elegant design for humans translates
really well to the models.
>> So, you're just thinking about what
would make sense to you and the model
generally, it makes sense to the model,
too, if it makes sense to you.
>> Yeah. I think one of the really cool
things about Cloud Code being um a
terminal UI and what made it work really
well is that Cloud Code has access to
everything that an engineer does at the
terminal. And I think when it comes to
whether the tool should be dual use or
not, I think making them dual use
actually makes the tools a lot easier to
understand. It just means that okay,
everything you can do, cloud code can
do. There's nothing in between.
>> Yeah, that's interesting. Yeah, there
there are a couple of those decisions.
So, um
no no code editor, it's in the terminal,
so it has access to your files. Um, and
it's it's on your computer versus like
in the cloud in a virtual machine. So
you get like repeated you you get to use
it in a repeated way where you can like
you know build up your cloud MD file or
you know like all all like build slash
commands and all that kind of stuff
where it becomes very composable um and
extensible [snorts] from a very simple
starting point. And I'm curious about
how you think about, you know, for for
people who are thinking about, okay, I
want to build an agent, I want to build
probably not cloud code, but like
something else, how you get that that
simple package that then can extend and
be really powerful over time.
>> For me, I I start by just thinking about
it like developing any kind of product
where you have to solve the problem for
yourself before you can solve it for
others. And like this is something that
they teach in YC is you have to start
with yourself. So like if you if you can
solve your own problem, it's much more
likely you're solving the problem for
others. And I I think for coding
starting locally is the reasonable thing
and you know now we have cloud code on
the web. So you can also use it with a
virtual machine and um you know you can
use it in a remote setting and this is
super useful when you're on the go you
want to take that from your phone
>> and and this is sort of we we started
proving this out kind of a step bat a
time
>> where you can do atcloud in GitHub and
uh I use this every day like on the way
to work I'm like at a red light I
probably shouldn't be doing this but I'm
like you know on GitHub at a red light
and then I'm like at claude you know fix
this issue or whatever and so it's it's
just real useful to be able to control
it from your phone um and this kind
proves out this experience. I I don't
know if this necessarily makes sense for
every kind of use case. For coding, I
think starting local is right. Um I
don't know if this is true for
everything, though.
>> Got it. What are the slash commands you
guys use?
>> Slashprit.
[laughter]
>> Yeah.
>> Um yeah, it it's I I think the
pritcomand makes it a lot faster for
claw to know exactly what bash commands
to run in order to make a commit.
>> And what does the prit slash command do
for people who are unfamiliar? Oh, it it
just tells it like exactly how to make a
commit. Okay.
>> Um and you can like dynam you can say
like, okay, these are the three bash
commands that need to be run.
>> Got it. And and what's pretty cool is
also we have um this kind of templating
system built into slash commands. So we
actually run the bash commands ahead of
time. They're like embedded into the
slash command. Um and you can also
pre-allow certain tool invocations. So
for that slash command we say allow um
you know get commit get push gh and so
you don't get asked for permission after
you run the slash command because we
have like a permission uh based security
system. Um and then also it uses haik
coup which is pretty cool. Um so it's
kind of a cheaper model and faster. Um
yeah and for me I I use like commit uh
commit PR uh feature dev we use a lot.
So like sid created this one. It's kind
of cool. So it kind of like walks you
through step by step um building
something. So we prompt quad to like
first ask me how to what exactly I want
like build the specification
>> and then um you know kind of like build
like a detailed plan and then make a
to-do list walk through step by step. So
it's kind of like more structured
feature development
>> and then I think the last one that we
probably use a lot so we use like
security review for all of our PRs and
then also code review. Um so like quad
does all of our code review internally
at anthropic. Um, you know, there's
still a human approving it, but quad
does kind of the first step in code
review. That's just a slashcode review
command.
>> Got it. Yeah. What are the things I
would love to go deeper into like the
how do you make a good plan? So, the
sort of the feature dev thing because I
think there's a lot of like little
tricks that um I'm starting to find or
people at every start starting to find
that work and I'm curious like what what
are things that that we're missing. So
for example, one um step in the one
unintuitive step of the of the you know
plan development process is even if I
don't exactly know what the thing that
needs to be built is I just have like a
little sentence in my mind like I want
feature X I have Claude just like
implement it just without giving it
anything else and I see what it does and
that helps me understand like okay
here's actually what I mean because it
made all these different mistakes or
like it it did something that I didn't
expect that might be
And then I use that like the learning
from the sort of throwaway development.
I just clear it out. And then that helps
me write a better plan spec for the
actual feature development, which is
something that you would never do before
because it'd be too expensive to just
like yolo send an engineer on a feature
that you hadn't actually speced out. But
because you have cloud going through
your codebase and doing stuff, you can
like learn stuff from it. Um that helps
inform the actual plan that you make.
>> Yeah. I feel maybe I I can start and I'm
curious how you use it too.
>> I think there's like a few different
modes maybe for me like one one is
prototyping mode.
>> So like traditional engineering
prototyping you want to kind of build
the simplest possible thing that touches
all the systems just so you can kind of
get a vague sense of like what are the
systems there's unknowns and just to
kind of trace through everything.
>> Um and so I I do the exact same thing as
you Dan like Claude just does the thing
and then I see where it messes up and
then I'll ask it to just throw it away
and do it again. So just hit escape
twice, go back to the old checkpoint and
then try again. I think there's also
maybe two other kinds of tasks. So one
is just things that quad can one-shot
and I feel pretty confident it can do
it. So I'll just tell it and then I'll
just go to a different tab and I'll I'll
shift tap to auto accept and then just
go do something else or go to another
one of my quads and tend to that while
it does this.
>> Um but also there's this kind of like
harder feature development. So these are
you know things are maybe in the past it
would have taken like a few hours of
engineering time and for this usually I
would I'll shift tap into plan mode and
then align on the plan first before it
even writes any code. Um and and I think
what's really hard about this is the
boundary changes with every model and it
in kind of a surprising way where the
newer models they're more intelligent so
the boundary of what you need plan mode
for got pushed out like a little bit
>> like before you used to need to plan now
now you don't. And I think it's this
general trend of like stuff that used to
be scaffolding with a more advanced
model, it gets pushed into the model
itself and the model kind of tends to
subsume everything over time. Yeah. How
do you think about like building a agent
harness that isn't just going to like
you're you're not spending a bunch of
time um building stuff that is just
going to be subsumed into the model in 3
months when the new cloud comes out?
like, yeah, how do you how do you know
what to build versus what to just say it
doesn't work quite yet, but next time
it's going to work, so we're not going
to spend time on it.
>> I think we build most things that we
think would improve Cloud Code's
capabilities, even if that means we'll
have to get rid of it in 3 months. If
anything, we hope that we will get rid
of it in three months.
>> I think for now, we just want to offer
the most premium experience possible and
so we're not too worried about throwaway
work. H
>> interesting. Yeah. And an example of
this is something like even like plan
mode itself. I think we'll probably un
ship it at some point when Quad can just
figure out from your intent that you
probably want to plan first. Um or you
know, for example, I just deleted like
2,000 tokens or something from the
system prompt yesterday just cuz like
Sonnet 45 doesn't need it anymore. Um
but Opus Opus 41 did need it. What about
um you know in the case where uh the the
latest frontier you know model doesn't
need it but you know you're trying to
figure out how to make it more efficient
because you have so many users that you
know you're maybe you you're not going
to use Opus or Sonnet 45 for everything.
Maybe you're going to use Haiku. So
there's a trade-off between having a
more um elaborate harness for Haiku
versus just like not spending time on it
using Sonnet eating the cost and working
on more Frontier type stuff. In general,
we've positioned Quad Code to be a very
premium offering. So, our north star is
making sure that it works incredibly
well with the absolutely most powerful
model we have, which is Sonnet 45 right
now.
>> Um, we are investigating how to make it
work really well for like future
generations of smaller models, but it's
um it's not the top priority for us.
>> Okay. What do you think about um you
know one thing that I notice is
we get models um often and thank you
very much for this. We get models a lot
before they come out and it's our job to
kind of figure out is it any good and
over the last six months
when I'm testing claude for example in
the claude app with a new frontier model
it's actually very hard to tell whether
it's how whether it's better
immediately. Um, but it's really easy to
tell in cloud code because the the
harness matters a lot for the
performance that you get out of the
model. And you guys have the benefit of
building cla or building cloud code
inside of the um inside of enthropic. So
there's like a much tighter integration
between um the fundamental like model
training and the harness that you're
building and and they seem to kind of
like really impact each other. So how
does that how does that work internally
and and um what are the benefits you get
from having that like tight integration?
>> Yeah, I think the biggest thing is like
researchers just use this and so you
know as they see what's working, what's
not, they can they can improve stuff. Um
we do like a lot of eval to kind of
communicate back and forth and
understand where exactly the model's at.
Um, but yeah, there's this frontier
where you need to give the model a hard
enough task to really push the limit of
the model. And if you don't do this,
then all models are kind of equal. But
if you give it a pretty hard task, you
can you can tell the difference.
>> What sub aents do you use?
>> Um, I I have a few. I have like a
planner sub agent that I use. I have a
code review sub aent. Code review is
actually something where sometimes I use
a sub agent, sometimes I use a slash
command. So usually in CI to slash
command, but in synchronous use I use a
sub aent for the same thing.
Um
>> um it's a good question. Yeah, maybe
it's like a matter of taste. Yeah, I
don't know. I don't know. Um I think
it's maybe when you're running
synchronously, it's kind of nice to fork
off the the context window a little bit
because all the stuff that's going on in
the code review, it's not relevant to
what I'm doing next. But in CI, it just
doesn't matter.
>> Are you ever spawning like 10 sub agents
at once? And for what?
>> For me, I do it mostly for like big
migrations. Okay,
>> this like the big thing. Um, actually we
have so this like coder slash command
that we use there's a bunch of sub aents
there and so one of the steps is like
find all the issues and so there's one
sub agent that's like checking for
quadmd compliance. There's another sub
agent that's looking through git history
to see what's going on. Another sub aent
that's looking for kind of obvious bugs
and then we do this like kind of dduping
quality step after. So they find a bunch
of stuff. A lot of these are false
positives and so then then we spawn like
five more sub aents and these are all
just like checking for false positives.
And in the end, the result is awesome.
It finds like all the real issues
without the false issues.
>> That's great. I actually do that. Um, so
one of my non-technical cloud code use
cases is um expense filing. So like when
I'm I'm in SF right now, so like I have
all these expenses. And so I built this
little cloud project that uh in in cloud
code that um it uses uh one of these,
you know, finance APIs to just download
all my credit card transactions. And
then it uh decides like these are
probably the expenses that I'm going to
have to like file. And then I have two
sub agents, one that represents me and
one that represents the company. And
they like do battle to like figure out
like what's the proper um like actual
set of expenses. [laughter] uh it's like
an auditor sub agent and like you know
pro Dan sub agent. So um yeah that kind
of thing the the sort of like opponent
processor uh pattern seems to be like an
interesting one.
>> Yeah. Yeah. It's it's it's it's cool. I
I feel like when sub aents were first
becoming a thing actually what inspired
us there's like a Reddit thread a while
back where someone made sub agents for
like there was like a front end dev and
a backend dev and like a think it was
like a designer
>> testing dev
>> testing dev like there was like a PM sub
agent and this is like you know it's
cute like it feels like a little maybe
too anthropomorphic um maybe maybe
there's something to this but I I think
like the value is actually like the
uncorrelated context windows where you
have like these two context windows that
don't know about each other and this is
kind of interesting um and you tend to
get better results this way. What about
you? Do you have any interesting sub
agents you use?
>> So, I've been tinkering with one um that
is really good at front-end testing. So,
it uses Playright to like see all right,
what are like all the errors that are
client side and pull them in and try to
test more steps of the app. Um,
it's not totally there yet, but I'm
seeing signs of life and I think it's
the kind of thing that we could
potentially um, bundle in one of our
plugins marketplaces.
>> Yeah. Um, definitely. I I' I've used
something like that just with Puppeteer
and just like watching it build
something and then open up the browser
and then be like, "Oh, I need to change
this." It's like this is like, "Oh my
god."
>> Yeah. It's really cool.
>> It's really cool. I think I think we're
starting to see the beginnings of this
like massive like multi- massive sub
aents. I I don't know what they call
this like swarms or something like that.
There's a bunch of people there's
actually an increasing number of people
internally at anthropic that are using
like a lot of credits every month like
you know like spending like over a
thousand bucks every month. Um and this
like this percent of people is growing
actually pretty fast. And I think the
common use case is like code migration.
And so what they're doing is like
framework A to framework B. uh there's
like the main agent, it makes a big
to-do list for everything and then just
kind of map produce over a bunch of sub
agents. So you instruct quad like yeah
like start 10 agents and then just go
like you know 10 at a time and just
migrate all all the stuff over.
>> That's interesting.
What would be like a concrete example of
the kind of migration that you're
talking about?
>> I think the most classic is like lint
rules.
>> So there's like you know there's some
kind of lint rule you're rolling out.
There's no autofixer because it's like
you know like as an analysis can't
really it's kind of too simplistic for
it. Um I think other stuff is like
framework migrations like um we just
migrated from like one testing framework
to a different one. That's a pretty
common one where it's super easy to
verify the output.
>> One of the things I found is and this is
both for project projects inside of
every and then just open source
projects. It's like if you're someone
building a product and you want to build
a feature that's um been done before. So
maybe like an an example that people
might need to implement a bunch is like
memory. How do you do memory? Um because
we have a bunch of different products
internally, you can just like spawn
cloud sub agents to be like how do these
three other products do it? And there's
like possibility for just like tacit
code sharing where you don't need to
like have an API or you don't need to
like ask ask anyone. You can just be
like how does how do we do this already?
And then use the best practices to um uh
to uh build your own. And you can also
do that with open source because there's
like tons of open source projects where
people are like you know they've been
working on memory for like a year and
it's like really really good. You be
like what are the patterns that um
people have figured out and which ones
do I want to implement?
>> Totally. You can also connect your
version control system. If you've built
a similar feature in the past, cloud
code can use those APIs like query
GitHub directly and find how people
implemented a similar feature in the
past and read that code and um copy the
relevant parts.
>> Yeah. Is there um have you found any use
for like log files of okay you know
here's here's the full history of like
how I implemented it and like is that
important to give to claude and and and
how are you how are you um implementing
that or making it useful for it?
>> Some people swear by it. Uh there are
some people at anthropic where for every
task they do, they tell cloud code to
write a diary entry in a specific format
that just documents like what did it do,
what did it try, why didn't it work, and
then they even have these agents that
like look over the past memory and
synthesize it into observations.
>> I think this is like the starting
budding
>> like there's like something interesting
here that we could productize.
>> Um but it's a new emerging pattern that
we're seeing that works well. I think
the hard thing about like oneshotting
memory from just one transcript is that
it's hard to know how relevant a
specific instruction is to all future
tasks. Like our canonical example is if
I say make the button pink, I don't want
you to remember to make all buttons pink
in the future. And so I think um
synthesizing memory from a lot of logs
is a is a way to um find these patterns
more um consistently. It seems like you
probably need like there's some things
where you're going to know um you'll be
able to summar like synthesize or
summarize in this sort of like top down
way like this this will be useful later
and and you'll you'll know the right
level of abstraction at which it might
be useful but then there's also a lot of
stuff where it's like you actually you
know any given like commit log like make
the button pink it could be useful for
kind of an infinite number of different
reasons um that you're not going to know
beforehand. So you also need the the
model to be able to look up all similar
past, you know, commits and surface that
at the right time. Is that something
that you're also thinking about? Yeah, I
think I think there could there could be
something like that. And maybe I think
one way to see it is this kind of like
traditional memory storage work like
like mex like kind of stuff where you
just want to like put all the
information into the system and then
it's kind of a retrieval problem problem
after that. Um,
yeah. I think as the model also gets
smarter, it naturally I've seen it start
to naturally do this also with Sonnet 45
where if it's stuck on something, it'll
just naturally start looking like we
talked about before like using bash
spontaneously. So just like look through
git history and be like, "Oh, okay.
Yeah, this is kind of an interesting way
to do it."
>> Yeah. One of the things that like we
were talking before we started
recording, one of the um things that
we're doing inside of every like I feel
like it has really um change the way
that we do engineering because everyone
is cloud code build like CLI build and
um we have this engineering paradigm
that we call compounding engineering
where in normal engineering every
feature you add it makes it harder to
add the next feature and in compounding
engineering your goal is to make the
next feature easier to build um from the
feature that you just added. And the the
way that we do that is we try to um
codify all the learnings from um from
everything that we've done to build the
feature. So like you know how did we
make the plan and and what parts of the
plan needed to be changed or like when
we started testing it like what what
issues did we find? What are the things
that we missed? Um and then we codify
them back into all the prompts and all
the sub agents and all the slash
commands so that the next time when
someone does something like this uh it
catches it and that makes it easier. And
that's why for me, for example, I can
like hop into one of our code bases and
start like being productive even though
I'm I don't know anything about how the
code works because we have this like
builtup memory system of um of all the
stuff that we've learned as we've
implemented stuff, but we've had to
build that ourselves. I'm curious, are
you working on that kind of loop so it
the cloud code does that automatically?
>> Yeah, we're we're starting to think
about it. Uh it's funny. We we're just
uh we we heard the same thing from
Fiona. She just joined the team. And you
know, she she's our she's our manager.
She hasn't coded in like 10 years,
something like that. And she was landing
PRs on her first day. And she was like,
"Yeah, like not only did I kind of I
forgot how to code and quad code kind of
made it super easy to just get back into
it,
>> but also I didn't need to ramp up on any
context because I kind of knew all
this." And I think a lot of it is about
like when people put up poll requests
for quad code itself and I think our
customers tell us that they do like
similar stuff pretty often. Um if you
see a mistake I'll just be like add quad
add this to quad MD so that the next
time it just knows this automatically
and you you can kind of like instill
this memory in kind of a variety of
ways. So you can say like at quad add it
to quadmd. You can also say add quad
write a test. You know, that's like easy
way to make sure this doesn't regress.
And I don't feel bad asking anyone to
write tests anymore, right? It's just
like super easy. And like I think
probably close to 100% of our tests are
just written by Quad. And if they're
bad, we just won't commit it. And then
the good ones stay committed. Um, and
then also I think lint rules are a big
one. So for stuff that's enforced pretty
often, we actually have a bunch of
internal lint rules. Claude writes 100%
of these. Um, and this is mostly just
like at Claude in a PR write write this
lint rule. And yeah, there's sort of
this problem right now about like how
how do you do this automatically? And I
think generally how like Cat and I think
about it is we see this like power user
behavior and the first step is how do
you enable that by making the product
hackable so the best users can figure
out how to do this cool new thing
>> but then really the hard work starts of
like how do you take this and bring it
to everyone else. Um, and for me, I I
kept myself in the everyone else bucket.
Like, you know, I don't really know how
to use Vim. Like, I don't have this like
crazy like T-box setup. So, I have like
a pretty vanilla setup. So, if you can
make a feature that I'll use, it's a
pretty good indicator that like other
kind of average engineers will use it.
That is interesting. Like, tell me about
that because like that's something I
think about all the time is um making
something that is extensible and
flexible enough that power users can
find like novel ways to use it that you
would not have even dreamed of. But it's
also simple enough that anyone can use
it and it's and they can be productive
with it and you can you can kind of pull
what the power users find back into like
the basic experience. Like how do you
think about making those design and
product decisions so that you enable
that?
>> In general we think that like every
engine environment is a little bit
different from the others and so it's
really important that every part of our
system is extensible. Um so everything
from your status line to adding your own
slash commands through to hooks which
let you um insert a bit of determinism
at pretty much any step in quad code. So
we think these are the these are like
the basic building blocks that we give
to every engineer that they can play
with. um for plugins. Plugins is
actually our um so it was built by Daisy
on our team and this is this is our
attempt to make it a lot easier for the
average user like us um to bring these
slashcomands and hooks into our
workflows. And so what plugins does is
it lets you browse existing MCP servers,
existing hooks, existing plugins and
just like or sorry existing like sash
commands and just let you write one
command in quad code to pull pull that
in for yourself.
>> There's this like really old idea in
product called latent demand which I
think is probably the main way that I
personally think about product and like
thinking about what to build next is
it's a super simple idea. It's you build
a product in a way that is hackable that
is kind of open-ended enough that people
can abuse it for other use cases it
wasn't really designed for. Then you see
how people abuse it and then you build
for that cuz like you you kind of know
there was demand for it,
>> right?
>> Um and like you know when I when I was
at Meta, this is how we built kind of
all the big products. I think almost
every single big product had this nugget
of latent demand in it. um you know like
for example something like Facebook
dating it came from this idea that when
uh we looked at who looks at people's
profiles I think 60% of views were
between people of opposite gender so
kind of like traditional setup that were
not friends with each other and so we're
like oh man okay maybe there's like
maybe if we like launch a dating product
we can kind of harness this demand that
exists
>> that's interesting
>> and for you know marketplace it was
pretty similar I think it was like 40%
of posts in Facebook groups at the time
were by sell posts and so I Okay, people
are trying to use this product to buy
themselves. We just build a product
around it that's probably going to work.
And so we think about it kind of
similarly, but also we have the luxury
of building for developers and
developers love hacking stuff and they
love customizing stuff and it's like as
a user of our own product, it makes it
so fun to build and and use this thing.
Um, and so yeah, like like I said, we
just build the right extension points.
We see how people use it and that kind
of tells us what to build next. Like for
example, we got all these user requests
where people were like, "Dude, Quad Code
is asking me for all these permissions
and I'm out here getting coffee. I don't
know that it's asking me for
permissions. How could I just get it to
like ping me on Slack?" And so we built
hooks. Uh Dixon built hooks um so that
people could get pinged on Slack and you
could get pinged on Slack for anything
that you want to get pinged on Slack
for. Um, and so it was very much like
people really wanted the ability to do
something. We didn't want to build the
integration ourselves. And so we we
exposed hooks for people to do that.
>> The thing that makes me think of is um
you you recently um released you kind of
moved or rebranded how you talk about
cloud code to be this like more general
purpose agent SDK. Is that was that
driven by some latent demand where you
you sort of saw there's like a more
general purpose use case for what you
built?
>> We realized that similar to how you were
talking about using cloud code for
things outside of coding, we saw this
happen a lot like um we get a ton of
stories of people who are using cloud
code to like help them write a blog and
like manage all the like data inputs and
take a first pass in their own tone. Um
we find people building like email
assistants on this. Um I use it for a
lot of just like market research. Um
because at the core it's like an agent
that can just go on for an infinite
amount of time as long as you give it a
concrete task and it's able to fetch the
right underlying data. So one of the
things I was working on was I wanted to
look at all the companies in the world
and how many engineers they had and to
create a ranking. And this is something
that quad code can do even though it's
not a traditional coding use case. So we
realized that like the underlying
primitives were really general as long
as you give as long as you have like an
agent loop that can continue running for
a long period of time and you're able to
like access the internet and write code
and run code pretty much you can if you
squint you can kind of build anything on
it. Mhm.
>> And and I think like by at the point
where we like rebranded it so like from
the quad code SDK to the quad Asian SDK,
there was already like many thousands of
companies using this thing and a lot of
those use cases were not about coding.
So it's like both both internally and
externally. We kind of saw that
>> like health assistants, like financial
analysts, legal assistance. Um it was
pretty broad.
>> Yeah. What are the coolest ones?
I feel like actually you you had Noah
Brier on the the podcast recently. I
thought like the obsidian like kind of
mind mapping notekeeping use case is
really cool. It's funny. It's insane how
many people use it for this [laughter]
>> particular combination. Uh I think some
other like some coding or kind of coding
adjacent use cases that are kind of cool
is um we have this like issue tracker
for quad code. The team's just like
constantly underwater like trying to
keep up with all the issues coming in.
There's just so many. And so I quad
ddupes the issues and it automatically
finds duplicates and it's extremely good
at it. It also does first pass
resolution. So usually when there's an
issue it'll um proactively put up a PR
internally and this is a new uh thing
that Enigo on the team built. Um so this
is pretty cool. Uh there's also like on
call and kind of collecting signals from
other places like getting like sentry
logs and getting like logs from BigQuery
and kind of collating all this. um plus
just really good at doing this because
it's all just bash in the end, right?
>> And so these are all kind of these
internal use cases that that I saw.
>> Is it um so when it's you know collating
logs or um you doing issues is that like
you have clouds like continually running
in the background and is that something
that you're building for?
>> Um it gets triggered for that particular
one. It gets triggered whenever a new
issue is filed. So it runs once but it
can choose to run for as long as it
needs.
>> Got it. What about the idea of clouds
always running? Oo, proactive quads. I
think it's definitely where we want to
get to. U I would say right now we're
very focused on making quad code
incredibly reliable for like individual
tasks. And you know, if you think about
like if you think about like multi-line
autocomplete and then like single turn
agents and then now we're working on
like quad code that can complete tasks.
I feel like if you trace this curve
eventually you go to even higher levels
of abstraction like even more
complicated tasks and then hopefully the
next step after that is a lot more
productivity. So just understanding what
your team's goals are what your goals
are being able to say hey I think you
probably want to try this feature and
here's a first pass at the code and here
are the assumptions I made and are these
correct?
>> I can't wait. Um and I think probably
right after that is um Claude is now
your manager. [laughter]
Um,
>> that's not in the plan. [laughter]
>> So, everyone on the team was like super
excited that uh we were we were talking
today and they gave me a bunch of
questions and I want to make sure I I
hit all the questions. Um,
uh, oh, here's a good one. Why did you
choose agentic rag over vector search in
your architecture? And are like vector
embeddings uh still relevant? Um so
actually initially we did use vector
embeddings. Um they're just a really
tricky to maintain because you have to
continuously reindex the code and they
might get out of date and you have local
changes. So those need to make it in.
And then as we thought about what does
it feel like for an external enterprise
to adopt it, we realized that this
exposes a lot more surface area and like
security risk. Um we also found that
actually cloud code is really good and
cloud models are really good at agentic
search. So um you can get to the same
accuracy level with agentic search and
it's just a much cleaner deployment
story.
>> H that's really interesting.
>> Um if you do want to bring semantic
search to quad code, you can do so via
an MCP tool. So if you want to manage
your own index and expose an MCP tool
that lets Quad Code call that, that that
would work. What do you think are the
top MCPS to use with cloud code?
>> Puppeteer and Playright are pretty high
up there.
>> Definitely. Yeah.
>> Century has a really good one. Asana has
a really good one. Hm. Do you think that
there are um
any any power user tips that you see
people inside of anthropic or you know
other people who are you know big power
you know inside of organizations that
are big cloud code power users that
people don't know about but they should.
Um, one thing that QuadCo doesn't
naturally like to do, but that I
personally find very useful is, um,
QuadCo doesn't naturally like to ask
questions, but you know, if you're
brainstorming with a thought partner, a
collaborator, usually you do ask
questions back and forth to each other.
And so, this is one of the things that,
um, I like to do, especially in plan
mode. I'll just tell Cloud Code like,
"Hey, we're just brainstorming this
thing. Um, please ask me questions if
there's anything you're unsure about."
um I want you to ask questions and it'll
do it. And I think that actually helps
you arrive at a better answer
>> there. There's like there's also like so
many tips that we can share. I think
like there there's a few really common
mistakes I see people make. One is like
like you said like not using plan mode
enough. This is this is just super
important. And I think this is people
that are kind of new to a coding. They
kind of assume this thing can do
anything and it can't. It's like not
that good today and it's going to get
better but today it can oneshot some
tests. can't one-shot most things. Um,
and so you kind of have to understand
the limits and you have to understand
like where you get in the loop. And so
[snorts] like something like plan mode,
it can like two 3x success rates pretty
easily if you like land on the plan
first. Um, other stuff that I've seen
power users do really well is companies
that have really big deployments of quad
code and now um, you know, luckily
there's a lot of these companies so we
can kind of learn from them. Uh having
settings JSON that you check into the
codebase is really important because you
can use this to pre-allow certain
commands so you don't get permission
prompted every time and also to block
certain commands. Let's say you don't
want web fetch or whatever and this way
as an engineer I don't get prompted and
um I can check this in and share it with
the whole team so everyone gets to use
it.
>> I I get around that by just using
dangerous they skip permissions.
[laughter]
>> Yeah, we kind of we kind of have this
here but we don't you know we don't
recommend it. It's like it's a model,
you know, it can do it can do weird
stuff. Um, I think another kind of cool
use case that we've seen is people using
stop hooks for interesting stuff. So
stop hook runs whenever the turn is
complete. So like the assistant did some
tool calls back and forth with you know
whatever and uh it's done and it returns
control back to the user then we run the
stop hook and so you can define a stop
hook that's like um if the tests don't
pass return the text keep going and
essentially it's like you can just like
make the model like keep going until the
thing is done and this is just like
insane when you combine it with the SDK
and this kind of programmatic usage
>> you can you know this is a stochcastic
thing it's a nondeterministic thing but
with scaffolding you can get these
determin deterministic outcomes.
>> So you guys started this sort of CLI,
this CLI paradigm shift. Um, do you
think the CLI is the final form factor?
Are we are we going to using cloud code
in the CLI primarily in a year or in
three years, or is there something else
that's better?
>> I mean, it's not the final form factor,
but we are very focused on making sure
the CLI is like the most intelligent
that we can make it and that's as
customizable as possible. you can talk
about the next form factors.
>> Yeah, I mean [laughter]
cat C's asking me to talk about because
no one knows like this this stuff's like
it's just moving like so fast, right?
Like no no one knows what these form
factors are. Like right now I think our
team is in experimentation mode. So we
have uh CLI then we came out with the ID
extension. Now we have a new ID
extension that's like a guey. It's a
little more accessible. Um we have add
quad and github so you can just add quad
anywhere. Um, now there's at quad,
there's quad on web and on mobile, so
you can use it on any of these places.
Um, and we're just in experimentation
mode, so we're trying to figure out
what's next. I think like if we kind of
zoom out and see where this stuff is
headed. I think one of the big trends is
longer periods of autonomy. And so with
every model, we kind of time how long
can the model just keep going and do
tasks autonomously and just, you know,
in dangerous mode in a container, keep
autocompacting until the task is done.
And now we're on the order of like
double digit hours. I think it's like
the last model is like 30 hours,
something like this. And I, you know,
the next model is going to be days. And
as you think about kind of parallelizing
models,
um there's kind of a bunch of problems
that come out of this. So one is what is
the container this thing runs in because
you don't want to have to like close
your laptop. I have that right now
because I'm doing a lot of uh disb I
don't know I've only heard I've only
read it but DSPY or disb prompt
optimization and like it's on my laptop
and it's like I don't want to close I'm
like in the way [laughter] middle like
with my laptop open because I'm like I
don't want to close it. Yeah.
>> Yeah. That's right. Yeah. We've like
visited companies before like like
customers that everyone's just like
walking around with their like quad
codes. [laughter]
>> Is this running? So, I think like one is
kind of getting getting away from this
mode and then I also think pretty soon
we're going to be in this mode of like
quads monitoring quads.
>> Yeah.
>> Um and kind of I I don't know what the
right form factor for this is because as
as a human you need to be able to
inspect this and kind of see what's
going on. Um but also it needs to be
quad optimized where um you're
optimizing for kind of bandwidth between
like the quad to quad communication. Um
so my prediction is terminal is not the
final form factor. My prediction is
there's going to be a few more form
factors in the coming months, you know,
maybe like year or something like that.
And it's going to keep changing very
quickly.
>> What do you think about, you know, I
teach a lot of cloud code to a lot of
every subscribers and
>> thank you.
>> You're welcome. Doing doing your work
for you. [laughter]
Um uh and I think the like one of the
big things is just the terminal is
intimidating and uh just like being on a
call with subscribers being like here's
how you open the terminal and you're
allowed to do this even if you're
non-technical is like a big deal.
[laughter]
How do you think about that? Yeah, I um
one of the people on our marketing team
uh started using cloud code because she
was writing some content that touched on
cloud code and I was like you should
really experience it and she got like 30
popups on her screen where she had to
accept various permissions because she'd
never used a terminal before. So I
completely see eye to eye with you on
that. It's definitely um hard for
non-engineers and there's even some
engineers we've found who aren't fully
comfortable with working day-to-day in
the terminal. Um, our VS Code GUI
extension is our first step in that
direction because you don't have to
think about the terminal at all. It's
like a traditional interface with a
bunch of buttons. Um, I think we are
working on more um graphical interfaces.
Uh, so quad code on the web is a guey. I
think that actually might be a good
starting point for people who are less
technical.
>> Yeah. Yeah. There there was this like
magic moment maybe like a few months ago
where like I walked into the office and
the some of the data scientists at
Anthropic like sit right next to the
quad code team and the data scientist
just had like quad code running on their
computers and I was like what what is
this like how did you figure this out? I
think it was like Brandon uh was like
the first one to do it and he was like,
"Oh yeah, I just like installed it. Like
I work on this product so like I should
use it." And I was like, "Oh my god." So
he like he figured out how to like use a
terminal and JS like you know he hasn't
really done this kind of workflow
before. Obviously like very technical.
Um so I think now we're we're starting
to see all these kind of like code
adjacent
uh like functions. people you use quad
code and um yeah it's kind of
interesting like from a latent demand
point of view these are people hacking
the product so there's like demand to
use it for this and so we want to make
it a little bit easier with more
accessible interfaces but at the same
time for us for quad code we're laser
focused on building the best product for
the best engineers and so um we're
focused on software engineering and we
want to make this like really good but
we want to make it a thing that other
people can can hack
>> some sometimes cloud code will write
code that's a bit verbose post. Um, but
you can just tell it to simplify it and
it does a really good job.
>> Interesting. And so, and how are how and
when are you doing that? So, you're
you're using a slash command or you're
>> I just say it. I just
>> Sometimes you're like, "Hey, this should
be a oneline change and I'll write five
lines and you're like, simplify it and
it understands immediately what you mean
and it'll fix it."
>> Yeah. I think a lot of people on our
team do that, too. Um, that's that's
interesting. Why do you like why not
then if you're saying that all the time
why not then you know push that into
like a slash command or the harness or
something like that to yeah make it just
happen automatically.
>> We do have instructions for this in the
cloud MD. I think it impacts such a low
percentage of conversations that we
don't want it to like over rotate in the
other direction.
>> Um and then the reason why not a slash
command is because you actually don't
need that much context. I think slash
command's really good for situations
where you would otherwise need to write
two three lines but for simp like even
for plan mode you actually can use a few
words but sometime but it actually takes
two or three lines to capture the
entirety of what you want in plan mode.
Um for simplify it you can just write
simplify it and it gets it.
>> Yeah. Yeah, that makes sense. Cool.
>> Yeah.
>> Um okay, now we're we can [laughter]
um that's interesting. Yeah, but but
this stuff like you know it still feels
just so early.
>> Yeah.
>> You know, like we we were talking before
before the recording about like kind of
where are we on the adoption curve and
it still
>> the hian curve or whatever [laughter]
whatever that term was.
>> Exactly. And it just feels it just feels
like we're you know like first 10% still
like the stuff is going to change so
fast it's going to keep changing. Even
when I talk to researchers outside of
enthropic who who abuse quad code um
they also get stuck on things like this
like not realizing that they can just
tell the LLM to simplify it and I think
that just goes to show that even for
people who are like working in this
industry they don't always realize that
you can just talk to the model. That's
the thing is like I I think that there's
this underlying expectation that using
AI shouldn't have to be a skill like
because it just does whatever you say
and you're like well I mean whatever you
say is going to matter for what it does.
So if you can say things better it's
going to do better. [laughter]
>> Yeah. I mean it it changes with every
model though. That's the that's the hard
part. like you know prompt engineer was
a job and now famously it's not a job
anymore and there's going to be more
jobs that are then like not not jobs
anymore of these kind of like little
micro skills that you have to learn to
use this thing and as the model gets
better it can just like interpret it
better
>> but I think that's also like for us this
is part of this kind of humility that we
have to have building a product like
this that we just really don't know
what's next and we're just trying to
figure it out kind of along with
everyone else we're just here for the
ride
>> and that's why it's cool that you're
building it for yourself cuz I think
that's the that's the best way to know
that is just like you're and this is
what we do too is like you're sort of
living in the future. You're using it
all the time. And uh it's pretty clear
what's missing. You're like I just want
this thing and you can just do the next
thing rather than being like hm let me
ask like some enterprise product manager
at like some gigantic company like what
kind of AI feature do you want? And
they're like I don't know like you know
put a little chatbot on the side of my
you know IDE and you're like okay.
[laughter]
>> Yeah.
>> Yeah. This is like the luxurious thing
about building dev tools right you're
your own customer. I think it's also
really um a unique thing about AI
because um it sort of reset the game
board for all software. So
um you know we have Kora this like email
assistant and we have like Sparkle which
organizes your files and it's like
anything that you do for something that
you want to use on your computer if
you're if you're building it with AI
there's a good chance that hasn't been
done before because like the whole whole
landscape has been reset. And so it's a
it's a uniquely exciting time to build
stuff for yourself.
>> Totally. I think it totally opens the
playing field, too. It's like any
individual can now build an app to fill
their need and then distribute it to
everyone else.
>> Yeah,
>> it's really cool.
>> I've been prototyping all these like
random pet projects. Um
>> um I just moved into a new apartment and
it's empty. And so I've been um I've
been building this like shopping advisor
assistant on like the Cloud Agent SDK
cuz who has time to like read all the
reviews and like look at all the options
and find their pricing and everything's
like really hard to discover. And so it
just like asks me a bunch of questions
and I tell it what I want and it shows
me a bunch of Yeah, exactly. and it
shows me a bunch of photos of like
different sofas and options and what
people say online
>> and then I tell it what I don't like and
it's literally feels like working with a
shopping assistant
>> and it it's been really cool.
>> That's really cool.
>> Um I also have my little email response
agent that like drafts responses for me
but I don't use email that much so
>> Oh, and I knew it wasn't you responding.
[laughter]
>> That's why it's seven days delayed.
The agent's just take doing a very
thorough job. [laughter]
>> Yeah,
>> agent SDK is cool though.
>> Yeah, agent SDK is cool.
>> Yeah, it's it always just feels amazing
like how much we're able to build with
such a small team.
>> Yeah.
>> So, I feel like
>> the other thing that's really cool is
that I think people are just shifting
their mindset from docs to demos. Like
internally, our currency is actually
demos. It's like you want people to be
excited about your thing. Yeah,
>> show us like show us 15 seconds of what
it can do.
>> And we find that everyone on the team
now has this kind of indoctrinated
>> demo culture for sure. And I think
that's better because
>> there's a lot of things that you might
have in your head that if you're a great
writer, maybe you could figure out how
to explain it, but it's just even then
it's just really hard to explain. But if
someone can see it, they like get it
immediately. And I think that's
happening for product building, but it's
also happening for like all sorts of
other types of creative endeavors like
making a movie for example. Like you had
to pitch it, but now you can just be
like I made this Sora video and like you
know check like you can kind of see like
like the glimmer of the thing you're
trying to make for very cheap. And so
that means you don't have to spend time
convincing people as much. You can just
be like here I made it.
>> Yeah. And and also as a builder like you
can just make it and then like make it
again and then make it again [laughter]
until you're happy. Like
>> I I feel like that like the flip side is
like you used to make a dock or you know
like whiteboard something or you know
like I I would draw stuff in like Sketch
or Figma or whatever and now we'll just
like build it until until I like how it
feels.
>> And it's just like so easy to get that
feeling out of it now. And I I think
it's like you could see it visually
before or you could describe it in words
but it's like you could never get the
vibe. And now like the vibe is really
easy.
>> Yeah. And you built plan mode like three
times.
>> Yeah. Yeah.
>> Because of this.
>> Like you you built it and then you threw
it out and rebuilt it and then threw it
out and rebuilt it.
>> Yeah. Or like Tudos's uh like Sid built
the original version like also like
three or four he built like three or
four prototypes and then I prototype
maybe like 20 versions after that like
in like a day. Yeah. I think this is
like a lot of pretty much everything we
released there was at least a few
prototypes behind it. How do you like um
keep track of and carry forward the
things you learn from prototype to
prototype? And especially if it's like,
you know, some one person is prototyping
it and then you're like, I'm going to
take it over. I'm going to do 20 more.
Like how do you how do you maximize what
you get out of that?
You know, it's it's like there there's
maybe a few elements of it. One is the
style guide. So there's like some
elements of style that we discover. And
I think a lot of this is like building
for the terminal or like we're kind of
discovering a new design language for
for the terminal and kind of building it
as we go. Um, and I think some of this
you can codify in a style guide. So this
is our quad MD, but then there's this
other part of it that's like kind of
product sense where I don't think the
model totally gets it yet. And I think
maybe we should be trying to find ways
to like teach the model this this kind
of product sense about like this works
and this doesn't, right? Because in in
product, you want to solve the person's
problem in the simplest way possible and
then delete everything else that's not
that and just get everything out of the
way. So you kind of you you align the
product to the intent as cleanly as
possible. And maybe the model doesn't
totally get that yet.
>> Yeah. It's never it doesn't really feel
what it's like to use quad code. Like
the model doesn't use quad code.
>> Yeah.
Yeah. And so I think like when you know
like quad code can like test itself and
it can kind of use itself. Um and like
we we do this when developing and it can
see like UI bugs and things like that.
I don't know maybe we should just try
prompting it though. It could like
honestly a lot of the stuff is as simple
as that. Like when there's some new idea
usually you just prompt it and often it
just works. Maybe we should just try
that.
>> A lot of the prototypes are actually the
UX interactions.
Um, and so I think once we discover a
new UX interaction like shift tab for
auto accept, I think uh Boris figured
out. Um, then
>> that was Eigor actually.
>> Oh, Eigor.
>> Yeah, we went back and forth can like
fit into that.
>> We did like dueling prototypes for like
a week. [laughter]
>> Yeah, shift tab felt really nice. And
then one of the the now current plan
mode iteration um uses shift tab because
it's actually just like another way to
tell the model how agentic it should be.
>> And so I think as as more features use
the same uh interaction, you form like a
stronger mental model for what should go
where.
>> Yeah. Or like thinking I think is
another really good one. Like first we
were like before we released quad code
or maybe it was like the first thinking
model was it like 37? I forget what the
first one was.
>> Yeah.
>> But yeah and it it was like it was able
to think and we're like brainstorming
like how do we like toggle thinking? And
then someone was just like what if you
just like ask the model to think in
natural language and it knows how to
think and we're like okay sweet let's do
that. [laughter]
And so like we we did that for a while
and then um we realized that people were
accidentally toggling it. So they were
like don't think and then the model was
like oh I should think. it just started
thinking
>> and so we had to kind of like tune it
out so you know don't think didn't
trigger it but then it still wasn't
obvious but then we made a UX
improvement to like highlight the
thinking that
>> and that was like that was so fun and it
felt really magical
>> when you do ultra think it's like
rainbow or whatever exactly [laughter]
and then with uh with sonet 45 we
actually find like a really really big
performance improvement when you turn on
extended thinking um and so uh we made
it really easy to toggle it because
sometimes you want it sometimes you
because you you kind of for a really
simple task, you don't want the model to
think for like five minutes. You want it
to just do the thing. And so we used tab
as the interaction to toggle it. And
then we unchipped a bunch of the
thinking words. Although I I think we
kept ultra think just for like
sentimental reasons. [laughter] It was
such a cool UX.
>> Interesting. Do you think there's some
there's some new metric that's about
what you deleted? And I I think
programmers have always felt like, you
know, deleting a bunch of code feels
really good, but there's something about
because you can build stuff so fast, it
becomes more important to like also
delete stuff.
I think my favorite kind of diff to see
is a red diff. [laughter] This is the
best whenever I'm like, "Yeah, bring it
on. Another one. Another one." Um, but
it, you know, but it's hard because like
anything you ship, people are using it.
And so you got to keep people happy. And
so I think generally our principle is if
we un ship something, we need to ship
something even better. um that can kind
of um that people can can take advantage
of that that kind of matches that intent
uh even better. Um and yeah, I think
this is kind of back to like how do you
measure like quad code and the impact of
it and this is something like every
company every customer asks us about and
I think like in so internally at
anthropic I think we like doubled in
size since January or something like
that but then productivity per engineer
has increased like almost 70% in that
time. um
>> measured by
>> uh I think we actually measured it yeah
in a few ways but kind of PRs are the
the simplest one and the main one um but
like you said like this doesn't capture
the full extent of it because a lot of
this is like making it easier to
prototype making it easier to try new
things making it easier to these things
that you never would have tried because
they're way below the cut line. Um
you're launching a feature and there's
this kind of like wish list of stuff now
you just do all it because it's so easy
>> and you just wouldn't have done it.
>> So yeah, it's really hard to talk about
it. And then there's this flip side of
it where more code is written. So you
have to delete more code. You have to
code review more carefully and you know
automate automate code review as much as
you can. There's also like an
interesting like new product management
challenge because you can ship so much
that you end up it it ends up not
feeling as cohesive because you could
just like add button here and like a tab
there and like a little thing here. Like
it's just it's much easier to build a
product that has all the features you
want but doesn't have any sort of
organizing principle because you're just
shipping lots of stuff all the time. I
think we try to be pretty disciplined
about this and making sure that all the
abstractions are really easy to
understand for someone even if they just
hear the name of the feature. We have
this principle that I believe Boris
brought to the team that I really like
where we don't want a new user
experience. Everything should be so
intuitive that you just drop in and it
just works. And I think that's that's
really set the bar really high for
making sure every feature is really
intuitive. How do you do that with um a
conversational UI? Because um you know
when there's not a bunch of but buttons
and knobs and it's just a blank text box
to start, how do you think about making
it intuitive?
>> Um there's a lot of like little things
that we do like um we teach people that
they can use the question mark to see
tips. Um we show tips as quad code is
working. We have like the change log on
the side. um we tell you about like oh
there's a new model that's out or like
we show you at the bottom we have a
notification section for thinking. I
think there's just like subtle ways in
which we tell users about features. I
think the other thing that's really
important is to just make sure that all
the primitives are very clearly defined
like hooks have a common meaning um in
the developer ecosystem. plugins have a
very common meaning in the developer
ecosystem and just making sure that what
we build matches what like the you know
the average developer would immediately
think of when they hear that
>> there there's this also this like
progressive disclosure thing like you
know to to any anytime in quad code when
you run it you can hit control O to see
like the full raw transcript the same
thing the model sees and we don't like
show you this until it's actually
relevant so when there's a tool result
that's collapsed then we'll say use
control O to see it so we kind of we
don't want to put too much complexity on
you at the start because this thing can
do you know anything. Um I think there's
this other kind of new principle which
we've just started exploring which is
like the model teaches you how to use
the thing and so you can ask quad code
about itself and it it kind of knows to
look up its own documentation to tell
you about it but we can also go even
deeper like for example slash commands
are a thing that people can use but also
the model can call slash commands and
maybe you see the model calling it and
then you'll be like oh yeah I guess I
can do that too.
>> Yeah. Yeah. Yeah. Interesting. How has
it changed like you know when you first
started doing this cloud code was this
sort of like singular thing this
singular way of thinking about you know
using AI through a CLI other people had
stuff like this but it it felt like this
shift and now there's a whole landscape
of everyone is like going CLI CLI CLI
like how has that changed how you think
about building how it feels to build and
how are you dealing with the sort of
pressure of the race that you're in? I
>> think for for me like imitation is the
greatest flattery. Mhm. Um, so it's like
it, you know, it's it's awesome and it's
just like it's cool to see all this
other stuff that everyone else is
building like inspired by this. And I
think this is ultimately the goal is to
kind of inspire people to build this
next thing for this just incredible
technology that's that's coming. And
that that's just really exciting.
Personally, I don't really use a lot of
other tools. So, usually when something
new comes out, I'll I'll maybe just try
it to get a vibe. Um, but otherwise
[snorts] I think we're pretty focused on
just solving problems that we have and
our customers have and kind of building
the next thing.
>> Cool.
Sweet. Um,
I I loved this part of the interview,
too. [laughter]
>> Did we answer all of your team's
questions?
>> Questions?
>> Do Oh, did we get through all my team's
questions? Let's see. Uh, I think we
did. Um,
uh,
I'm curious also how you would answer
like the unshipping question cuz also
like if you're doing this kind of like
AIdriven development, you ship a lot.
You have a small team, so it's a lot of
operational load.
>> The reason I asked that is because I
don't think we do a good job of that.
Um,
and
I have this feeling that some of the
products are like a little bit messy
because of that. And I think
particularly for Kora,
um
there's just a big product surface area
and it can do a lot of different things
like it we have an email assistant so
you can ask it like you know uh tell me
about the trip I'm taking and it'll go
through all your emails and you know
summarize the the trip. Um or we have
this feature that it automatically
archives any email that you don't need
to respond to immediately. Um, and then
twice a day you get a brief that
summarizes all the stuff that you
probably need to see but you don't need
to like actually do anything with and
you just scroll through it and you're
done. Um, and there's just like all this
there's all this complexity that around
you know for example
how are emails categorized? So now we
have a whole view of we have all these
categorization rules and you can order
them and whatever, but like it's just
complicated and hard to communicate and
and uh and I want to retain a lot of the
like all the power and flexibility, but
also you can't look at a screen and be
like I have no idea what's going on.
This is like way too complicated. So
that's I'm just like I'm processing all
that stuff. So the the kind of like
deletion, you know, un unshipping idea
feels like an interesting
um cultural principle that we haven't
really explored.
>> Yeah, it's really hard. I think there's
like a social cost to it, too, where
like you kind of want to be the person
who tells your coworker to unship their
thing. [laughter]
>> It's definitely tricky. It's more than
just the code. Yeah, I I definitely
learned this at Instagram honestly cuz I
I think Facebook does a terrible job at
unshipping and we had this problem where
>> every time we I think even like
unshipping pokes was like really spicy
cuz there's a bunch of these like
old-timers. They're like, "No pokes,
you're never going to take it away." But
like if you look at the data, no one
really uses it anymore.
>> But for sentimental reasons, they were
kind of tied to it.
>> And so like for Facebook, it always
maybe nothing ever got unchipped. It
always got moved to like a secondary
place like a, you know, like an overflow
menu somewhere that no one looks at,
like a graveyard.
>> Yeah.
>> And I think Instagram was just very
principled. There was like, you know,
very strong in a product and design
point of view that was like, if this
thing isn't used by like half of people,
you know, 50% of WOW or whatever, we're
just going to delete it and deal with it
and then we'll figure out some next
thing that's used by more people.
>> I love it. Um, well, thank you. This was
amazing. I'm really uh glad I got to
talk to you and uh keep building.
>> Thank you for having us.
>> Yeah. Thanks.
[music]
>> Oh my gosh, folks. You absolutely
positively have to smash that like
button and subscribe to AI and I. Why?
Because this show is the epitome of
awesomeness. It's like finding a
treasure chest in your backyard, but
instead of gold, it's filled with pure
unadulterated knowledge bombs about chat
GPT. Every episode is a roller coaster
of emotions, insights, and laughter that
will leave you on the edge of your seat,
craving for more. It's not just a show,
it's a journey into the future with Dan
Shipper as the captain of the spaceship.
[snorts]
So, do yourself a favor, hit like, smash
subscribe, and strap in for the ride of
your life. And now, without any further
ado, let me just say, Dan, I'm
absolutely hopelessly in love with you.
