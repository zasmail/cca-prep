---
title: Fireside Chat, Head of Claude Code
speaker: Boris Cherny
source: https://www.youtube.com/watch?v=Z47vatpsGPI
retrieved: 2026-07-16
method: youtube_transcript_api
word_count: 9105
---
Good morning, guys.
I'm here joined with Boris. Before we
get started, we need to take a selfie
real quick. If you guys can join us.
I'm going to take one real quick, all
right?
All right, here we go.
Everyone say cheese.
Just kidding.
Okay. Um we have 40 minutes joined by my
amazing friend Boris.
Um
who doesn't need any introduction, but
in case you haven't heard of him, he's
the head of Cloud Code. I'm a director
of product on the Dev Infra team here at
Meta supporting our AI developer
productivity stuff.
And we're going to just have a friendly
fireside chat to chat about a bunch of
different questions that we have for
Boris.
There's a QR code, I think that was
shared up screen earlier or somewhere.
Um we are going to have a later portion
of the talk to be open open mic. So, I
have an iPad here with a bunch of
questions that you guys are submitting.
We'll go through some of those top voted
questions. But, as you guys are going to
fill those out, um
I want to quickly ask folks, uh how many
people here use AI to write their code?
Just Just a quick raise of hands.
Okay, good amount of people. Um
keep your hands up though if you 100% of
your code is written by AI. Let's look
around the room. How many people is
that? Okay. It's a lot more than before
when I asked these questions. So, it's
really kind of an interesting time to be
here talking about this stuff because
all of us are witnessing this
transformation in our industry. And so,
I think we're going to get this question
started. I'm going to have a few
questions that I'm going to start off
first. And then, as you guys fill this
out and vote on the top questions, I'll
get to those afterwards.
So, just a few quick warmer questions.
Boris,
how many lines of code have you written
this year?
>> How many lines of code?
>> Yeah.
>> Um so, I actually I I pulled the answer
for this in prep because I knew you were
going to ask that question.
>> Yeah.
>> Um okay. So, uh 1.7 thousand PRs.
Uh four added 400,000 lines, deleted
250,000 lines.
>> Okay.
>> think last year it was actually I
deleted more than I added.
Um but this year I added a little bit
more than I deleted and I also tried to
get the token account. Unfortunately,
the the data kind of gets deleted due to
retention and stuff. But since March, I
used 8 billion tokens.
>> 8 billion tokens. And so, those lines of
code that you deleted and added, those
are all written by you or Claude code?
>> Um 100% of my code has been written by
Claude code since Opus 4.5. So, that's
like November of last year.
>> That's crazy. And then, do you use your
phone or your laptop? Like what's the
split nowadays when when you code?
>> Yeah, this is sort of like the the the
craziest thing like I would not have
predicted this if you asked me like 6
months ago, where are we going to be
doing our coding? Um but yeah, like most
of my coding now is on my phone.
Um I would have said you're crazy if if
you told me that 6 months ago. But yeah,
here we are.
>> Yeah, it's crazy, right?
Um
Okay, I think uh
one of the questions that a lot of
people have been pinging me about and we
really want to get your thoughts on is
they're really starting to think about
like efficiency and ROI.
Um
we kind of like hear of Uber and other
companies starting to set like annual
like monthly budgets, for example, like
$1,500
per engineer.
Um but at the same time, Anthropic, you
guys and other frontier labs are pushing
out these more capable but also more
expensive models.
What do you think uh about this? Like
what are your thoughts on how companies
should balance this tension between like
more performing but costly models versus
like having to start to demonstrate more
efficiency, token efficiency?
>> Yeah, totally. So, you know, like I
luckily I get to talk to so many
companies every day, you know, that are,
you know, our customers and kind of
future customers. And broadly, people
think about it in two ways. Some
companies think about it in terms of the
cost.
And other companies think about it in
terms of ROI. And I'm like ROI is
absolutely the right framing because you
don't want to just think about cost
because you kind of spend something on
it and you get something back.
Um
when you think about ROI and kind of
like deploying cloud code in general, I
think it's useful to think about like
what's a a really good way to deploy it.
And I I think like the most successful
companies we've seen, they sort of give
everyone tokens, not just engineers, but
also like the product managers, the
designers, the data scientists. They
give everyone tokens and let the company
experiment to see where the ideas come
from
because often it's just like not the
person that you would expect. Often some
of the most interesting ideas and the
most innovative like ways to improve
processes and kind of like new product
ideas, it's going to come from like, you
know, like an accountant somewhere in
the corner of the org or like a
marketing person that you've never heard
that the CEO has never heard of.
That's where a lot of the innovation
comes from. It won't necessarily be like
the most senior engineer always.
Um
and so I think for this reason like you
kind of want companies to experiment and
you like you want to you want your team
to experiment. The way to do this is
give people tokens and give them safety
to experiment so they feel
like like like they can try stuff and
they're not going to get kind of
penalized for it.
Once you find these internal use cases
that kind of work,
then you want to control the costs and
you want to do that on the back end, not
on the front end. And you know, like
once there's some use case that takes
off, uses a lot of tokens, then you want
to think about how to like optimize
that. There's all sorts of ways like you
know, like in cloud code we have like
per-seat cost controls. There's ways to
use like advisor models. You can change
the model for your entire company. You
can control the effort level for your
entire company.
Um you can set budgets like based on
department, based on our back. So
there's just like all sorts of ways to
do this.
I I think the maybe like the second way
to think about it. So this is kind of
like the deployment side and like how to
actually get it out and like when you're
like at the very beginning. Once
companies have been using cloud code for
a while,
you really do want to think about ROI.
And you know, like for ROI, there's kind
of like two parts. There's the
investment and there's the return.
In the past, the way that, you know,
investment is easy to measure. That's
just tokens.
Return in the past, the way that we used
to measure it is what percent of the
code is written by AI. Or maybe like
percent increase in the lines of code or
something.
And um yeah, like, you know, we just saw
a bunch of hands go up that said, you
know, like 100% of your code is AI. So,
once it gets to 100%, how do you
actually like measure that return? And
that's where it gets kind of hard
because, you know, like we worked on
Devin for back in the day. And you know,
like on on Devin for, you know, like if
if you have like a percentage, like like
2, 3% productivity improvement for a
year, that used to be like pretty good.
Now, the productivity improvements we're
looking at are, you know, like hundreds
of percentage points. And at Anthropic,
you know, we've seen like a 8x
increase in code per engineer since the
beginning of this year.
And so, like in the in this kind of
regime, how do you think about the
return? And I so, I think part of it is
get to 100% of your code written by
Claude. Then think about how much is the
code per engineer accelerating?
And then the third thing to think about
is like what are the other bottlenecks
that are getting in the way?
Because once you get it to this point
where engineers are just like writing a
lot of code, the bottleneck is going to
be like good ideas. So, how do you kind
of unhubble that so that your company
can generate ideas faster? And this
could mean like more PMs or user
researchers or something. Um then you
have to think about how to get these
ideas to market faster. So, this is kind
of unhubbling on the GTM and on the
marketing side.
Um so, this is this is kind of roughly
the order that I think about it in. And
when I look at our customers, everyone
is kind of like a a different step of of
of this adoption curve.
>> Yeah. I think it's really interesting to
think about, like kind of how you said,
it started with coding and just getting
more and progressively more hands up
where is like 100% of their code is AI.
But then you start to realize there's
upstream and downstream bottlenecks, the
ultimate thing that companies want,
which is delivering more business value.
So like un-hobbling those ideas, getting
code to be deployed faster and safely
and more accurate. I think those are all
the things that the the whole industry
is like figuring out. It's like, okay,
let's say coding is like more or less
largely getting solved with AI. What are
the things now that's blocking
coordination and collaboration? I
actually see one of the top voted
questions is about that. So we'll we'll
talk about that in a moment. But I think
that's that's like the interesting
question we're in now. It's like a year
ago if we were doing this fireside chat,
we'd be talking about like how can we
use AI more for coding? How can we sort
of like do all that? But now it's kind
of like the next question. It's like,
okay, what's next now that coding is
more or less going to be more and more
just written by AI. So I think that's a
really interesting situation that we're
in right now.
Um
All right, next question I have uh so
for context Boris Boris and I actually
used to work together on Threads. So of
course and also Threads just hit 500
million monthly actives yesterday, we
announced.
>> Congratulations.
>> Thank you. So I had to obviously ask
some folks on Threads some for some
questions. So I have one question from
there I want to pull out. It's actually
from our ex-colleague uh old colleague
Peter. He asked like, is Loops the next
hype cycle or is it real? Um
maybe you can explain what Loops are for
maybe people who don't aren't familiar
with it and then how you use it
personally.
>> Yeah, yeah. Um have people here tried
Loops, routines?
>> Still pretty nascent, yeah. Not
>> Okay, and and just so I know like how
technical to make the explanation. Raise
your hand if you're like an engineer
that codes.
Okay. So I I think like for the engi-
for the engineers in the room, the way
to think about it is um
2 years ago
we wrote source code by hand.
We started to transition to make it so
agents write the code.
And now we're transitioning to the point
where agents are prompting agents that
then write the code.
Maybe that's like the less technical
explanation. The Vortex explanation like
actually my mental model is sort of like
if code if like source code is like
kind of like the basic level that's sort
of like a statement in programming then
the agent run
writing the code is like a function in
programming and then loops are like a
higher order function. So it's it's sort
of like we're we're stepping up the
abstraction ladder. It's one more step
up. Yeah. So loops are sort of like as
big as the step from source code to
agents was loops are the step from
agents to the next thing. It's just as
important and as big a step.
To me it feels like right now in the
world of like loops where um
I don't know like maybe we're agents
were like a year and a half ago. So it's
still like fairly early but we're
starting to see signs that it's working.
And the the idea is like okay let's say
um
as an engineer a lot of my work is to do
code review.
And so like one thing that I could do is
like I could do the code review by hand.
The other thing that I could do is I can
have an agent and I can prompt my agent
to do the code review.
The loop version of this is I have an
agent that's running in a loop that does
all of the code reviews.
Or like another example is um you know
like I read threads to to see like
people's feedback. Um and so like I
could do this by hand or I can have an
agent do it or I can have an agent
that's constantly looping over and every
like 5 or 10 minutes reading the
feedback and putting up PRs for the
fixes.
Um and so like a couple you know like a
year and a half ago we were kind of at
the first step now we're kind of at the
third step.
And so like when you think about all the
work that we do as engineers and all the
work that you know like non-engineers do
like like like designers and data
scientists and you know like marketing
people and so on.
A lot of the work I think we can
probably chunk up into loops in this
way.
And I think we're starting to get to the
point in the industry where like a
bigger and bigger percentage of the code
is like expressed as loops and a bigger
percentage of the work.
And so for me personally maybe at this
point like 30% of my code is written by
loops
on an average day.
Um if I try really hard I can get to
like 100% for some days, but it it
doesn't totally click yet.
>> Nice.
I feel like if we ask the question of
how many engineers write loops maybe in
a year from now we'll see more hands. So
in some ways you're always like just
kind of living
the like 3 months 6 months ahead of the
rest of the team here and so like I
think loops is something that's been
fascinating to internally. I think
people have been starting to explore
what are these what are the various ways
you can orchestrate all the various
tools you need to kind of create this
sort of like automatic loop because like
right now humans are in the loop, right?
You have to be every single part of the
way. We were just talking about in the
first question how to kind of like get
this sort of process more and more
automated. And so getting this loop
going is really sort of like the key to
to figuring this out um and getting
getting more productivity.
Um
the other thing we've been talking about
for a while is that Anthropic's been
investing a lot in co-work as of late.
I'm pretty sure a lot of the audience
here primarily uses Claude Code. I think
um it'd be great if you could tell us
sort of like why folks here should use
co-work, what are some of the use cases
you're most excited about, you know,
especially related to the first question
we talked about just like um how how
people are using it beyond just coding.
>> Yeah, totally. So for folks that don't
know like the way that you try co-work
is you download the Claude desktop app.
That's the same app that has chat and
Claude Code in it. It also has co-work
in it. Um so you just download it. You
can use it. Works on Mac, works on
Windows.
Co-work is Claude Code for
non-engineers.
Um it's just Claude Code under the hood
and it actually uses the same like
Claude agent SDK that Claude Code is
built on. So the infra is the same and
you can actually build on the SDK
yourself, too. It's exactly the same
thing.
Um the reason we say it's not for
engineer is it's for non-engineers is
there's a bunch more guardrails built
in. So co-work has like an entire
virtual machine. It has this like
actually quite sophisticated
Uh and then we like hook into the
operating system to make sure you don't
accidentally delete stuff. There's a lot
of protection for prompt injection.
There's all sorts of things that we do
that are, you know, make it a little bit
harder to shoot yourself in the foot.
When I think about how I use Cogram, I I
actually use it for everything that's
like non-engineering.
So, you know, like one example is I do
it I use it for project management. And
so like we have stand-up We used to have
stand-up every morning where we talk
about here's what everyone on the team
did.
And now actually what we do is I have
Cogram and it opens up uh this like
spreadsheet in the browser and the
spreadsheet has essentially like all of
the work streams for the week. And it'll
message every engineer in Slack for me
automatically to ask like what's the
latest status. And often their clouds
will respond.
>> What's agents talking to agents?
>> It's like the clouds talking to the
clouds.
>> Yeah, clouds.
>> Um but sometimes like engineers will
respond and then like Cogram sees this
and then it'll fill out the status in
the spreadsheet.
And all this is is like Cogram will open
a browser and it'll do this for you.
It's like zero setup. You just need
Cogram and you need the cloud Chrome
extension and then they'll just kind of
work together to do this.
So, this is like this kind of magic of
combining tools. And I think this that's
like this like magic moment that that
people see when they use Cogram. It's
like, "Oh my god, this thing can use my
tools and it can combine all my tools
for me in the way that I would." And it
it just feels incredible. It feels like
using like a AI chat app for the first
time. It's like a revelation.
There There's this like more
sophisticated usage um
One thing that I used to do is I would
use Cogram to book all of my travel.
So, what I would say is like, "Okay,
here's like my itinerary. I need to be
here on this day, here on this day. Can
you like go out and book the plane
tickets for me?" And it I guess it would
like open a browser and it would go to
this like, you know, travel site that we
used to book stuff at Athropic. And it
would just like fill it out and book the
tickets.
And what I've done now is I've actually
automated it a little bit more. And so
what Cogram does now is it has a
scheduled task where every day it'll
look through my email.
It'll look for any events that I've
accepted on my Google Calendar.
If the event is in a different location,
then, you know, like it's not in San
Francisco, it'll go and it'll
automatically book the tickets. And then
it'll send it to me. It'll book like the
tickets. It knows to book like hotels
and it knows all my like flight and
hotel preferences. And it'll just do
this automatically.
And so, you know, like I was just in
Tokyo for Code with Claude, and then,
you know, I was in London and Berlin for
Code with Claude before that.
And uh it just fully booked all the
tickets for me. It was It was like like
multi-leg like flight and hotel thing,
and it just booked everything. I did I
wasn't involved at all.
>> at all?
>> Not at all. Yeah, it just like it found
it in my email and then and it booked it
after I confirmed.
Crazy.
>> Okay. Yeah, I mean, how many people here
has tried Code Work? Just curious.
Good amount, actually, right?
Hopefully more.
Um
That's great. I think um
another question that I got a lot of
pings about, would love to hear your
take on this, is that many of us only
got access to Fable for like maybe 3
days or so. So, while we wait to hear
what happens next, like, you know,
obviously I'm I'm assuming you had
access to them for much longer, share
maybe some of your experiences with how
you use Fable for coding and like, you
know, now you guys have a family of
different models. Um how do you think
about using different models for
different software engineering use
cases?
>> Yeah, totally. Um and you know, like
first of all, like, you know, with with
Fable, just want to say it from our
point of view, it is a it's like a it's
a misunderstanding and we're working uh
to hopefully get it back really soon.
Um
the the the way that I think about Fable
is
with coding, there was this moment back
in November of last year. I don't know
if everyone like remembers this, but
everyone started like posting on Twitter
and kind of talking about like how good
the model has gotten at coding. And what
happened is Opus 4.5 came out.
And the leap from the previous model to
Opus 4.5 was so big that for a lot of
people they just started writing all of
their code using Claude for the first
time. And that that was actually the
moment for me where I just uninstalled
my IDE cuz I wasn't using it anymore.
Wow. And so like for me that's the same
moment when Claude started to write all
the code.
The leap from Opus 4.8 to Fable
feels to me like a leap of at least that
same size. And I think it might be even
a larger leap in model capability.
For me Fable is um
it it's just like it has this like
nuance and dimensionality and kind of
like way of thinking about things that
is kind of like similar to like my
smartest co-workers. It's not just like
a blunt instrument the way the previous
models were where it doesn't understand
nuance. It it's actually like really
able to grapple with a problem. And this
is useful for all sorts of things from
like data analysis cuz there's a lot of
nuance there and you have to understand
like you know, you have to ask why like
three times to get to the bottom of a
question. Fable just naturally does
this.
Um it's useful in debugging where you
have to form a hypothesis and you have
to kind of like chase down that
hypothesis. Look for evidence. It's able
to do this really well. And for coding
I feel like I actually just ran out of
hard problems to give it.
Like I I just couldn't think of a harder
problem. Like every problem that I gave
it, it essentially one shotted or maybe
like few shotted with a few prompting.
With a with a little bit of prompting. I
just kind of ran out of hard problems
and this is something that I heard from
a lot of the team also.
So yeah, it's like it's it's a it's
quite a big step.
>> Is Claude code just basically 100%
written by Claude code at this point?
>> Yes. Uh that has been the case again
since November of last year.
>> Oh, so it wasn't even like with Fable,
it was like with Opus 4.5.
>> Yeah, with Opus 4.5. Yeah, that's true
for Claude code, that's true for
co-work, it's true for an increasing
number of
Anthropic's products. I think I think
across all of Anthropic um 80 to 90% of
the code is written by Claude code on
average. But actually for a larger and
larger share of teams, it's just 100%.
>> I also heard that um Fable is like more
expensive, but it's it's also a little
slower, but it's also like incredibly
intelligent, like you said. How do you
Do you Do you just use Fable for like
all of your tasks, or do you use like Do
you drop down to like Opus or Sonnet for
different kind of use cases?
>> Yeah, I use Fable for everything. Just a
feel for everything. Is it because
Anthropic has no
>> budget?
>> [laughter]
>> So, you know, like I don't
>> topic, we do actually think about token
use, right?
>> Yeah.
>> Like, you know, like we we essentially
make the tokens.
>> Yeah.
>> Um but they're not free for us because
every token we use is a token we do not
give to a customer. Right. So, there's
an opportunity cost.
Um
when I think about it, it actually maybe
comes back to ROI. So, like when you
think about kind of ROI for something
like Fable, you can reduce the
investment maybe like 50% or something
if you use like, you know, Fable with an
advisor model or, you know, use Opus by
default and have a call out to Fable
when it needs. So, there's like all
sorts of ways to optimize usage, and as
new models come out, you have to kind of
keep tuning the way they optimize this
usage. It's actually quite a bit of work
to keep up with it and to keep that you
have to like run evals to make sure it
works pretty well.
Um although, you know, like you can use
advisors. That's kind of the recommended
out of the box approach.
But I I actually think that if you think
about ROI, there's probably like 50%
chance to reduce the investment, but
probably like a thousand percent
opportunity or even hundred thousand or
ten thousand, whatever, percent
opportunity to increase the return.
And so, what I would think about is just
use the most expensive model and focus
on how do I get more out of it? How do I
increase the return? Do not focus on
cost cutting. It's just like it's so
early in kind of like the adoption of
this technology to think a lot about
this. And you probably want to spend
like some effort on cost cutting, and
like you definitely want to make sure
costs are under control and kind of
well-governed. But I would focus almost
all your effort on increasing returns.
>> Yeah, focus on the upside more than like
the potential downsides, essentially.
>> Exactly, because there's so much more
upside right now than there is uh than
there is kind of like room to optimize
the downside.
>> Yeah. Hopefully we the rest of us get
access to fuel soon so we can kind of
all explore
that as well. Okay, I think
we got a decent amount of questions.
Actually there's 107 questions. We're
obviously not going to get through all
of them, but I'm going to handpick and
kind of like MC some of the top voted
questions that we got here.
So Andrew kind of the top voted question
here is saying, "What is quad code doing
to improve collaboration? Currently it
feels like a solo work product with only
awful things like GitHub for working
with others." Well, that's a
interesting question. What do you think?
>> Yeah,
you know, we have a bunch of stuff in
the fire that that we're that we're
cooking up.
So hopefully we'll have something there
soon.
In the meantime, the thing that I would
recommend is use an MCP
to hook up quad code to slack or to
teams or to G chat or whatever you use
for cooperation.
>> Sounds good.
The next voted question was, "Since
agents can do most of the code now,
where should engineers focus most?"
Kind of touched on this earlier, but
yeah, curious.
>> Yeah, yeah. So you know, like as we
think about like what engineers do, one
of the things that we do is coding, but
we do like a lot of stuff that's not
coding. All right, so we do um
you know, like talking to customers,
coming up with ideas, jamming on stuff
with with with designers and PMs, doing
data analysis,
figuring out what to build next,
aligning with other parts of the org.
There's just like all sorts of things
that we do as engineers.
I think over time the model will be able
to do all of these things better than we
better than we can.
We are not there yet.
And so I think in the meantime, like the
model does the coding, but someone has
to prompt the model.
And figuring out what prompt to give the
model, there's actually like a lot that
goes into that, right? Like you have to
kind of figure out what's the next
thing. You have to do the market
research. You have to talk to your team.
You have to do all this other work. Um
so yeah, it's it's kind of all all these
other things.
>> Yeah, and then I think like you said
with loops, too, that's also
progressively moving up the abstraction
layer, where maybe at some point for
some certain cases, you don't even
actually need a prompt. And so, I think
it's interesting, like I said earlier in
in this in this conference, is like
we're in this like transformational
stage. We're all figuring this out
together as an industry. Um we also see
have seen at Meta that like like you
said, it's actually a minority of an
average software engineer's time is
actually spent coding. It's all the
other things that kind of happen
upstream and downstream with it, whether
it's like managing your code
deployments, or if it's like
collaboration, and working kind of like
in docs and planning. And so, I think
this is kind of like where
where like Claude and other other apps
and products for AI is just thinking
about how can we just accelerate the
whole development life cycle. This is
something that we're we're largely
solving now with coding, and we're going
to continue doing so, but then the
upstream and downstream parts of
development life cycle is still still
the thing we're discovering.
>> Yeah, yeah. And like like coding, I
think was always the minority of the
time, right?
>> been, yeah.
>> And for me, it's like sometimes it's
like really fun to code and like write a
bunch of code by hand, and then
sometimes it's just like a total slog.
And you know, like I never wanted to do
it by hand in the first place.
>> Yeah.
>> Um I heard the Twitter laughing.
>> [laughter]
>> Yeah, yeah.
Um and so like, you know, like sometimes
like when I don't have, you know, Wi-Fi
on like an airplane or something, I'll
I'll still like write code by hand like
just for fun.
But it's uh it's actually like not
something that I personally really miss.
It it feels to me like Claude code is
just like this like jetpack, where like
as the model gets better, I get like
more jets or something in my jetpack,
and I can go faster and faster. And at
this point, I'm like purely bottlenecked
on how fast I can prompt. And most of my
prompting now is actually just like
audio, like talking to Claude. And how
and and being bottlenecked on good
ideas. But but coding is just no longer
the the bottleneck.
>> Right. And this is kind of like what a
lot of conversations have been about is
like what is the role of software
engineering? It's like less and less
about the coding aspect and more about
sort of like how you supervise these
agents, how you sort of manage the agent
end-to-end, and help generate and
product productize some of the ideas
that you have.
Um
I think related to that is like, you
know, with the explosion of AI-generated
code, everyone's just like writing code
so quickly now with AI. How does How How
do you or Anthropic sort of like handle
the downstream impacts of that? So like
with code review, right? Like I think a
lot of a lot of companies require a a
human code review. That paradigm may or
may not be actually breaking or shifting
because of the increased supply from
upstream. How are you thinking about
that?
>> Yeah. So when we think about code,
essentially like you you write code and
then it it it gets to production and
then hopefully it drives a business
metric for you like like revenue or
usage or whatever whatever it is that,
you know, like whatever business metric
you care about.
When you think about this process,
there's all sorts of different
bottlenecks and the biggest bottleneck
used to be coding.
We've now solved that bottleneck and,
you know, at Anthropic and for a lot of
our customers that, you know, have
adopted Claude Code for a bit, they're
getting to this point also.
And so like now we're thinking about the
next bottleneck and, you know, for us
the next bottleneck was code review. You
write a lot of code, now someone has to
review it.
And our answer was to build a product
for this and so we built this product,
it's called Claude Code Review. It's
available to anyone. Um you can use it.
It is the the exact same code review
product that we use internally at
Anthropic for every single pull request.
It is different than any other code
review product on the market
because it's a lot more expensive.
And the reason it's a lot more expensive
is it uses a large number of tokens to
fully automate the code review.
So by the time that I see a pull request
as an engineer, there's essentially a
guarantee that all the bugs have been
caught. And it's not, you know, it's
it's not 100%. We're still working on
improving it, but it's like, you know,
like 98, 99% of the bugs. So, like when
I look at the code, essentially, like
I'm not looking for bugs anymore. I know
there's no bugs cuz Claude caught it and
Claude fixed it. Um the next thing is
like, is this a pull request that should
exist? Is this a good idea?
The next bottleneck for us was security
review because you're running all this
code, you need it to be secure. Um you
know, like agents can introduce
vulnerabilities the same way that people
can. And so, how do you make sure the
code is really good and secure?
And the answer for the for us is the
Claude is is is the Claude security
product. And again, like we we built
this internally to solve our own
problem, to solve our own bottleneck.
And what it does is every week
we run it and it scans over all of our
codebases, it finds issues, and it fixes
them autonomously.
And we're actually at the point now
where, you know, we we we do red teaming
and we do penetration testing for like
every big new feature launch to make
sure that it's secure. And we're we're
actually getting to the point where
Claude security is catching issues that
even pen testers didn't catch.
>> Oh, wow.
>> This didn't used to be the case. We've
had this product for a bit, but because
of the model with Opus 4.8, it's now
starting to get to that point.
And so, you know, like this was the next
bottleneck. And so, you know, we solved
it. And again, we make this available to
our product, so as a product so
customers can use the same product, too.
And this is just like the Claude
security product.
And, you know, now we're thinking about
the next bottleneck. And the next
bottleneck might be like idea
generation. Um it might be like
optimizing CI to make it kind of scale
better.
And so, like in a for example, a thing
that I did last night is um I noticed
that our CI was a little bit slow.
And so, what I did is I I had Claude
code run and I said, "Use a workflow
to look at my data,
look at real CI timings from, you know,
like you know, from from the data set,
and optimize CI to make it much faster."
That was my prompt. That was the entire
prompt.
>> That's it?
>> That's it.
>> [laughter]
>> Um it used a dynamic workflow, which is
this new feature that we launched a few
weeks ago where essentially the model
kind of orchestrates uh dozens,
hundreds, thousands of sub agents
dynamically. It's essentially like a
form it's a new form of test time
compute.
And uh it used I think something like uh
you know like like a few a few million
tokens and it ran for like a few hours.
And it produced four power quests
that reduce the eye time by 50%.
And so I I landed those last night. And
you know like this is work, you know,
that would have taken days or you know
weeks or months in the past to do all
this kind of profiling and this is just
like, you know, it's just the next
bottleneck and we can use Claude for it,
too.
>> That's crazy. So you basically, I mean,
the way you just described all
everything since we started is like just
keep going after the next bottleneck,
keep going after the next bottleneck. So
far in the base model is just keep like
just has the underlying capabilities to
be able to progressively solve it. Um so
that's really cool. I think um
it's actually a good segue into the next
question that I wanted to ask, which is
like what is the next big thing for you
and your team? Like what is your vision
for the next year? I mean, kind of
mentioned like just solving bottlenecks
and bottlenecks um as they as you come
across, but like what is the vision for
Claude code over the next year?
>> Yeah, so okay, as a caveat, we plan on
like a weekly or monthly cycle.
We don't have a one-year plan.
>> [laughter]
>> Um this space is changing too fast. So
like the exponential is the exponential
is crazy. You just like you have to hang
on and plan like a little bit at a time.
Um broadly, the direction for us is very
similar to the direction from before,
you know, like from the last year or
from the last two years. It's we want to
be the most capable uh agent. We want to
work anywhere. So wherever your team
works, Claude works.
You don't have to like switch to our,
you know, full stack to to use it.
And we want to let people experience the
capabilities that the new model brings
in a way that other products don't
really let you experience. And this is
something that we realized a couple
years ago, you know, song 3.5 was a
quite a big leap in coding, but we felt
like there weren't really a lot of
products that let you fully experience
that week.
And so Claude code was like a way to get
at that. It was that the idea was like,
okay, no more source code, you're just
using an agent. That's the way that you
experience this. And as we think about
the model over the next few months, over
the next year, it's going to get even
better at long running work.
Um you know, like Claude is already by
far the best at long running work. That
lead is going to increase, I think.
The code is going to become more secure.
It's going to become higher quality.
And the model is going to become even
better aligned.
So whatever your intent is as the user
of the model, as an engineer or a
product manager or a designer that's
using the model, the model will be even
better at expressing that intent. And so
like we're going to be kind of like
looking at these capabilities. We're
going to be looking at like what are the
products that we can build
to let people experience this in the
easiest way possible.
>> Nice.
Um Reza asks a question here that I
thought was really good, too. Coding in
large-scale projects is not the biggest
problem. Maintenance is.
How should the code be maintained in
long term? Like how do you guys deal
with maintenance?
>> Yeah, so with something that I've been
experimenting with is uh actually using
like loops for maintenance.
>> Loops for maintenance. Can you share
more?
>> Yeah, so like so one example is um you
know, like you you can have Claude code
running in a loop to be like
uh look at the code base and improve the
architecture.
Or look at the code base and uh find
places where the test suite is, you
know, flaky and improve it. So, you
know, to get rid of the flakes. Or find
instances of tests that are not useful
that we can just like delete. Um or, you
know, like look at the code base, look
for duplicated abstractions and unify it
into a single abstraction. And so these
are actually like all loops that I have
running.
>> Do you So like in those cases do you
check or review what the code does
before they delete or make any changes
or you're just kind of they just send
out PRs and you're just like reviewing
them after they run the loop?
>> Yeah, it's the second one. So I just
look at the PRs.
>> You just look at it the change after
they made it.
>> Exactly, exactly. For problems like this
it's actually like quite easy I think
for Claude to kind of wrap its head
around these these shape problems so
it's usually quite good.
>> Yeah.
>> If you use the latest model and if the
result isn't good, all you have to do is
say, you know, like look for
opportunities to improve the quality of
the code base and then just add the
magic words
use a workflow.
>> I thought you were going to say make no
mistakes.
>> [laughter]
>> I thought that was going to be the
answer.
>> But yeah, it's like essentially like you
say use a workflow and it'll throw more
test time compute at it and it'll give
you a much better result.
>> Yeah. That's really cool. Workflows is a
pretty new concept. I think I saw an
announcement about it. I don't know how
many people here are familiar with it
but it seems like another one that we
should be watching out for. Like is
there is there a quick summary of the
difference between workflows and loops
or is it kind of like the same thing?
>> Um yeah, it's like it's fairly
different. So the way I would think
about it is, you know, like there's
these traditional scaling laws in AI and
you know, there's this like scaling laws
paper a while back that kind of
introduced this idea that the way that
transformer scale and the way that LLM
scale is it's a function of the the
data, the size of the neural network,
and the amount of compute that used to
train the neural network. And so like
this is this kind of exponential
property of the model. This is why
intelligence keeps increasing
exponentially is because of these three
scaling factors.
Over the last couple years what's
happened is we've actually added a
fourth factor which is test time
compute. And essentially what this is
what test time compute is actually just
a fancy way of saying how many tokens
does the model generate. That's it. So
there's a way to like make it so the
model can productively generate more
tokens
in order to achieve a better outcome.
There's a few ways to do this. One is
effort settings. And so you know, for
Claude models, there's like low effort,
medium, high, extra high, max. This is a
way to configure how many tokens
essentially you want the model to
output. This is tuning the test time
compute behavior. The more tokens, the
better the result.
The second way to do it, which we just
introduced, is dynamic workflows. And
this uses Claude to essentially write a
little kind of like program that's
running actually in a virtual machine to
orchestrate other Claude's
to solve a problem. It's a new form of
test time compute that we're still just
exploring, but essentially it's a way
for Claude to, you know, launch dozens,
hundreds, thousands of agents to get
work done.
>> Wild.
Awesome.
Um okay, next question. What are some of
the hard problems that Fable has had a
hard time to solve?
>> Yeah, I think that, you know, like our
models are not perfect. And there's a
lot of, you know, places where they
still need to improve.
Um one of the places is product sense.
So, I still come up with better product
ideas than Fable does.
>> So, idea generation.
>> Idea generation.
>> Yeah.
>> Yeah, it's not there yet.
>> that. Okay.
>> Um its code is now better than the code
I would have written. Its front end
design is better than my design.
Um another place where I think I'm still
a lot better than Fable is is
distributed system design. So, kind of
thinking through like, what are the
services? How do we organize it? How
does data flow? How do we like think
about load factors and things like that?
Um this is a place where I think Fable
is still there's still a lot of
opportunity to improve it.
>> How many more months before that's not
true anymore?
>> Um
>> Or weeks? Or days?
>> No, I I don't like giving predictions,
but I would I would say by probably by
the end of the year, it'll it'll be
quite good.
>> Okay. All right.
We heard it here. Um
we're approaching the last few minutes,
so I'm going to probably close this out
with this last question here.
This is a question from Andrew. He asks,
"How do you prevent engineers from
getting lazy and accepting everything
they output in Claude.
>> There's a couple ways to think about it.
Um
One I I think there's like maybe like
two parts to this question.
I think one part is
how do you make sure that the output is
really good and that people are kind of
doing the right thing.
Um one one way we think about this is
how do we get Claude to do the right
thing so you don't have to.
And like an example of this is um you
know like since the beginning we've had
these permission prompts for for Claude
code. And you know like the the prompt
like anytime Claude wants to run a
command on your computer, it asks you is
it okay to run this yes or no.
Um you know like can I run this bash
command? Can I use this MCP? Can I fetch
this URL in a browser? Yes or no.
And an engineer sitting there has to
approve it or decline it and say yes or
no.
And um
something that we found is over time it
felt like you get kind of like a little
lazy and you know at least for me I just
like kept saying yes. I wasn't really
reading the commands.
And I'm sure this is kind of true for a
lot of people. I don't know if like you
admit this to your boss, but
>> [snorts]
>> And and so like our security people
actually saw this and they were like hey
like there's a human in the loop. The
goal of that human in the loop was to
improve security.
But actually what's happening is that it
is hurting security because people are
just like they have this like prompt
fatigue. They just like keep saying yes
without actually reading the details.
And so the thing that this led us to
build is auto mode
which is a new permission mode in Claude
code. This is what we use internally at
Anthropic and actually now like the vast
majority of our users use it also. And
what this is is every permission prompt
that we route to a model
and the model decides yes or no based on
what you've said so far in that
conversation.
And not only is it more secure and we've
kind of shown that the results are
better than dangerous mode and better
than the default yes no permission mode
because of prompt fatigue.
But it's actually like kind of one less
thing I need to do as an engineer.
And so the thing that it unblocks is
very long running agents. Because you
don't have to sit there saying yes or
no, it means I can now run Claude for
hours or for days. And there's all sorts
of benchmarks that show that, you know,
like Claude is the best at these kind of
long-running tasks.
And of course, you know, like there's
years of research that went into making
auto mode working because like
uh that that made it work because like
if you look at, you know, a Claude
models, they're essentially not
resistant to prompt injection anymore.
They're they're not susceptible to
prompt injection anymore.
And this is a thing that I think
surprises people sometimes, but if you
look at our system cards, the success
rate at 100 attempts is like around 1%.
It's just by far the best in the
industry.
And when you take this and combine it
with a prompt injection classifier,
which we run for a large share of
traffic now, essentially the models are
not susceptible to this kind of attack
anymore. And what this enables us to do
is ship auto mode. And what this means
is that as an engineer, I don't have to
sit there and say yes or no.
So, this is I think like part one
answer to the question, which is
let Claude do more and figure out how do
you unblock Claude to do more safely
rather than trying to control yourself.
I think the second thing is kind of like
what is the feeling day-to-day as an
engineer when you're not writing the
code anymore? How do you still learn?
How do you still stay in the loop? And
actually one thing that I found really
powerful for this is output styles in
Claude code.
Whenever any new engineer joins our
team, we tell them to use the
exploratory output style. So, this is
just like {slash} config output style
equals exploratory. You run this in
Claude code or you can ask Claude to set
this for you.
And what it does is that anytime Claude
will make a change, it'll explain to
you, "Hey, here's how the architecture
works. Here's how this language works if
you haven't used it before. Here's how
this part of the code base works." It'll
explain to you so that you can learn.
And then there's also a learning output
style which you can use, and this is for
people that are not coders.
And it'll explain to them, "Hey, here's
like how this language works. Here's
like, you know, like at a very basic
level, it's going to teach you how to do
the thing instead of doing the thing."
So, it'll say, "Okay, in JavaScript, you
know, for example, here's how something
works. I'm not going to make the change
for you.
I'm going to walk you through it. Step
one is open this file and edit it in
this way. Step two is run this command.
Okay, I see you done that. Step three is
do this." So, actually, I think like
output styles and using Cloud even more
are a super powerful powerful learning
tool. And it helps me as an engineer
kind of understand what's going on even
as our stack changes as our infra
changes. And especially when I'm working
in new languages.
>> Awesome.
Well, we're at time. It's been Like I
said, it's a very interesting time in
our industry, and it's been a privilege
to have Boris here working on Cloud Code
share some of his thoughts. Um and yeah,
let's give a round of applause to them.
Thank you so much.
>> Yeah.
