# Alan Nichol, Episode 3 field notes

Alan Nichol is co-founder and CTO of [Rasa](https://rasa.com/), a developer platform for building AI agents. He holds a PhD in machine learning from the University of Cambridge and has been building chatbots since 2016, with over a decade of experience delivering AI products to enterprise. The segment centered on programmatic video generation with Claude and [Remotion](https://www.remotion.dev/), the tradeoffs between code-based and no-code interfaces (vibe coding vs agentic engineering), and the challenge of encoding domain judgment into skills when working outside your area of expertise.

## On working with agents

### What he loves: fitting productivity into fragmented time

Alan values agents for making productive work possible in small windows between meetings and context switches. Without agents, a project requiring half a day becomes feasible in 20 minutes over a coffee break. *"You know, the kind of project that would take me half a day, I can just fire off and just get done. And so it just makes your whole day so much more productive."* [[02:41:20]](https://youtube.com/live/ud2WzkKeDZs?t=9680)

### What he finds most frustrating: prompt and pray, no systematic debugging

Alan's primary frustration is the lack of a systematic way to improve outputs. When something does not work, the only option is trial and error with no principled path forward, reminding him of deep learning research in 2014-2015 where you throw architectures at the wall and see what sticks. *"I think the thing that frustrates me most about it is prompt and pray. For real. I mean, it's so frustrating when you don't have a systematic way to say, here's the thing I didn't like about the output. How can I achieve the output that I do want? Right? It's only trial and error. It's the only thing you have available to you."* [[02:41:37]](https://youtube.com/live/ud2WzkKeDZs?t=9697)

## Skills

### Remotion video generation skill

Alan has built a skill that encodes design rules for programmatic video generation with Remotion, a JavaScript library for code-based video creation. The skill exists because Claude requires no help whatsoever writing Remotion code; instead, the skill teaches Claude what Alan wants in terms of animations, easing functions, layout modes, styling, and text treatment. *"Claude needs no help whatsoever writing remotion code. So it will just do it. And everything that's in the skill is me telling it like what I want in there and how to do animations and style guides and rules and text."* [[02:51:23]](https://youtube.com/live/ud2WzkKeDZs?t=10283)

The skill contains conceptual design rules: only one central focal point at a time, animated text should not verbatim repeat speech (show, do not tell), audio timestamps from Whisper enable precise timing of on-screen elements, and distinct layout modes (talking head on left, animation on right). Canvas safe areas, minimum font sizes, and easing functions (cubic, quintic) all prevent common visual mistakes. *"There should only be one thing that's the central focal point at any point in time... you shouldn't your text that you're animating that you show shouldn't be repeating verbatim what I said. It should just you know, because that doesn't add any value just distracts right."* [[02:53:33]](https://youtube.com/live/ud2WzkKeDZs?t=10413)

### Short-form vertical video re-editing skill (in progress)

Alan has attempted to build a skill for converting the horizontally-framed videos into short-form vertical content for TikTok and YouTube Reels, with different rules: full-screen talking head, dynamic animated subtitles overlaid, illustrations as face overlays, aggressive jump-cut editing. He has not yet brought this to production quality. *"I've tried to make a skill that will take this raw content and re-edit it as like short form vertical video, you know, for TikTok reels YouTube. And there's different rules, right?"* [[03:07:49]](https://youtube.com/live/ud2WzkKeDZs?t=11269)

## Workflows

### Encode judgment into skills when you lack vocabulary

When working in an unfamiliar domain, Alan starts by making vague, subjective requests to Claude and observes how it interprets them into technical implementations, learning the vocabulary in the process. He then encodes that vocabulary back into the skill for consistency. *"So when I was first building these, I would just say like, hey, can you make this a bit more high energy? Don't go full influencer, but just, it needs to pop a little bit. And just these sort of very vague subjective inputs. then Claude would kind of reason about, what makes a video feel that way? And what do I need to do?"* [[02:54:02]](https://youtube.com/live/ud2WzkKeDZs?t=10442)

The friction point: Alan lacks the videography vocabulary to specify what he likes and dislikes, making it difficult to encode nuanced judgment into instructions. *"I would say it's probably the biggest gap right now. And partly because I don't really have the vocabulary to understand what I like and what I don't like and what I would want to change about it."* [[03:02:39]](https://youtube.com/live/ud2WzkKeDZs?t=10959)

### Render frames for visual inspection, but accept spatial reasoning limits

Alan's skill instructs Claude to render individual frames throughout the video for inspection, which helps catch some issues. But spatial reasoning remains weak: Claude frequently misses layout problems and needs explicit correction. *"it says, hey, go and render individual frames throughout this video and then take a look at those, which is good and it's helpful. But I would still say that sort of visual spatial reasoning is one of the weak points of Claude and it doesn't do it particularly well and it can often miss like really obvious layout issues or things like that and then I have to really spell it out."* [[03:00:09]](https://youtube.com/live/ud2WzkKeDZs?t=10809)

### Open abstraction levels for non-coders with vibe coding

At Rasa, Alan has observed that no-code UIs surface the same abstractions as code, making them harder to use, not easier. Vibe coding (conversational agentic interface) solves this by allowing users to interact at whatever abstraction level makes sense to them: non-developers can say "make this friendlier," while expert domain users can make precise edits. *"Someone can come in and say, Hey, can you make this agent friendlier? And that will, you know, produce some output, right? Or someone could come in who's that have been on the project for 12 months and knows it in detail and could come in spearfishing with a very precise edit."* [[02:56:24]](https://youtube.com/live/ud2WzkKeDZs?t=10584)

Rasa made a deliberate bet that no-code is dead and vibe code is in. *"We very clearly took the bet that no code is out, no code is dead, and vibe code is in."* [[02:56:24]](https://youtube.com/live/ud2WzkKeDZs?t=10584)

## Tools / projects he showed

### Remotion

Remotion is a JavaScript library for programmatically generating video. Alan uses it because the productivity gains from having code-based video production far outweigh GUI-based video editing, which he finds fundamentally frustrating. All animated text, graphics, animation of graphics, and timing are written in code. *"Yeah, and like all the animated text and the graphics and the animation of the graphics and all that stuff. That's all just defined in Remotion. It's all just written in code."* [[02:49:09]](https://youtube.com/live/ud2WzkKeDZs?t=9749)

The videos are hosted at https://2026.rasa.com/.

### HeyGen

[HeyGen](https://www.heygen.com/) is the AI video-generation tool Alan uses to create the avatar video component. The demo video he showed was made with the V4 model; the newer V5 is considerably better. *"the video you saw there is from the V4 model. The new model is the V5 and it's considerably better."* [[03:09:06]](https://youtube.com/live/ud2WzkKeDZs?t=11346)

### Whisper

Alan runs Whisper on his recorded audio to extract timestamps for each word, allowing Claude to time text animations and cuts precisely to when he is speaking. *"I've got, I run whisper on the audio so that I've got timestamps so that Cloud knows exactly when the text is coming in so it can like, if it wants to pop up some text or an animation as I'm saying it, it figures out the timing on its own."* [[02:53:33]](https://youtube.com/live/ud2WzkKeDZs?t=10413)

### Bear

Alan uses [Bear](https://bear.app/) for weekly note-taking. He creates one note per week (dated by Monday) and writes raw thoughts into it. He does not use a structured filing system or knowledge base. *"I use Bear for note taking and I have a new note per week, week of whatever the Monday is. And I just like write shit down in there and I'm not like a filer or an organizer or whatever."* [[03:13:26]](https://youtube.com/live/ud2WzkKeDZs?t=11606)

### Google models for video analysis (attempted)

Alan tried Google's video-capable models, uploading videos he liked and asking them to describe the editing and transitions in video-editing jargon. The models were unable to extract or describe the technical details meaningfully, despite being able to generate cinematic video themselves. *"I tried this as well with some of the Google models, which do have video input as a modality. And I uploaded some videos that I liked and I said, you know what, like describe in video editing terms, what makes these good... It really didn't do a good job at all."* [[03:00:09]](https://youtube.com/live/ud2WzkKeDZs?t=10809)

### Claude

Claude is Alan's primary tool for video generation and design instruction. He has strong opinions about its spatial reasoning limitations but considers it superior for the collaborative aspect of the work.

## Explainers

### Everything that can be code will be code

Alan is "code-pilled" on the principle that anything expressed in code becomes vastly more productive when paired with a coding agent than when trapped in a GUI. He has never used an IDE and has always hated graphical interfaces. *"I think that the thesis that I'm fully like, piled on, subscribed to Choose Your Slang is that everything that can be code will be code. Because I'm code-pilled. Yeah. Because the productivity gains from making something code and being able to work on it with a coding agent are so massive that I think nothing survives that."* [[02:46:01]](https://youtube.com/live/ud2WzkKeDZs?t=9961)

### Vibe coding is not "not looking at code," it is asymmetric verification

Early in the conversation, Alan said he does not look at Remotion code, but Hugo challenged the definition of vibe coding. Alan clarified: vibe coding is working without looking at code because you have robust verification (tests, rendering, visual inspection) and you do not care about the code artifact itself, only the output. *"I am definitely vibe coding, and I'm not looking at the code because I really don't care about the code. I only care about the video and the app because no one else needs to run this code ever. It just needs to produce one nice looking video once."* [[02:59:40]](https://youtube.com/live/ud2WzkKeDZs?t=10780)

Agentic engineering (Wes McKinney's approach mentioned in the conversation) is when you skip looking at code but have systematic verification loops to build confidence in correctness.

### Abstraction levels matter, and natural language unlocks multiple levels simultaneously

When building a platform, forcing a single abstraction level (whether code or no-code UI) excludes users. Natural language allows a newcomer to make vague requests and an expert to make precise ones without learning a UI. *"The amazing thing about interacting with natural language is you don't have to pick like the one size fits all. This is the abstraction you work at."* [[02:56:24]](https://youtube.com/live/ud2WzkKeDZs?t=10584)

This principle applies to both video editing and to Rasa's platform design. Developers want branches and code; non-developers want high-level control. Neither should have to learn a UI to get their level of control.

### Verification loops are essential; they are 100 times more effective than instructions alone

Any agent-based work becomes vastly faster and more effective when the agent can inspect its output and validate it. *"you really need that verification loop. And any time you're building with an agent, it's a hundred times faster and more effective if you give it a way to inspect the output that it's produced and is it happy with that output."* [[03:00:09]](https://youtube.com/live/ud2WzkKeDZs?t=10809)

In video generation, this means rendering frames to inspect layout and composition. In code, it means tests and observability.

### Domain knowledge asymmetry: effectiveness scales with familiarity

When Alan works on agent architectures or browser features (domains where he is expert), the effectiveness is vastly higher than when working on video production (where he is a novice). The difference is not the agent, it is his ability to specify and validate. *"When I'm using an agent for something that I understand very well, like agent architectures or building browser features or things like that, it's just a level of... The effectiveness is just vastly different, isn't it?"* [[03:02:49]](https://youtube.com/live/ud2WzkKeDZs?t=11009)

The implication: agents expose the limits of your own knowledge. They are not a substitute for domain expertise, they amplify it.

### Learning by doing in an agent context

Alan no longer bothers to learn unfamiliar libraries before using them with an agent. He just produces. This is a shift from the older practice of deliberately learning one new framework per month to maintain beginner's mind. *"Well now, a lot of the time I won't bother to learn. I'll just do. Right? Like I've never written a line of remotion code by hand."* [[02:58:36]](https://youtube.com/live/ud2WzkKeDZs?t=10716)

However, he still values occasional deep learning for beginner's mindset and perspective. The agent approach works when you have a verification loop and do not need to understand the underlying details.

### Millisecond timing is human judgment

Video editing requires decisions at a resolution of milliseconds between word endings and cuts, between dead air pauses and the next phrase. Whisper timestamps are reasonably accurate but not precise enough. The gap between a jump cut that feels energetic and one that feels like it loses energy is milliseconds, and no amount of instruction bridges that gap. This is a human judgment problem, not an LLM limitation. *"The difference between something that feels like a jump cut, like a TikTok style, you know, almost interrupting yourself cut and something that feels like it loses energy. I mean, it's, it's milliseconds."* [[02:56:24]](https://youtube.com/live/ud2WzkKeDZs?t=10584)

### Easing functions and animation details convey energy and personality

Small animation details like easing (cubic, quintic) are what give animated text personality and energy. A linear animation (like a DVD logo bouncing) feels dead. Easing in and overshooting then returning feels alive. These details are never taught, yet Claude learns to apply them when asked for high-energy video. *"Easing means when you move a piece of text into a screen, you typically you don't move it at a linear rate. Typically you kind of move it fast and then sometimes you even overshoot and then you go back. And that's really what gives it personality."* [[03:10:15]](https://youtube.com/live/ud2WzkKeDZs?t=11415)

### Thought leadership is shifting from annual essays to raw, rapid insights

The market has shifted away from rewarding polished, well-reasoned annual essays toward continuous sharing of rough, evolving thinking. Alan now publishes frequent short videos about features, ideas, and emerging thinking within Rasa rather than comprehensive treatises. The goal is to convey how Rasa thinks and operates, not to present finished theories. *"The way I used to think about sort of like thought leadership, right, is I would write like a big essay once or twice a year with like, you know, really like a thesis, right, like well thought out stuff and I just don't think the market rewards that right now."* [[03:06:33]](https://youtube.com/live/ud2WzkKeDZs?t=11193)

## Additional quotations

- On the frustration of learning video vocabulary: *"I didn't even have the vocabulary to describe what it is I want to achieve. Right. And I've learned a little bit of the vocabulary since then about like jump cuts."* [[02:54:02]](https://youtube.com/live/ud2WzkKeDZs?t=10442)
- On HeyGen V4's terrifying default face: *"The V4 also had this weird quirk where anytime there was dead air or there was just no audio, I wasn't speaking, I was pausing between words. It's like bass that it would return to was me doing like this face. Which was absolutely terrifying."* [[03:09:06]](https://youtube.com/live/ud2WzkKeDZs?t=11346)
- On cost reduction and solo capability: *"I'm turning these out in a couple of afternoons, just to like share some ideas about Rasa... It's just, it's really like a hundred X reduction in cost to produce these things to the point that like we just wouldn't be doing it. I wouldn't be doing it if, you know, if I couldn't do it solo."* [[03:05:51]](https://youtube.com/live/ud2WzkKeDZs?t=11151)
- On thinking before building: *"If I really want to think about a problem, I got to stack a print of paper, I clear my desk, and I just sit and write things down, and I draw pictures and things like that."* [[02:41:20]](https://youtube.com/live/ud2WzkKeDZs?t=9680)
- On getting endorsed for stickers on LinkedIn: *"I put stickers as a skill on LinkedIn and people started endorsing me for it. So I'll just I'll take it."* [[02:44:32]](https://youtube.com/live/ud2WzkKeDZs?t=9872)
- On staying in the terminal: *"I just can't get out of the terminal because the GUI just annoys me."* [[02:47:01]](https://youtube.com/live/ud2WzkKeDZs?t=10021)
- On word timing before speech creates anticipation: *"It's cool to have the words emergent personalization show up as I'm saying them. But actually, the really cool thing is you want to do it just a hair before you say it. And that really makes it feel, you know, if that the video is leading and that it's sizing and your brain starts to engage with it."* [[03:11:29]](https://youtube.com/live/ud2WzkKeDZs?t=11489)
- On timing refinement as fantasy: *"To trim at exact word boundaries from transcript, this It's a nice fantasy, but it's not really realistic."* [[03:09:34]](https://youtube.com/live/ud2WzkKeDZs?t=11374)
- On the final message to builders: *"Just have fun. Just have fun... just tinker, tinker and have fun. I mean, it's just, it's just the greatest."* [[03:14:57]](https://youtube.com/live/ud2WzkKeDZs?t=11697)
