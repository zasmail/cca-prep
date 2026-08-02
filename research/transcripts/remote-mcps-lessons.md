---
title: Remote MCPs - What We Learned from Shipping
speaker: John Welsh
source: https://www.youtube.com/watch?v=0NHCyq8bBcM
retrieved: 2026-07-16
method: youtube_transcript_api
word_count: 2677
---

Awesome.
[Music]
Thanks so much for coming. Um, I wanted
to give a bit of a talk on implementing
MCP clients and talk to more about MCP
at scale within a large organization
like Anthropic. Um, I wanted to give
first a little introduction from me. Uh,
my name is John. I've spent 20 years
building large scale systems and dealing
with the problems that that causes. And
so I've made a lot of mistakes and uh
I'm excited to give maybe some thoughts
on avoiding some of those mistakes. I'm
currently a member of technical staff
here at Anthropic and I've spent the
past few months um focusing on tool
calling and integration and implementing
MCP support for all of our internal like
external integrations within the or
so
looking at tool integration with models
we've kind of hit this timeline where uh
models only really got good at calling
tools
uh like kind of late midl last year and
suddenly
Everyone got very excited because like
your model could go and call your Google
Drive and then it could call your maps
and then it could send a text message to
people. And so there's a huge explosion
with like very little effort you can
make very cool things and so um teams
are all trying to move fast. Everyone's
moving very fast in AI. Custom endpoints
start proliferating for every use case
there's a lot of like services popping
up with like slashcall tool and slash
like get context and then people um
start to realize there's additional
needs some authentication a b a bunch of
stuff there and this kind of led to some
integration chaos where you're
duplicating a bunch of functionality
around your org nothing really works the
same you have an integration that works
really well in service A but then you
want to use it in service B but you
can't because it's going to take you
three weeks to rewrite it to talk to the
new interface And so we're in this kind
of spot and the place that we came to at
Anthropic is realizing that over time
all of these endpoints started to look a
lot like MCP. Uh you you end up with
some get tools, some get resources, some
elicitation of of details. Um,
and even if you're not using the entire
feature space of MCP uh as a whole
immediately, like you're probably going
to go extend into something that kind of
looks like it over time. And when I'm
talking about MCP here, there's kind of
two sides to MCP that in my mind feel a
bit unrelated. There's this JSON RPC
specification which is really valuable
as engineers. It's like a standard way
of sending messages and communicating
back and forth between uh providers of
context for your models and the code
that's interacting with the models. And
uh getting those messages right is the
topic of huge debate on like the MCP
uh repos. If you're involved with any
standardization process ever, you know
how those conversations end up going.
And then on the other side there's this
global transport standard which is the
stuff around streamable HTTP oath 2.1
session management. And global transport
standard is hard because you're trying
to get everyone to speak the same
language. And so it's really nitty but
there's not a lot of like most of the
juice of MCP is in this the message
specification and the way that the uh
servers are interacting. Um and so we
started asking ourselves like can we
just MCP for everything and we said yes
with the caveat that yes is for
everything involved in presiding model
context to models. Um we have this
format where your client is sending
these messages. Something's responding
with these messages. Um where that
stream is going it really doesn't
matter. It can be on the same process.
It can be another data center. can be
through a giant pile of uh enterprise
networking stuff. Um, it doesn't really
care at the point that your code is
interacting with it. You're just calling
a connect to MCP and you have a a set of
uh a set of tools and methods that you
can call. So, uh,
standardizing on that seemed useful. Um,
standard why standardize on anything
internally? Um, being boring on stuff
like this is good. It's not a
competitive advantage to be really good
at making Google Drive talk to your app.
It's just a thing that you need to do.
It's not your differentiator. Uh having
a single approach to learn as engineers
makes things faster. You can spend your
cycles working on interesting problems
instead of trying to figure out how to
plum uh integration. And uh if you're
using the same thing everywhere, then
like each new integration might clean up
the field a bit for the next person who
comes along. Um it's it's over overall a
good thing in cases like this where
we're we're not really doing anything
interesting. We're plumbing context
between integrations and things that are
consuming the integrations. Uh
what is standardized on MCP internally?
Um I this is where I might make an
argument to everyone that there's
already ecosystem demand. You have to
implement MCP because everyone's
implementing MCP. So why do two things?
Um it's becoming an industry standard.
there's a large coalition of engineers
and organizations that are all involved
in building out the standard. Uh all of
the major AI labs are represented in
that. So you you know that as new model
capabilities start to be developed uh
those patterns will be added to the
protocol because all the labs want you
to use their features. So I think the
standardizing on MCP internally for this
type of context is a is a good bet. And
one of the things you get with MCP is
that it solves problems that you haven't
actually run into yet. like there's a
bunch of stuff in the protocol that
exists because there's a problem and a
need and
having those solutions at hand when you
run into them is really important. So
sampling an example of where this might
be valuable in your company. You might
have four products that have four
different billing models uh for reasons
because you're building fast. Um you
might have a bunch of different token
limits. You might have different ways of
tracking usage. This is really painful
because you want to write one
integration service to connect your
slides and how do you go and like hook
the billing and the tokens up correctly
and MCP has uh already has sampling
primitives so you can build your
integration you can just be like okay
your integration sends a sampling
request over the stream uh the other end
of the pipe fulfills that request you
can go and hook it in everything works
great and so this is a thing that uh a
shape problem that might take you a
bunch of effort
uh internally without this, but you
already have the answer kind of gift
wrapped for you in the protocol.
And so at Anthropic, we're running into
some requirements converging. We're
starting to see external remote MCP
services popping up like mcp.
We wanted to be able to talk to those.
Talking to those is complex because you
need external network connectivity, you
need authentication. Uh
there's a proliferation of internal
agents. people have started building uh
PR review bots and like Slack management
things and just lots of people have lots
of ideas. No one's really sure what's
going to hit. So, we're having a huge
explosion of LLMbacked services
internally. Uh with that explosion,
there's a bunch of security concerns
where uh you don't really want all of
those services to be going and accessing
user credentials uh because that ends up
being being kind of a nightmare. don't
want uh outbound external network
connectivity everywhere. Um auditing
becomes really complex. Uh and so we are
looking at this problem. We wanted to be
able to build our integrations once and
use them anywhere. And so, uh, a model I
was introduced to by a mentor of mine
and a while ago is the pit of success,
which is the idea that, um, if you make
the
right thing to do, the easiest thing to
do, then everyone in your org kind of
falls into it. And so uh we designed a
service which is just a piece of shared
infrastructure called the MCP gateway
that provides a single point of entry
and provided engineers just with a
connect to MCP call that returns a MCP
SDK client session on the end and we're
trying to make that as simple as
possible uh
because
that way people will use it if it's the
easiest thing to do. Um, we used URL
based routing to route to external
servers, internal servers, it doesn't
matter. It's all the same call. Uh, we
handle all the credential management
automatically because you don't want to
be implementing OOTH five times in your
company. Uh, gives you a centralized
place for rate limiting and
observability.
Uh, I have an obligatory diagram here of
a bunch of lines going in and out. But,
uh, here's a a gateway in the middle.
This is kind of the thing. Just one more
box will solve all our problems. Uh, can
I go next?
Uh where is my
yeah ah uh so the uh the code that we
have here we just made some client
libraries where we just MCB gateway
connect to MCP uh we pass in a URL an
org ID account ID this is like a bit
simplified we actually pass a signed
token to authenticate because it's
accessing credentials but this is the
basic idea and then importantly this
call returns an MCP SDK object which
means that when new features get added
to protocol. You just update your MCP
packages internally. You get those
features across the board. Everything
works great. The same code seamlessly
connects to internal external
integrations.
When it comes to transports, uh, and
this is a bit high level and handwavy
because everyone's setup is different.
Um, internally within your network, it
really doesn't matter. You can do
anything you want. We've got the
standardized transport for connecting to
external MCP servers. Um, but really
just picking the best thing for your
org. So we went and picked
uh websockets for our internal
transport. And here's just a quick code
example. It's nothing special. We just
have a websocket uh that's being opened.
We are sending these JSON RPC blobs back
and forth over the websocket. And then
if I can make this scroll down
at the end, we just pipe those uh read
streams and write streams into an MCPS
SDK client session and we're good to go.
We've got MCP going. Um you might want
to do this with gRPC because you want to
wrap these in some multipplexed
transport so you don't have to open one
soocket per connection. That's pretty
simple. Also, uh we have read stream
right stream at the end. Uh starting to
see a pattern here. You can do like Unix
socket transport if you want. You can
just have uh messages be passed that
way. Read, stream, write, stream at the
end. MCU works great. Um I threw in an
enterprisegrade email transport
implementation over IMAP. Um which is
pretty much the same thing. You just go
through here is our server. We're
sending emails back and forth. Uh dear
server, I hope this finds you well. Uh
MCP request start. And then we pipe
those into a client session at the end.
And so it truly doesn't matter like
whatever it takes inside your
organization is great. We set up this
unified authentication model where we're
handling
ooth at the gateway uh which means that
consumers don't have to worry about all
that uh all that complexity in their
apps. Uh we added a get ooth
authorization URL function and a
complete ooth flow because you might
have different endpoints at anthropic.
We have api.anthropic.com and we have
cloud.ai AI and we might want those
redirects to go back to different
places, but uh this is tied on the
gateway. It's really easy to start a new
authentication. Uh a real advantage of
having this put on your gateway is that
the credentials are portable. If you
have a batch job that you're kicking
off, um your users don't have to
reauthenticate to that. You're just
calling the same MCP with your internal
user ID and they get everything added
correctly. You're also internal services
don't have to worry about your tokens.
Um so your request comes in internally
for us. We're hitting a websocket
connection to MCP gateway uh with O
token provided as headers to that. Uh
the gateway receives your stored
credentials. You create an authenticated
SDK client. You just pass in the bearer
token to the O header. Uh and then
you're good to go. The MCP client
receives a readstream and a right
stream. And so you just plum those read
stream and write stream into your
internal transport and you're and you're
you're good to go. Uh one of the things
that this gives for your org that's not
immediately obvious but is really
valuable is a central place for all of
your context that your models are asking
for and all the context that's flowing
into your models for your org. Uh
there's some papers written on MCP
prompt injection attacks. There is a
general risk of uh models going and
having access to Google Drive and
deleting everything in Google Drive.
There's some need of uh enforcing
policy. You might want to be able to
like ban
malicious servers. Um do some content
classification on the request, see
what's coming in, kind of given audit.
And the really nice thing about this is
that because it's MCP, all of your
messages are in a standardized format.
So it's really easy to hook into that
stream and be like, "Okay, here is my
tool execution message processor or here
is my tool definition thing or here's my
resource management." And so the payoff
that you get from this is um adding MCP
support to new services is as simple as
possible. You just go and import a
package. Uh it doesn't matter what
language you're in. We've got multiple
languages internally. They all have
their own kind of packages. Engineers
can focus on building features and not
plumbing. uh you have the operational
simplicity of having a single point of
ingress egress and standardized message
formats and you get future features for
free as the protocol involves you get
all of that work uh naturally
and so just wanted to go through some
takeaways from this that I I want to put
to you is that MCP is really just JSON
streams and how you pipe those streams
around your infrastructure is a small
implementation detail. That's a couple
lines of code hook the stream into the
client SDK that makes the messages. Uh
the
you should standardize on something,
anything. I think MCP is a good idea. If
you don't think it's a good idea, like
just pick something. Um your future self
will thank you. Uh build some pits of
success. You really want to make the
right way to do a thing the easiest way
to do a thing and then everyone just
falls into doing the right thing
naturally. And also centralizing at the
correct layer. So solving some shared
problems off and external connectivity
once allows you to spend your time
working on uh more interesting problems
that are more valuable to you and your
your business.
Thanks. That's all I got for you. Uh
thank you so much for coming out.
[Music]
