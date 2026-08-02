---
title: Claude Code & the Future of Engineering
speaker: Boris Cherny, Acquired Unplugged
source: https://www.youtube.com/watch?v=RkQQ7WEor7w
retrieved: 2026-07-16
method: youtube_transcript_api
word_count: 6354
---

All right, so we need the origin 
story. Where did Claude code come from?  
By the way, it's is it's crazy being here 
and hearing you guys voices because I'm  
used to hearing it from here and probably at 2x. 
Probably at 2x [laughter] 2x and with all the um  
editing that we do on all of our little verbal 
ticks and you know all that. Um yeah, it was it  
was sort of an accident in in a lot of ways. Um so 
I I joined a team at Anthropic late in 2024 and it  
it was kind of a prototyping team. Um it was 
called the labs team. We actually brought it back  
and the idea was to figure out what's the next 
big product and at the same time we pushed the  
frontier of the model and we figure out how do 
we improve the model to support that best you  
know that future product that hasn't been built. 
And it's just hard to know which way to evolve the  
model because until there's a product that really 
pushes the frontier then you don't really know.  
And at the time there was this like just 
crazy feeling of product overhang that  
you know the model can do all the stuff that 
the there's no product that has yet captured.  
Um you know if you think about coding tools 
at the time there was like autocomplete tools.  
Um there was like you can ask the agent a 
question but it couldn't write code. Yeah. Yeah.  
Yeah. And like until recently, the model just 
wasn't good. It couldn't really do it. And so  
we felt like there there's room to just go all in, 
build a product that's just a coding agent. And um  
you know, we built it and it kind of sucked 
at the beginning. It it wrote maybe, you know,  
like 10 20% of my code for for a while. Real 
quick before before this moment, what was the  
state of coding at Anthropic? How much of a focus 
was it? So, you know, internally at Anthropic,  
we were using ideides still at at the time. Um, 
but for Anthropic as a company, we've always  
cared about coding. Um, we've always cared about 
tool use. We've always cared about computer use.  
This has always been kind of the core research 
direction because, uh, you know, for us,  
we exist to research AI safety. That's the reason 
that we exist. Like, if you ask like a random  
person at anthropic, you just like pull them over 
in the hallway and ask like, why are you here?  
They're going to say AI safety. That's the reason 
every single person is at the company that's  
they deeply believe including me this is just 
the single most important problem to solve  
and there's kind of a bunch of ways to solve 
it. You can look at kind of me mechanistic  
interpretability. You can do alignment work. 
There's all sorts of ways to study the model  
in a petri dish but fundamentally you have 
to study it in the wild to see what it does  
once it's safe in all these other ways. And 
so that's kind of where Claude Code comes in.  
But you know for anthropic as a company the 
direction has always been safety and the way  
you study safety you know it has all these kind 
of layers including setting the model in the wild  
and uh kind of what's a useful way to do that it's 
coding because that's the way the model interacts  
with the world and so if you want to study kind 
of various sorts of model misalignment you want to  
uh make it useful enough that people use it 
so that you can study it coding is just a very  
obvious application. Um so that's just from 
the beginning that's that's been the focus.  
It's just such an unbelievably clean universe 
because you've got all this training data.  
It either works or doesn't work and like depending 
on the language, it either compiles or doesn't  
compile or it either, you know, there's sort of a 
very clear like pass fail ability to test it. Um,  
and it's a very constrained universe of correct 
solutions. English is there's an infinite number  
of correct beautiful poems, but there's a very 
constrained uh there's a non- infinite number of  
ways that you can write the correct code to solve 
a certain problem. Yeah. And it's there's sort of  
a an elegance to using it as your petri dish 
given that. Yeah, that's right. There was uh  
you know you know Hofstadter, he's the guy that 
wrote Gödel, Escher, Bach . Did anyone Yeah. Yeah.  
Yeah. Yeah. Great book. Yeah, it was really good. 
But he he wrote this other really weird book in  
the in the 80s about uh like his idea about like 
the path to artificial intelligence because he's a  
like he's a professor. He taught AI in school and 
like he was kind of teaching at the time and he  
was he was talking about like the the the basis of 
cognition the basis of intelligence is recognizing  
patterns and one way that he studied that is one 
of his one of his hobbies was translating poetry  
from English to French. And a direct translation 
is rarely the right translation. there's actually  
a lot of taste that goes into it and sometimes 
you want to like fudge it a little bit so like  
the meter is good and there's kind of various 
ways to do it. Yeah, it's like a fuzzy problem  
but coding is easier to solve I think. It's also 
very commercially valuable. Um so it helps us  
kind of build a business and it's also the kind of 
business that our favorite customers, enterprises,  
startups, companies have and so it helps us 
have this kind of aligned business model. So,  
you know, we don't need to do ads and, 
you know, we can kind of focus on safety,  
which is the thing that we care about. It helps 
us build a business where we can actually do that.  
Um, you came from Meta before 
coming to Anthropic. Uh,  
and you had a lot of focus on on code at Meta. 
I'm curious connecting the dots looking back now.  
Um, how did what you were doing at Meta 
help inform the beginnings of Claude Code?
For me, building DevTools has always been 
a side hustle. It was never the main thing.  
And I feel like that's the that's 
the best way to build DevTools  
because you want to focus on solving a 
business problem and building a thing that  
people love and that's useful for people. That's 
fundamentally what we're here for as engineers.  
You know, at least YC like beats this into you. 
Like I feel this way. Had you done YC before?  
Yeah. Yeah. I was actually I I was the first 
hire at a YC company. back in like 2010 2011  
something like that. It was like one of the first 
few batches. Wow. Cool. Um so for me DevTools has  
always been this kind of side hustle and I I build 
product and on the way to building product if  
uh you know the DevX isn't good then I'll 
build tools to make that a little bit better.  
That's just always been the way that I approach 
it. Um and so here I just applied kind of that  
mindset of build the thing for yourself first 
and then hopefully it's useful for others.  
And uh I was surprised to see that it is which 
is awesome. So you said it was kind of crappy  
at first and you only trusted it with like 10% 
of your work or only did about 10% of your work.  
What was the bottleneck early on and how did you 
solve it to to make it better? Because from what  
I understand it's been like six months since 
you've written a line of code in your job. Yes.  
So that's extremely different than it it 
only does about 10%. What changed? Um I  
remember it. It was it in May it was sonnet 4 and 
opus 4 uh and then in November it was opus 4.5.  
So it was just the mo the underlying model 
changing. It was the model. There's a lot of  
work that went into the harness. There's a lot of 
work into making Claude Code better. You know like  
everyone likes to use this stuff differently. 
This is the thing about building for engineers.  
It's not a consumer product because engineers are 
so opinionated in the way they like to use stuff.  
And so you know we started with a CLI but then we 
built we built a desktop app. We built a mobile  
app. We build uh iOS and Android apps. We have 
like Slack app, GitHub app. You can use Claude  
Code in whatever way you want. And so a lot of 
this has was us innovating, learning, trying to  
figure out what features are useful. And this is 
like plan mode for example came out of this. A lot  
of different kind of tools and experiences came 
out of this. But fundamentally when I think about  
the step changes and what percent of my code the 
model wrote, it was just the model like the model  
got better and it just went up. How tightly to the 
extent you are able to talk about it how tightly  
was the experience that claude code was having 
feeding back into the the model work leading up  
to 4.0 4.5 etc. So every you know everyone at 
anthropic uses quad code every day. Um so the  
researchers building the model use quad code and 
the people building the product use quad code. So  
that that's essentially the cycle. Do you have any 
metrics that like u ways to numerically describe  
how much it's changed the company's trajectory? 
Like it feels from the outside that you guys are  
shipping a whole lot more product now than 
you used to. It seems reasonable to assume  
a lot of that is because you guys are using 
Claude Code all over the company internally.  
What's the right way to really grasp how 
much of that is attributable to Claude Code?  
Yeah. So being at a AI lab, you get you get kind 
of used to thinking in exponentials. Essentially  
all the charts are exponential. So we actually use 
like log linear charts for pretty much everything.  
So it's like x-axis is you know like linear 
and then the y is like log-linear. Um and so  
you know everything's kind of exponential like the 
revenue is exponential, the usage is exponential.  
Um which is just like the funnest problem as an 
engineer and thank you for bearing with it. Um  
and uh essentially like everything is going up 
including the like the code. Um and so when we  
look at the lines of code written the number of 
pull requests written by people at Anthropic since  
we released quad code this has grown many hundreds 
of percentage points. Um I think the latest stat  
we shared was like something like 3x. Um but this 
is actually very very outdated. So it's it's a lot  
higher now. What what was 3x? Uh the amount of 
code per engineer that everyone at the propic is  
writing. I see. So the size of the engineering 
team went up, you know, like many multiples.  
And usually what happens as the size of the 
engineering team grows is productivity goes down.  
And when I was at Meta, one of my responsibilities 
was code quality for all the code bases.  
And the reason we cared about that was it's useful 
for productivity. If the code is high quality,  
it makes engineers more productive. And 
we kind of showed this empirically. Um,  
and typically what happens is the code quality 
gets worse, productivity goes down. Another thing  
that happens is as the number of engineers grows 
the productivity goes down because the new people  
who are kind of asking engineers like how do I 
do this how do I do this so the engineers they're  
asking don't get to write code and it takes just 
you know like it takes ramp up time and the the  
first thing that we saw at anthropic is when new 
people join the ramp up time is like two days  
because you know like this used to be weeks but 
now it's two days because you just like ask quad  
and we still have to explain to new people that 
join the team like people ask like how do I query  
the database and And the answer is open quad, 
run it in the Claude codebase and have quad  
query the database because there's like a skill 
for quering the database and it just knows.  
So of of the new engineers that you've hired in 
2026, how many of them have written any code?  
Um I mean define writing code. Um right, 
right. That's [laughter] Wait, wait,  
how do you define writing code? You know, for for 
me it's like engineering has always been like like  
you know my grandpa coded with punch cards like 
in the Soviet you like you like for him like  
programming was like it was like a paper thing 
like punch holes into it and you feed into this  
like big machine and it chucks for a while and 
it gives you the answer that was that was coding  
right it's like my dad who wrote a lot of assembly 
would have like made fun of me for writing Python  
and be like you're not coding. Exactly. Exactly. 
It's like it's not for you know real engineers  
or it's very high level but this is sort of 
the nature of programming is the the level of  
abstraction always goes up. So it's it's g it went 
from like switches to punch cards to like assembly  
then to like cobalt forrand and java and the the 
high level languages and then like javascript and  
python and the really high level languages. 
This has just always happened and like I see  
what we're doing as somewhere on this continuum. 
Um and so for me the way that I coded a year ago  
was I wrote code with some kind of autocomplete 
in IDE. In November I uninstalled my ID because  
I wasn't using it. [laughter] I I just like 
I I was just you know for I I was like in the  
last month I just haven't opened it so I'll just 
uninstall it. Wow. At that point I was running  
you know maybe five 10 quads in parallel and my 
coding was prompting quad to to write code. Now  
it's actually leveled up I think again to the next 
abstraction where I don't prompt quad anymore.  
I have loops that are running. They're the ones 
that are prompting Claude and kind of figuring  
out what to do. My job is to write loops. And this 
is this kind of next transition that I think we're  
going to see in the next few months. you know, 
maybe through the rest of the year. Wow. Um,  
hypothetical me, obviously, not actual 
me, uh, is an engineer who wants to join  
the engineering team at Anthropic. Um, 
how do you evaluate me today? [laughter]
I think something that I look for in our team in 
particular for Claude code is we love generalists.  
So I I think a thing that we started to 
see maybe six months ago is there were  
very few engineers on the team that were just 
doing engineering in the traditional sense  
of like you know you have a user researcher they 
talked to the user and then they handed that down  
in a document to a designer who then made a mock 
and then that went to a product manager you know  
scoped it and then it goes to an engineer 
for implementation. I I worked at Microsoft  
I'm extremely familiar with this process. 
[laughter] This is what it used to be. But it,  
you know, we we just realized this is 
not what the team is doing anymore.  
And our team was always kind of more prototypy 
than this. But maybe six months ago, the thing  
we found is every engineer on the team does 
scoping. Everyone talks to users every day.  
People are doing design engineers. Everyone on 
the team is comfortable like pulling data and  
doing data science work, building dashboards 
and things like that. So I think like we're  
we're kind of starting to see all the roles merge 
and kind of melt into one builder. I think like  
Satia calls it a builder. So, it's something 
like that. It's almost like a product engineer,  
but you don't even really necessarily have to be 
an engineer. That's right. And you know, like we  
have designers that are shipping code. Our finance 
guy ships code. Um I think this our chief of staff  
ships code. Yeah. I mean, we actually all of our 
infrastructure at at Acquired now is is pretty  
rapidly shifted to Claude Code. Um which is why 
can I tell a little fun acquired story? So we um  
we are an audio podcast. YouTube doesn't have 
a way to upload just audio. You have to upload  
something in the video. It should be interesting. 
Um for a long time it was just a a black screen  
MP4. [laughter] Uh so a transcript would be 
a good idea, but we don't have a transcript  
yet because it takes it a week for humans to make 
the transcript. Fortunately, there's AI. Anyway,  
um there's a whole like claude code set 
of scripts that I sloppily wrote. Well,  
I and Claude wrote and then at some point I 
sort of heaved it over to David and I was like,  
can you like continue working on this? And there 
at first little resistance, but then you you did  
spin up an I like Yeah. Yeah. Yeah. Um open the 
terminal. Uh one day after CS classes in college  
and that was the last time I opened a terminal. 
One day after that, uh, co-work comes out and the,  
you know, the the pitch for cowork is it 
it's if you want the power of Claude Code,  
but you don't want to have to deal with the 
terminal and, you know, typing commands and  
um, installing npm and blah blah blah. We actually 
heard that David had to open a terminal. So,  
we were like, we have to release this. We have one 
day. So, uh, I want to use that as my like hook to  
like, uh, tell us the story of Claude Co-work 
because to me it seems Claude Co-work is a much  
much bigger market of people who don't want to 
open terminals than people who do know how to open  
terminals. It's kind of interesting that it went 
the direction of Claude code first and then to be  
honest like kind of a really long time before 
Claude Co-work came out. Yeah, that's right.  
Honestly, it was this story. It it was like 
it was some version of this played out like  
in April I remember walking into the 
office and right next to where the  
quad code you know the a few of us sit 
there's the a couple data scientists  
and I walked in and one [clears throat] of the 
data scientists had quad code up on his screen  
and this was like this was back in the day when 
quad code was only available in a terminal.  
It wasn't yet available in the desktop app. 
It wasn't available in the mobile app. So,  
like you really had to know what you're doing. And 
I asked Brandon like, "Dude, what are you doing?  
Are you like dog fooding it? Just trying to 
kind of figure out what this thing is?" Because,  
you know, like he just joined the team. And he 
was like, "No, I'm using it for data analysis."  
And so he figured out how to open a terminal. He 
figured out how to um, you know, download Node.js  
because you had to do that. Uh, he figured out 
how to install quad code, how to set up a API  
key. I don't think we even had subscriptions then. 
And he was just like using it to do analysis. Then  
the the next week all of the data scientists had 
multiple quad code windows doing their analysis  
because it was just good at it. Um and then fast 
forward to maybe or June or something and there  
there was some guy on Twitter. Do you guys see 
this? He was using it to grow his tomato plants.  
He has like he had like a little webcam like he 
set it up to like just monitor his tomato plants  
and it was controlling like the nutrition 
for the plants and like over over weeks  
and then at some point like 
the little tomato like butted  
and Claude was like this is so delightful like all 
our work is paying off and like I just saw this  
tweet and I was like oh my god I think it's time 
like now we're we're starting to break through to  
the mainstream. It took a while to get engineers 
to understand what this is and finally they did  
and now we're starting to see a critical mass 
of non-engineers do it. And when the wait and  
demand is that strong I think that just means 
it's like it's the time to build a product.  
And so we started exploring there's a bunch of 
different ideas. Co-work itself we built in it  
was like a little over a week like maybe eight 
nine days something like that. It was 100% built  
using quad code. It was one of a bunch of ideas 
and as soon as we had it we were like this is it.  
What were the other paths that you killed? 
Because it um if I were to describe the sort of  
creative brief as take all the power of Claude 
Code and make it available to people who don't  
want to open a terminal, it doesn't really 
translate one to one. You kind of have to be  
opinionated in the product that you build to bite 
off some set of the work that Claude Code can do.  
Yeah, we tried man I don't even remember all the 
prototypes. So, we tried something I think that  
was based in Slack and it didn't really work 
cuz building Slack chatbots that feel good is  
just really hard. Um, we tried something that was 
based on web. There was a bunch of different web-  
based prototypes um that we weren't sure 
about and none of them really felt great.  
Like there there's something about being in 
a browser that just didn't feel really good.  
Um, and it also if it's in a browser, it 
doesn't have access to all your tools. So,  
I have a Word document on my desktop. I can't tell 
something in the browser. File system access feels  
necessary. And just that little bit of friction 
of like having to drag and drop the file to the  
to the browser that was enough to make it feel not 
good. And I I think this is just back to the way  
that we think about product is we build the thing 
that we love and you want to build a product that  
you yourself fall in love with and that you use 
every day and then maybe some users will like  
it too and hopefully it's useful for other people 
too. I have um it has been surprising to me how my  
claud code usage has dropped because of how much 
Python gets written in claude the chat window.  
I'll ask it questions that require a lot of 
data analysis and I can see like oh it's it's  
writing some software right now to do the analysis 
and then it's going to write a bunch of html and  
CSS and JavaScript and then render a brand new UI 
for me to play with it in. And that used a lot of  
claude code generation although I never once 
interacted with claude code the product to to have  
that be accomplished. Yeah. Yeah. There there's 
this kind of interesting kind of theoretical thing  
about like when do you want to do the computation? 
Do you want to do it in real time when you sample  
from the model and kind of do inference or do 
you want to kind of premputee so you can have  
the model write a program and then you can run 
that program repeatedly and that's free for you.  
And essentially we want to do the latter as much 
as possible. Um, but really it's up to the model,  
you know, like this is just back to like the 
model exists as software and it needs a way  
to interact with the world because it exists 
as software. The way it does this is coding.  
That's just kind of the natural language it 
speaks. It's the thing it understands. And so,  
you know, like from the earliest days of quad 
code, I the very first version I gave it a  
bash tool so it can run commands on my computer. I 
didn't tell it anything about the tool and it just  
kind of figured out how to use it. And you know, 
there's this anecdote I've told a thousand times,  
but I asked it like, "What music am I listening 
to?" And it opened up the batch tool. It wrote a  
little program that wrote a Apple script script. 
And like, I've never written Apple script.  
And it wrote a little Apple script and it opened 
my music player and was like, "This is the song  
that you're listening to." And even back then, 
this was like sonnet 35. That was like not a very  
intelligent model. It was like the best at the 
time, but you know, by now by modern standards,  
it's not very intelligent. Um, it it just knew 
how to do this. So there there's something about  
writing code. There's something about, you know, 
using tools to interact with the world. It's  
it's just something the model wants to do. 
I want to ask I'm going to come off of this  
product specific questions for a minute to ask 
a little bit about culture and org design. Um,  
you're a member of the technical staff. I think 
a lot of people have that title. [laughter] Um,  
what's up with that? What are the pros? What are 
the cons? Would you recommend that to this group?  
Okay. So, so the worst thing that was pretty 
annoying when I joined is uh you message someone  
on Slack and you know it just says member 
of technical staff. So, you're like is this  
person like a designer? Are they an engineer? Are 
they like manager? You don't know. And like what  
do they work on? What do they work on? Yeah. 
You don't know. Um I actually really like it.  
Um when when I was at Meta, something I really 
liked is every software engineer their title is  
software engineer. There's no like senior software 
engineer, principal software engineer. Oh,  
really? Yeah. It's like not a thing. Huh. Um, and 
I I I like it because actually if you give people  
kind of senior titles, sometimes they'll give 
you bad ideas and people out of deference will  
just go with those ideas. But actually they should 
push back and it's actually a really good cultural  
forcing function to put everyone on the same 
playing field in that way. Does it come out though  
like okay yeah I know you're just a software 
engineer and I'm just a software engineer but like  
I'm well aware you're a level something software 
engineer even though it's not in your title.  
I think sometimes you know this but oftentimes 
you don't. Yeah. [clears throat] like um you  
know I was like uh when I was at Facebook 
I when I joined I was like a L4 engineer  
and I had an idea and then I like I found like 
the VP of connectivity and like went to him  
and was like here's my idea let's go build 
it and like he didn't know what level I am  
oh that's interesting and like he 
it was a bad idea and it didn't work  
but then I did this again with a different VP and 
then that also didn't work but but the third time  
it worked and then you know we started a team and 
we started building stuff and then moved on to  
the next idea I and I kind of see this all the 
time now you know people on our team old these  
kind of old seniority ideas it's sort of like it 
doesn't matter anymore in in a lot of ways like  
these engineers that have 20 years of experience 
30 years like they have to unlearn so much and  
you spend months teaching them how to unlearn all 
these old habits that just aren't relevant anymore  
whereas sometimes a new grad joins the team 
and they will teach me something about how  
to use Claude Code better because they think 
about it natively whereas it's not my instinct  
and it it's extra hard because with every new 
model you just have to recalibrate and relearn.  
But going back to the member of technical staff 
thing, I I think it's actually a really important  
thing because all these old distinctions 
about engineer versus PM versus designer  
versus user researcher by the end of the year it's 
gone. And so this helps us kind of very clearly  
see this and kind of act in this way today. And 
this is I think I think you have to do within a  
AI lab is kind of push everyone to be more AGI 
build and think about the future more in this way.  
I'm curious on that front maybe 
generalize a bit you know for  
all the founders all the companies in this 
room um what should they be thinking about  
now for their organizations by the end of 
the year? Um, what do you think that founders  
and companies are going to have to change in 
their mindset over the coming set of months?  
I would I would think today the thing that I 
would do is I would give everyone as many and  
I'm going to say this because 
I work at a AI lab of course,  
but give everyone as many tokens as possible. 
[laughter] The more to to quote Jensen,  
the more you buy, the more the more 
you buy, the more you save. [laughter]
So this is this is sort of the place that I 
would start is like give people as many tokens as  
possible. Let them experiment. And the other thing 
I would do is underfund everything a little bit.  
So if you're working on a project and you're like 
this feels like it needs like four engineers,  
put two engineers on it and give them a bunch 
of tokens and have them figure out how to do it.  
And chances are they can do it. There's probably 
a bunch of stuff they can automate. There's  
a bunch of stuff they can streamline. And 
because they're automating it, they can do it  
better next time. It'll just be cheaper next 
time. And of course a compounding effect to  
it's compounding a compounding effect to having 
fewer resources besides tokens. That's right. It's  
sort of like you know like in business and product 
you you make so many decisions it's really good  
to have a set of principles so you don't have to 
you can lean on the principles and you don't have  
to make ad hoc decisions every time. And oftent 
times founders and you know companies they have  
these like principles documents and so this is 
kind of like that but you know the model can use  
these principles also and you know comes in the 
form of skills and and of course like if there's  
some use case that takes off and uses a bunch 
of tokens that's when you go in and optimize it  
and try to make it efficient but in general if I 
were to parrot back the advice to you of um staff  
with fewer humans shift budget from humans 
to tokens what the output of that is is to  
raise your upfront costs but decrease your ongoing 
costs because you you've already like it's almost  
like pre-ompiling like you've done a big pile 
of work up front so that the over and over and  
over again tasks are easy and streamlined. Yeah. 
Yeah. That's maybe a way to think about it and and  
because you put less people on it that means you 
know the people at your company can do much more.  
This feels like the biggest reckoning to me 
of building teams is people are pretty used  
to having a title and a discipline and people 
take great pride in being a good a good PM.  
I'm going to write a bunch of blog posts and 
stuff about the the discipline of product.  
You there's a lot of those people out there or 
designers. I can't wait to show off my portfolio  
of my beautiful designs. And like, do we all just 
need to within 12 months shake off the idea that  
we are an anything and everybody is just this 
like flexible bag of token generation? Wow, Ben,  
you're so optimistic. [laughter] Uh, I I might use 
slightly different words, but something like that.  
You should make a t-shirt out of that. [laughter] 
I think I think it's something like that. So,  
you know, for for me, I I've been an engineer for 
for a bit, but I I've always worn different hats.  
Like, I I've started startup startups before and 
I've been on the business side. I've worked on the  
product side. I've been on the user research side, 
on the design side. So, for me personally, I just  
love building product. I don't I don't care that 
it has to be an engineering hat that I'm wearing.  
And sort of like right now, I see that being 
borne out. So, yeah, I feel like right now,  
this is just the golden age of of the generalist. 
People that want to do more than one thing,  
it's just it's never been more fun. It's never 
been easier. Maybe one more question. Um,  
we spoke about with Garrett a little 
bit. I'm curious your take on it. Um,  
how do you think about taste? Uh, 
either you personally or anthropic.  
I I feel like every time I think there's, you 
know, something kind of special about the way that  
I do coding, I'm wrong. I I used to have all these 
opinions about the way that we write the code.  
like um you know I I I really like functional 
programming and so you know I'm a big like I like  
like Haskell and Scull and these kind of weird 
functional languages and at the very beginning  
I had this rule for our codebase. We have no 
classes in the codebase. We only have functions  
in the codebase because that's the way that I 
write my code. That's the way that I like it.  
And um on the weekends engineers just 
started sneaking in changes that had classes.  
And uh I would find that on Monday and then 
I would like pull out the pull requests and  
I would be like no no no don't do that. And then 
at some point the model started writing all the  
code and it just started writing classes and 
I was like okay well maybe the model's right  
like maybe this opinion is kind of stupid and 
it's just like this particular thing that I have  
but in it doesn't matter because the business 
outcome is met and it's met faster as a result  
and the code actually is not bad. Um and obviously 
the code's been getting better over time.  
And so I I feel like every time that I have 
this kind of like sense that like I'm special  
in in some way I'm often proven wrong. And 
and I think right now kind of with the current  
model capability, something that people talk a 
lot about is like the alpha is product taste.  
And I think this is also going to go away. Like 
this is the alpha today. But also, you know,  
right now I have, you know, like a couple hundred 
quads running doing stuff and a bunch of them  
are looking at like Twitter feedback and they're 
looking at like GitHub issues and they're looking  
at Slack and they're figuring out what to build 
next. And right now most of the ideas are bad,  
but maybe 20% are good. if you wait for the next 
model and you know if you project out maybe three  
months six months most ideas will probably 
be good um and you know there's gonna be  
some new there's gonna be some new thing there's 
gonna be something else that we're really grate  
erodess any guesses at what it is is there some 
final thing where humans are uniquely good at it
I I think the final thing that we're going to 
be teaching the model is values and how to be,  
you know, the the way that 
we teach our kids how to be  
good people. We're going to teach 
the model how to be a good model.
Fascinating. Well, that is 
quite the place to leave it.  
Yeah, Boris, thank you so much. This 
is fascinating. Thank you. [applause]
