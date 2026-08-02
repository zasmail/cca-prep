---
title: Evolving Claude APIs for Agents
speaker: Katelyn Lesse, AIE Code Summit 2025
source: https://www.youtube.com/watch?v=aqW68Is_Kj4
retrieved: 2026-07-16
method: youtube-transcript-api
word_count: 2467
---

[music]
Good morning. Um, so first let's give a
huge thank you to Swix and the whole AI
engineer organizing team for bringing us
together. [applause]
I'm Caitlyn and I lead the claw
developer platform team at Anthropic.
Um, so let's start with a show of hands.
Who here is integrated against an LLM
API to build agents?
Okay, I'm talking to the right people.
Love it. Um, so today I want to share
how we're evolving our platform to help
you build really powerful agentic
systems using claude.
So, we love working with developers who
do what we call raising the ceiling of
intelligence. They're always trying to
be on the frontier. They're always
trying to get the best out of our models
and build the most high performing
systems. Um, and so I want to walk you
through how we're building a platform
that helps you get the best out of
Claude. Um, and I'm going to do that
using a product that you hopefully have
all heard of before. Um, it's an Agentic
coding product. We love it a lot and
it's called Claude Code.
So when we think about maximizing
performance um from our models, we think
about building a platform that helps you
do three things. Um so first, the
platform helps you harness Claude's
capabilities. We're training Claude to
get good at a lot of stuff and we need
to give you the tools in our API to use
the things that Claude is actually
getting good at. Next, we help you
manage Claude's context window. Keeping
the right context in the window at any
given time is really really critical to
getting the best outcomes from Claude.
And third, we're really excited about
this lately. We think you should just
give Claude a computer and let it do its
thing. So I'll talk about how we're
we're evolving the platform to give you
the infrastructure and otherwise that
you need to actually let Claude do that.
So starting with harnessing Claude's
capabilities. Um, so we're getting
Claude really good at a bunch of stuff
and here are the ways that we expose
that to you um in our API as ideally
customizable features. So here's a first
example um relatively basic. Claude got
good at thinking um and Claude's
performance on various tasks um scales
with the amount of time you give it to
reason through those problems. Um, and
so, uh, we expose this to you as an API
feature that you can decide, do you want
Claude to think longer for something
more complex or do you want Claude to
just give you a quick answer? Um, we
also expose this with a budget. Um, so
you can tell Claude how many tokens to
essentially spend on thinking. Um, and
so for cloud code, um, pretty good
example. Obviously, you're often
debugging pretty complex systems with
cloud code or sometimes you just want a
quick, um, answer to the thing you're
trying to do. And so, um, Claude Code
takes advantage of this feature in our
API to decide whether or not to have
Claude think longer.
Another basic example is tool use.
Claude has gotten really good at
reliably calling tools. Um, so we expose
this in our API with both our own
built-in tools like our web search tool,
um, as well as the ability to create
your own custom tools. You just define a
name, a description, and an input
schema. Um, and Claude is pretty good at
reliably knowing when to actually go um,
and call those tools and pass the right
arguments. So, this is relevant for
cloud code. Cloud code has many, many,
many tools and it's calling them all the
time to do things like read files,
search for files, write to files, um,
and do stuff like rerun tests and
otherwise.
So, the next way we're evolving the
platform to help you ma maximize
intelligence from claude um, is helping
you manage Claude's context window.
Getting the right context at the right
time in the window is one of the most
important things that you can do to
maximize performance.
But context management is really complex
to get right. Um especially for a coding
agent like Claude Code. You've got your
technical designs, you've got your
entire codebase. Um you've got
instructions, you've got tool calls. All
these things might be in the window at
any given time. And so how do you make
sure the right set of those things are
in the window? Um, so getting that
context right and keeping it optimized
over time is something that we've
thought a lot about.
So let's start with MCP model context
protocol. We introduced this a year ago
and it's been really cool to see the
community swarm around adopting um MCP
as a standardized way for agents to
interact with external systems. Um, and
so for cloud code, you might imagine
GitHub or Century. there are plenty of
places kind of outside of the agent's
context where there might be additional
information or tools or otherwise that
you want your agent to be able to
interact with or the cloud code agent to
be able to interact with. Um, and so
this will obviously get you much better
performance than an agent that only sees
the things that are in its window as a
result of your prompting.
Uh, so the next thing is memory. So, if
you can use tools like MCP to get
context into your window, we introduced
a memory tool to help you actually keep
context outside of the window that
Claude knows how to pull back into the
window only when it actually needs it.
Um, and so we introduced the first
iteration of our memory tool as
essentially a clientside file system.
So, you control your data, but Claude is
good at knowing, oh, this is like a good
thing that I should store away for
later. And then, uh, it knows when to
pull that context back in.
[clears throat] So for cloud code, you
could imagine um your patterns for your
codebase or maybe your preferences for
your git workflows. These are all things
that claude can store away in memory and
pull back in only when they're actually
relevant.
And so the third thing is context
editing. If memory helps you keep stuff
outside the window and pull it back in
when it makes sense, context editing
helps you clear stuff out that's not
relevant right now and shouldn't be in
the window. Um, so our first iteration
of our context editing is just clearing
out old tool results. Um, and we did
this because tool results can actually
just be really large and take up a lot
of space in the window. And we found
that tool results from past calls are
not necessarily super relevant to help
claude get good responses later on in a
session. And so you can think about for
cloud code, cloud code is calling
hundreds of tools. Um, those files that
it read otherwise, all these things are
taking up space within the window. Um so
they take advantage of um context
management to clear those things out of
the window.
And so um we found that if we combined
our memory tool with context editing, we
saw a 39% bump in performance over o
over the benchmark on our own internal
evals. Um which was really really huge.
And so it just kind of shows you the
importance of keeping things in the
window that are only relevant at any
given time. And we're expanding on this
by giving you larger context windows. So
for some of our models, you can have a
million token context window. Combining
that larger window with the tools to
actually edit what's in your window
maximizes your performance. Um, and over
time we're teaching Claude to get better
and better at actually understanding
what's in its context window. So maybe
it has a lot of room to run, maybe it's
almost out of space. Um, and Claude will
respond accordingly depending on how
much time uh or how much room it has
left in the window.
So, here's the third thing. Um, we think
you should give Claude a computer and
just let it do its thing. We're really
excited about this one. Um, because
there's a lot of discourse right now
around agent harnesses. Um, you know,
how much scaffolding should you have?
How opinionated should it be? Should it
be heavy? Should it be light? Um, and I
think at the end of the day, Claude has
access to writing code. And if Claude
has access to running that same code, it
can accomplish anything. you can get
really great professional outputs for
the things that you're doing just by
giving Claude runway to go and do that.
But the challenge for letting you do
that is actually the infrastructure as
well as stuff like expertise like how do
you give cloud access to things that um
when it's using a computer it will get
you better results.
So a fun story is we recently launched
cloud code on web and mobile. Um and
this was a fun project for our team
because we had a lot of problems to
solve. When you're running cloud code
locally, cloud code is essentially using
your machine as its computer. But if
you're starting a session on the web or
on mobile and then you're walking away,
what's happening? Like where is that
where is um cloud code running? Where is
it doing its work? Um and so we had some
hard problems to solve. We needed a
secure environment for cloud to be able
to write and run code that's not
necessarily like approved code by you.
Um we needed to solve or container
orchestration at scale. Um and we needed
session persistence um because uh we
launched this and many of you were
excited about it and started many many
sessions and walked away and we had to
make sure that um all of these things
were ready to go when you came back and
um wanted to see the results of what
Claude did.
So one key primitive in this is our code
execution tool. Um so we released our
code execution tool in the API um which
allows Claude to run write code and run
that code in a secure sandboxed
environment. Um, so our platform handles
containers, it handles security, and you
don't have to think about these things
because they're running on our servers.
Um, so you can imagine deciding that um,
you you want Claude to write some code
and you want Claude to go and be able to
run that code. And for cloud code,
there's plenty of examples here. Um,
like make an animation more sparkly that
uh, you want Claude to actually be able
to run that code. Um, so we really think
the future of agents is letting the
model work pretty autonomously within a
sandbox environment and we're giving you
the infrastructure to be able to do
that.
And this gets really powerful once you
think about giving the model actual
domain expertise in the things that
you're trying to do. So we recently
released agent skills which you can use
in combination with our code execution
tool. Skills are basically just folders
of scripts, instructions, and resources
that Claude has access to and can decide
to run within its sandbox environment.
Um, it decides to do that based on the
request that you gave it as well as the
description of a skill. Um, and Claude
is really good at knowing like this is
the right time to pull this skill into
context and go ahead and use it. And you
can combine skills with tools like MCP.
So MCP gives you access to tools and
access to context. Um, and then skills
give you the expertise to actually make
use of those tools and make use of that
context. Um, and so for cloud code, a
good example is web design. Maybe
whenever you launch a new product or a
new feature, um, you build landing
pages. And when you build those landing
pages, you want them to follow your
design system and you want them to
follow the patterns that you've set out.
Um, and so Claude will know, okay, I'm
being told to build a landing page. This
is a good time to pull in the web design
skill. um and use the right patterns and
and design system for that landing page.
Uh tomorrow Barry and Mahes from our
team are giving a talk on skills.
They'll go much deeper and I definitely
recommend checking that out.
So these are the ways that we're
evolving our platform um to help you
take advantage of everything that Claude
can do to get the absolute best
performance for the things that you're
building. First, harnessing Claude's
capabilities. So, as our research team
trains Claude, we give you the API
features to take advantage of those
things. Next, managing Claude's context,
it's really, really important to keep
your context window clean with the right
context at the right time. And third,
giving Claude a computer and just
letting it do its thing.
So, we're going to keep evolving our
platform. Um, as Claude gets better and
has more capabilities and gets better at
the capabilities it already has, we'll
continue to evolve the API around that
so that you can stay on the frontier and
take advantage of the best that Claude
has to offer. Um, second, as uh, memory
and context evolve, we're going to up
the ante on the tools that we give you
in order to let Claude decide what to
pull in, what to store away for later,
and what to clean out of the context
window. [clears throat] And third, we're
really going to keep leaning into agent
infrastructure. Some of the biggest
problems with the idea of just let
Claude have a computer and do its thing
are those problems that I talked about
around orchestration, secure
environments, and sandboxing. And so
we're going to keep working um to make
sure that those are um ready for you to
take advantage of.
Um and I'm hiring. We're hiring at
Anthropic. We're really growing our
team. Um, and so if you're someone who
loves um, building delightful developer
products um, and if you're excited about
what we're doing with Claude, we would
love to work with you across end product
design um, Devril, lots of functions. So
please reach out to us
and thank you [applause]
[music]
