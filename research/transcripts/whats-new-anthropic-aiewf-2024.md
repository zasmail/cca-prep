---
title: Whats New from Anthropic
speaker: Alex Albert
source: https://www.youtube.com/watch?v=EuC1GWhQdKE
retrieved: 2026-07-16
method: youtube_transcript_api
word_count: 2239
---

[Music]
morning
everyone so today I want to start with a
uh a little story um a short history
lesson if you will so you know sit back
get comfortable uh I'm going to take us
back to the year 188 too it's the dawn
of the electrical Revolution really the
world's first commercial power plant
just opened up electricity this amazing
new force is all the rage in the
manufacturing
industry people are claiming that it's
going to change
everything and yet something very
interesting happened around this
time or rather it didn't happen you see
despite electricity's obvious
superiority in comparison to the
traditional techniques that the time
like steam engines it didn't immediately
improve manufacturing
productivity why well because Factory
owners were simply trying to replace
their old technology with this new
technology into an outdated
Paradigm let's picture a typical Factory
at the time so we have a huge cool fired
steam engine on one end and we have a
network of transmission lines going
across the top all driving hundreds of
machines locked in the same
Rhythm these Legacy steam power
factories were incredibly inefficient
you know if one station needed power all
of a sudden you had to turn on that
entire steam engine and it had to power
all of them Factory layouts were
dictated by the limitations of the
transmission lines not by what was best
for the process or for the
workers when electricity arrived many
Factory owners simply swapped out the
steam engine for an electric one and
sure you know they added some lights and
you know workers didn't have to toil
next to a Coal Fired furnace all say but
the fundamental limitations of the
factory
remained so this real electrical
Revolution well it didn't actually come
until we imagined factories from the
ground up with electricity at its
core factories started to become
flexible and adaptable they allowed for
smaller specialized tools workers could
bring their tools to the items instead
of having to Lug the items back to their
workstations the entire Manu facturing
process became more efficient more
Humane and more
productive now let's fast forward 140
something years to today and you can see
that we find ourselves at a similar
point in regards to Ai and
llms Enterprises startups developers are
all building and integrating LMS into
their products but often they're just
tacking it onto their existing product
surface adding a few star icon buttons
in the top left corner and calling it a
day and this is not the first time we've
seen this in Silicon Valley let's think
back to when mobile first emerged right
companies simply tried to just shrink
down their website and put it on a
phone it wasn't until we redesigned apps
from the ground up with the unique
capabilities of mobile like always on
camera and GPS that we actually began to
see true innovation in the space and
adoption this is when the Snapchats and
the Ubers of the world started to
emerge so just as companies and just as
factories went through their you know
replace steam engines with electric one
phase and tech companies went through
their just hire a couple mobile web dev
people phase we're now in our magic star
icon phase with respect to
Ai and yeah it's funny but the thing is
you can't blame any of the companies or
developers that are actually trying to
do this right now right like all of us
are trying to do this but in many ways
we're just still so early llms are
non-deterministic they're hard to build
on they're completely different than
what most developers are used to
using reliability is still an issue
prompts still take rounds and rounds of
optimization and we've also just started
to scratch the surface of potential
product
opportunities so far not much has really
stuck Beyond just the text
box we've been missing something
something that's a little hard to put a
finger on but just last week I think we
scratched the surface of a potential new
product future that we can
build as some of you may have heard last
Thursday we released our new model
Claude 3.5
Sonet 3.5 Sonet is the first model that
we released in the new Claude 3.5 family
is only the middle model and yet it is
better than our last best model Claude 3
Opus in my opinion Claude 3.5 Sonic is
one of the best models in the world
right now and the benchmarks seem to
back it up MML
human eval gpq tool use all the common
characters here it's top of its class in
many regards in these academic lab type
environments but what I am most excited
for is how it actually does in the real
world the model is particularly strong
in rag use cases thanks to its 200k
context and also has near perfect recall
over that entire context as
well on coding tasks 3.5 Sonet seems to
grasp debugging problems better it's not
getting stuck in those same Loops as
much as previous
models one of the best methods that we
found for actually measuring more
complicated chains of reasoning is pull
request they have a defined task they
usually take a few steps to solve and
the model is able to iteratively write
and test its way to a
solution in our own internal pull
request EV valves we're seeing that
cloud 3.5 Sonet scores a
64% and to put that number in comparison
Claud 3 Opus only scored a 38%
3.5 Sonet also has state-of-the-art
Vision abilities it shows considerable
improvement over three Opus in basically
every Benchmark that we tested it
on things like table transcriptions and
OCR are Breeze now passed this table in
a uh 3.5 Sonet and basically replicated
it perfectly and marked down um probably
can't read all those numbers but trust
me I I double checked them to make sure
they're all right uh Vision capabilities
were actually what amazed me the most
when I started playing around with this
model it feels like we are really on The
Cutting Edge of unlocking so many more
use
cases and you know as you're hearing me
say all this you might be thinking well
that's great Alex but I mean it doesn't
mean anything if I can't actually use
the model and you're right and we heard
you and that's why 3.5 son is available
on RI AWS bedrock and vertex
AI we understand that developers want
Choice when they're building and we want
CLA to be available wherever you
are in terms of price ing 3.5 Sonet is
five times cheaper than three Opus it's
only $3 per million input tokens and $15
per million output
tokens 3.5 sonnet's combo of speed
intelligence and low cost makes it much
more economical to use and embed in your
apps than three
Opus but 3.5 Sonet is not all that we've
released in the past week we also
released a new product feature that I
think is actually more inspiring to
developers in terms of thinking about in
building those AI products from the
ground up it's called
artifacts artifacts separate the content
that CLA produces from the actual chat
dialogue
itself this allows you to work
collaboratively with Claude on things
from essays to svgs to react
websites artifacts become really
powerful when you combine it with 3.5
Sonet those coding skills plus that
reasoning ability plus that strong
visual Acuity enables a new product
experience that's really fun to use
it's also a developer's best friend and
that it allows you to quickly take
screenshots and figma diagrams and
quickly turn it into code and components
that you can actually just go use uh as
you can see in this I basically cloned
her entire claw. a chat layout and react
just from a single
screenshot and this feature has
practically been hiding in plain sight
now uh just waiting really to be
discovered for over a year and a half
maybe this tweet is right and we really
are early on this scurve of production
productionizing llms which I think is
actually pretty
inspiring an artifact is not the only AI
feature that we launched recently on
Tuesday we released
projects projects enables Dev teams to
work and collaborate much more
efficiently by grounding cla's outputs
in your own knowledge whether it's style
guides or code bases or transcripts or
even your past
work on our CLA team plan you can even
share these projects and your chats with
all your
teammates at anthropic our Engineers now
upload code repos and documentation that
they use and I've started to see people
actually just share the chats and the
artifacts instead of Google docs or site
documentation projects is another great
example of when you think from an llm
and an AI standpoint first you can
actually start to build product
experiences that compl these
Technologies and don't feel like a
simple add-on to what you already
have so now that hopefully the creative
product juices are flowing in everyone's
Minds I want to dive a little bit into
API improvements that we've rolled out
recently and things that allow you to
actually build this cool
stuff I also want to give a preview of
what's coming next that will enable you
to build even
more so a month ago we released our new
tool use API tool use allows you to give
Claude custom client side functions that
it can then intelligently
leverage tool use also enables things
like consisted structure Json
output with 3.5 son it I've actually
started to seen devs give Claude
hundreds of tools at a
time on the developer console front
we're also continuing to iterate we
added a prompt generator that uses Claud
to write prompts for you based on a task
description so you can see in this video
we put in a task description and then
out comes a optimized prompt and then
once that prompt is all done you can
actually just start editing it right in
the workbench itself you can see we've
also added support for variables so you
can edit prompt templates as well test
things like rag use
cases and finally we're also working on
a new evaluate feature which is
currently in console right now with a
beta tag uh and we will plan to share
more on this and continue to iterate on
it very
soon so what else is next um well
there's there's two things that I can
share right now first is that you can
expect more models
3.5 ha cou and 3.5 Opus are coming later
this
year with each model generation we're
looking to increase the intelligence
decrease the latency and decrease the
cost the number one thing that I tell
developers is to not forget to build
with that in mind models will become
smarter cheaper and faster in orders of
months not years when you're planning
your product road map be ambitious
enough to build with the belief that new
models may arrive during your
development period
we are also working on other areas of
research like
interpretability in one of our latest
papers called scaling monos semanticity
we explained how we've been able to find
features within models that activate for
different
topics once you identify a feature
you're able to clamp its value and turn
it up or down to actually steer the
model's
outputs a few weeks ago we showed claw.
AI users how this worked through Golden
Gate CLA which was a version of Claude
that had the Golden Gate Bridge feature
turned up
significantly yeah fan
favorite we currently have a few beta
testers also experimenting with a
steering API um this allows developers
to find and clamp features for specific
attributes and actually turn that dial
up or down which again allows you to
control cla's outputs in in addition to
actually just prompting
it we hope to be able to roll this out
to more developers in the very near
future as
well now anything in this talk has
sparked any ideas I want to encourage
you guys to just go out there and build
and make quick prototypes as fast as
you can to get that validation and that
feedback loop started and for even more
of an incentive uh we actually just
launched another build with Claud
contest
yesterday it runs until July 10th the
top three projects will each receive 10K
in anthropic API credits to see more
details just visit that link below it's
just at the top of our docs page as well
so you can find it there too I'll leave
that up for a second
and finally if you have any questions or
you want to hear more about just what
we're thinking about uh I'll be at that
AWS Booth down the hall for the next few
hours you can also find me on X Twitter
Alex Alber with2 unor um I do try to
read all my DMs I spend way too much
time on that site so feel free to ask
questions there as
well and with that I want to say thank
you guys very much and enjoy the uh last
day of the summit
[Music]
